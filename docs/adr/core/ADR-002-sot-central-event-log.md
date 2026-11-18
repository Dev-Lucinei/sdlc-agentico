---
title: "ADR-002 — SoT central + Event Log append-only"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead"
status: "accepted"
---

## Contexto

A rastreabilidade ponta a ponta (`request → task → delegation(s) → run(s) → artifact(s)/evidence → gate result → decisão/aceite`) exige uma fonte única de verdade para tarefas, runs, artefatos, estados e decisões, além de uma trilha imutável de eventos de ciclo de vida. A baseline (`docs/30`) propõe **Task/Run Registry (SoT)** + **Event Bus/Log** append-only como componentes centrais.

## Decisão

Persistir tasks/runs/artefatos/estados em um **registry canônico (SoT)** e eventos de ciclo de vida em um **Event Log append-only**, com lineage obrigatório (`task_id`, `run_id`, `parent_run_id`, `schema_version`, `decision_id`) em cada emissão. Eventos mínimos: `task.created`, `delegation.dispatched`, `run.started`, `run.emitted`, `run.blocked`, `run.partial`, `run.done`, `aggregation.updated`, `gate.evaluated`, `approval.requested`, `approval.granted|rejected`.

## Status

`accepted` (APROVADO E MATERIALIZADO — Classe C, 2026-11-17; DEC-020).

## Consequências

- **Positivas:** rastreabilidade, replay controlado e auditoria; base para idempotência e dedupe; observabilidade correlacionável.
- **Negativas/custos:** complexidade operacional e custo de storage `[LACUNA: infra]`; dependência de política de retenção/integridade `[LACUNA]`.
- **Condicionais:** mecanismos de criptografia/retention permanecem `[LACUNA]` até D-V0-01 (resolvido — DEC-018); nenhum diretório `docs/evidence/` é criado (DEC-005).

## Alternativas consideradas

1. **Estado distribuído por agente** — rejeitada: perde SoT único e dificulta auditoria/replay.
2. **Apenas logs sem registry estruturado** — rejeitada: logs sem schema não suportam idempotência/lineage auditável.

## Evidências

- `docs/30-arquitetura-tech-lead-baseline-v0.md` §SoT, ingestão/idempotência e rastreabilidade; §Eventos/observabilidade.
- `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` §(i) envelope (campos de correlação).
- DEC-003 (normativos externos por caminho+sha256, sem cópia física).
- DEC-005 (rejeição de `docs/evidence/`).
