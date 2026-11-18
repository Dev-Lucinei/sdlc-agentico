---
title: "ADR-005 — Modelo de estados e autonomia (execução vs aceite, classes A/B/C)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead"
status: "accepted"
---

## Contexto

A distinção entre execução técnica (`done`), conclusão operacional (`completed`) e aceite de valor (`approved`) precisa ser estrutural, não convencional, para evitar falso "approved/completed". A baseline (`docs/30`) propõe taxonomia de estados com classes de autonomia A/B/C e transições proibidas (ex.: `approved` apenas via Human Review com evidência).

## Decisão

Adotar o **modelo de estados e autonomia** com: (i) camadas distintas — execução (agente), resumo (subagente: `done|blocked|partial`), orquestração (OPS: `completed`), valor (PO: `approved`), gate técnico (`go/condicional/no_go`); (ii) classes de autonomia A/B/C; (iii) regra `done ⇏ completed ⇏ approved`; (iv) Classe C nunca conclui como `go/approved` sem aprovação humana explícita registrada; estados terminais de execução não retrocedem (retrabalho = nova execução/run). `approved` é terminal e exclusivo do PO, com `evidence` + `decided_by` + `decided_at`.

## Status

`accepted` (APROVADO E MATERIALIZADO — Classe C, 2026-11-17; DEC-020).

## Consequências

- **Positivas:** semântica clara e controle de risco (Classe C); evita promoção indevida de status; auditoria de transições.
- **Negativas/custos:** mais etapas de aprovação/escalonamento; maior carga de governança.
- **Condicionais:** critério operacional exato de `completed` no tracking alvo permanece `[LACUNA]` (docs/10 §3.2).

## Alternativas consideradas

1. **Estado único "done"** — rejeitada: colapsa execução/valor e permite falso approved.
2. **Aprovação implícita** — rejeitada: viola regra de ouro (Classe C exige humano explícito).

## Evidências

- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Contratos/Estados (mapeamento de estados; regras de compatibilidade).
- `docs/41-agentstate-esquema-v0.md` (invariantes `done_neq_completed_neq_approved`; `approved_requires`).
- `docs/45-grafo-langgraph-classe-c-v0.md` (nó `human_review` único escritor de `approved`).
- `~/.opencode/references/autonomia-e-estados.md` (classes A/B/C, transições proibidas, 3 strikes/1 crítico).
- `~/.opencode/references/contrato-resumo-subagentes.md` (R1–R7).
- DEC-019 (D-V0-03) — APROVADO E MATERIALIZADO (Classe C, 2026-11-17); DEC-020 (D-V0-04) — APROVADO E MATERIALIZADO (Classe C, 2026-11-17).
