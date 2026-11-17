---
title: "ADR-007 — Observabilidade e segurança mínima by design"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead"
status: "proposed"
---

## Contexto

Detecção tardia de falhas e ausência de controles básicos de acesso/segredos aumentam risco operacional e de conformidade. A baseline (`docs/30`) propõe Observability & Security Layer com logs estruturados correlacionáveis, métricas de fluxo, RBAC/segredos/redação desde o MVP.

## Decisão

Adotar **observabilidade e segurança mínima by design**: logs estruturados correlacionáveis (campos de correlação `correlation_id/request_id`, `task_id`, `run_id`, `agent`, `classe_autonomia`, `schema_version`, `timestamp`, `status`), métricas de fluxo (contagem por status, latência por fase, taxa de retry, fila/pendências, falhas de gate), RBAC por papel/agente, redação de segredos em observabilidade, integridade/auditoria via trilha append-only e validação de schema na ingestão. Hardening avançado conforme `[LACUNA]` de infra.

## Status

`proposed` (ADR inicial; aprovação Classe C pendente — D-V0-04).

## Consequências

- **Positivas:** detecção precoce de falhas e conformidade básica; auditoria de trilhas; menor risco de exposição de segredos.
- **Negativas/custos:** custo inicial e dependências de infra `[LACUNA]`; esforço de redação/controle de acesso.
- **Condicionais:** mecanismos de criptografia em trânsito/repouso e sandboxing permanecem `[LACUNA]` até D-V0-01.

## Alternativas consideradas

1. **Observabilidade tardia** — rejeitada: dificulta detecção e resposta a incidentes.
2. **Segurança apenas perimetral** — rejeitada: insuficiente para controles por papel/agente e redação de segredos.

## Evidências

- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Observabilidade/segurança; §Eventos/observabilidade; §Segurança básica.
- `docs/00-painel-gerencial-consolidado.md` (governança; normativos).
- DEC-007 (política de segredos permanece `[LACUNA]`).
- DEC-005 (sem `docs/evidence/`; evidências embutidas/referenciadas por caminho+hash).
