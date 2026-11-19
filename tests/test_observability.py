"""Testes de observabilidade mínima (DEC-032 F2.3-téc)."""

from __future__ import annotations

import io
import json
import logging
import uuid

import pytest

from src.graph import run_graph
from src.observability import (
    JSONFormatter,
    Metrics,
    get_correlation_id,
    get_logger,
    metrics,
    new_correlation_id,
    set_correlation_id,
)
from src.quality_gates import quality_gate
from src.state import new_state, transition_task


@pytest.fixture(autouse=True)
def _reset_correlation_id():
    set_correlation_id(None)
    yield
    set_correlation_id(None)


def _capture_logger(name: str) -> tuple[logging.Logger, io.StringIO]:
    logger = get_logger(name)
    buf = io.StringIO()
    handler = logging.StreamHandler(buf)
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    return logger, buf


def test_new_correlation_id_is_uuid() -> None:
    cid = new_correlation_id()
    assert str(uuid.UUID(cid)) == cid
    assert new_correlation_id() != new_correlation_id()


def test_set_get_correlation_id_roundtrip() -> None:
    assert get_correlation_id() is None
    set_correlation_id("cid-123")
    assert get_correlation_id() == "cid-123"
    set_correlation_id(None)
    assert get_correlation_id() is None


def test_get_logger_idempotent_and_no_propagate() -> None:
    logger = get_logger("test.observability.idempotent")
    n_handlers = len(logger.handlers)
    logger2 = get_logger("test.observability.idempotent")
    assert logger is logger2
    assert len(logger.handlers) == n_handlers
    assert logger.propagate is False


def test_logger_emits_parseable_json_with_correlation_id() -> None:
    logger, buf = _capture_logger("test.observability.json")
    set_correlation_id("cid-xyz")
    logger.info("mensagem teste", extra={"event": "test.event", "foo": "bar"})
    line = buf.getvalue().strip().splitlines()[-1]
    record = json.loads(line)
    assert record["msg"] == "mensagem teste"
    assert record["level"] == "INFO"
    assert record["logger"] == "test.observability.json"
    assert record["correlation_id"] == "cid-xyz"
    assert record["event"] == "test.event"
    assert record["foo"] == "bar"
    assert "ts" in record


def test_logger_prefers_record_correlation_id_over_context() -> None:
    logger, buf = _capture_logger("test.observability.json2")
    set_correlation_id("cid-context")
    logger.info("m", extra={"correlation_id": "cid-record"})
    record = json.loads(buf.getvalue().strip().splitlines()[-1])
    assert record["correlation_id"] == "cid-record"


def test_metrics_increment_snapshot_reset() -> None:
    m = Metrics()
    assert m.snapshot() == {}
    m.increment("runs")
    m.increment("runs", 4)
    m.increment("gate_pass")
    assert m.snapshot() == {"runs": 5, "gate_pass": 1}
    m.reset()
    assert m.snapshot() == {}
    with pytest.raises(ValueError):
        m.increment("runs", -1)


def test_quality_gate_increments_metrics() -> None:
    before = metrics.snapshot()
    ok, _ = quality_gate(100.0, 0)
    assert ok is True
    ok2, _ = quality_gate(0.0, 0)
    assert ok2 is False
    after = metrics.snapshot()
    assert after.get("gate_pass", 0) - before.get("gate_pass", 0) == 1
    assert after.get("gate_fail", 0) - before.get("gate_fail", 0) == 1


def test_run_graph_increments_runs_and_logs() -> None:
    before = metrics.snapshot().get("runs", 0)
    state = new_state(request_id="req-obs", task_id="task-obs", autonomy_class="A")
    run_graph(state, exit_code=0)
    after = metrics.snapshot().get("runs", 0)
    assert after - before == 1
    assert get_correlation_id() is not None


def test_transition_logs_and_continues_best_effort_with_broken_db() -> None:
    logger, buf = _capture_logger("src.state")

    class BrokenDB:
        def insert_event(self, *args: object, **kwargs: object) -> str:
            raise RuntimeError("db quebrado")

    result = transition_task(
        "task-obs-1",
        "todo",
        "in_progress",
        db=BrokenDB(),
        event_id="evt-obs-1",
    )
    assert result == "in_progress"
    lines = [ln for ln in buf.getvalue().strip().splitlines() if ln]
    records = [json.loads(ln) for ln in lines]
    events = [r.get("event") for r in records]
    assert "state.transition" in events
    assert "state.transition.persist_failed" in events
    persist_fail = next(
        r for r in records if r.get("event") == "state.transition.persist_failed"
    )
    assert "db quebrado" in persist_fail.get("error", "")
    assert persist_fail.get("correlation_id")
    assert metrics.snapshot().get("event_log_persist_failures", 0) >= 1


def test_transition_generates_and_propagates_correlation_id() -> None:
    result = transition_task("task-obs-2", "todo", "ready", persist=False)
    assert result == "ready"
    assert get_correlation_id() is not None
