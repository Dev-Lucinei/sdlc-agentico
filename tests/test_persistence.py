from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

from src.persistence import (
    PersistenceDB,
    compute_hash,
    create_persistence_db,
    create_test_db,
)


def test_create_and_insert_event() -> None:
    db = create_test_db()
    try:
        result = db.insert_event("task.created", {"x": 1}, idempotency_key="k1")
        assert result.event_id
        assert result.deduplicated is False
        ev = db.get_event(result.event_id)
        assert ev is not None
        assert ev["event_type"] == "task.created"
        assert ev["payload"] == {"x": 1}
        assert ev["idempotency_key"] == "k1"
        assert len(ev["hash_integrity"]) == 64
    finally:
        db.close()


def test_event_log_append_only() -> None:
    db = create_test_db()
    try:
        eid = db.insert_event("e", {"a": 1}).event_id
        conn = db.connection
        try:
            conn.execute("UPDATE events SET event_type='x' WHERE event_id=?", (eid,))
            conn.commit()
            assert False, "update should fail"
        except sqlite3.DatabaseError:
            pass
        try:
            conn.execute("DELETE FROM events WHERE event_id=?", (eid,))
            conn.commit()
            assert False, "delete should fail"
        except sqlite3.DatabaseError:
            pass
    finally:
        db.close()


def test_reentrega_mesma_key_deduplica() -> None:
    db = create_test_db()
    try:
        e1 = db.insert_event("e", {"a": 1}, idempotency_key="k")
        e2 = db.insert_event("e", {"a": 1}, idempotency_key="k")
        # DEC-033: mesma key → no-op deduplicado; registro original preservado.
        assert e1.deduplicated is False
        assert e2.deduplicated is True
        assert e2.event_id == e1.event_id
        rows = db.list_events(idempotency_key="k")
        assert len(rows) == 1
        # Chaves distintas → registros independentes.
        e3 = db.insert_event("e", {"a": 1}, idempotency_key="k-outra")
        assert e3.deduplicated is False
        assert len(db.list_events()) == 2
    finally:
        db.close()


def test_chain_hash_verificacao() -> None:
    db = create_test_db()
    try:
        db.insert_event("e1", {"a": 1})
        db.insert_event("e2", {"a": 2})
        assert db.verify_chain().ok is True
    finally:
        db.close()


def test_tasks_crud() -> None:
    db = create_test_db()
    try:
        tid = db.insert_task(title="t", status="todo", domain="d", estimates={"h": 2})
        assert tid
        task = db.get_task(tid)
        assert task is not None
        assert task["title"] == "t"
        assert task["estimates"] == {"h": 2}
        assert db.update_task(tid, status="done", output_log={"ok": True}) is True
        task2 = db.get_task(tid)
        assert task2["status"] == "done"
        assert task2["output_log"] == {"ok": True}
        assert len(db.list_tasks(status="done")) == 1
    finally:
        db.close()


def test_decisions() -> None:
    db = create_test_db()
    try:
        did = db.insert_decision(status="pending", classe="C", evidencia=["ev"], lacunas=["l"])
        assert did
        dec = db.get_decision(did)
        assert dec is not None
        assert dec["evidencia"] == ["ev"]
        assert dec["lacunas"] == ["l"]
        assert db.update_decision(did, status="approved") is True
        assert db.get_decision(did)["status"] == "approved"
    finally:
        db.close()


def test_file_db() -> None:
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "test.sqlite"
        db = create_persistence_db(path)
        try:
            db.insert_event("e", {"x": 1})
            assert path.exists()
        finally:
            db.close()
        # reopen
        db2 = PersistenceDB(path)
        try:
            assert len(db2.list_events()) == 1
        finally:
            db2.close()


def test_context_manager() -> None:
    with PersistenceDB() as db:
        eid = db.insert_event("e", {"x": 1}).event_id
        assert db.get_event(eid) is not None


def test_compute_hash_deterministic() -> None:
    h1 = compute_hash({"a": 1}, "", "")
    h2 = compute_hash({"a": 1}, "", "")
    assert h1 == h2
    assert len(h1) == 64


def test_get_event_none() -> None:
    db = create_test_db()
    try:
        assert db.get_event("nope") is None
        assert db.get_task("nope") is None
        assert db.get_decision("nope") is None
    finally:
        db.close()


