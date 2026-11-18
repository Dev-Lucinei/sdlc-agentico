"""Portoes de qualidade com thresholds absolutos (Fase 1).

Thresholds absolutos (D-V0-01 resolvido: Python 3.12 + pytest + ruff + mypy):
- cobertura minima >= 50%
- erros criticos de linting = 0
Comparacoes de regressao contra historico inexistente sao ignoradas (R7).
"""

from __future__ import annotations

# D-V0-01 resolvido: thresholds absolutos (cobertura >= 50%, 0 erros criticos).
MIN_COVERAGE_PERCENT: float = 50.0
MAX_CRITICAL_ERRORS: int = 0

# Alias historico
MIN_COVERAGE = MIN_COVERAGE_PERCENT


def quality_gate(
    coverage_percent: float,
    critical_errors: int,
) -> tuple[bool, str]:
    """Avalia o portao de qualidade com thresholds absolutos.

    Retorna (aprovado, motivo).
    """
    if coverage_percent < MIN_COVERAGE_PERCENT:
        return False, (
            f"cobertura {coverage_percent} < {MIN_COVERAGE_PERCENT}"
        )
    if critical_errors > MAX_CRITICAL_ERRORS:
        return False, (
            f"erros criticos {critical_errors} > {MAX_CRITICAL_ERRORS}"
        )
    return True, "ok"


def gate_quality(coverage_percent: float, critical_errors: int) -> tuple[bool, str]:
    return quality_gate(coverage_percent, critical_errors)


def validate_quality(coverage_percent: float, critical_errors: int) -> tuple[bool, str]:
    return quality_gate(coverage_percent, critical_errors)


# Nomes alternativos
quality_gate_pass = quality_gate
run_quality_gate = quality_gate
check_quality = quality_gate


class QualityGate:
    def check(self, coverage_percent: float, critical_errors: int) -> tuple[bool, str]:
        return quality_gate(coverage_percent, critical_errors)

    def run(self, coverage_percent: float, critical_errors: int) -> tuple[bool, str]:
        return quality_gate(coverage_percent, critical_errors)


quality_gate_instance = QualityGate()
QualityGates = QualityGate

