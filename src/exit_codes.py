"""Manipulador deterministico de exit codes (Fase 1).

Mapeamento (task spec):
- exit 0  -> prosseguir (autopromocao done->completed para A/B)
- exit 1-3 -> retornar a Coding (falha de lint/tipo/teste)
- exit 4  -> bloquear (falha de ambiente) [T2]
- exit 5  -> bloquear (falha de seguranca)
- exit 6  -> bloquear PR generation (cobertura abaixo do threshold)
- exit 10 / >=64 -> escalar (erro de ambiente/fatal)
- exit 130 -> interromper (SIGINT)
"""

from __future__ import annotations

from typing import Literal

from .state import AgentState

EXIT_PROCEED = 0
EXIT_LINT_FAILURE = 1
EXIT_TYPE_FAILURE = 2
EXIT_TEST_FAILURE = 3
EXIT_ENV_FAILURE = 4
EXIT_SECURITY_FAILURE = 5
EXIT_COVERAGE_BELOW = 6
EXIT_ARCH_INCONSISTENCY = 10
EXIT_SIGINT = 130
EXIT_FATAL_MIN = 64

ExitAction = Literal[
    "proceed",
    "coding",
    "blocked",
    "pr_blocked",
    "escalate",
    "interrupt",
]


def classify_exit_code(code: int) -> ExitAction:
    """Classifica o exit code em uma acao deterministica."""
    if code == EXIT_PROCEED:
        return "proceed"
    if code in (EXIT_LINT_FAILURE, EXIT_TYPE_FAILURE, EXIT_TEST_FAILURE):
        return "coding"
    if code == EXIT_ENV_FAILURE:
        return "blocked"
    if code == EXIT_SECURITY_FAILURE:
        return "blocked"
    if code == EXIT_COVERAGE_BELOW:
        return "pr_blocked"
    if code == EXIT_SIGINT:
        return "interrupt"
    if code == EXIT_ARCH_INCONSISTENCY or code >= EXIT_FATAL_MIN:
        return "escalate"
    if 1 <= code <= 4:
        return "coding"
    return "escalate"


def _error_class_for(code: int) -> str:
    mapping = {
        EXIT_LINT_FAILURE: "logica",
        EXIT_TYPE_FAILURE: "logica",
        EXIT_TEST_FAILURE: "logica",
        EXIT_ENV_FAILURE: "ambiente",
        EXIT_SECURITY_FAILURE: "logica",
        EXIT_COVERAGE_BELOW: "lacuna",
        EXIT_ARCH_INCONSISTENCY: "lacuna",
    }
    if code in mapping:
        return mapping[code]
    if code == EXIT_SIGINT:
        return "critico"
    if code >= EXIT_FATAL_MIN:
        return "lacuna"
    return "ambiente"


def apply_exit_code(
    state: AgentState,
    exit_code: int,
    *,
    task_id: str | None = None,
    source_gate: str = "make",
) -> ExitAction:
    """Aplica o exit code ao estado, registrando erro/evidencia quando != 0."""
    action = classify_exit_code(exit_code)
    if exit_code == EXIT_PROCEED:
        return action

    state["errors"].append(
        {
            "error_id": f"ERR-{len(state['errors']) + 1:04d}",
            "task_id": task_id,
            "source_gate": source_gate,
            "exit_code": exit_code,
            "error_class": _error_class_for(exit_code),
            "message": f"exit code {exit_code}",
            "resolved": False,
        }
    )

    if task_id is not None:
        for task in state["tasks"]:
            if task.get("task_id") == task_id:
                if action in ("blocked", "escalate", "interrupt", "pr_blocked"):
                    task["status"] = "blocked"

    if action == "pr_blocked":
        state["pr_ready"] = False
    if action == "interrupt":
        state["integration_test_output"] = "failure"

    return action


def autopromote_done_to_completed(
    state: AgentState,
    task_id: str,
    autonomy_class: str,
) -> bool:
    """Autopromocao done -> completed para classes A/B quando exit code == 0.

    Nao notifica o mantenedor humano para classes A/B (R4).
    """
    if autonomy_class not in ("A", "B"):
        return False
    for task in state["tasks"]:
        if task.get("task_id") == task_id and task.get("status") == "done":
            task["status"] = "completed"
            return True
    return False


def notify_maintainer(state: AgentState, message: str) -> None:
    """Notificacao ao mantenedor (usada apenas para classe C / bloqueios)."""
    state["global_context"]["maintainer_notified"] = True
    state["global_context"].setdefault("notifications", []).append(message)


# Aliases para compatibilidade com nomes alternativos.
handle_exit_code = apply_exit_code
process_exit_code = apply_exit_code
auto_promote = autopromote_done_to_completed
promote_done_to_completed = autopromote_done_to_completed
handle_exit = apply_exit_code


class ExitCodeHandler:
    """Wrapper de compatibilidade."""

    def handle(
        self,
        state: AgentState,
        exit_code: int,
        *,
        task_id: str | None = None,
        source_gate: str = "make",
    ) -> ExitAction:
        return apply_exit_code(state, exit_code, task_id=task_id, source_gate=source_gate)

    def classify(self, code: int) -> ExitAction:
        return classify_exit_code(code)


exit_code_handler = ExitCodeHandler()
EXIT_OK = EXIT_PROCEED
EXIT_SUCCESS = EXIT_PROCEED

