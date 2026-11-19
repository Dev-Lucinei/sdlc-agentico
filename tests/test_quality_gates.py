"""Testes de src/quality_gates.py — delegação da classe QualityGate (DEC-032 F2.5-téc)."""

from __future__ import annotations

from src.quality_gates import MAX_CRITICAL_ERRORS, MIN_COVERAGE_PERCENT, QualityGate


def test_quality_gate_class_delegates_to_quality_gate() -> None:
    gate = QualityGate()
    ok_run, reason_run = gate.run(MIN_COVERAGE_PERCENT, MAX_CRITICAL_ERRORS)
    ok_check, reason_check = gate.check(MIN_COVERAGE_PERCENT, MAX_CRITICAL_ERRORS)
    assert ok_run is True and reason_run == "ok"
    assert ok_check is True and reason_check == "ok"

    ok_fail, reason_fail = gate.run(0.0, MAX_CRITICAL_ERRORS)
    assert ok_fail is False and "cobertura" in reason_fail
    ok_fail_check, _ = gate.check(100.0, MAX_CRITICAL_ERRORS + 1)
    assert ok_fail_check is False
