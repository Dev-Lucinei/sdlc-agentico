---
title: "DEC-011 — D-V0-05 — Contrato canônico v1.0.0 (pauta)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "aprovado (Classe C) — reconciliado em docs/41/45 (1.0.0)"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-011 — Pauta D-V0-05: Consolidação do contrato canônico v1.0.0 (resumo + envelope + estados + correlação + `schema_version`) (Classe C — pauta; proposta do trio 2026-11-16)

- **Contexto:** D-V0-05 (painel `docs/00` §5) exige consolidação do contrato canônico v1.0.0 (resumo + envelope + estados + correlação + `schema_version`) e da taxonomia operacional (`completed`/tracking). Proposta em `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (status `condicional`); adoção exige Classe C (CR-007-C).
- **Decisão (pauta, não execução):** submeter o Contrato Canônico v1.0.0-PROPOSTA (`docs/48`) à decisão do Mantenedor (+PO+PM). **Status: aguardando decisão do Mantenedor.** Nada aqui tem efeito normativo até lá; `0.1.0-draft` permanece vigente nos designs.
- **Decisão Recomendada (proposta do trio, 2026-11-16):** **Sim** — adotar o contrato v1.0.0 (resumo + envelope + estados + correlação + `schema_version`), com migração aditiva de `0.1.0-draft` e `completed`≠`approved`. Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).
- **Evidência:** `docs/48-*`; `docs/47` §(vi) (migração aditiva); `docs/00` §5 (D-V0-05); `docs/30-*` §Contratos; CR-007-C no log; proposta PO (gerente-produto, 2026-11-16): DEC-011 Sim (adoção contrato v1.0.0) + AC Given/When/Then + KPIs iniciais; proposta TL (tech-lead, 2026-11-16): DEC-012 Sim (política unificada de gates/evidência/thresholds) + contrato canônico v1.0.0.
- **Ressalvas dos gestores:** PO — KPIs iniciais e AC Given/When/Then; TL — "no new errors" sobre baseline declarada, G0–G3, exit_code 6 fail-closed; PM — consenso condicional, divergência residual de ritmo.
- **Status final:** **[RESOLVIDO-PROPOSTA]** (Classe C — pauta; proposta emitida pelos 3 gestores; nenhuma aprovação inferida; aguardando decisão do Mantenedor).
