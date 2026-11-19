---
title: "PROPOSTA — Decisão de contrato N6: divergências ADR-005 × docs/10 × schema v1.0.0 (2026-11-19)"
date: "2026-11-19"
project: "sdlc-agentico"
source: "executor operacional (tarefa #4 — proposta, não decisão)"
status: "proposta — decisão humana pendente"
---

# PROPOSTA — Contrato N6: divergências entre ADR-005, docs/10 e schema v1.0.0

> **Este arquivo é uma PROPOSTA. Não é decisão. Nada aqui foi aplicado.**
> Nenhuma das opções foi executada. Quem decide é o Mantenedor (Classe C).

## Contexto resumido — as 4 divergências (audit §3, confirmadas em 2026-11-19)

Fontes lidas: `docs/adr/core/ADR-005-modelo-estados-autonomia.md` (status `accepted`),
`docs/10-produto-visao-v0.md` §3 ("Semântica Canônica de Estados"), `.agents/schemas/contract-v1.0.0.schema.json`.

| # | Divergência | ADR-005 | docs/10 §3 | schema v1.0.0 |
|---|---|---|---|---|
| (a) | `gate técnico (go\|condicional\|no_go)` | Presente — camada explícita de gate técnico ("gate técnico (`go/condicional/no_go`)") | **Ausente** — §3 só cobre execução (`done/blocked/partial`), operacional (`completed`) e valor (`pending/approved/rejected`); nenhuma camada de gate | **Parcial** — `condicional` existe em `state_value`, mas sem `gate_status`, sem `go`/`no_go`, sem discriminador de camada |
| (b) | `condicional` em `state_value` sem discriminador de camada | Implícito na camada de gate | Ausente de §3 | Presente em `state_value` (enum: `done, blocked, partial, completed, approved, rejected, pending, condicional`) — mistura gate com valor/execução sem desambiguar |
| (c) | `execution_status` (`done\|blocked\|partial`) duplicado em `state_value` | Camadas distintas (execução ≠ gate ≠ valor) | Distingue §3.1 (execução) / §3.2 (operacional) / §3.3 (valor) | `execution_status` é enum próprio (`done/blocked/partial`) **e** os mesmos valores reaparecem em `state_value` — duplicação literal |
| (d) | `go` / `no_go` ausentes de qualquer enum | Presentes (`go/condicional/no_go`) | Ausentes | **Ausentes** — nenhum enum do schema contém `go` ou `no_go` |

## Opção A — "Schema é a verdade; ADR-005 vira rationale histórico"

- **Mudanças:** 1 linha em ADR-005 (nota de "camada de gate é operacional, não de estado")
- **Schema:** nenhuma alteração
- **Custo:** ~30 min
- **Prós:** zero risco de quebrar consumidores atuais; menor diff possível
- **Contras:** `condicional` continua em `state_value` (misturado sem discriminador);
  ADR-005 `accepted` fica sem efeito normativo real na camada de gate; divergência (d) persiste

## Opção B — "Bump schema para 1.1 (4 camadas + gate_status)"

- **Mudanças:**
  - Adicionar `gate_status: null | go | condicional | no_go` (nullable)
  - Remover `condicional` de `state_value`
  - Unificar `execution_status` em `status`
  - Adicionar regra `if/then`: se `decision_status == "pending"` então `gate_status` obrigatório
- **Schema:** 1 mudança breaking (bump `1.0.0 → 1.1`)
- **Custo:** ~2–3h (inclui atualizar validador/testes/docs se o mantenedor autorizar)
- **Prós:** alinha com ADR-005; elimina ambiguidade permanentemente; camadas separadas por design
- **Contras:** consumidores de v1.0.0 podem quebrar se não aceitarem o campo novo;
  requer atualizar `schema_version`const, validador (`tools/validate_contract.py`) e testes;
  decisão de versionamento (1.1 vs 2.0) também precisa ser humana

## Opção C — "Congelar como está + nota de divergência conhecida"

- **Mudanças:** 1 arquivo `DIVERGENCIA-CONHECIDA.md` em `.agents/schemas/` registrando as
  4 divergências + motivo de não resolver agora
- **Custo:** ~10 min
- **Prós:** mínimo esforço; documenta honestamente; nenhuma quebra
- **Contras:** divergência persiste; futuro audit reabre o tema; não resolve nada tecnicamente;
  `condicional` segue ambíguo para consumidores

## Tabela comparativa

| Dimensão | Opção A | Opção B | Opção C |
|---|---|---|---|
| Custo | ~30 min | ~2–3h | ~10 min |
| Impacto em consumidores v1.0.0 | Nenhum | Breaking (campo novo obrigatório no caso `pending`) | Nenhum |
| Alinha schema ↔ ADR-005 | Parcial (só nota) | Total | Nenhum |
| Elimina ambiguidade `condicional` | Não | Sim | Não (documentada) |
| Risco de regressão | Baixo | Médio (validador/testes/exemplos) | Nenhum |
| Dívida técnica remanescente | Alta (mistura persiste) | Baixa | Alta (registrada) |
| Reversibilidade | Alta | Média (bump é irreversível sem novo bump) | Total |

## Recomendação (proposta — decisão humana pendente)

**Recomendação desta agente: Opção B** — é a única que resolve as 4 divergências na raiz,
alinha o contrato com o ADR-005 `accepted` e elimina a ambiguidade de camadas em vez de
documentá-la ou contorná-la. O custo (~2–3h) é compatível com a capacidade declarada
(~4–8h/sem, DEC-032) e cabe em uma fatia Classe B após a decisão Classe C do mantenedor.

Ressalvas honestas:
- Se o mantenedor priorizar **zero risco de quebrar consumidores hoje**, Opção A é o
  meio-termo aceitável — mas deve ser encarada como paliativo, não resolução.
- Se o tema não for prioridade agora, Opção C é legítima desde que registrada como
  dívida com gatilho de reavaliação explícito.
- Qualquer opção escolhida **não** altera `docs/10` §3 nem ADR-005 por si só — a opção B
  exigiria change set próprio (schema + validador + testes + docs), com decisão humana.

**Nada foi aplicado. Aguardando escolha do Mantenedor (Classe C).**
