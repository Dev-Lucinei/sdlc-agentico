---
title: "ADR-006 — Qualidade incremental por gates e evidência ('no new errors')"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead"
status: "accepted"
---

## Contexto

Gates rígidos desde o início são inviáveis sem baseline/infra; ausência de gates permite regressão silenciosa. A baseline (`docs/30`) propõe estratégia de gates incremental (G0–G3) com critério "no new errors" sobre baseline declarada e thresholds lidos do projeto-alvo (nunca hardcoded).

## Decisão

Adotar **qualidade incremental por gates e evidência**: gates mínimos no MVP, baseline explícita, endurecimento progressivo por fase (G0 Fundacional → G1 MVP operacional → G2 Endurecimento → G3 Escala/governança). Critério "no new errors" vs baseline versionada; thresholds numéricos (cobertura/lint/tipos) lidos do `pyproject.toml` do projeto-alvo, nunca hardcoded. Gates bloqueiam não conformidades; Classe C exige aprovação humana.

## Status

`accepted` (APROVADO E MATERIALIZADO — Classe C, 2026-11-17; DEC-020).

## Consequências

- **Positivas:** baixo risco de adoção e feedback rápido; rastreabilidade de evidências; compatibilidade com fail-closed quando `pyproject.toml` ausente.
- **Negativas/custos:** risco residual até maturação; dependência de baseline `[LACUNA]`; necessidade de infra/CI no projeto-alvo.
- **Condicionais:** ferramentas específicas de lint/test/CI e repositório-alvo permanecem `[LACUNA]` (D-V0-01/D-V0-06 — resolvido — DEC-018 / DEC-022).

## Alternativas consideradas

1. **Gate rígido completo desde o início** — rejeitada: inviável sem baseline/infra; alto risco de bloqueio.
2. **Sem gates formais** — rejeitada: sem controle de regressão nem evidência.

## Evidências

- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Qualidade e Gates (DoD técnico; tabela G0–G3).
- `docs/42-mapeamento-gates-makefile-v0.md` (exit codes determinísticos; fail-closed exit 6).
- `docs/44-loop-feedback-coding-tdd-qa-v0.md` (loop coding→tdd→qa; 3 strikes).
- `docs/45-grafo-langgraph-classe-c-v0.md` (`gate_pr_generation` fail-closed por threshold parametrizado).
- DEC-022 (D-V0-06) — APROVADO E MATERIALIZADO (Classe C, 2026-11-17).
- DEC-005 (sem `docs/evidence/`).
