"""Testes adicionais para elevar a cobertura dos módulos com gaps (fatia B, DEC-036).

Cobre ramos de src/contract_validator.py, src/exit_codes.py, src/human_review.py
e src/stubs/infra.py sem alterar src/. Thresholds nunca hardcoded: o fail_under
real é sempre lido do pyproject.toml via tomllib.
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

import pytest

import src.contract_validator as cv
from src.contract_validator import (
    EXIT_INVALID,
    EXIT_MISSING_REQUIRED,
    EXIT_OK,
    ContractValidator,
    is_missing_required,
    validate,
    validate_file,
    validate_transition,
)
from src.exit_codes import (
    ExitCodeHandler,
    apply_exit_code,
    autopromote_done_to_completed,
    classify_exit_code,
    notify_maintainer,
)
from src.human_review import (
    GuardrailViolation,
    HumanReview,
    human_review_node,
    write_approval,
)
from src.state import new_state
from src.stubs.infra import (
    StubDatabase,
    StubEnvironment,
    _find_real_pyproject,
    _read_coverage_threshold,
    create_stub_db,
    write_stub_pyproject,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
REAL_PYPROJECT = REPO_ROOT / "pyproject.toml"


def _real_fail_under() -> int:
    with REAL_PYPROJECT.open("rb") as fh:
        return int(tomllib.load(fh)["tool"]["coverage"]["report"]["fail_under"])


# ---------------------------------------------------------------------------
# contract_validator — helpers internos
# ---------------------------------------------------------------------------


def test_load_schema_missing_file_returns_empty(tmp_path: Path) -> None:
    assert cv._load_schema(tmp_path / "nope.json") == {}


def test_load_schema_non_dict_json_returns_empty(tmp_path: Path) -> None:
    p = tmp_path / "schema.json"
    p.write_text("[1, 2, 3]", encoding="utf-8")
    assert cv._load_schema(p) == {}


def test_branch_candidates_delegation_match() -> None:
    schema = {"$defs": {"envelope": {"type": "object"}, "subagent_summary": {"type": "object"}}}
    out = cv._branch_candidates({"schema_name": "sdlc.task.delegation"}, schema)
    assert out == [("envelope", {"type": "object"})]


def test_branch_candidates_summary_match() -> None:
    schema = {"$defs": {"envelope": {"type": "object"}, "subagent_summary": {"type": "object"}}}
    out = cv._branch_candidates({"schema_name": "sdlc.subagent.summary"}, schema)
    assert out == [("subagent_summary", {"type": "object"})]


def test_branch_candidates_unknown_name_collects_defs() -> None:
    schema = {"$defs": {"envelope": {"type": "object"}}}
    out = cv._branch_candidates({"schema_name": "x.y"}, schema)
    assert out == [("envelope", {"type": "object"})]
    schema2 = {"$defs": {"subagent_summary": {"type": "object"}}}
    assert cv._branch_candidates({"schema_name": "x.y"}, schema2) == [
        ("subagent_summary", {"type": "object"})
    ]
    assert cv._branch_candidates({"schema_name": "x.y"}, {"$defs": {}}) == []


def test_branch_candidates_non_dict_data() -> None:
    schema = {"$defs": {"envelope": {"type": "object"}}}
    assert cv._branch_candidates(["not", "a", "dict"], schema) == [("envelope", {"type": "object"})]


def test_jsonschema_available_exception_returns_false(monkeypatch: pytest.MonkeyPatch) -> None:
    import importlib.util

    def boom(name: str) -> object:
        raise RuntimeError("boom")

    monkeypatch.setattr(importlib.util, "find_spec", boom)
    assert cv._jsonschema_available() is False


# ---------------------------------------------------------------------------
# contract_validator — validate()
# ---------------------------------------------------------------------------


def test_validate_non_dict_data_returns_expected_object() -> None:
    assert validate(["nope"]) == ["<root>: expected object"]


def test_validate_non_dict_schema_is_coerced() -> None:
    errors = validate({"schema_name": "x", "schema_version": "1.0.0"}, schema="notadict")  # type: ignore[arg-type]
    assert isinstance(errors, list)


def test_validate_schema_none_loads_default() -> None:
    errors = validate({})
    assert isinstance(errors, list)
    assert any("schema_name" in e for e in errors)


def test_validate_summary_requires_status_and_machine_readable() -> None:
    data = {"schema_name": "sdlc.subagent.summary", "schema_version": "1.0.0"}
    errors = validate(data, schema={"type": "object"})
    assert "<root>: 'status' is a required property" in errors
    assert "<root>: 'machine_readable' is a required property" in errors


def test_validate_summary_machine_readable_missing_keys() -> None:
    data = {
        "schema_name": "sdlc.subagent.summary",
        "schema_version": "1.0.0",
        "status": "done",
        "machine_readable": {},
    }
    errors = validate(data, schema={"type": "object"})
    assert "machine_readable: 'decision_id' is a required property" in errors
    assert "machine_readable: 'evidencia' is a required property" in errors


def test_validate_summary_invalid_top_status_flagged() -> None:
    data = {
        "schema_name": "sdlc.subagent.summary",
        "schema_version": "1.0.0",
        "status": "completed",
        "machine_readable": {"decision_id": "D-1", "evidencia": "e", "status": "done"},
    }
    errors = validate(data, schema={"type": "object"})
    assert any("status de execução inválido 'completed'" in e for e in errors)


def test_validate_summary_machine_readable_not_dict_skips_invariant() -> None:
    data = {
        "schema_name": "sdlc.subagent.summary",
        "schema_version": "1.0.0",
        "status": "completed",
        "machine_readable": "notadict",
    }
    errors = validate(data, schema={"type": "object"})
    assert "<root>: 'machine_readable' is a required property" in errors
    assert not any("status de execução inválido" in e for e in errors)


def test_validate_no_candidates_falls_back_to_root_schema() -> None:
    schema = {"type": "object", "required": ["foo"]}
    errors = validate({"schema_name": "x", "schema_version": "1.0.0"}, schema=schema)
    assert any("foo" in e for e in errors)


def test_validate_branch_candidates_path_with_schema_key() -> None:
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$defs": {"envelope": {"type": "object", "required": ["bar"]}},
    }
    data = {"schema_name": "sdlc.task.delegation", "schema_version": "1.0.0"}
    errors = validate(data, schema=schema)
    assert any("bar" in e for e in errors)


def test_validate_branch_candidates_best_effort_pick() -> None:
    schema = {
        "$defs": {
            "envelope": {"type": "object", "required": ["bar"]},
            "subagent_summary": {"type": "object"},
        }
    }
    data = {"schema_name": "other.name", "schema_version": "1.0.0"}
    errors = validate(data, schema=schema)
    assert isinstance(errors, list)


def test_validate_without_jsonschema_reports_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cv, "_jsonschema_available", lambda: False)
    errors = validate({"schema_name": "x", "schema_version": "1.0.0"}, schema={"type": "object"})
    assert any("jsonschema não instalado" in e for e in errors)


def test_validate_with_jsonschema_missing_symbol(monkeypatch: pytest.MonkeyPatch) -> None:
    import types

    fake = types.ModuleType("jsonschema")  # sem Draft202012Validator
    monkeypatch.setitem(sys.modules, "jsonschema", fake)
    errors = validate({"schema_name": "x", "schema_version": "1.0.0"}, schema={"type": "object"})
    assert isinstance(errors, list)


# ---------------------------------------------------------------------------
# contract_validator — validate_file / is_missing_required / transitions
# ---------------------------------------------------------------------------


def test_validate_file_not_found(tmp_path: Path) -> None:
    errors = validate_file(tmp_path / "missing.json")
    assert errors and "arquivo não encontrado" in errors[0]


def test_validate_file_invalid_json(tmp_path: Path) -> None:
    p = tmp_path / "bad.json"
    p.write_text("{not json", encoding="utf-8")
    errors = validate_file(p)
    assert errors and "JSON inválido" in errors[0]


def test_validate_file_oserror(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    p = tmp_path / "ok.json"
    p.write_text("{}", encoding="utf-8")

    def boom(path: Path) -> object:
        raise OSError("disk gone")

    monkeypatch.setattr(cv, "_load_json", boom)
    errors = validate_file(p)
    assert errors and "não foi possível ler" in errors[0]


def test_validate_file_with_explicit_schema(tmp_path: Path) -> None:
    data_file = tmp_path / "data.json"
    data_file.write_text('{"schema_name": "x", "schema_version": "1.0.0"}', encoding="utf-8")
    schema_file = tmp_path / "schema.json"
    schema_file.write_text('{"type": "object"}', encoding="utf-8")
    assert validate_file(data_file, schema_path=schema_file) == []


def test_is_missing_required_true_and_false() -> None:
    assert is_missing_required(["<root>: 'x' is a required property"]) is True
    assert is_missing_required(["outra coisa"]) is False


def test_validate_transition_all_branches() -> None:
    assert validate_transition("done", "approved") == (
        False,
        "G1: done->approved bloqueado (vedação de auto-aceite)",
    )
    assert validate_transition("completed", "approved")[0] is False
    assert validate_transition("completed", "approved", manual_confirmation=True) == (True, "ok")
    assert validate_transition("done", "completed", autonomy_class="A") == (True, "ok")
    assert validate_transition("done", "completed", autonomy_class="B") == (True, "ok")
    assert validate_transition("done", "completed", autonomy_class="C")[0] is False
    assert validate_transition("done", "completed")[0] is False
    assert validate_transition("in_progress", "blocked") == (True, "ok")
    assert validate_transition("completed", "rejected")[0] is False
    assert validate_transition("completed", "rejected", manual_confirmation=True) == (True, "ok")
    assert validate_transition("blocked", "done") == (True, "ok")


def test_contract_validator_class_with_and_without_schema(tmp_path: Path) -> None:
    schema_file = tmp_path / "schema.json"
    schema_file.write_text('{"type": "object"}', encoding="utf-8")
    validator = ContractValidator(schema_path=schema_file)
    assert validator.validate({"schema_name": "x", "schema_version": "1.0.0"}) == []
    data_file = tmp_path / "data.json"
    data_file.write_text('{"schema_name": "x", "schema_version": "1.0.0"}', encoding="utf-8")
    assert validator.validate_file(data_file) == []
    default_validator = ContractValidator()
    assert isinstance(default_validator.validate({}), list)


# ---------------------------------------------------------------------------
# contract_validator — main()
# ---------------------------------------------------------------------------


def _permissive_schema(tmp_path: Path) -> Path:
    p = tmp_path / "schema.json"
    p.write_text('{"type": "object"}', encoding="utf-8")
    return p


def test_main_invalid_inline_json_returns_invalid(tmp_path: Path) -> None:
    schema = _permissive_schema(tmp_path)
    assert cv.main(["--data", "{not json", "--schema", str(schema)]) == EXIT_INVALID


def test_main_missing_required_returns_5(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    schema = _permissive_schema(tmp_path)
    assert cv.main(["--data", "{}", "--schema", str(schema)]) == EXIT_MISSING_REQUIRED
    assert "INVALID" in capsys.readouterr().out


def test_main_invalid_without_required_returns_invalid(tmp_path: Path) -> None:
    schema = _permissive_schema(tmp_path)
    data = {
        "schema_name": "sdlc.subagent.summary",
        "schema_version": "1.0.0",
        "status": "completed",
        "machine_readable": {"decision_id": "D-1", "evidencia": "e", "status": "done"},
    }
    assert cv.main(["--data", json.dumps(data), "--schema", str(schema)]) == EXIT_INVALID


def test_main_valid_returns_ok(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    schema = _permissive_schema(tmp_path)
    data = {
        "schema_name": "sdlc.subagent.summary",
        "schema_version": "1.0.0",
        "status": "done",
        "machine_readable": {"decision_id": "D-1", "evidencia": "e", "status": "done"},
    }
    assert cv.main(["--data", json.dumps(data), "--schema", str(schema)]) == EXIT_OK
    assert "VALID" in capsys.readouterr().out


def test_main_input_file_not_found(tmp_path: Path) -> None:
    schema = _permissive_schema(tmp_path)
    assert cv.main([str(tmp_path / "nope.json"), "--schema", str(schema)]) == EXIT_INVALID


def test_main_input_file_invalid_json(tmp_path: Path) -> None:
    schema = _permissive_schema(tmp_path)
    bad = tmp_path / "bad.json"
    bad.write_text("{not json", encoding="utf-8")
    assert cv.main([str(bad), "--schema", str(schema)]) == EXIT_INVALID


def test_main_input_file_oserror(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    schema = _permissive_schema(tmp_path)
    ok = tmp_path / "ok.json"
    ok.write_text("{}", encoding="utf-8")

    def boom(path: Path) -> object:
        raise OSError("disk gone")

    monkeypatch.setattr(cv, "_load_json", boom)
    assert cv.main([str(ok), "--schema", str(schema)]) == EXIT_INVALID


def test_main_input_file_valid(tmp_path: Path) -> None:
    schema = _permissive_schema(tmp_path)
    good = tmp_path / "good.json"
    good.write_text(
        json.dumps(
            {
                "schema_name": "sdlc.subagent.summary",
                "schema_version": "1.0.0",
                "status": "done",
                "machine_readable": {
                    "decision_id": "D-1",
                    "evidencia": "e",
                    "status": "done",
                },
            }
        ),
        encoding="utf-8",
    )
    assert cv.main([str(good), "--schema", str(schema)]) == EXIT_OK


def test_main_no_input_returns_invalid(tmp_path: Path) -> None:
    schema = _permissive_schema(tmp_path)
    assert cv.main(["--schema", str(schema)]) == EXIT_INVALID


def test_main_schema_not_found_returns_invalid(tmp_path: Path) -> None:
    assert cv.main(["--data", "{}", "--schema", str(tmp_path / "nope.json")]) == EXIT_INVALID


def test_main_schema_invalid_json_returns_invalid(tmp_path: Path) -> None:
    bad_schema = tmp_path / "bad_schema.json"
    bad_schema.write_text("{not json", encoding="utf-8")
    assert cv.main(["--data", "{}", "--schema", str(bad_schema)]) == EXIT_INVALID


def test_main_default_schema_loads() -> None:
    assert cv.main(["--data", "{}"]) == EXIT_MISSING_REQUIRED


# ---------------------------------------------------------------------------
# exit_codes
# ---------------------------------------------------------------------------


def test_classify_exit_code_all_codes() -> None:
    assert classify_exit_code(0) == "proceed"
    assert classify_exit_code(1) == "coding"
    assert classify_exit_code(2) == "coding"
    assert classify_exit_code(3) == "coding"
    assert classify_exit_code(4) == "blocked"
    assert classify_exit_code(5) == "blocked"
    assert classify_exit_code(6) == "pr_blocked"
    assert classify_exit_code(10) == "escalate"
    assert classify_exit_code(64) == "escalate"
    assert classify_exit_code(100) == "escalate"
    assert classify_exit_code(130) == "interrupt"
    assert classify_exit_code(7) == "escalate"


def test_apply_exit_code_proceed_records_nothing() -> None:
    state = new_state(task_id="t-0", autonomy_class="A")
    assert apply_exit_code(state, 0, task_id="t-0") == "proceed"
    assert state["errors"] == []


def test_apply_exit_code_sigint_marks_failure_and_blocks() -> None:
    state = new_state(task_id="t-1", autonomy_class="A")
    state["tasks"].append({"task_id": "t-1", "status": "in_progress"})
    action = apply_exit_code(state, 130, task_id="t-1")
    assert action == "interrupt"
    assert state["integration_test_output"] == "failure"
    assert state["tasks"][0]["status"] == "blocked"
    assert state["errors"][-1]["error_class"] == "critico"


def test_apply_exit_code_coverage_blocks_pr() -> None:
    state = new_state(task_id="t-2", autonomy_class="A")
    state["tasks"].append({"task_id": "t-2", "status": "done"})
    state["pr_ready"] = True
    action = apply_exit_code(state, 6, task_id="t-2")
    assert action == "pr_blocked"
    assert state["pr_ready"] is False
    assert state["tasks"][0]["status"] == "blocked"
    assert state["errors"][-1]["error_class"] == "lacuna"


def test_apply_exit_code_arch_inconsistency_escalates_and_classifies_lacuna() -> None:
    state = new_state(task_id="t-3", autonomy_class="A")
    state["tasks"].append({"task_id": "t-3", "status": "in_progress"})
    action = apply_exit_code(state, 10, task_id="t-3")
    assert action == "escalate"
    assert state["tasks"][0]["status"] == "blocked"
    assert state["errors"][-1]["error_class"] == "lacuna"


def test_apply_exit_code_fatal_min_classifies_lacuna() -> None:
    state = new_state(task_id="t-4", autonomy_class="A")
    state["tasks"].append({"task_id": "t-4", "status": "in_progress"})
    action = apply_exit_code(state, 64, task_id="t-4")
    assert action == "escalate"
    assert state["errors"][-1]["error_class"] == "lacuna"


def test_apply_exit_code_unknown_code_classifies_ambiente() -> None:
    state = new_state(task_id="t-5", autonomy_class="A")
    state["tasks"].append({"task_id": "t-5", "status": "in_progress"})
    action = apply_exit_code(state, 7, task_id="t-5")
    assert action == "escalate"
    assert state["errors"][-1]["error_class"] == "ambiente"


def test_apply_exit_code_without_task_id_skips_task_loop() -> None:
    state = new_state(task_id="t-6", autonomy_class="A")
    state["tasks"].append({"task_id": "t-6", "status": "in_progress"})
    action = apply_exit_code(state, 4)
    assert action == "blocked"
    assert state["tasks"][0]["status"] == "in_progress"


def test_apply_exit_code_coding_action_does_not_block_task() -> None:
    state = new_state(task_id="t-7", autonomy_class="A")
    state["tasks"].append({"task_id": "other", "status": "in_progress"})
    state["tasks"].append({"task_id": "t-7", "status": "in_progress"})
    action = apply_exit_code(state, 1, task_id="t-7")
    assert action == "coding"
    assert state["tasks"][0]["status"] == "in_progress"
    assert state["tasks"][1]["status"] == "in_progress"
    assert state["errors"][-1]["error_class"] == "logica"


def test_autopromote_rejects_class_c_and_missing_done() -> None:
    state = new_state(task_id="t-8", autonomy_class="C")
    state["tasks"].append({"task_id": "t-8", "status": "done"})
    assert autopromote_done_to_completed(state, "t-8", "C") is False
    assert state["tasks"][0]["status"] == "done"

    state2 = new_state(task_id="t-9", autonomy_class="A")
    state2["tasks"].append({"task_id": "t-9", "status": "in_progress"})
    assert autopromote_done_to_completed(state2, "t-9", "A") is False

    state3 = new_state(task_id="t-10", autonomy_class="A")
    assert autopromote_done_to_completed(state3, "t-10", "A") is False


def test_notify_maintainer_sets_flag_and_appends_message() -> None:
    state = new_state(task_id="t-11", autonomy_class="C")
    notify_maintainer(state, "guardrail G1 acionado")
    assert state["global_context"]["maintainer_notified"] is True
    assert "guardrail G1 acionado" in state["global_context"]["notifications"]


def test_exit_code_handler_wrapper() -> None:
    state = new_state(task_id="t-12", autonomy_class="A")
    state["tasks"].append({"task_id": "t-12", "status": "in_progress"})
    handler = ExitCodeHandler()
    assert handler.classify(6) == "pr_blocked"
    assert handler.handle(state, 4, task_id="t-12") == "blocked"
    assert state["tasks"][0]["status"] == "blocked"


# ---------------------------------------------------------------------------
# human_review
# ---------------------------------------------------------------------------


def _valid_approval() -> dict[str, object]:
    return {
        "status": "approved",
        "evidence_refs": ["ev-1"],
        "human_interaction_ref": "session-1",
        "decided_by": "humano",
        "subject_ref": "t-1",
    }


def test_write_approval_without_manual_confirmation_blocks_all_tasks() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    state["tasks"].append({"task_id": "t-1", "status": "done"})
    state["tasks"].append({"task_id": "t-2", "status": "done"})
    with pytest.raises(GuardrailViolation):
        write_approval(state, {"status": "approved"}, manual_confirmation=False)
    assert all(t["status"] == "blocked" for t in state["tasks"])


def test_write_approval_without_manual_confirmation_blocks_only_subject() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    state["tasks"].append({"task_id": "t-1", "status": "done"})
    state["tasks"].append({"task_id": "t-2", "status": "done"})
    with pytest.raises(GuardrailViolation):
        write_approval(state, {"status": "approved", "subject_ref": "t-1"})
    assert state["tasks"][0]["status"] == "blocked"
    assert state["tasks"][1]["status"] == "done"


def test_write_approval_missing_evidence_refs() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    approval = _valid_approval()
    del approval["evidence_refs"]
    with pytest.raises(GuardrailViolation, match="evidence_refs"):
        write_approval(state, approval, manual_confirmation=True)


def test_write_approval_missing_human_interaction_ref() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    approval = _valid_approval()
    del approval["human_interaction_ref"]
    with pytest.raises(GuardrailViolation, match="human_interaction_ref"):
        write_approval(state, approval, manual_confirmation=True)


def test_write_approval_missing_decided_by() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    approval = _valid_approval()
    del approval["decided_by"]
    with pytest.raises(GuardrailViolation, match="decided_by"):
        write_approval(state, approval, manual_confirmation=True)


def test_write_approval_valid_appends() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    write_approval(state, _valid_approval(), manual_confirmation=True)
    assert state["approvals"][-1]["status"] == "approved"


def test_human_review_node_class_ab_returns_state_untouched() -> None:
    state = new_state(task_id="t-1", autonomy_class="A")
    out = human_review_node(state, autonomy_class="A", approval=_valid_approval())
    assert out is state
    assert state["approvals"] == []


def test_human_review_node_class_c_without_approval_returns_state() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    out = human_review_node(state, autonomy_class="C", approval=None)
    assert out is state
    assert state["approvals"] == []


def test_human_review_node_guardrail_notifies_maintainer() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    state["tasks"].append({"task_id": "t-1", "status": "done"})
    with pytest.raises(GuardrailViolation):
        human_review_node(state, autonomy_class="C", approval=_valid_approval())
    assert state["global_context"]["maintainer_notified"] is True
    assert "guardrail G1 acionado" in state["global_context"]["notifications"]


def test_human_review_class_wrapper() -> None:
    state = new_state(task_id="t-1", autonomy_class="C")
    reviewer = HumanReview()
    out = reviewer.review(state, approval=None)
    assert out is state


# ---------------------------------------------------------------------------
# stubs/infra
# ---------------------------------------------------------------------------


def test_find_real_pyproject_from_file_start(tmp_path: Path) -> None:
    f = tmp_path / "marker.txt"
    f.write_text("x", encoding="utf-8")
    assert _find_real_pyproject(f) is None  # tmp_path e pais não têm pyproject.toml


def test_read_coverage_threshold_none_returns_default() -> None:
    assert _read_coverage_threshold(None) == 50


def test_read_coverage_threshold_missing_file_returns_default(tmp_path: Path) -> None:
    assert _read_coverage_threshold(tmp_path / "nope.toml") == 50


def test_read_coverage_threshold_invalid_toml_returns_default(tmp_path: Path) -> None:
    p = tmp_path / "pyproject.toml"
    p.write_text("[tool.coverage.report\nfail_under = ", encoding="utf-8")
    assert _read_coverage_threshold(p) == 50


def test_read_coverage_threshold_missing_key_returns_default(tmp_path: Path) -> None:
    p = tmp_path / "pyproject.toml"
    p.write_text("[tool.coverage.report]\nshow_missing = true\n", encoding="utf-8")
    assert _read_coverage_threshold(p) == 50


def test_read_coverage_threshold_non_numeric_returns_default(tmp_path: Path) -> None:
    p = tmp_path / "pyproject.toml"
    p.write_text('[tool.coverage.report]\nfail_under = "abc"\n', encoding="utf-8")
    assert _read_coverage_threshold(p) == 50


def test_read_coverage_threshold_reads_real_value() -> None:
    assert _read_coverage_threshold(REAL_PYPROJECT) == _real_fail_under()


def test_stub_database_with_file_path(tmp_path: Path) -> None:
    db = StubDatabase(path=str(tmp_path / "stub.sqlite"))
    conn = db.connect()
    conn.execute("CREATE TABLE t (x INTEGER)")
    db.close()
    db.close()  # idempotente: segundo close não faz nada
    assert db._conn is None


def test_stub_database_context_manager() -> None:
    with StubDatabase() as db:
        assert db.connection is not None


def test_create_stub_db_use_file_roundtrip() -> None:
    with create_stub_db(use_file=True) as db:
        assert db.path is not None
        path = Path(db.path)
        assert path.exists()
    assert not path.exists()  # descartado ao sair do contexto


def test_create_stub_db_use_file_unlink_oserror_is_swallowed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def boom(self: Path, *args: object, **kwargs: object) -> None:
        raise OSError("locked")

    monkeypatch.setattr(Path, "unlink", boom)
    with create_stub_db(use_file=True) as db:
        assert db.path is not None


def test_write_stub_pyproject_falls_back_to_repo_pyproject(tmp_path: Path) -> None:
    stub = write_stub_pyproject(tmp_path)
    text = stub.read_text(encoding="utf-8")
    assert f"fail_under = {_real_fail_under()}" in text


def test_stub_environment_context_manager() -> None:
    with StubEnvironment() as env:
        assert env.root is not None and env.root.exists()
        assert env.db is not None
        stub = env.root / "pyproject.toml"
        assert f"fail_under = {_real_fail_under()}" in stub.read_text(encoding="utf-8")
