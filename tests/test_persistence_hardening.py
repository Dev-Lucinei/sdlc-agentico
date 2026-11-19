"""Testes de hardening da camada de persistência (DEC-032 F2.2-téc).

Cobre: PRAGMAs (WAL/busy_timeout/foreign_keys), verify_chain estruturado,
corrupção detectada, concorrência básica, backup/restore e enforcement de FK.
"""

from __future__ import annotations

import sqlite3
import tempfile
import threading
from pathlib import Path

import pytest

from src.persistence import (
    ChainVerificationResult,
    PersistenceDB,
    PersistenceIntegrityError,
    create_persistence_db,
    create_test_db,
    restore_backup,
)


def test_pragmas_aplicados_em_arquivo(tmp_path: Path) -> None:
    db = create_persistence_db(tmp_path / "wal.sqlite")
    try:
        conn = db.connection
        assert conn.execute("PRAGMA journal_mode").fetchone()[0] == "wal"
        assert conn.execute("PRAGMA busy_timeout").fetchone()[0] == 5000
        assert conn.execute("PRAGMA foreign_keys").fetchone()[0] == 1
    finally:
        db.close()


def test_pragma_memory_db_nao_quebra() -> None:
    # :memory: não suporta WAL (retorna 'memory'); busy_timeout/FK ainda valem.
    db = create_test_db()
    try:
        conn = db.connection
        assert conn.execute("PRAGMA busy_timeout").fetchone()[0] == 5000
        assert conn.execute("PRAGMA foreign_keys").fetchone()[0] == 1
    finally:
        db.close()


def test_verify_chain_ok_em_db_integro() -> None:
    db = create_test_db()
    try:
        for i in range(5):
            db.insert_event("e", {"n": i})
        result = db.verify_chain()
        assert isinstance(result, ChainVerificationResult)
        assert result.ok is True
        assert result.eventos_verificados == 5
        assert result.primeiro_elo_invalido is None
    finally:
        db.close()


def test_verify_chain_detecta_corromper_do_meio() -> None:
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "tamper.sqlite"
        db = create_persistence_db(path)
        try:
            db.insert_event("e", {"n": 1})
            db.insert_event("e2", {"n": 2})
            db.insert_event("e3", {"n": 3})
        finally:
            db.close()
        # Adulteração direta fora da API: derruba o trigger append-only e altera o meio.
        raw = sqlite3.connect(path)
        raw.row_factory = sqlite3.Row
        try:
            mid_rowid = raw.execute(
                "SELECT rowid FROM events ORDER BY rowid ASC LIMIT 1 OFFSET 1"
            ).fetchone()["rowid"]
            raw.execute("DROP TRIGGER events_no_update")
            raw.execute(
                "UPDATE events SET payload = ? WHERE rowid = ?",
                ('{"n": 999}', mid_rowid),
            )
            raw.commit()
        finally:
            raw.close()
        db2 = PersistenceDB(path)
        try:
            result = db2.verify_chain()
            assert result.ok is False
            assert result.primeiro_elo_invalido == mid_rowid
            assert result.eventos_verificados == 1
            with pytest.raises(PersistenceIntegrityError):
                db2.verify_chain(strict=True)
        finally:
            db2.close()


def test_verify_chain_db_vazio() -> None:
    db = create_test_db()
    try:
        result = db.verify_chain()
        assert result.ok is True
        assert result.eventos_verificados == 0
    finally:
        db.close()


def test_concorrencia_dois_writers_sequenciais(tmp_path: Path) -> None:
    path = tmp_path / "conc.sqlite"
    db = create_persistence_db(path)  # cria schema
    db.close()
    errors: list[BaseException] = []

    def writer(tag: str) -> None:
        local = PersistenceDB(path)
        try:
            for i in range(5):
                local.insert_event("conc", {"tag": tag, "i": i})
        except BaseException as exc:
            errors.append(exc)
        finally:
            local.close()

    t1 = threading.Thread(target=writer, args=("a",))
    t2 = threading.Thread(target=writer, args=("b",))
    t1.start()
    t1.join(timeout=30)
    t2.start()
    t2.join(timeout=30)
    assert not t1.is_alive() and not t2.is_alive()
    assert not errors, f"erros de concorrência: {errors!r}"
    db2 = PersistenceDB(path)
    try:
        assert len(db2.list_events()) == 10
    finally:
        db2.close()


