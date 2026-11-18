---
title: "ADR-003 — Idempotência e dedupe (ingestão at-least-once)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead"
status: "accepted"
---

## Contexto

Retries e reentregas são esperados no fluxo agêntico (falhas `flaky`/`ambiente`, reprocessamento). Sem idempotência, reentregas duplicam efeitos ou perdem eventos. O normativo de resumo de subagentes (R7) define: reentrega = novo registro, sem alterar efeitos já persistidos; consumidor deduplica.

## Decisão

Adotar **idempotência por chave** e ingestão **at-least-once com dedupe**: `idempotency_key = hash(task_id + agent_role + input_fingerprint + schema_version)` para comandos/ingestões; `event_id` único por emissão. Reentrega gera novo registro (R7) sem mutar efeitos persistidos; agregador deduplica por chave e mantém histórico. Exactly-once fim-a-fim é explicitamente **não** adotado.

## Status

`accepted` (APROVADO E MATERIALIZADO — Classe C, 2026-11-17; DEC-020).

## Consequências

- **Positivas:** resiliência a retries/reentregas; histórico preservado; compatibilidade com semântica de eventos append-only.
- **Negativas/custos:** necessidade de store de dedupe e disciplina de chaves; complexidade de governança de versões (chave inclui `schema_version`).
- **Condicionais:** política de detecção de flake e triagem `ambiente` vs `logica` permanecem `[LACUNA]`.

## Alternativas consideradas

1. **Exactly-once fim-a-fim** — rejeitada: custo/complexidade desproporcional para MVP; não viável sem infra dedicada.
2. **Best-effort sem dedupe** — rejeitada: risco de duplicação de efeitos e perda de eventos.

## Evidências

- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Idempotência (chave, at-least-once, reentrega).
- `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` §(i) (`idempotency_key`); §(vi) (idempotência preservada na migração).
- `~/.opencode/references/contrato-resumo-subagentes.md` (R7).
- `docs/42-mapeamento-gates-makefile-v0.md` (retry/3 strikes).
