"""Portoes de qualidade com thresholds absolutos (Fase 1).

Thresholds absolutos (D-V0-01 resolvido: Python 3.12 + pytest + ruff + mypy):
- cobertura minima >= 50%
- erros criticos de linting = 0
Comparacoes de regressao contra historico inexistente sao ignoradas (R7).
"""

from __future__ import annotations

from .observability import get_logger, metrics

logger = get_logger(__name__)

# Thresholds absolutos (D-V0-01): sem aliases duplicados — nomes canônicos apenas.
MIN_COVERAGE_PERCENT: float = 50.0
MAX_CRITICAL_ERRORS: int = 0


def quality_gate(
    coverage_percent: float,
    critical_errors: int,
) -> tuple[bool, str]:
    """Avalia o portao de qualidade com thresholds absolutos.

    Retorna (aprovado, motivo).
    """
    if coverage_percent < MIN_COVERAGE_PERCENT:
        reason = f"cobertura {coverage_percent} < {MIN_COVERAGE_PERCENT}"
        metrics.increment("gate_fail")
        logger.warning(
            "quality_gate FAIL: %s",
            reason,
            extra={"event": "quality_gate.fail", "reason": reason,
                   "coverage_percent": coverage_percent,
                   "critical_errors": critical_errors},
        )
        return False, reason
    if critical_errors > MAX_CRITICAL_ERRORS:
        reason = f"erros criticos {critical_errors} > {MAX_CRITICAL_ERRORS}"
        metrics.increment("gate_fail")
        logger.warning(
            "quality_gate FAIL: %s",
            reason,
            extra={"event": "quality_gate.fail", "reason": reason,
                   "coverage_percent": coverage_percent,
                   "critical_errors": critical_errors},
        )
        return False, reason
    metrics.increment("gate_pass")
    logger.info(
        "quality_gate PASS",
        extra={"event": "quality_gate.pass",
               "coverage_percent": coverage_percent,
               "critical_errors": critical_errors},
    )
    return True, "ok"


class QualityGate:
    def check(self, coverage_percent: float, critical_errors: int) -> tuple[bool, str]:
        return quality_gate(coverage_percent, critical_errors)

    def run(self, coverage_percent: float, critical_errors: int) -> tuple[bool, str]:
        return quality_gate(coverage_percent, critical_errors)

