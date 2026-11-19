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
- `docs/48-contrato-canonico-v1-0-0.md` §(i) (`idempotency_key`); §(vi) (idempotência preservada na migração).
- `~/.opencode/references/contrato-resumo-subagentes.md` (R7).
- `docs/42-mapeamento-gates-makefile-v0.md` (retry/3 strikes).

## Adendo 2026-11-18 — DEC-033 (dedupe atômico)

- **Decisão (Classe C, 2026-11-18, Mantenedor Lucinei — sessão OpenCode 2026-11-18, pergunta interativa; corpo em `docs/decisions/DEC-033-dedupe-atomico-idempotency-key.md`):** adotar **dedupe ATÔMICO na persistência** para eventos **com** `idempotency_key`: índice UNIQUE parcial `WHERE idempotency_key IS NOT NULL` em `events`; `insert_event` passa a usar `INSERT ... ON CONFLICT DO NOTHING` (ou equivalente) e retorna `event_id` + `deduplicated: bool` (contrato definido em DEC-033 §b). Reentrega com a mesma chave é **idempotente** (no-op deduplicado, sem exceção, chain hash íntegro).
- **SUPERSEDED por DEC-033:** o item desta ADR que fixa "reentrega gera novo registro" (seção Decisão, e R7 derivado) **somente para eventos COM `idempotency_key`**.
- **Permanece vigente:** append-only para eventos **sem** `idempotency_key`; chain hash e `verify_chain()`; dedupe no consumidor (R7) para fluxos **sem key**; histórico preservado; exactly-once fim-a-fim NÃO adotado.
- **Escopo do adendo:** adenda a ADR `accepted` (DEC-020) — **não** é promoção de ADR novo; o corpo original acima permanece intacto e vigente exceto pelo item superseded acima. Revisão do Contrato v1.0.0 (R7 / `§(vi)`) = decisão Classe C futura (D-V0-05/DEC-021 vigente até lá). LAC-IDEMP-02..05 não resolvidos por este adendo (ver DEC-033 §e).
