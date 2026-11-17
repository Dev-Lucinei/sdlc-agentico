#!/usr/bin/env python3
"""Validador do Contrato Canônico v1.0.0.

Recebe um arquivo JSON como input, valida contra o schema
docs/schemas/contract-v1.0.0.schema.json e retorna exit code 0 se válido,
1 se inválido. Imprime erros de validação detalhados.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_SCHEMA = Path(__file__).resolve().parents[1] / "docs" / "schemas" / "contract-v1.0.0.schema.json"


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _branch_candidates(data: object, schema: dict) -> list[tuple[str, dict]]:
    defs = schema.get("$defs", {})
    if isinstance(data, dict):
        name = data.get("schema_name")
        if name == "sdlc.task.delegation" and "envelope" in defs:
            return [("envelope", defs["envelope"])]
        if name == "sdlc.subagent.summary" and "subagent_summary" in defs:
            return [("subagent_summary", defs["subagent_summary"])]
    out = []
    if "envelope" in defs:
        out.append(("envelope", defs["envelope"]))
    if "subagent_summary" in defs:
        out.append(("subagent_summary", defs["subagent_summary"]))
    return out


def validate(data: object, schema: object) -> list[str]:
    try:
        import importlib.util

        if importlib.util.find_spec("jsonschema") is None:
            raise ImportError("jsonschema ausente")
        from jsonschema import Draft202012Validator
    except ImportError:
        return ["jsonschema não instalado: impossível validar"]

    schema = schema if isinstance(schema, dict) else {}
    candidates = _branch_candidates(data, schema)
    if not candidates:
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        return [f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in errors]

    best: tuple[int, list] | None = None
    for _name, branch in candidates:
        branch_schema = dict(branch)
        branch_schema["$defs"] = schema.get("$defs", {})
        branch_schema["$schema"] = schema.get("$schema")
        validator = Draft202012Validator(branch_schema)
        errs = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if best is None or len(errs) < best[0]:
            best = (len(errs), errs)
    assert best is not None
    messages: list[str] = []
    seen: set[str] = set()
    for err in best[1]:
        path = "/".join(str(p) for p in err.path) or "<root>"
        msg = f"{path}: {err.message}"
        if msg not in seen:
            seen.add(msg)
            messages.append(msg)
    return messages


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Valida JSON contra o Contrato Canônico v1.0.0.")
    parser.add_argument("input", help="Caminho do arquivo JSON a validar.")
    parser.add_argument(
        "--schema",
        default=str(DEFAULT_SCHEMA),
        help="Caminho do schema JSON (default: docs/schemas/contract-v1.0.0.schema.json).",
    )
    args = parser.parse_args(argv)

    input_path = Path(args.input)
    schema_path = Path(args.schema)

    if not input_path.is_file():
        print(f"ERRO: arquivo de entrada não encontrado: {input_path}", file=sys.stderr)
        return 1
    if not schema_path.is_file():
        print(f"ERRO: schema não encontrado: {schema_path}", file=sys.stderr)
        return 1

    try:
        data = load_json(input_path)
    except json.JSONDecodeError as exc:
        print(f"ERRO: JSON inválido em {input_path}: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"ERRO: não foi possível ler {input_path}: {exc}", file=sys.stderr)
        return 1

    try:
        schema = load_json(schema_path)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"ERRO: não foi possível carregar o schema: {exc}", file=sys.stderr)
        return 1

    errors = validate(data, schema)
    if errors:
        print(f"INVALID: {input_path}")
        for msg in errors:
            print(f"  - {msg}")
        return 1

    print(f"VALID: {input_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())