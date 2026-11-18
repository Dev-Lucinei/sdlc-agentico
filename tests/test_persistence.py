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
        eid = db.insert_event("task.created", {"x": 1}, idempotency_key="k1")
        assert eid
        ev = db.get_event(eid)
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
        eid = db.insert_event("e", {"a": 1})
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


def test_reentrega_gera_novo_registro() -> None:
    db = create_test_db()
    try:
        e1 = db.insert_event("e", {"a": 1}, idempotency_key="k")
        e2 = db.insert_event("e", {"a": 1}, idempotency_key="k")
        assert e1 != e2
        rows = db.list_events(idempotency_key="k")
        assert len(rows) == 2
    finally:
        db.close()


def test_chain_hash_verificacao() -> None:
    db = create_test_db()
    try:
        db.insert_event("e1", {"a": 1})
        db.insert_event("e2", {"a": 2})
        assert db.verify_chain() is True
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
        eid = db.insert_event("e", {"x": 1})
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
        assert db.verify_chain() is True
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
