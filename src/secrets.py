"""Modelo de injeção segura de segredos (DEC-007).

- Segredos vêm de variáveis de ambiente (os.environ), nunca de código/arquivo.
- get_secret(key) lê de env var.
- mask_secret(value) mascara para logs.
- Proíbe escrita de segredos em logs, SoT e artefatos.
"""

from __future__ import annotations

import json
import os
from typing import Any

__all__ = [
    "SecretNotFoundError",
    "get_secret",
    "mask_secret",
    "contains_secret",
    "validate_no_secrets",
    "redact",
    "secret_env_keys",
]


class SecretNotFoundError(Exception):
    """Segredo ausente no ambiente."""


_SECRET_NAME_TOKENS = ("SECRET", "TOKEN", "PASSWORD", "PASSWD", "API_KEY",
                       "PRIVATE_KEY", "CREDENTIAL")


def secret_env_keys() -> list[str]:
    """Lista chaves de ambiente que parecem conter segredos."""
    out: list[str] = []
    for key in os.environ:
        upper = key.upper()
        if any(tok in upper for tok in _SECRET_NAME_TOKENS):
            out.append(key)
    return out


def get_secret(key: str) -> str:
    """Lê um segredo da variável de ambiente `key`. Nunca de arquivo/código."""
    if not isinstance(key, str) or not key.strip():
        raise ValueError("key deve ser string não vazia")
    if key not in os.environ:
        raise SecretNotFoundError(f"segredo não encontrado no ambiente: {key}")
    value = os.environ[key]
    if value == "":
        raise SecretNotFoundError(f"segredo vazio no ambiente: {key}")
    return value


def mask_secret(value: str) -> str:
    """Mascara um segredo para exibição em logs (ex.: 'sk-...****')."""
    if value is None:
        return ""
    text = str(value)
    if text == "":
        return ""
    if len(text) <= 4:
        return "****"
    return f"{text[:3]}...****"


def _secret_values(secrets: list[str] | None) -> list[str]:
    if secrets is not None:
        return [str(s) for s in secrets if s]
    out: list[str] = []
    for key in secret_env_keys():
        val = os.environ.get(key, "")
        if val:
            out.append(val)
    return out


def contains_secret(payload: Any, secrets: list[str] | None = None) -> bool:
    """Verifica se algum segredo aparece na serialização do payload."""
    try:
        text = json.dumps(payload, sort_keys=True, ensure_ascii=False, default=str)
    except (TypeError, ValueError):
        text = str(payload)
    for secret in _secret_values(secrets):
        if len(secret) >= 4 and secret in text:
            return True
    return False


def validate_no_secrets(payload: Any, secrets: list[str] | None = None) -> None:
    """Lança ValueError se um segredo for encontrado no payload."""
    if contains_secret(payload, secrets):
        raise ValueError("segredo detectado em payload (proibido em SoT/logs/artefatos)")


def redact(text: str, secrets: list[str] | None = None) -> str:
    """Redige segredos de um texto para logs."""
    result = text
    for secret in _secret_values(secrets):
        if secret and len(secret) >= 4:
            result = result.replace(secret, mask_secret(secret))
    return result
