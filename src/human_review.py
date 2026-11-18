"""Aprovacao manual para classe C (approved) + guardrail G1 (Fase 1).

G1: se agente LLM tentar gravar 'approved' sem confirmacao manual ->
abortar e reverter para 'blocked'.
"""

from __future__ import annotations

from typing import Any

from .exit_codes import notify_maintainer
from .state import AgentState


class GuardrailViolation(Exception):
    """Violacao de guardrail (ex.: approved sem confirmacao manual)."""


def write_approval(
    state: AgentState,
    approval: dict[str, Any],
    *,
    manual_confirmation: bool = False,
) -> None:
    """Escreve uma aprovacao no estado, aplicando o guardrail G1."""
    status = approval.get("status")

    if status == "approved" and not manual_confirmation:
        # Reverter tarefas afetadas para blocked
        subject = approval.get("subject_ref")
        for task in state["tasks"]:
            if subject is None or task.get("task_id") == subject:
                task["status"] = "blocked"
        raise GuardrailViolation(
            "approved requer confirmacao manual e sincrona (G1)"
        )

    if status == "approved":
        if not approval.get("evidence_refs"):
            raise GuardrailViolation("approved requer evidence_refs nao vazio")
        if not approval.get("human_interaction_ref"):
            raise GuardrailViolation("approved requer human_interaction_ref")
        if not approval.get("decided_by"):
            raise GuardrailViolation("approved requer decided_by humano")

    state["approvals"].append(dict(approval))


def human_review_node(
    state: AgentState,
    *,
    autonomy_class: str = "C",
    manual_confirmation: bool = False,
    approval: dict[str, Any] | None = None,
) -> AgentState:
    """No de human review do grafo.

    Para classes A/B nao exige decisao manual. Para classe C, approved
    exige manual_confirmation=True.
    """
    if autonomy_class in ("A", "B"):
        # Sem notificacao ao mantenedor (R4)
        return state

    if approval is None:
        return state

    try:
        write_approval(state, approval, manual_confirmation=manual_confirmation)
    except GuardrailViolation:
        # Reverter para blocked ja feito em write_approval
        notify_maintainer(state, "guardrail G1 acionado")
        raise
    return state


# Aliases
human_review_gate = human_review_node
review_node = human_review_node
manual_approval = write_approval
record_approval = write_approval
approve = write_approval
guardrail_g1 = write_approval


class HumanReview:
    def review(
        self,
        state: AgentState,
        *,
        autonomy_class: str = "C",
        manual_confirmation: bool = False,
        approval: dict[str, Any] | None = None,
    ) -> AgentState:
        return human_review_node(
            state,
            autonomy_class=autonomy_class,
            manual_confirmation=manual_confirmation,
            approval=approval,
        )


human_review = HumanReview()
HumanReviewGate = HumanReview
G1Guardrail = write_approval

