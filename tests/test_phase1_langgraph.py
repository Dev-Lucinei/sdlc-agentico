"""Testes da Fase 1 (LangGraph local simulado)."""

from __future__ import annotations

from src.exit_codes import (
    EXIT_ENV_FAILURE,
    EXIT_PROCEED,
    apply_exit_code,
    autopromote_done_to_completed,
)
from src.graph import run_graph
from src.human_review import GuardrailViolation, write_approval
from src.quality_gates import quality_gate
from src.state import new_state
from src.stubs import create_stub_db, write_stub_pyproject


def test_t1_exit_0_autopromotes_done_to_completed() -> None:
    state = new_state(task_id="task-1", autonomy_class="A")
    state["tasks"].append({"task_id": "task-1", "status": "done"})

    action = apply_exit_code(state, EXIT_PROCEED, task_id="task-1")
    assert action == "proceed"

    promoted = autopromote_done_to_completed(state, "task-1", "A")
    assert promoted is True
    assert state["tasks"][0]["status"] == "completed"
    # sem notificacao ao mantenedor
    assert state["global_context"].get("maintainer_notified") is False


def test_t1b_no_notification_for_class_b() -> None:
    state = new_state(task_id="task-2", autonomy_class="B")
    state["tasks"].append({"task_id": "task-2", "status": "done"})
    apply_exit_code(state, 0, task_id="task-2")
    autopromote_done_to_completed(state, "task-2", "B")
    assert state["tasks"][0]["status"] == "completed"
    assert not state["global_context"].get("maintainer_notified", False)


def test_t2_env_failure_blocks_with_evidence() -> None:
    state = new_state(task_id="task-3", autonomy_class="A")
    state["tasks"].append({"task_id": "task-3", "status": "in_progress"})

    action = apply_exit_code(state, EXIT_ENV_FAILURE, task_id="task-3")
    assert action == "blocked"
    assert state["tasks"][0]["status"] == "blocked"
    assert len(state["errors"]) >= 1
    assert state["errors"][-1]["exit_code"] == EXIT_ENV_FAILURE
    assert state["errors"][-1]["error_class"] == "ambiente"


def test_t3_quality_gate_approves_55_percent() -> None:
    ok, reason = quality_gate(55.0, 0)
    assert ok is True
    assert "ok" in reason.lower() or reason == "ok"


def test_t3_quality_gate_rejects_low_coverage() -> None:
    ok, _ = quality_gate(40.0, 0)
    assert ok is False


def test_t3_quality_gate_rejects_critical_errors() -> None:
    ok, _ = quality_gate(80.0, 2)
    assert ok is False


def test_g1_approved_without_manual_reverts_to_blocked() -> None:
    state = new_state(task_id="task-4", autonomy_class="C")
    state["tasks"].append({"task_id": "task-4", "status": "in_progress"})
    approval = {
        "decision_id": "d1",
        "kind": "classe_c",
        "subject_ref": "task-4",
        "status": "approved",
        "decided_by": "llm-agent",
        "decided_at": "2026-01-01T00:00:00Z",
        "evidence_refs": ["ev1"],
        "human_interaction_ref": "session-1",
    }
    try:
        write_approval(state, approval, manual_confirmation=False)
    except GuardrailViolation:
        pass
    assert state["tasks"][0]["status"] == "blocked"


def test_g1_approved_with_manual_requires_evidence() -> None:
    state = new_state(task_id="task-5", autonomy_class="C")
    state["tasks"].append({"task_id": "task-5", "status": "in_progress"})
    approval = {
        "decision_id": "d2",
        "kind": "classe_c",
        "subject_ref": "task-5",
        "status": "approved",
        "decided_by": "human-op",
        "decided_at": "2026-01-01T00:00:00Z",
        "evidence_refs": ["ev1"],
        "human_interaction_ref": "session-2",
    }
    write_approval(state, approval, manual_confirmation=True)
    assert len(state["approvals"]) == 1
    assert state["approvals"][0]["status"] == "approved"


def test_stubs_sqlite_and_pyproject() -> None:
    with create_stub_db() as db:
        conn = db.connection
        conn.execute("CREATE TABLE t (x INTEGER)")
        conn.execute("INSERT INTO t VALUES (1)")
        conn.commit()
        cur = conn.execute("SELECT COUNT(*) FROM t")
        assert cur.fetchone()[0] == 1

    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as d:
        p = write_stub_pyproject(d)
        assert Path(p).exists()
        text = Path(p).read_text()
        # Threshold-agnostic: o stub deve espelhar o fail_under real do pyproject.toml.
        import tomllib

        real = Path(__file__).resolve().parents[1] / "pyproject.toml"
        expected = tomllib.loads(real.read_text(encoding="utf-8"))["tool"]["coverage"]["report"][
            "fail_under"
        ]
        assert f"fail_under = {expected}" in text


def test_run_graph_smoke() -> None:
    state = new_state(task_id="task-6", autonomy_class="A")
    state["tasks"].append({"task_id": "task-6", "status": "done"})
    state["integration_test_output"] = "success"
    run_graph(
        state,
        autonomy_class="A",
        exit_code=0,
        task_id="task-6",
        coverage_percent=55.0,
        critical_errors=0,
    )
    assert state["tasks"][0]["status"] == "completed"
    assert state["pr_ready"] is True
