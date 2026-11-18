from __future__ import annotations

from src.state import new_state, transition_task


def test_t2_done_to_approved_blocked() -> None:
    state = new_state(task_id="t1", autonomy_class="A")
    state["tasks"].append({"task_id": "t1", "status": "done"})
    result = transition_task("t1", "done", "approved", "ev1", "eref1", state=state)
    assert result == "blocked"
    assert state["tasks"][0]["status"] == "blocked"


def test_done_to_completed_autopromo() -> None:
    state = new_state(task_id="t2", autonomy_class="A")
    state["tasks"].append({"task_id": "t2", "status": "done"})
    result = transition_task("t2", "done", "completed", "ev2", "eref2",
                             state=state, autonomy_class="A")
    assert result == "completed"
    assert state["tasks"][0]["status"] == "completed"


def test_done_to_completed_class_c_blocked() -> None:
    state = new_state(task_id="t3", autonomy_class="C")
    state["tasks"].append({"task_id": "t3", "status": "done"})
    result = transition_task("t3", "done", "completed", "ev3", "eref3",
                             state=state, autonomy_class="C")
    assert result == "blocked"


def test_completed_to_approved_requires_manual() -> None:
    state = new_state(task_id="t4", autonomy_class="C")
    state["tasks"].append({"task_id": "t4", "status": "completed"})
    # sem manual -> blocked
    result = transition_task("t4", "completed", "approved", "ev4", "eref4",
                             state=state, manual_confirmation=False)
    assert result == "blocked"
    assert state["tasks"][0]["status"] == "blocked"


def test_completed_to_approved_with_manual() -> None:
    state = new_state(task_id="t5", autonomy_class="C")
    state["tasks"].append({"task_id": "t5", "status": "completed"})
    result = transition_task("t5", "completed", "approved", "ev5", "eref5",
                             state=state, manual_confirmation=True)
    assert result == "approved"


def test_transition_event_persisted() -> None:
    from src.persistence import create_test_db

    db = create_test_db()
    try:
        state = new_state(task_id="t6", autonomy_class="A")
        state["tasks"].append({"task_id": "t6", "status": "done"})
        transition_task("t6", "done", "completed", "ev6", "eref6",
                        state=state, autonomy_class="A", db=db)
        events = db.list_events(event_type="state.transition")
        assert len(events) == 1
        assert events[0]["payload"]["evidence_ref"] == "eref6"
    finally:
        db.close()


def test_positional_state_first() -> None:
    state = new_state(task_id="t7", autonomy_class="A")
    state["tasks"].append({"task_id": "t7", "status": "done"})
    result = transition_task(state, "t7", "done", "approved", "ev", "eref")
    assert result == "blocked"


def test_transition_task_missing_raises() -> None:
    import pytest
    with pytest.raises(ValueError):
        transition_task()


def test_validate_transition_wrapper() -> None:
    from src.state import validate_transition
    ok, _ = validate_transition("done", "approved")
    assert ok is False
    ok2, _ = validate_transition("done", "completed", autonomy_class="A")
    assert ok2 is True


def test_transition_task_no_state_return() -> None:
    result = transition_task("t", "done", "blocked", "e", "r", persist=False)
    assert result == "blocked"


def test_transition_task_positional_event() -> None:
    st_mod = __import__("src.state", fromlist=["new_state"])
    state = st_mod.new_state(task_id="tx", autonomy_class="A")
    state["tasks"].append({"task_id": "tx", "status": "done"})
    result = transition_task("tx", "done", "completed", "evx", "refx",
                             state=state, autonomy_class="A")
    assert result == "completed"
