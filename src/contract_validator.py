"""Validador do Contrato Canônico v1.0.0 (sdlc.task.delegation + sdlc.subagent.summary).

- Valida contra docs/schemas/contract-v1.0.0.schema.json quando disponível.
- Campos obrigatórios: schema_name, schema_version, status, decision_id, evidencia.
- Enums de status.
- Invariante: done ⇏ completed ⇏ approved (validar transições).
- Exit code 5 se campos obrigatórios ausentes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

__all__ = [
    "DEFAULT_SCHEMA_PATH",
    "REQUIRED_CORE_FIELDS",
    "EXIT_MISSING_REQUIRED",
    "validate",
    "validate_file",
    "validate_transition",
    "is_missing_required",
    "main",
    "ContractValidator",
    "validate_contract",
    "validate_envelope",
    "validate_summary",
    "check_contract",
]

DEFAULT_SCHEMA_PATH = (
    Path(__file__).resolve().parents[1] / "docs" / "schemas" / "contract-v1.0.0.schema.json"
)

EXIT_MISSING_REQUIRED = 5
EXIT_INVALID = 1
EXIT_OK = 0

REQUIRED_CORE_FIELDS = ["schema_name", "schema_version"]


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _load_schema(schema_path: Path | None = None) -> dict[str, Any]:
    path = schema_path or DEFAULT_SCHEMA_PATH
    try:
        data = _load_json(path)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _branch_candidates(data: Any, schema: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    defs = schema.get("$defs", {}) if isinstance(schema, dict) else {}
    if isinstance(data, dict):
        name = data.get("schema_name")
        if name == "sdlc.task.delegation" and "envelope" in defs:
            return [("envelope", defs["envelope"])]
        if name == "sdlc.subagent.summary" and "subagent_summary" in defs:
            return [("subagent_summary", defs["subagent_summary"])]
    out: list[tuple[str, dict[str, Any]]] = []
    if "envelope" in defs:
        out.append(("envelope", defs["envelope"]))
    if "subagent_summary" in defs:
        out.append(("subagent_summary", defs["subagent_summary"]))
    return out


def _jsonschema_available() -> bool:
    try:
        import importlib.util

        return importlib.util.find_spec("jsonschema") is not None
    except Exception:
        return False


def validate(data: Any, schema: Any = None) -> list[str]:
    """Valida `data` contra o schema. Retorna lista de erros (vazia = válido)."""
    if schema is None:
        schema = _load_schema()
    if not isinstance(schema, dict):
        schema = {}
    errors: list[str] = []

    if not isinstance(data, dict):
        return ["<root>: expected object"]

    # Campos obrigatórios mínimos (prompt): schema_name, schema_version.
    for field in REQUIRED_CORE_FIELDS:
        if field not in data:
            errors.append(f"<root>: '{field}' is a required property")

    # Status (para subagent summary) — obrigatório conforme prompt.
    name = data.get("schema_name")
    if name == "sdlc.subagent.summary" and "status" not in data:
        errors.append("<root>: 'status' is a required property")

    # decision_id / evidencia: no summary ficam em machine_readable.
    if name == "sdlc.subagent.summary":
        mr = data.get("machine_readable")
        if not isinstance(mr, dict):
            errors.append("<root>: 'machine_readable' is a required property")
        else:
            if "decision_id" not in mr:
                errors.append("machine_readable: 'decision_id' is a required property")
            if "evidencia" not in mr:
                errors.append("machine_readable: 'evidencia' is a required property")

    # jsonschema validation (se disponível).
    if _jsonschema_available():
        try:
            from jsonschema import Draft202012Validator
        except Exception:
            Draft202012Validator = None  # type: ignore
        if Draft202012Validator is not None:
            candidates = _branch_candidates(data, schema)
            if not candidates:
                validator = Draft202012Validator(schema)
                json_errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
                for e in json_errors:
                    path = "/".join(str(p) for p in e.path) or "<root>"
                    msg = f"{path}: {e.message}"
                    if msg not in errors:
                        errors.append(msg)
            else:
                best: tuple[int, list[Any]] | None = None
                for _n, branch in candidates:
                    branch_schema = dict(branch)
                    branch_schema["$defs"] = schema.get("$defs", {})
                    if "$schema" in schema:
                        branch_schema["$schema"] = schema.get("$schema")
                    validator = Draft202012Validator(branch_schema)
                    errs = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
                    if best is None or len(errs) < best[0]:
                        best = (len(errs), errs)
                if best is not None:
                    for e in best[1]:
                        path = "/".join(str(p) for p in e.path) or "<root>"
                        msg = f"{path}: {e.message}"
                        if msg not in errors:
                            errors.append(msg)
    else:
        if not errors:
            errors.append("jsonschema não instalado: impossível validar")

    # Invariante done ⇏ completed ⇏ approved em machine_readable.status
    if name == "sdlc.subagent.summary":
        mr = data.get("machine_readable")
        if isinstance(mr, dict):
            st = mr.get("status")
            top = data.get("status")
            # status de execução não pode ser 'completed'/'approved'/'rejected'
            if top in ("completed", "approved", "rejected"):
                errors.append(
                    f"<root>: status de execução inválido '{top}' (use done/blocked/partial)"
                )
            if st in ("done",) and top not in ("done", "blocked", "partial"):
                pass

    return errors


def validate_file(path: Path, schema_path: Path | None = None) -> list[str]:
    input_path = Path(path)
    if not input_path.is_file():
        return [f"arquivo não encontrado: {input_path}"]
    try:
        data = _load_json(input_path)
    except json.JSONDecodeError as exc:
        return [f"JSON inválido: {exc}"]
    except OSError as exc:
        return [f"não foi possível ler: {exc}"]
    schema = _load_schema(schema_path) if schema_path else _load_schema()
    return validate(data, schema)


def is_missing_required(errors: list[str]) -> bool:
    return any("required property" in e or "is a required" in e for e in errors)


def validate_transition(
    from_status: str,
    to_status: str,
    *,
    manual_confirmation: bool = False,
    autonomy_class: str | None = None,
) -> tuple[bool, str]:
    """Valida transição de estado. Retorna (permitido, motivo)."""
    fs = str(from_status)
    ts = str(to_status)
    # done -> approved: bloqueado (G1)
    if fs == "done" and ts == "approved":
        return False, "G1: done->approved bloqueado (vedação de auto-aceite)"
    # completed -> approved: apenas human_review
    if fs == "completed" and ts == "approved":
        if not manual_confirmation:
            return False, "approved requer human_review com confirmação manual"
        return True, "ok"
    # done -> completed: apenas autopromoção A/B
    if fs == "done" and ts == "completed":
        if autonomy_class in ("A", "B"):
            return True, "ok"
        return False, "done->completed apenas via autopromoção A/B"
    # qualquer -> blocked permitido
    if ts == "blocked":
        return True, "ok"
    # completed -> rejected permitido com humano
    if fs == "completed" and ts == "rejected":
        if not manual_confirmation:
            return False, "rejected requer human_review"
        return True, "ok"
    return True, "ok"


class ContractValidator:
    def __init__(self, schema_path: Path | None = None) -> None:
        self.schema_path = schema_path

    def validate(self, data: Any) -> list[str]:
        schema = _load_schema(self.schema_path) if self.schema_path else _load_schema()
        return validate(data, schema)

    def validate_file(self, path: Path) -> list[str]:
        return validate_file(path, self.schema_path)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Valida JSON contra o Contrato Canônico v1.0.0.")
    parser.add_argument("input", nargs="?", help="Caminho do arquivo JSON a validar.")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA_PATH),
                            help="Caminho do schema JSON.")
    parser.add_argument("--data", help="JSON inline a validar.")
    args = parser.parse_args(argv)

    schema_path = Path(args.schema)

    if args.data is not None:
        try:
            data = json.loads(args.data)
        except json.JSONDecodeError as exc:
            print(f"ERRO: JSON inválido: {exc}", file=sys.stderr)
            return EXIT_INVALID
    elif args.input is not None:
        input_path = Path(args.input)
        if not input_path.is_file():
            print(f"ERRO: arquivo de entrada não encontrado: {input_path}", file=sys.stderr)
            return EXIT_INVALID
        try:
            data = _load_json(input_path)
        except json.JSONDecodeError as exc:
            print(f"ERRO: JSON inválido em {input_path}: {exc}", file=sys.stderr)
            return EXIT_INVALID
        except OSError as exc:
            print(f"ERRO: não foi possível ler {input_path}: {exc}", file=sys.stderr)
            return EXIT_INVALID
    else:
        print("ERRO: informe um arquivo ou --data", file=sys.stderr)
        return EXIT_INVALID

    if not schema_path.is_file():
        print(f"ERRO: schema não encontrado: {schema_path}", file=sys.stderr)
        return EXIT_INVALID

    try:
        schema = _load_json(schema_path)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"ERRO: não foi possível carregar o schema: {exc}", file=sys.stderr)
        return EXIT_INVALID

    errors = validate(data, schema)
    if errors:
        print("INVALID")
        for msg in errors:
            print(f"  - {msg}")
        if is_missing_required(errors):
            return EXIT_MISSING_REQUIRED
        return EXIT_INVALID

    print("VALID")
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())


# Aliases de compatibilidade
validate_contract = validate
validate_envelope = validate
validate_summary = validate
check_contract = validate
