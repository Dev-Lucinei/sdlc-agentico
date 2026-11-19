"""Detecta drift entre docs canônicos de status e o JSON derivado (painel-status.json).

Falha em `make test` até a regeneração manual do JSON após novo DEC.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PAINEL = REPO_ROOT / "docs" / "00-painel-gerencial-consolidado.md"
DECISIONS_MD = REPO_ROOT / ".agents" / "DECISIONS.md"
PAINEL_STATUS_JSON = REPO_ROOT / ".agents" / "schemas" / "painel-status.json"
DECISIONS_DIR = REPO_ROOT / ".agents" / "decisions"


def _max_dec_number() -> int:
    numbers = []
    for path in DECISIONS_DIR.glob("DEC-*.md"):
        match = re.match(r"DEC-(\d+)", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers, "nenhum corpo de decisão DEC-NNN-*.md encontrado em .agents/decisions/"
    return max(numbers)


def test_painel_status_json_valido_e_derivado() -> None:
    data = json.loads(PAINEL_STATUS_JSON.read_text(encoding="utf-8"))
    assert data["derived"] is True
    assert "DECISIONS.md" in data["derivation_note"]
    for chave in (
        "aggregation_status",
        "decisions_log",
        "lacunas_consolidadas",
        "proxima_acao_recomendada",
    ):
        assert chave in data, f"chave esperada ausente em painel-status.json: {chave}"


def test_max_dec_presente_nos_tres_artefatos() -> None:
    token = f"{_max_dec_number():03d}"
    artefatos = {
        ".agents/DECISIONS.md": DECISIONS_MD.read_text(encoding="utf-8"),
        "docs/00-painel-gerencial-consolidado.md": PAINEL.read_text(encoding="utf-8"),
    }
    for nome, conteudo in sorted(artefatos.items()):
        assert f"DEC-{token}" in conteudo, (
            f"{nome} não referencia DEC-{token} — regenerar após novo DEC"
        )
    data = json.loads(PAINEL_STATUS_JSON.read_text(encoding="utf-8"))
    for campo in ("decisions_log", "proxima_acao_recomendada"):
        assert f"DEC-{token}" in str(data.get(campo, "")), (
            f".agents/schemas/painel-status.json não referencia DEC-{token} "
            f"no campo {campo} — regenerar após novo DEC"
        )


def test_painel_nao_cita_extracao_desatualizada() -> None:
    texto = PAINEL.read_text(encoding="utf-8")
    assert "extraído do §8" not in texto, (
        "docs/00-painel-gerencial-consolidado.md cita 'extraído do §8' — "
        "frase desatualizada; a derivação do JSON é .agents/DECISIONS.md + .agents/decisions/"
    )


def test_dec_bodies_parseaveis() -> None:
    corpos = sorted(DECISIONS_DIR.glob("DEC-*.md"))
    assert corpos, "nenhum corpo de decisão DEC-NNN-*.md encontrado em .agents/decisions/"
    for corpo in corpos:
        conteudo = corpo.read_text(encoding="utf-8")
        assert conteudo.strip(), f"corpo de decisão vazio: {corpo}"
