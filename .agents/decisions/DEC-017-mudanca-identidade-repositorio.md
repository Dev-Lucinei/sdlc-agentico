---
title: "DEC-017 — Mudança de identidade do repositório: documentação + gates/CI"
date: "2026-11-16"
project: "sdlc-agentico"
status: "registrado — mudança de identidade documentada em AGENTS.md"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-017 — Mudança de identidade do repositório: documentação + gates/CI (registro; Classe B)

- **Contexto:** o repo era "somente documentação" (sem código-fonte, manifests, build, testes, lint, CI). Em 2026-11-16 o Mantenedor aprovou (Classe C) a materialização de gates/CI parametrizados (Makefile + pyproject.toml) e ADRs numerados, alterando a identidade do repo para "documentação + gates/CI parametrizados (fail-closed)". A implementação de aplicação (F-ÚNICO-1) permanece bloqueada por D-V0-01 (adiado).
- **Decisão:** registrar a mudança de identidade; qualificar AGENTS.md ("Somente documentação" → "documentação + gates/CI parametrizados (sem código de aplicação)"). Makefile/pyproject.toml criados com thresholds parametrizados (fail_under=0 placeholder) e fail-closed (exit_code 6) para ausência de pyproject.toml.
- **Status:** registrado (Classe B — registro; efeito Classe C executado via DEC-009…DEC-012/DEC-014…DEC-016).
- **Consequências:** repo agora tem verificação documental (lint/typecheck/test/build/audit) parametrizada; thresholds reais pendentes de D-V0-06; implementação de aplicação não iniciada (F-ÚNICO-1 bloqueada).
- **Evidência:** Makefile, pyproject.toml, AGENTS.md (qualificado), docs/README.md, docs/00 (adendo §8.6).
- **Lacunas persistentes:** D-V0-01 adiado; thresholds reais [LACUNA]; completed operacional indefinido; IDs/storage; capacidade real; DEC-007.
