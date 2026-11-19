"""Observabilidade mínima (DEC-032 F2.3-téc) — stdlib apenas, sem backend externo.

Fornece:
- ``get_logger(name)``: logger JSON estruturado (uma linha JSON por registro),
  com ``ts`` (ISO-8601 UTC), ``level``, ``logger``, ``msg``, ``correlation_id``
  (do registro ou do contextvar), ``event`` (se fornecido via ``extra``) e
  campos extras. Handler ``StreamHandler(sys.stderr)``, ``propagate=False``.
- Context de ``correlation_id`` via ``contextvars``: ``set_correlation_id``,
  ``get_correlation_id``, ``new_correlation_id`` (uuid4).
- Métricas técnicas locais: contadores in-memory (runs, retries, gate_pass,
  gate_fail) com ``snapshot()``. Sem persistência, sem backend, sem rede.

Nada aqui emite valores de segredos; o chamador é responsável por não passar
segredos em ``msg``/extras.
"""

from __future__ import annotations

import json
import logging
import sys
import threading
import uuid
from contextvars import ContextVar, Token
from datetime import datetime, timezone
from typing import Any

__all__ = [
    "JSONFormatter",
    "Metrics",
    "get_logger",
    "set_correlation_id",
    "get_correlation_id",
    "new_correlation_id",
    "metrics",
]

_correlation_id_var: ContextVar[str | None] = ContextVar(
    "sdlc_correlation_id", default=None
)

_STANDARD_ATTRS = frozenset(
    logging.makeLogRecord({}).__dict__.keys()
) | {"message", "asctime", "taskName"}


def new_correlation_id() -> str:
    """Gera um novo correlation_id (uuid4)."""
    return str(uuid.uuid4())


def set_correlation_id(correlation_id: str | None) -> Token[str | None]:
    """Define o correlation_id no contexto atual; retorna token para reset()."""
    return _correlation_id_var.set(correlation_id)


def get_correlation_id() -> str | None:
    """Retorna o correlation_id do contexto atual (ou None)."""
    return _correlation_id_var.get()


class JSONFormatter(logging.Formatter):
    """Formata cada registro como uma linha JSON."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "ts": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        cid = getattr(record, "correlation_id", None) or get_correlation_id()
        if cid:
            payload["correlation_id"] = cid
        event = getattr(record, "event", None)
        if event:
            payload["event"] = event
        for key, value in record.__dict__.items():
            if key in _STANDARD_ATTRS or key in ("correlation_id", "event"):
                continue
            if key.startswith("_"):
                continue
            payload[key] = value
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False, default=str)


def get_logger(name: str) -> logging.Logger:
    """Retorna logger JSON estruturado (stderr, propagate=False).

    Idempotente: chamadas repetidas para o mesmo nome não duplicam handlers.
    """
    logger = logging.getLogger(name)
    if getattr(logger, "_sdlc_json_configured", False):
        return logger
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(JSONFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    logger._sdlc_json_configured = True  # type: ignore[attr-defined]
    return logger


class Metrics:
    """Contadores in-memory thread-safe (sem persistência/backend)."""

    def __init__(self) -> None:
        self._counters: dict[str, int] = {}
        self._lock = threading.Lock()

    def increment(self, name: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("amount deve ser >= 0")
        with self._lock:
            self._counters[name] = self._counters.get(name, 0) + amount

    def snapshot(self) -> dict[str, int]:
        with self._lock:
            return dict(self._counters)

    def reset(self) -> None:
        with self._lock:
            self._counters.clear()


metrics = Metrics()
