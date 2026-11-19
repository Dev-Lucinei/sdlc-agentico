---
title: "DEC-022 — D-V0-06 — Política unificada de gates/thresholds"
date: "2026-11-17"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-022 — D-V0-06: Política unificada de gates/evidência/thresholds (Classe C, 2026-11-17)

- **Contexto:** D-V0-06 (painel `docs/00` §5) exige política unificada de gates/evidência e thresholds (ex.: cobertura) lidos do projeto-alvo quando aplicável. Proposta em `docs/30` (gates G0–G3) e `docs/42` (mapeamento gates↔Makefile, exit_code 6 fail-closed). Registrada como pauta DEC-012 ([RESOLVIDO-PROPOSTA], 2026-11-16). DEC-018 (2026-11-17) fixou thresholds absolutos (cobertura ≥50%, 0 erros críticos) para o MVP.
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **APROVADO E MATERIALIZADO.** Adotar a política unificada de gates/evidência/thresholds: "no new errors" sobre baseline declarada; G0–G3; exit_code 6 fail-closed; thresholds absolutos para o MVP (cobertura ≥50%, 0 erros críticos — hardcoded em `pyproject.toml`/`Makefile`); thresholds parametrizados (lidos do projeto-alvo) para projetos-alvo futuros. Artefatos: `pyproject.toml`, `Makefile`, `docs/42`.
- **Referência:** DEC-012 (pauta registrada em 2026-11-16); DEC-018 (thresholds absolutos, 2026-11-17).
- **Artefatos:** `pyproject.toml`, `Makefile`, `docs/42-mapeamento-gates-makefile-v0.md`.
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).
