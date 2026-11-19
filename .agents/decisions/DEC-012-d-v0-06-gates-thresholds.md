---
title: "DEC-012 — D-V0-06 — Política unificada de gates/thresholds (pauta)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "aprovado (Classe C) — materializado em Makefile/pyproject.toml (parametrizados)"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-012 — Pauta D-V0-06: Política unificada de gates/evidência e thresholds (lidos do projeto-alvo) (Classe C — pauta; proposta do trio 2026-11-16)

- **Contexto:** D-V0-06 (painel `docs/00` §5) exige política unificada de gates/evidência e thresholds (ex.: cobertura) lidos do projeto-alvo quando aplicável. Proposta em `docs/30-*` (gates G0–G3) e `docs/42-*` (mapeamento gates↔Makefile, exit_code 6 fail-closed). Evitar hardcode; "no new errors" sobre baseline declarada. Decisão de **qualidade (Classe C)**.
- **Decisão (pauta, não execução):** submeter a política de gates unificada (G0–G3 × exit_code → AgentState, thresholds lidos do alvo) à decisão do Mantenedor (+TL/PM/PO). **Status: aguardando decisão do Mantenedor.** Nenhum gate é adotado nem threshold fixado por este registro.
- **Decisão Recomendada (proposta do trio, 2026-11-16):** **Sim** — adotar a política unificada de gates/evidência/thresholds parametrizada ("no new errors" sobre baseline declarada, G0–G3, exit_code 6 fail-closed, thresholds lidos do projeto-alvo). Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).
- **Evidência:** `docs/30-*` §Qualidade e Gates; `docs/42-*` §2 (exit_code 6); `docs/48-*` §(v); `docs/00` §5 (D-V0-06); CR-008-C no log; proposta TL (tech-lead, 2026-11-16): DEC-012 Sim (política unificada de gates/evidência/thresholds parametrizada, "no new errors" sobre baseline declarada, G0–G3, exit_code 6 fail-closed) + estrutura técnica de ADRs neutra; proposta PM (gerente-projeto, 2026-11-16): trilha TL (schemas offline), trilha PO (AC/KPIs/handoff), trilha PM (R8/R10/R11), gatilho de implementação.
- **Ressalvas dos gestores:** TL — consenso condicional de substância com PO/PM; PM — R8 reavaliado (M×A Alto, mitigação ativa), R10/R11 mitigados; PO — critérios mínimos de aceite (Given/When/Then) e KPIs iniciais.
- **Status final:** **[RESOLVIDO-PROPOSTA]** (Classe C — pauta; proposta emitida pelos 3 gestores; nenhuma aprovação inferida; aguardando decisão do Mantenedor).
