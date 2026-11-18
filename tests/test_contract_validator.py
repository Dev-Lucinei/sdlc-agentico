from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from src.contract_validator import (
    EXIT_MISSING_REQUIRED,
    validate,
    validate_file,
    validate_transition,
)

ROOT = Path(__file__).resolve().parents[1]


def test_valid_summary() -> None:
    data = json.loads((ROOT / "docs/examples/subagent-summary-valid.json").read_text())
    errs = validate(data)
    assert errs == [], errs


def test_valid_envelope() -> None:
    data = json.loads((ROOT / "docs/examples/envelope-valid.json").read_text())
    errs = validate(data)
    assert errs == [], errs


def test_invalid_summary_missing_objetivo() -> None:
    data = json.loads((ROOT / "docs/examples/subagent-summary-invalid.json").read_text())
    errs = validate(data)
    assert errs, "expected errors"
    assert any("objetivo" in e.lower() or "required" in e.lower() for e in errs)


def test_missing_required_fields_exit_5() -> None:
    # payload sem campos obrigatórios
    data = {"foo": "bar"}
    errs = validate(data)
    assert errs
    # CLI
    tmp = ROOT / "tmp_missing.json"
    tmp.write_text(json.dumps(data))
    try:
        r = subprocess.run(
            [sys.executable, str(ROOT / "tools/contract_validator.py"), str(tmp)],
            capture_output=True, text=True,
        )
        assert r.returncode == EXIT_MISSING_REQUIRED, r.stdout + r.stderr
    finally:
        tmp.unlink(missing_ok=True)


def test_validate_file_missing() -> None:
    errs = validate_file(ROOT / "nope.json")
    assert errs


def test_transition_invariant() -> None:
    ok, _ = validate_transition("done", "approved")
    assert ok is False
    ok2, _ = validate_transition("done", "completed", autonomy_class="A")
    assert ok2 is True
    ok3, _ = validate_transition("completed", "approved", manual_confirmation=True)
    assert ok3 is True
    ok4, _ = validate_transition("completed", "approved", manual_confirmation=False)
    assert ok4 is False


def test_state_transition_exit_code_5_cli() -> None:
    # T1: inputs sem campos obrigatórios -> exit 5
    tmp = ROOT / "tmp_t1.json"
    tmp.write_text(json.dumps({"schema_name": "sdlc.subagent.summary"}))
    try:
        r = subprocess.run(
            [sys.executable, str(ROOT / "tools/contract_validator.py"), str(tmp)],
            capture_output=True, text=True,
        )
        assert r.returncode == 5, r.stdout + r.stderr
    finally:
        tmp.unlink(missing_ok=True)


def test_cli_valid_summary() -> None:
    import subprocess
    import sys
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools/contract_validator.py"),
         str(ROOT / "docs/examples/subagent-summary-valid.json")],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_cli_missing_file() -> None:
    import subprocess
    import sys
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools/contract_validator.py"),
         str(ROOT / "docs/examples/nope.json")],
        capture_output=True, text=True,
    )
    assert r.returncode == 1


def test_cli_data_arg() -> None:
    import json
    import subprocess
    import sys
    payload = json.loads((ROOT / "docs/examples/subagent-summary-valid.json").read_text())
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools/contract_validator.py"), "--data", json.dumps(payload)],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_contract_validator_class() -> None:
    from src.contract_validator import ContractValidator
    cv = ContractValidator()
    data = {"schema_name": "sdlc.task.delegation", "schema_version": "1.0.0"}
    errs = cv.validate(data)
    assert errs  # missing fields


def test_validate_transition_all_branches() -> None:
    from src.contract_validator import validate_transition
    assert validate_transition("done", "blocked")[0] is True
    assert validate_transition("completed", "rejected", manual_confirmation=True)[0] is True
    assert validate_transition("completed", "rejected", manual_confirmation=False)[0] is False
    assert validate_transition("done", "completed", autonomy_class="B")[0] is True
    assert validate_transition("done", "completed", autonomy_class="C")[0] is False
