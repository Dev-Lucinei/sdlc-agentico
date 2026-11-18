---
title: "DEC-025 — Reconciliação de docs/41 e docs/45 para contrato v1.0.0"
date: "2026-11-17"
project: "sdlc-agentico"
status: "concluído (Classe B, 2026-11-17)"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-025 — Reconciliação de docs/41 e docs/45 para contrato v1.0.0 (Classe B, 2026-11-17)

- **Contexto:** F-ÚNICO-2 (Evolução) iniciada (DEC-024). Os canônicos de design `docs/41` e `docs/45` permaneciam em `0.1.0-draft` (DIV-2) e precisavam ser reconciliados para o contrato v1.0.0 adotado (DEC-021), com campos do envelope canônico, mapeamento de estados (ADR-005), exit codes com ação automática (docs/42) e gates G2/G3 com thresholds do `pyproject.toml`. Ação de classe B (reversível, documental), sem promoção a `approved`/`completed` de artefatos de valor.
- **Decisão (Classe B, tech-lead, 2026-11-17):** **RECONCILIADO.** Alterações aplicadas:
  1. `docs/41-agentstate-esquema-v0.md`: migração aditiva `0.1.0-draft → 1.0.0` confirmada; campos do contrato adicionados ao bloco JSON_STRICT (`schema_name`, `schema_version`, `envelope_id`, `idempotency_key`, `correlation_id`); seção §4.1 "Mapeamento de estados (execução → operação → valor) — ADR-005" adicionada (camadas, transições com guardas, invariantes; critério operacional de `completed` permanece `[LACUNA]`). Campos existentes preservados (`global_context`, `ads`, `tasks`, `errors`, `approvals`, `integration_test_output`, `pr_ready`).
  2. `docs/45-grafo-langgraph-classe-c-v0.md`: migração aditiva confirmada; seção §2.1 "Exit codes → ação automática" (fonte docs/42 §2) adicionada; seção §2.2 "Gates G2/G3 com thresholds do pyproject.toml" adicionada (G0–G3, thresholds absolutos cobertura ≥50%, 0 erros críticos, fail-closed exit_code 6); nota LangGraph (CR-009-C) mantida condicional com stack mínima definida (DEC-018) e máquina de estados Python pura (src/) como baseline.
  3. `docs/00-painel-gerencial-consolidado.md`: §1 semáforo atualizado para F-ÚNICO-2; §8 `aggregation_status` → "F-ÚNICO-2 em andamento"; `proxima_acao_recomendada` → "Reconciliar docs/41/45, obter aceite PO, resolver D-V0-02"; `last_reviewed` 2026-11-17.
  4. `docs/README.md`: data da última atualização 2026-11-17 (verificado; consistência mantida).
- **Referência:** DEC-021 (D-V0-05, contrato v1.0.0 adotado), DEC-020 (ADR-005 accepted), DEC-022 (D-V0-06, gates/thresholds), DEC-018 (D-V0-01, stack mínima), DEC-024 (baseline v0 publicada, F-ÚNICO-2 iniciada).
- **Artefatos:** `docs/41-agentstate-esquema-v0.md`, `docs/45-grafo-langgraph-classe-c-v0.md`, `docs/00-painel-gerencial-consolidado.md`, `docs/README.md`, `docs/DECISIONS.md`.
- **Nota:** migração aditiva — sem remoção/re-tipagem de campos; consumidores de `0.1.0-draft` permanecem compatíveis por leitura tolerante. `machine_readable.schema_version` do painel (`"1.0"`) permanece distinto do `schema_version` de contrato (`"1.0.0"`) (decisão de D-V0-05). Nenhum campo `approved` escrevível por agente; `approved` permanece exclusivo do PO.
- **Status final:** **concluído** (Classe B, 2026-11-17 — registro documental reversível; nenhuma promoção a `approved`/`completed` de artefatos de valor).
