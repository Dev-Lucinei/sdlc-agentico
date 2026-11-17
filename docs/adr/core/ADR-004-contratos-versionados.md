---
title: "ADR-004 — Contratos versionados (envelope + resumo + JSON)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead"
status: "proposed"
---

## Contexto

Sem contratos versionados e validação na borda, não há schema registry, compatibilidade aditiva verificável nem idempotência checável. Os canônicos de design usam `schema_version` (0.1.0-draft nos designs; proposta v1.0.0 no `docs/48`). A baseline (`docs/30`) propõe Contract & Schema Registry com imutabilidade por versão e validação na borda.

## Decisão

Adotar **contratos versionados** (envelope de delegação + resumo de subagente + JSON machine-readable) com **versionamento semântico**, **schema registry**, **validação na borda** e **compatibilidade aditiva em minor** (quebra = major + migração explícita). Migração `0.1.0-draft → 1.0.0` é aditiva (sem remoção/re-tipagem). `machine_readable.schema_version` ("1.0") × `schema_version` de contrato ("1.0.0") permanece decisão de D-V0-05 quando aplicável.

## Status

`proposed` (ADR inicial; aprovação Classe C pendente — D-V0-04).

## Consequências

- **Positivas:** evolução segura e interoperabilidade; validação automática de emissões; base para idempotência e dedupe.
- **Negativas/custos:** governança e migração de versões; overhead de validação na borda.
- **Condicionais:** registry/tooling permanecem `[LACUNA]`; thresholds numéricos não se aplicam a este ADR (contratos).

## Alternativas consideradas

1. **Contratos implícitos/ad-hoc** — rejeitada: impossibilita validação e evolução segura.
2. **Breaking changes sem versionamento** — rejeitada: quebra compatibilidade e rastreabilidade.

## Evidências

- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Contratos/Estados (envelope, resumo, mapeamento de estados).
- `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` §(i)–§(ii), §(vi) migração.
- `docs/41-agentstate-esquema-v0.md` (schema `sdlc.agentstate`, `schema_version` 1.0.0).
- `docs/45-grafo-langgraph-classe-c-v0.md` (gate de cobertura parametrizado, fail-closed).
- DEC-011 (pauta D-V0-05).
