"""Camada de persistência SQLite — SoT + Event Log append-only (Fase 1).

- Tabelas: events (imutável), tasks, decisions.
- Event Log: INSERT only; reentregas geram novos registros vinculados por idempotency_key.
- Hash de integridade: SHA-256 do payload + timestamp/hash anterior (chain hash).
- Banco descartável para testes (path None => :memory: ou tempfile).

Hardening (DEC-032 F2.2-téc): conexões aplicam PRAGMA journal_mode=WAL (arquivo),
busy_timeout=5000 e foreign_keys=ON. verify_chain() retorna ChainVerificationResult
estruturado (ok/eventos_verificados/primeiro_elo_invalido) — API pública alterada de
bool para resultado; use `.ok` para o veredito booleano. Backup via backup_to();
restore via restore_backup() (valida integridade antes de copiar).
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sqlite3
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .observability import get_logger

logger = get_logger(__name__)

__all__ = [
    "ChainVerificationResult",
    "PersistenceIntegrityError",
    "restore_backup",
    "PersistenceDB",
    "PersistenceStore",
    "SqlitePersistence",
    "compute_hash",
    "create_persistence_db",
    "create_db",
    "create_test_db",
    "Persistence",
    "SQLiteStore",
    "EventLog",
    "SQLitePersistence",
]


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, default=str)


class PersistenceIntegrityError(RuntimeError):
    """Cadeia de integridade do event log inválida (modo estrito) ou backup corrompido."""


@dataclass(frozen=True)
class ChainVerificationResult:
    """Resultado estruturado da verificação da cadeia SHA-256 do event log."""

    ok: bool
    eventos_verificados: int
    primeiro_elo_invalido: int | None  # rowid do primeiro evento com hash inválido


def compute_hash(
    payload: Any,
    previous_timestamp: str = "",
    previous_hash: str = "",
) -> str:
    """SHA-256 do payload (canônico) + timestamp anterior + hash anterior."""
    data = f"{_canonical(payload)}|{previous_timestamp or ''}|{previous_hash or ''}"
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


class PersistenceDB:
    """Banco SQLite descartável para SoT + Event Log."""

    def __init__(self, path: str | Path | None = None) -> None:
        self.path = None if path is None else str(path)
        self._conn: sqlite3.Connection | None = None

    # ------------------------------------------------------------------ conn
    def connect(self) -> sqlite3.Connection:
        if self._conn is None:
            target = ":memory:" if self.path is None else self.path
            self._conn = sqlite3.connect(target, timeout=5.0)
            self._conn.row_factory = sqlite3.Row
            self._apply_pragmas(self._conn)
            self._ensure_schema(self._conn)
        return self._conn

    @property
    def connection(self) -> sqlite3.Connection:
        return self.connect()

    def close(self) -> None:
        if self._conn is not None:
            self._conn.close()
            self._conn = None

    def __enter__(self) -> "PersistenceDB":
        self.connect()
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # ------------------------------------------------------------------ pragmas
    @staticmethod
    def _apply_pragmas(conn: sqlite3.Connection) -> None:
        # journal_mode=WAL é inócuo em :memory: (retorna 'memory') e ativo em arquivo.
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA busy_timeout=5000")
        conn.execute("PRAGMA foreign_keys=ON")

    @staticmethod
    def _verify_connection(conn: sqlite3.Connection) -> ChainVerificationResult:
        cur = conn.execute(
            "SELECT rowid AS seq, timestamp, payload, hash_integrity "
            "FROM events ORDER BY rowid ASC"
        )
        prev_ts = ""
        prev_hash = ""
        verified = 0
        for row in cur.fetchall():
            try:
                payload = json.loads(row["payload"])
            except (json.JSONDecodeError, TypeError):
                payload = row["payload"]
            expected = compute_hash(payload, prev_ts, prev_hash)
            if expected != row["hash_integrity"]:
                return ChainVerificationResult(
                    ok=False,
                    eventos_verificados=verified,
                    primeiro_elo_invalido=int(row["seq"]),
                )
            prev_ts = row["timestamp"]
            prev_hash = row["hash_integrity"]
            verified += 1
        return ChainVerificationResult(ok=True, eventos_verificados=verified,
                                       primeiro_elo_invalido=None)

    # ------------------------------------------------------------------ schema
    @staticmethod
    def _ensure_schema(conn: sqlite3.Connection) -> None:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS events (
                event_id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                event_type TEXT NOT NULL,
                payload TEXT NOT NULL,
                idempotency_key TEXT,
                hash_integrity TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS tasks (
                task_id TEXT PRIMARY KEY,
                title TEXT,
                status TEXT,
                domain TEXT,
                estimates TEXT,
                input_data TEXT,
                output_log TEXT,
                result_path TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS decisions (
                decision_id TEXT PRIMARY KEY,
                status TEXT,
                classe TEXT,
                evidencia TEXT,
                lacunas TEXT,
                created_at TEXT NOT NULL
            );
            CREATE TRIGGER IF NOT EXISTS events_no_update
            BEFORE UPDATE ON events
            BEGIN
                SELECT RAISE(ABORT, 'events is append-only');
            END;
            CREATE TRIGGER IF NOT EXISTS events_no_delete
            BEFORE DELETE ON events
            BEGIN
                SELECT RAISE(ABORT, 'events is append-only');
            END;
            """
        )
        conn.commit()

    # ------------------------------------------------------------------ events
    def insert_event(
        self,
        event_type: str,
        payload: Any,
        *,
        idempotency_key: str | None = None,
        event_id: str | None = None,
        timestamp: str | None = None,
    ) -> str:
        conn = self.connect()
        eid = event_id or str(uuid.uuid4())
        ts = timestamp or _now()
        try:
            cur = conn.execute(
                "SELECT timestamp, hash_integrity FROM events ORDER BY rowid DESC LIMIT 1"
            )
            row = cur.fetchone()
            prev_ts = row["timestamp"] if row is not None else ""
            prev_hash = row["hash_integrity"] if row is not None else ""
            payload_text = _canonical(payload)
            hash_integrity = compute_hash(payload, prev_ts, prev_hash)
            conn.execute(
                "INSERT INTO events (event_id, timestamp, event_type, payload, "
                "idempotency_key, hash_integrity) VALUES (?,?,?,?,?,?)",
                (eid, ts, event_type, payload_text, idempotency_key, hash_integrity),
            )
            conn.commit()
        except Exception as exc:
            logger.warning(
                "insert_event falhou (event_type=%s): %s",
                event_type,
                exc,
                extra={"event": "persistence.insert_event.failed",
                       "event_type": event_type, "error": str(exc)},
            )
            raise
        return eid

    def get_event(self, event_id: str) -> dict[str, Any] | None:
        conn = self.connect()
        cur = conn.execute("SELECT * FROM events WHERE event_id = ?", (event_id,))
        row = cur.fetchone()
        if row is None:
            return None
        return self._row_to_event(row)

    def list_events(
        self,
        *,
        event_type: str | None = None,
        idempotency_key: str | None = None,
    ) -> list[dict[str, Any]]:
        conn = self.connect()
        query = "SELECT * FROM events"
        params: list[Any] = []
        clauses: list[str] = []
        if event_type is not None:
            clauses.append("event_type = ?")
            params.append(event_type)
        if idempotency_key is not None:
            clauses.append("idempotency_key = ?")
            params.append(idempotency_key)
        if clauses:
            query += " WHERE " + " AND ".join(clauses)
        query += " ORDER BY rowid ASC"
        cur = conn.execute(query, params)
        return [self._row_to_event(r) for r in cur.fetchall()]

    @staticmethod
    def _row_to_event(row: sqlite3.Row) -> dict[str, Any]:
        try:
            payload = json.loads(row["payload"])
        except (json.JSONDecodeError, TypeError):
            payload = row["payload"]
        return {
            "event_id": row["event_id"],
            "timestamp": row["timestamp"],
            "event_type": row["event_type"],
            "payload": payload,
            "idempotency_key": row["idempotency_key"],
            "hash_integrity": row["hash_integrity"],
        }

    def verify_chain(self, *, strict: bool = False) -> ChainVerificationResult:
        """Verifica o encadeamento SHA-256 do event log (sem side-effects).

        Retorna ChainVerificationResult(ok, eventos_verificados, primeiro_elo_invalido).
        `eventos_verificados` conta os eventos válidos anteriores ao primeiro inválido
        (ou o total, quando íntegro). `primeiro_elo_invalido` é o rowid do elo quebrado.
        Com strict=True, levanta PersistenceIntegrityError em vez de retornar ok=False.
        """
        result = self._verify_connection(self.connect())
        if not result.ok:
            logger.warning(
                "verify_chain: cadeia de integridade inválida (rowid=%s, verificados=%s)",
                result.primeiro_elo_invalido,
                result.eventos_verificados,
                extra={"event": "persistence.verify_chain.invalid",
                       "primeiro_elo_invalido": result.primeiro_elo_invalido,
                       "eventos_verificados": result.eventos_verificados},
            )
        if strict and not result.ok:
            raise PersistenceIntegrityError(
                f"cadeia de integridade inválida no rowid={result.primeiro_elo_invalido}"
            )
        return result

    def backup_to(self, dest_path: str | Path) -> Path:
        """Backup consistente via SQLite backup API. Falha se o destino já existe."""
        dest = Path(dest_path)
        if dest.exists():
            raise FileExistsError(f"backup de destino já existe: {dest}")
        if not dest.parent.exists():
            raise FileNotFoundError(f"diretório de destino não existe: {dest.parent}")
        conn = self.connect()
        conn.commit()
        target = sqlite3.connect(dest)
        try:
            conn.backup(target)
        finally:
            target.close()
        return dest

    # ------------------------------------------------------------------ tasks
    def insert_task(
        self,
        *,
        task_id: str | None = None,
        title: str = "",
        status: str = "todo",
        domain: str | None = None,
        estimates: Any = None,
        input_data: Any = None,
        output_log: Any = None,
        result_path: str | None = None,
        created_at: str | None = None,
        updated_at: str | None = None,
    ) -> str:
        conn = self.connect()
        tid = task_id or str(uuid.uuid4())
        now = _now()
        ca = created_at or now
        ua = updated_at or now
        estimates_text = None if estimates is None else (
            estimates if isinstance(estimates, str) else _canonical(estimates)
        )
        input_text = None if input_data is None else (
            input_data if isinstance(input_data, str) else _canonical(input_data)
        )
        output_text = None if output_log is None else (
            output_log if isinstance(output_log, str) else _canonical(output_log)
        )
        conn.execute(
            "INSERT INTO tasks (task_id, title, status, domain, estimates, "
            "input_data, output_log, result_path, created_at, updated_at) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (tid, title, status, domain, estimates_text, input_text,
             output_text, result_path, ca, ua),
        )
        conn.commit()
        return tid

    def get_task(self, task_id: str) -> dict[str, Any] | None:
        conn = self.connect()
        cur = conn.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
        row = cur.fetchone()
        if row is None:
            return None
        return self._row_to_task(row)

    def list_tasks(
        self, *, status: str | None = None, domain: str | None = None
    ) -> list[dict[str, Any]]:
        conn = self.connect()
        query = "SELECT * FROM tasks"
        params: list[Any] = []
        clauses: list[str] = []
        if status is not None:
            clauses.append("status = ?")
            params.append(status)
        if domain is not None:
            clauses.append("domain = ?")
            params.append(domain)
        if clauses:
            query += " WHERE " + " AND ".join(clauses)
        query += " ORDER BY created_at ASC"
        cur = conn.execute(query, params)
        return [self._row_to_task(r) for r in cur.fetchall()]

    def update_task(self, task_id: str, **fields: Any) -> bool:
        allowed = {"title", "status", "domain", "estimates", "input_data",
                   "output_log", "result_path"}
        sets: list[str] = []
        params: list[Any] = []
        for key, value in fields.items():
            if key not in allowed:
                continue
            if (key in ("estimates", "input_data", "output_log") and value is not None
                    and not isinstance(value, str)):
                value = _canonical(value)
            sets.append(f"{key} = ?")
            params.append(value)
        if not sets:
            return False
        sets.append("updated_at = ?")
        params.append(_now())
        params.append(task_id)
        conn = self.connect()
        cur = conn.execute(
            f"UPDATE tasks SET {', '.join(sets)} WHERE task_id = ?", params
        )
        conn.commit()
        return cur.rowcount > 0

    @staticmethod
    def _row_to_task(row: sqlite3.Row) -> dict[str, Any]:
        def _load(v: Any) -> Any:
            if v is None:
                return None
            try:
                return json.loads(v)
            except (json.JSONDecodeError, TypeError):
                return v

        return {
            "task_id": row["task_id"],
            "title": row["title"],
            "status": row["status"],
            "domain": row["domain"],
            "estimates": _load(row["estimates"]),
            "input_data": _load(row["input_data"]),
            "output_log": _load(row["output_log"]),
            "result_path": row["result_path"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }

    # ---------------------------------------------------------------- decisions
    def insert_decision(
        self,
        *,
        decision_id: str | None = None,
        status: str = "pending",
        classe: str | None = None,
        evidencia: Any = None,
        lacunas: Any = None,
        created_at: str | None = None,
    ) -> str:
        conn = self.connect()
        did = decision_id or str(uuid.uuid4())
        ca = created_at or _now()
        evidencia_text = None if evidencia is None else (
            evidencia if isinstance(evidencia, str) else _canonical(evidencia)
        )
        lacunas_text = None if lacunas is None else (
            lacunas if isinstance(lacunas, str) else _canonical(lacunas)
        )
        conn.execute(
            "INSERT INTO decisions (decision_id, status, classe, evidencia, "
            "lacunas, created_at) VALUES (?,?,?,?,?,?)",
            (did, status, classe, evidencia_text, lacunas_text, ca),
        )
        conn.commit()
        return did

    def get_decision(self, decision_id: str) -> dict[str, Any] | None:
        conn = self.connect()
        cur = conn.execute(
            "SELECT * FROM decisions WHERE decision_id = ?", (decision_id,)
        )
        row = cur.fetchone()
        if row is None:
            return None
        return self._row_to_decision(row)

    def list_decisions(self, *, status: str | None = None) -> list[dict[str, Any]]:
        conn = self.connect()
        query = "SELECT * FROM decisions"
        params: list[Any] = []
        if status is not None:
            query += " WHERE status = ?"
            params.append(status)
        query += " ORDER BY created_at ASC"
        cur = conn.execute(query, params)
        return [self._row_to_decision(r) for r in cur.fetchall()]

    def update_decision(self, decision_id: str, **fields: Any) -> bool:
        allowed = {"status", "classe", "evidencia", "lacunas"}
        sets: list[str] = []
        params: list[Any] = []
        for key, value in fields.items():
            if key not in allowed:
                continue
            if key in ("evidencia", "lacunas") and value is not None and not isinstance(value, str):
                value = _canonical(value)
            sets.append(f"{key} = ?")
            params.append(value)
        if not sets:
            return False
        params.append(decision_id)
        conn = self.connect()
        cur = conn.execute(
            f"UPDATE decisions SET {', '.join(sets)} WHERE decision_id = ?", params
        )
        conn.commit()
        return cur.rowcount > 0

    @staticmethod
    def _row_to_decision(row: sqlite3.Row) -> dict[str, Any]:
        def _load(v: Any) -> Any:
            if v is None:
                return None
            try:
                return json.loads(v)
            except (json.JSONDecodeError, TypeError):
                return v

        return {
            "decision_id": row["decision_id"],
            "status": row["status"],
            "classe": row["classe"],
            "evidencia": _load(row["evidencia"]),
            "lacunas": _load(row["lacunas"]),
            "created_at": row["created_at"],
        }


# Aliases
PersistenceStore = PersistenceDB
SqlitePersistence = PersistenceDB
Persistence = PersistenceDB
SQLiteStore = PersistenceDB
EventLog = PersistenceDB
SQLitePersistence = PersistenceDB


def restore_backup(
    backup_path: str | Path,
    target_path: str | Path,
    *,
    overwrite: bool = False,
) -> Path:
    """Restaura um backup validado para `target_path`.

    Valida o backup (PRAGMA integrity_check == 'ok' e verify_chain ok) antes de
    copiar. O alvo NÃO deve estar aberto por outra conexão desta camada; se já
    existir, exige overwrite=True. Retorna o Path restaurado.
    """
    src = Path(backup_path)
    dest = Path(target_path)
    if not src.exists():
        raise FileNotFoundError(f"backup não encontrado: {src}")
    if dest.exists() and not overwrite:
        raise FileExistsError(f"alvo já existe (use overwrite=True): {dest}")
    raw = sqlite3.connect(f"file:{src}?mode=ro", uri=True)
    raw.row_factory = sqlite3.Row
    try:
        row = raw.execute("PRAGMA integrity_check").fetchone()
        if row is None or row[0] != "ok":
            raise PersistenceIntegrityError(
                f"integrity_check falhou no backup: {row[0] if row else 'sem resultado'}"
            )
        result = PersistenceDB._verify_connection(raw)
        if not result.ok:
            raise PersistenceIntegrityError(
                f"cadeia de integridade inválida no backup (rowid={result.primeiro_elo_invalido})"
            )
    finally:
        raw.close()
    shutil.copy2(src, dest)
    return dest


def create_persistence_db(path: str | Path | None = None) -> PersistenceDB:
    db = PersistenceDB(path=path)
    db.connect()
    return db


def create_db(path: str | Path | None = None) -> PersistenceDB:
    return create_persistence_db(path)


def create_test_db() -> PersistenceDB:
    return create_persistence_db(None)

