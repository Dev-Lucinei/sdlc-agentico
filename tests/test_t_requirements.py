from __future__ import annotations

from src.exit_codes import EXIT_COVERAGE_BELOW, EXIT_ENV_FAILURE, apply_exit_code
from src.graph import node_pr_generation
from src.quality_gates import quality_gate
from src.state import new_state


def test_t3_env_failure_classified_ambiente() -> None:
    state = new_state(task_id="t", autonomy_class="A")
    state["tasks"].append({"task_id": "t", "status": "in_progress"})
    action = apply_exit_code(state, EXIT_ENV_FAILURE, task_id="t")
    assert action == "blocked"
    assert state["errors"][-1]["error_class"] == "ambiente"
    assert state["errors"][-1]["exit_code"] == EXIT_ENV_FAILURE


def test_t4_coverage_below_blocks_pr() -> None:
    state = new_state(task_id="t", autonomy_class="A")
    state["integration_test_output"] = "success"
    state["pr_ready"] = True
    node_pr_generation(state, coverage_percent=40.0, critical_errors=0)
    assert state["pr_ready"] is False
    assert any(e.get("exit_code") == EXIT_COVERAGE_BELOW for e in state["errors"])
    ok, _ = quality_gate(40.0, 0)
    assert ok is False


def test_t1_contract_missing_exit_5_cli() -> None:
    import json
    import subprocess
    import sys
    from pathlib import Path

    tmp = Path("/tmp/opencode/missing.json")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(json.dumps({}))
    r = subprocess.run(
        [sys.executable, str(Path("tools/contract_validator.py")), str(tmp)],
        capture_output=True, text=True,
    )
    assert r.returncode == 5, r.stdout + r.stderr