def test_concorrencia_escritor_leitor(tmp_path: Path) -> None:
    path = tmp_path / "rw.sqlite"
    db = create_persistence_db(path)
    db.insert_event("seed", {"n": 0})
    db.close()
    errors: list[BaseException] = []
    reads: list[int] = []

    def reader() -> None:
        local = PersistenceDB(path)
        try:
            for _ in range(5):
                reads.append(len(local.list_events()))
        except BaseException as exc:
            errors.append(exc)
        finally:
            local.close()

    def writer() -> None:
        local = PersistenceDB(path)
        try:
            for i in range(5):
                local.insert_event("rw", {"n": i})
        except BaseException as exc:
            errors.append(exc)
        finally:
            local.close()

    tr = threading.Thread(target=reader)
    tw = threading.Thread(target=writer)
    tw.start()
    tr.start()
    tw.join(timeout=30)
    tr.join(timeout=30)
    assert not errors, f"erros de concorrência: {errors!r}"


def test_backup_e_restore(tmp_path: Path) -> None:
    src_path = tmp_path / "orig.sqlite"
    backup_path = tmp_path / "backup.sqlite"
    restore_path = tmp_path / "restored.sqlite"
    db = create_persistence_db(src_path)
    try:
        for i in range(3):
            db.insert_event("b", {"n": i})
        db.backup_to(backup_path)
    finally:
        db.close()
    assert backup_path.exists()
    restore_backup(backup_path, restore_path)
    db2 = PersistenceDB(restore_path)
    try:
        assert len(db2.list_events()) == 3
        assert db2.verify_chain().ok is True
    finally:
        db2.close()


def test_backup_destino_existente_falha(tmp_path: Path) -> None:
    db = create_persistence_db(tmp_path / "orig2.sqlite")
    try:
        dest = tmp_path / "exists.sqlite"
        dest.write_bytes(b"x")
        with pytest.raises(FileExistsError):
            db.backup_to(dest)
    finally:
        db.close()


def test_restore_backup_corrompido_falha(tmp_path: Path) -> None:
    src_path = tmp_path / "orig3.sqlite"
    backup_path = tmp_path / "bad_backup.sqlite"
    db = create_persistence_db(src_path)
    try:
        db.insert_event("b", {"n": 1})
        db.insert_event("b", {"n": 2})
        db.backup_to(backup_path)
    finally:
        db.close()
    raw = sqlite3.connect(backup_path)
    try:
        raw.execute("DROP TRIGGER events_no_update")
        raw.execute("UPDATE events SET payload = '{\"n\": 999}' WHERE rowid = 1")
        raw.commit()
    finally:
        raw.close()
    with pytest.raises(PersistenceIntegrityError):
        restore_backup(backup_path, tmp_path / "should_not_exist.sqlite")


def test_restore_alvo_existente_exige_overwrite(tmp_path: Path) -> None:
    src_path = tmp_path / "orig4.sqlite"
    backup_path = tmp_path / "bk4.sqlite"
    target_path = tmp_path / "tgt4.sqlite"
    db = create_persistence_db(src_path)
    try:
        db.insert_event("b", {"n": 1})
        db.backup_to(backup_path)
    finally:
        db.close()
    target_path.write_bytes(b"occupied")
    with pytest.raises(FileExistsError):
        restore_backup(backup_path, target_path)
    restore_backup(backup_path, target_path, overwrite=True)
    db2 = PersistenceDB(target_path)
    try:
        assert db2.verify_chain().ok is True
    finally:
        db2.close()


def test_foreign_keys_pragma_ativo_e_sem_fks_declaradas() -> None:
    # O schema atual NÃO declara FOREIGN KEY em nenhuma tabela; foreign_keys=ON
    # é inócuo (enforcement sem FKs é no-op). Documentado como lacuna — ver resumo.
    db = create_test_db()
    try:
        assert db.connection.execute("PRAGMA foreign_keys").fetchone()[0] == 1
        fk_count = db.connection.execute(
            "SELECT count(*) FROM sqlite_master "
            "WHERE type = 'table' AND (sql LIKE '%FOREIGN KEY%' OR sql LIKE '%REFERENCES%')"
        ).fetchone()[0]
        assert fk_count == 0
    finally:
        db.close()
