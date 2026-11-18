"""Grafo de orquestracao (Fase 1) - simulacao local sem LangGraph.

Nos: design -> architecture -> coding -> tdd -> qa -> human_review -> pr_generation
"""

from __future__ import annotations

from typing import Any

from .exit_codes import apply_exit_code, autopromote_done_to_completed
from .human_review import human_review_node
from .quality_gates import quality_gate
from .state import AgentState, get_autonomy_class, transition_task


def node_design(state: AgentState) -> AgentState:
    state.setdefault("ads", [])
    return state


def node_architecture(state: AgentState) -> AgentState:
    return state


def node_coding(state: AgentState) -> AgentState:
    for task in state["tasks"]:
        if task.get("status") in ("todo", "ready"):
            task["status"] = "in_progress"
    return state


def node_tdd(state: AgentState) -> AgentState:
    return state


def node_qa(
    state: AgentState,
    *,
    exit_code: int = 0,
    task_id: str | None = None,
) -> AgentState:
    action = apply_exit_code(
        state, exit_code, task_id=task_id, source_gate="make test-unit"
    )
    state["global_context"]["last_exit_action"] = action
    if exit_code == 0:
        for task in state["tasks"]:
            if task_id is None or task.get("task_id") == task_id:
                if task.get("status") in ("in_progress", "done", None):
                    # marca done se ainda nao concluido
                    if task.get("status") != "completed":
                        task["status"] = "done"
    return state


def node_human_review(
    state: AgentState,
    *,
    autonomy_class: str | None = None,
    manual_confirmation: bool = False,
    approval: dict[str, Any] | None = None,
) -> AgentState:
    ac = autonomy_class or get_autonomy_class(state)
    return human_review_node(
        state,
        autonomy_class=ac,
        manual_confirmation=manual_confirmation,
        approval=approval,
    )


def node_pr_generation(
    state: AgentState,
    *,
    coverage_percent: float = 100.0,
    critical_errors: int = 0,
) -> AgentState:
    ok, reason = quality_gate(coverage_percent, critical_errors)
    if not ok:
        state["pr_ready"] = False
        state["errors"].append(
            {
                "error_id": f"ERR-{len(state['errors']) + 1:04d}",
                "source_gate": "coverage",
                "exit_code": 6,
                "error_class": "lacuna",
                "message": reason,
                "resolved": False,
            }
        )
        return state
    if state["integration_test_output"] == "success" and not state["pr_ready"]:
        state["pr_ready"] = True
    return state


def run_graph(
    state: AgentState,
    *,
    autonomy_class: str | None = None,
    exit_code: int = 0,
    task_id: str | None = None,
    coverage_percent: float = 100.0,
    critical_errors: int = 0,
    manual_confirmation: bool = False,
    approval: dict[str, Any] | None = None,
    notify: bool = False,
) -> AgentState:
    """Executa o grafo sequencialmente."""
    ac = autonomy_class or get_autonomy_class(state)

    node_design(state)
    node_architecture(state)
    node_coding(state)
    node_tdd(state)
    node_qa(state, exit_code=exit_code, task_id=task_id)

    # autopromocao para A/B quando exit code == 0
    if exit_code == 0 and task_id is not None and ac in ("A", "B"):
        promoted = autopromote_done_to_completed(state, task_id, ac)
        if promoted and not notify:
            # nao notificar mantenedor (R4)
            pass

    node_human_review(
        state,
        autonomy_class=ac,
        manual_confirmation=manual_confirmation,
        approval=approval,
    )
    node_pr_generation(
        state,
        coverage_percent=coverage_percent,
        critical_errors=critical_errors,
    )
    return state


# Aliases de nos (nomes alternativos)
design_node = node_design
architecture_node = node_architecture
coding_node = node_coding
tdd_node = node_tdd
qa_node = node_qa
human_review_gate_node = node_human_review
pr_generation_node = node_pr_generation
human_review_node_alias = node_human_review

# Aliases de execucao
build_graph = run_graph
orchestrate = run_graph
execute_graph = run_graph
run = run_graph
graph_run = run_graph
NODE_ORDER = ["design", "architecture", "coding", "tdd", "qa", "human_review", "pr_generation"]

# Exportar nos por nome string
NODES = {
    "design": node_design,
    "architecture": node_architecture,
    "coding": node_coding,
    "tdd": node_tdd,
    "qa": node_qa,
    "human_review": node_human_review,
    "pr_generation": node_pr_generation,
}



# Transições de estado (reexport)
transition_task_state = transition_task
graph_transition_task = transition_task