def test_list_events_filter_type() -> None:
    db = create_test_db()
    try:
        db.insert_event("a", {"x": 1})
        db.insert_event("b", {"x": 2})
        assert len(db.list_events(event_type="a")) == 1
    finally:
        db.close()


def test_update_task_false() -> None:
    db = create_test_db()
    try:
        assert db.update_task("nope", status="done") is False
    finally:
        db.close()


def test_list_decisions_filter() -> None:
    db = create_test_db()
    try:
        db.insert_decision(status="pending")
        db.insert_decision(status="approved")
        assert len(db.list_decisions(status="pending")) == 1
    finally:
        db.close()


def test_verify_chain_tamper() -> None:
    db = create_test_db()
    try:
        db.insert_event("e", {"x": 1})
        # verify chain on untouched log
        assert db.verify_chain().ok is True
    finally:
        db.close()


def test_insert_task_defaults() -> None:
    db = create_test_db()
    try:
        tid = db.insert_task()
        assert db.get_task(tid) is not None
    finally:
        db.close()


def test_update_decision_false() -> None:
    db = create_test_db()
    try:
        assert db.update_decision("nope", status="x") is False
    finally:
        db.close()


def test_unique_index_idempotente_em_reabertura(tmp_path: Path) -> None:
    """DEC-033: CREATE UNIQUE INDEX IF NOT EXISTS é idempotente — reabrir um DB
    com o índice já criado não falha e o dedupe continua operando."""
    path = tmp_path / "reopen.sqlite"
    db = create_persistence_db(path)
    try:
        db.insert_event("e", {"n": 1}, idempotency_key="dup")
    finally:
        db.close()
    db2 = PersistenceDB(path)  # reabre: _ensure_schema reexecuta o CREATE INDEX
    try:
        result = db2.insert_event("e", {"n": 1}, idempotency_key="dup")
        assert result.deduplicated is True
        assert len(db2.list_events(idempotency_key="dup")) == 1
        indexes = {row["name"] for row in db2.connection.execute("PRAGMA index_list(events)")}
        assert "ux_events_idempotency_key" in indexes
    finally:
        db2.close()


def test_unique_index_falha_clara_com_duplicatas_preexistentes(tmp_path: Path) -> None:
    """DEC-033: DB legado com duplicatas em events.idempotency_key faz o CREATE
    UNIQUE INDEX falhar — erro claro (PersistenceIntegrityError), SEM deletar dados."""
    import sqlite3 as _sqlite3

    from src.persistence import PersistenceIntegrityError

    path = tmp_path / "legacy.sqlite"
    raw = _sqlite3.connect(path)
    try:
        raw.executescript(
            """
            CREATE TABLE events (
                event_id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                event_type TEXT NOT NULL,
                payload TEXT NOT NULL,
                idempotency_key TEXT,
                hash_integrity TEXT NOT NULL
            );
            """
        )
        raw.execute(
            "INSERT INTO events VALUES ('e1','t','e','{}','dup','h1')"
        )
        raw.execute(
            "INSERT INTO events VALUES ('e2','t','e','{}','dup','h2')"
        )
        raw.commit()
    finally:
        raw.close()
    try:
        PersistenceDB(path).connect()
        assert False, "esperava PersistenceIntegrityError"
    except PersistenceIntegrityError as exc:
        assert "ux_events_idempotency_key" in str(exc)
    # Dados preservados (não deletados).
    raw = _sqlite3.connect(path)
    try:
        assert raw.execute("SELECT count(*) FROM events").fetchone()[0] == 2
    finally:
        raw.close()


def test_insert_event_same_event_id_sem_key_relanca_e_nao_corrompe() -> None:
    """DEC-033 §c: falha de INSERT (PK duplicada, sem key) é logada e re-levantada —
    nunca engolida. O evento original permanece e o chain hash fica íntegro."""
    import pytest

    db = create_test_db()
    try:
        db.insert_event("e", {"n": 1}, event_id="fixed-id")
        with pytest.raises(Exception):
            db.insert_event("e", {"n": 2}, event_id="fixed-id")
        assert len(db.list_events()) == 1
        assert db.verify_chain().ok is True
    finally:
        db.close()
