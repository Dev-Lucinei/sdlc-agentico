---
title: "ADR-001 — Orquestrador como Dispatcher+Agregador (sem domínio)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead"
status: "proposed"
---

## Contexto

O SDLC agêntico proposto exige coordenação entre múltiplos subagentes especializados (PO, PM, TL, analistas, implementadores) sem que o orquestrador assuma lógica de domínio. A baseline técnica (`docs/30-arquitetura-tech-lead-baseline-v0.md` §Arquitetura proposta) define o componente **Orchestrator (Dispatcher + Agregador)** como responsável por receber intenção, planejar/decompor delegações, rotear para subagentes, consolidar resumos/evidências/status e aplicar políticas de retry/escalonamento por taxonomia, **sem implementação direta de domínio**. O estado de execução é persistido no SoT/event log, não no orquestrador.

## Decisão

Adotar o orquestrador como **Dispatcher + Agregador stateless em lógica de domínio**: coordenação e agregação apenas, delegando toda execução de domínio a subagentes via contratos versionados. Subagentes emitem artefato + Resumo do Subagente padronizado; o orquestrador consolida e aplica políticas de retry/escalonamento.

## Status

`proposed` (ADR inicial; aprovação Classe C pendente — D-V0-04).

## Consequências

- **Positivas:** clareza de responsabilidades, testabilidade e auditabilidade; rastreabilidade ponta a ponta via SoT/event log; redução de acoplamento entre coordenação e domínio.
- **Negativas/custos:** overhead de coordenação/latência; exige contratos fortes (envelope + resumo + JSON) validados na borda; dependência de SoT central e event log.
- **Condicionais:** stack/infra/CI permanecem `[LACUNA]` (D-V0-01); promoção a `accepted` exige aprovação humana (Classe C).

## Alternativas consideradas

1. **Orquestrador monolítico com lógica de domínio** — rejeitada: mistura coordenação e execução, reduzindo testabilidade/auditabilidade e aumentando risco de drift.
2. **Coreografia pura sem agregador** — rejeitada: dificulta consolidação de status/evidências e aplicação uniforme de políticas de retry/escalonamento.

## Evidências

- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Arquitetura proposta (componentes; fluxos dispatcher→subagentes→agregação).
- `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` §(i) envelope de delegação; §(ii) contrato de resumo de subagente.
- `~/.opencode/references/contrato-resumo-subagentes.md` (R1–R7; status `done|blocked|partial`).
- DEC-010 (pauta D-V0-04) — aprovação Classe C pendente.
