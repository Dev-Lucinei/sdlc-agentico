"""Estado tipado do grafo de orquestracao (Fase 1).

LACUNA: stack LangGraph pendente de D-V0-01 (adiado). Esta implementacao
simula o grafo como maquina de estados Python pura, sem dependencia de
langgraph, para validacao local isolada (R1).

Semantica canonica (docs/41): done != completed != approved.
"""

from __future__ import annotations

from typing import Any, Literal, TypedDict

AutonomyClass = Literal["A", "B", "C"]
TaskStatus = Literal[
    "todo",
    "ready",
    "in_progress",
    "done",
    "partial",
    "blocked",
    "completed",
    "approved",
]
ErrorClass = Literal["flaky", "ambiente", "logica", "critico", "lacuna"]


class AgentState(TypedDict):
    """Estado compartilhado do grafo."""

    global_context: dict[str, Any]
    ads: list[dict[str, Any]]
    tasks: list[dict[str, Any]]
    errors: list[dict[str, Any]]
    approvals: list[dict[str, Any]]
    integration_test_output: str | None
    pr_ready: bool


def new_state(
    *,
    request_id: str = "req-0",
    task_id: str = "task-0",
    autonomy_class: AutonomyClass = "A",
) -> AgentState:
    """Cria um AgentState inicial."""
    return {
        "global_context": {
            "request_id": request_id,
            "task_id": task_id,
            "autonomy_class": autonomy_class,
            "project": "sdlc-agentico",
            "maintainer_notified": False,
        },
        "ads": [],
        "tasks": [],
        "errors": [],
        "approvals": [],
        "integration_test_output": None,
        "pr_ready": False,
    }


def get_autonomy_class(state: AgentState) -> AutonomyClass:
    value = state["global_context"].get("autonomy_class", "A")
    if value in ("A", "B", "C"):
        return value  # type: ignore[return-value]
    return "A"


def set_maintainer_notified(state: AgentState, value: bool) -> None:
    state["global_context"]["maintainer_notified"] = value
