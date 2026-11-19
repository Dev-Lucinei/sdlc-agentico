"""Estado tipado do grafo de orquestracao (Fase 1).

LACUNA: stack LangGraph pendente de D-V0-01 (adiado). Esta implementacao
simula o grafo como maquina de estados Python pura, sem dependencia de
langgraph, para validacao local isolada (R1).

Semantica canonica (docs/41): done != completed != approved.
"""

from __future__ import annotations

from typing import Any, Literal, TypedDict

from .observability import (
    get_correlation_id,
    get_logger,
    metrics,
    new_correlation_id,
    set_correlation_id,
)

logger = get_logger(__name__)

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


def _validate_transition_simple(
    from_status: str,
    to_status: str,
    *,
    manual_confirmation: bool = False,
    autonomy_class: str | None = None,
) -> tuple[bool, str]:
    """Regra de transição (done ⇏ completed ⇏ approved)."""
    fs = str(from_status)
    ts = str(to_status)
    if fs == "done" and ts == "approved":
        return False, "G1: done->approved bloqueado"
    if fs == "completed" and ts == "approved":
        if not manual_confirmation:
            return False, "approved requer human_review"
        return True, "ok"
    if fs == "done" and ts == "completed":
        if autonomy_class in ("A", "B"):
            return True, "ok"
        return False, "done->completed apenas autopromoção A/B"
    if ts == "blocked":
        return True, "ok"
    if fs == "completed" and ts == "rejected":
        if not manual_confirmation:
            return False, "rejected requer human_review"
        return True, "ok"
    return True, "ok"


def transition_task(*args: Any, **kwargs: Any) -> str:
    """Transição de estado de tarefa com validação de invariante.

    Assinatura canônica: transition_task(task_id, from_status, to_status,
    event_id, evidence_ref, ...). Também aceita AgentState como primeiro
    argumento posicional para compatibilidade.
    """
    state: dict[str, Any] | None = kwargs.pop("state", None)
    task_id: str | None = None
    from_status: str | None = None
    to_status: str | None = None
    event_id: str | None = kwargs.pop("event_id", None)
    evidence_ref: str | None = kwargs.pop("evidence_ref", None)
    manual_confirmation: bool = bool(kwargs.pop("manual_confirmation", False))
    autonomy_class: str | None = kwargs.pop("autonomy_class", None)
    db = kwargs.pop("db", None)
    persist: bool = bool(kwargs.pop("persist", True))
    correlation_id: str | None = kwargs.pop("correlation_id", None)

    positional = list(args)
    if positional and isinstance(positional[0], dict) and "tasks" in positional[0]:
        state = positional.pop(0)
    if positional:
        task_id = positional.pop(0)
    if positional:
        from_status = positional.pop(0)
    if positional:
        to_status = positional.pop(0)
    if positional and event_id is None:
        event_id = positional.pop(0)
    if positional and evidence_ref is None:
        evidence_ref = positional.pop(0)

    if task_id is None:
        raise ValueError("task_id obrigatório")
    if from_status is None or to_status is None:
        raise ValueError("from_status e to_status obrigatórios")

    if autonomy_class is None and isinstance(state, dict):
        autonomy_class = state.get("global_context", {}).get("autonomy_class")

    allowed, _reason = _validate_transition_simple(
        from_status, to_status, manual_confirmation=manual_confirmation,
        autonomy_class=autonomy_class,
    )
    result_status = str(to_status) if allowed else "blocked"

    # Correlation ID: propaga do kwarg ou do contexto; gera se ausente.
    cid = correlation_id or get_correlation_id() or new_correlation_id()
    set_correlation_id(cid)
    logger.info(
        "transição de estado %s->%s (%s) task=%s",
        from_status,
        to_status,
        result_status,
        task_id,
        extra={
            "event": "state.transition",
            "task_id": task_id,
            "from_status": from_status,
            "to_status": to_status,
            "result_status": result_status,
            "allowed": allowed,
            "correlation_id": cid,
        },
    )

    # Atualiza estado, se fornecido.
    if isinstance(state, dict):
        for task in state.get("tasks", []):
            if task.get("task_id") == task_id:
                task["status"] = result_status if allowed else "blocked"
                import datetime as _dt
                task["updated_at"] = (_dt.datetime.now(_dt.timezone.utc).isoformat()
                                      if "updated_at" in task else task.get("updated_at"))

    # Persiste evento no Event Log, se db fornecido.
    eid = event_id or str(__import__("uuid").uuid4())
    if persist and db is not None:
        try:
            insert_result = db.insert_event(
                "state.transition",
                {
                    "task_id": task_id,
                    "from_status": from_status,
                    "to_status": to_status,
                    "result_status": result_status,
                    "evidence_ref": evidence_ref,
                    "allowed": allowed,
                    "correlation_id": cid,
                },
                idempotency_key=f"transition:{task_id}:{eid}",
                event_id=eid,
            )
            if getattr(insert_result, "deduplicated", False):
                metrics.increment("event_log_persist_deduplicated")
                logger.debug(
                    "evento state.transition deduplicado (DEC-033): idempotency_key=%s",
                    f"transition:{task_id}:{eid}",
                    extra={
                        "event": "state.transition.persist_deduplicated",
                        "task_id": task_id,
                        "correlation_id": cid,
                    },
                )
        except Exception as exc:
            # Persistência do Event Log é best-effort: não bloqueia a transição,
            # mas o erro precisa ser visível (não silenciar — DEC-033 §c).
            metrics.increment("event_log_persist_failures")
            logger.warning(
                "falha ao persistir evento state.transition (best-effort): %s",
                exc,
                extra={
                    "event": "state.transition.persist_failed",
                    "task_id": task_id,
                    "error": str(exc),
                    "correlation_id": cid,
                },
            )

    return result_status


def validate_transition(*args: Any, **kwargs: Any) -> tuple[bool, str]:
    """Wrapper público para validação de transição (sem mutação)."""
    # Suporta chamada validate_transition(from, to, ...) ou (task_id, from, to,...)?
    # Detecta: se primeiro arg for status conhecido, trata como from.
    from_status = None
    to_status = None
    manual_confirmation = bool(kwargs.pop("manual_confirmation", False))
    autonomy_class = kwargs.pop("autonomy_class", None)
    positional = list(args)
    # Se 2+ args e primeiro não parece task_id? Heurística: status válidos.
    valid_statuses = {"todo", "ready", "in_progress", "done", "partial", "blocked",
                      "completed", "approved", "rejected", "pending", "condicional"}
    if len(positional) >= 2 and positional[0] in valid_statuses and positional[1] in valid_statuses:
        from_status = positional[0]
        to_status = positional[1]
    elif len(positional) >= 3:
        from_status = positional[1]
        to_status = positional[2]
    else:
        from_status = kwargs.pop("from_status", None)
        to_status = kwargs.pop("to_status", None)
    if from_status is None or to_status is None:
        raise ValueError("from_status e to_status obrigatórios")
    return _validate_transition_simple(
        str(from_status), str(to_status),
        manual_confirmation=manual_confirmation, autonomy_class=autonomy_class,
    )
