---
title: "AgentState — Esquema de Estado Tipado para LangGraph (v0, proposta)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead (subagente; classe B; t1 da demanda de design dos itens de execução agêntica)"
status: "condicional"
---
> **Migração aditiva (DEC-021, 2026-11-17 — D-V0-05, Classe C):** `schema_version` reconciliado de `0.1.0-draft` para `1.0.0` (contrato canônico v1.0.0; validador `docs/schemas/contract-v1.0.0.schema.json`). Migração **aditiva** — sem remoção/re-tipagem de campos; campos existentes preservados; consumidores de `0.1.0-draft` permanecem compatíveis por leitura tolerante. `machine_readable.schema_version` do painel (`"1.0"`) permanece distinto do `schema_version` de contrato (`"1.0.0"`). **Schema version 1.0.0 (DEC-021, 2026-11-17).**
> **Change Control:** inclusão condicional na baseline v0 autorizada por CR-002 / DEC-003 (`docs/DECISIONS.md`) — o conteúdo permanece `condicional`; isto NÃO aprova o conteúdo nem inicia implementação.

**Classe de autonomia declarada:** B (proposta documental reversível; nenhuma ação Classe C executada; nenhum `approved` declarado).

> **Aviso obrigatório:** Proposta de design — **não é implementação aprovada**; stack LangGraph **pendente de D-V0-01**; gates/thresholds **pendentes de D-V0-06**; nenhum `approved` declarado. Este documento é um canônico de *design*, não código executável.

## 🔧 Decisão / Conclusão
Propõe-se um **estado tipado `AgentState`** para um grafo LangGraph (proposta, não aprovada) com quatro coleções obrigatórias — `global_context`, `ads`, `tasks`, `errors` — mais os artefatos de governança `approvals[]`, `pr_ready` e `integration_test_output`, de modo que a distinção canônica entre execução técnica (`done`), conclusão operacional (`completed`) e aceite de valor (`approved`) seja **estrutural** (campos separados) e não apenas convencional. **Trade-off assumido:** verbosidade/explicitação do estado (campos redundantes e rastreabilidade pesada) em detrimento de compacidade — prioriza rastreabilidade e auditabilidade (requisito central do baseline v0) sobre ergonomia de implementação. Nenhum campo `approved` pode ser escrito por agente de execução; somente via nó de Human Review com evidência de interação humana (ver t5).

## 🗂️ Artefato

### 1) Papel do `AgentState` no LangGraph (proposta)
- No LangGraph (stack **proposto e não aprovado** — D-V0-01), o `AgentState` seria o objeto de estado compartilhado entre nós (`design` → `architecture` → `coding` → `tdd` → `qa/unit` → `qa/integration` → `pr_generation`, com Human Review para Classe C).
- Forma proposta de implementação futura (fora deste repo): `TypedDict`/modelo Pydantic com *reducers* por campo (ex.: `errors` e `ads` com append-reducer; `global_context` com replace; contadores com add-reducer). **Este repositório não contém código;** o bloco JSON abaixo é a *especificação documental* do estado, não um módulo Python.
- **Localização proposta (PREMISSA):** schema versionado em registry de contratos (ver `30-arquitetura-tech-lead-baseline-v0.md` §Contratos); `schema_version: "1.0.0"` — reconciliado de `0.1.0-draft` para `1.0.0` por DEC-021 (D-V0-05, Classe C, 2026-11-17; reconciliação materializada por DEC-025); migração **aditiva** (sem remoção/re-tipagem; campos preservados; consumidores de `0.1.0-draft` compatíveis por leitura tolerante). Validador de referência: `docs/schemas/contract-v1.0.0.schema.json`.

### 2) Campos obrigatórios (invariantes do esquema)
| Campo | Tipo (lógico) | Obrigatório | Semântica |
|---|---|---|---|
| `global_context` | objeto | **sim** | Contexto imutável-por-run: ids de correlação, projeto, restrições, policy refs. Injetado em **toda** chamada de agente (t3). |
| `ads` | array de `ADS` | **sim** | Artefatos de design (ADS) produzidos pelo Design Agent; cada ADS referencia evidências e lacunas. |
| `tasks` | array de `Task` | **sim** | Fila de tarefas; Coding Agent processa **uma tarefa por vez** (ver t4); unidade de tracking `todo → ready → in_progress → done|partial|blocked`. |
| `errors` | array de `AgentError` | **sim** | Erros tipados por gate de origem e classe de falha (`flaky|ambiente|logica|critico|lacuna`); alimenta o ciclo de reparo (t2/t4). |
| `approvals[]` | array de `Decision` | sim (governança) | Decisões Classe C/valor; `approved` só com `decided_by` humano + `evidence_refs`. |
| `integration_test_output` | `"success"\|"failure"\|null` | sim | Resultado da validação de integração (t2); chave exigida por t4/t5 para liberar `pr_generation`. |
| `pr_ready` | boolean | sim | Flag calculada; exige `integration_test_output == "success"` **e** critérios de gate verdes; exigida por t4/t5. |

### 3) Bloco `JSON_STRICT` — esquema de estado proposto (validável)

```json
{
  "schema_name": "sdlc.agentstate",
  "schema_version": "1.0.0",
  "envelope_id": "<ULID>",
  "idempotency_key": "<hash(task_id + agent_role + input_fingerprint + schema_version)>",
  "correlation_id": "<ULID>",
  "proposal_status": "condicional",
  "stack_proposal": "langgraph (pendente D-V0-01)",
  "semantic_contract": {
    "done_neq_completed_neq_approved": true,
    "approved_requires": ["decided_by humano (PO/Classe C)", "decided_at ISO-8601", "evidence_refs nao vazio"],
    "done_requires": ["evidence_refs nao vazio"],
    "completed_note": "completed (OPS) exige rastreio a resumos/evidencias; criterio operacional exato [LACUNA] (docs/10-produto-visao-v0.md §3.2)",
    "agents_may_not_write": ["approvals[].status=approved", "approvals[].decided_by"],
    "human_review_required_for_classe_c": true
  },
  "global_context": {
    "request_id": "<ULID>",
    "task_id": "<ULID>",
    "correlation_id": "<ULID>",
    "parent_run_id": "<ULID|null>",
    "project": "sdlc-agentico",
    "stack_hint": "langgraph (proposto; pendente D-V0-01)",
    "global_constraints": [
      "done != approved",
      "nenhuma promocao a approved sem Human Review registrado",
      "no new errors vs baseline declarada (D-V0-06)",
      "lacunas sempre explicitas como [LACUNA]"
    ],
    "gates_policy_ref": "docs/42-mapeamento-gates-makefile-v0.md (proposta)",
    "thresholds_source": "pyproject.toml (materializado; cobertura ≥50%, 0 erros críticos — DEC-018/DEC-022)",
    "created_at": "<ISO-8601>"
  },
  "ads": [
    {
      "ads_id": "ADS-0001",
      "task_id": "<ULID>",
      "title": "<string>",
      "status": "draft|in_review|validated|blocked",
      "template_ref": "specs/current_ads.md [LACUNA: specs/ inexistente; proposta]",
      "diagram_refs": ["mermaid:flowchart-..."],
      "mermaid_present": true,
      "evidence_refs": [],
      "lacunas": [],
      "created_at": "<ISO-8601>",
      "updated_at": "<ISO-8601>"
    }
  ],
  "tasks": [
    {
      "task_id": "<ULID>",
      "epic": "E1|E2|E3|E4|design|arch|coding|tdd|qa|pr",
      "title": "<string>",
      "owner_agent": "design|architecture|coding|tdd|qa|orchestrator",
      "status": "todo|ready|in_progress|done|partial|blocked",
      "autonomy_class": "A|B|C",
      "assigned_order": 1,
      "tdd_before_unit_validation": true,
      "acceptance_refs": [],
      "evidence_refs": [],
      "max_attempts": 3,
      "attempts": 0,
      "updated_at": "<ISO-8601>"
    }
  ],
  "errors": [
    {
      "error_id": "ERR-0001",
      "task_id": "<ULID>",
      "run_id": "<ULID>",
      "source_gate": "make lint-ads|make test-unit|make test-integration|architecture_review",
      "exit_code": 2,
      "error_class": "flaky|ambiente|logica|critico|lacuna",
      "message": "<string>",
      "attempt": 1,
      "detected_at": "<ISO-8601>",
      "resolved": false,
      "resolution_evidence_refs": []
    }
  ],
  "approvals": [
    {
      "decision_id": "<ULID>",
      "kind": "classe_c|valor",
      "subject_ref": "<ads_id|task_id|adr_ref|pr_id>",
      "status": "pending|approved|rejected",
      "decided_by": "<humano|null>",
      "decided_at": "<ISO-8601|null>",
      "evidence_refs": [],
      "rationale": "<string|null>",
      "human_interaction_ref": "<id de sessao/ata|null>"
    }
  ],
  "integration_test_output": null,
  "pr_ready": false,
  "pr": {
    "pr_id": "<string|null>",
    "pr_url": "<url|null>",
    "created_at": "<ISO-8601|null>"
  },
  "audit": {
    "events": ["agentstate.created", "ads.emitted", "gate.evaluated", "approval.requested", "approval.granted|rejected"],
    "idempotency_key": "<hash(task_id + agent_role + input_fingerprint + schema_version)>",
    "event_log_ref": "<SoT/Event Log — ver docs/30-arquitetura-tech-lead-baseline-v0.md>"
  }
}
```

### 4) Semântica de transições (execução do agente vs valor)
| De | Para | Gatilho/Guarda | Efeito |
|---|---|---|---|
| `tasks[].status=todo` | `ready` | DoR atendido (PO/PM) | Registra `ready_at`; habilita dispatch |
| `ready` | `in_progress` | Dispatch pelo orquestrador (envelope, ver `docs/30`) | `attempts += 1` na entrada |
| `in_progress` | `done` | Trabalho concluído **com** `evidence_refs` não vazio | **Não** implica `completed` nem `approved` |
| `in_progress` | `partial` | Interrompido/incompleto | Exige bloqueios + lacunas explícitas |
| `in_progress` | `blocked` | Falha crítica ou 3 tentativas na mesma validação | Escala humana; `errors[]` preenchido |
| qualquer (agente) | `approvals[].status=approved` | **PROIBIDO para agentes** | Só via Human Review (t5) com `human_interaction_ref` |
| `integration_test_output=failure` | retorno a `coding` | Falha em `make test-unit`/`make test-integration` (t2) | `pr_ready=false`; `errors[]` atualizado |

**Invariantes canônicos (herdados de `docs/10-produto-visao-v0.md` §3.4):** `done` ⇏ `completed` ⇏ `approved`; evidência obrigatória para `done` e `approved`; lacunas sempre explícitas; estados terminais não retrocedem (retrabalho = nova execução/run).

### 4.1) Mapeamento de estados (execução → operação → valor) — ADR-005

Referência: `docs/adr/core/ADR-005-modelo-estados-autonomia.md` (status `accepted`, DEC-020) e `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` §iii/§iv (contrato v1.0.0 adotado, DEC-021, 2026-11-17; validador `docs/schemas/contract-v1.0.0.schema.json`). **Schema version 1.0.0 (DEC-021, 2026-11-17).**

| Camada | Estados | Dono | Regra central |
|---|---|---|---|
| **Execução** (subagente) | `done` \| `blocked` \| `partial` | agente/orquestrador | `done` exige `evidence_refs` não vazio. Nunca implica `completed` nem `approved`. |
| **Operação** (OPS/tracking) | `completed` | OPS/sistema | Conclui o item no sistema operacional. Exige rastreio a resumo(s)/evidência(s). **NÃO implica `approved`.** |
| **Valor** (negócio) | `pending` \| `approved` \| `rejected` | **PO** | `approved` terminal; exige `evidence`, `decided_by=PO`, `decided_at`. Agente **nunca** escreve `approved`. |

**Mapeamento de transições (guardas):**

| De (camada) | Para (camada) | Condição/guarda |
|---|---|---|
| `done` (execução) | `completed` (OPS) | Item executado + evidência + gates aplicáveis atendidos + registro de conclusão no tracking |
| `done` (execução) | `pending` (valor) | Evidência + critérios Given/When/Then anexados; orquestrador marca "valor pendente de aceite do PO" |
| `completed` (OPS) | `pending` (valor) | Rastreio item↔resumo↔evidência disponível (habilita avaliação; não decide) |
| `pending` (valor) | `approved` (valor) | **PO** decide com `evidence` + `decided_by` + `decided_at` (terminal) |
| `pending` (valor) | `rejected` (valor) | PO decide com `rationale` + `decided_by` + `decided_at` |
| `rejected` (valor) | `pending` (valor) | **Nova** evidência submetida |

**Invariantes:** `done` ⇏ `completed` ⇏ `approved`; nenhuma transição é automática; `approved` só com humano identificável + evidência; `rejected → pending` somente com nova evidência. Critério operacional exato de `completed` no tracking alvo (`docs/` como trilha, DEC-006(vi)) permanece `[LACUNA]` (D-V0-05).

### 5) Rastreabilidade e evidência
- Correlação ponta a ponta: `request_id → task_id → run(s) → ads[]/tasks[]/errors[] → evidence_refs → approvals[]/PR`.
- `global_context.correlation_id` é propagado em todo envelope/evento (ver `docs/30` §SoT); `idempotency_key` em `audit` deduplica reentregas (R7 do contrato de resumo).
- Toda escrita em `errors[]` referencia `source_gate` + `exit_code` (t2) para permitir ciclo de reparo automático determinístico.
- `approvals[].human_interaction_ref` é a **única** via legítima para `approved` (Classe C); ausência ⇒ `status` permanece `pending`.

## Evidências
- `docs/00-painel-gerencial-consolidado.md` §3–§5 (semântica de estados; D-V0-01/05/06) — lido 2026-11-16.
- `docs/10-produto-visao-v0.md` §3 (semântica canônica: execução/operação/valor; invariantes) — lido 2026-11-16.
- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Contratos/Estados (envelope, mapeamento de estados, idempotência, eventos) — lido 2026-11-16.
- `docs/20-governanca-pm-plano-baseline-v0.md` §5 (DoR/DoD; `done ≠ accepted`) — lido 2026-11-16.
- Verificação local: bloco JSON validado com `python3 -m json.tool` no momento da criação (ver t1 do Protocolo de Retorno).
- Contrato canônico v1.0.0 adotado por DEC-021 (2026-11-17); validador de referência `docs/schemas/contract-v1.0.0.schema.json`; reconciliação deste canônico registrada por DEC-025 (2026-11-17).

## Premissas e Lacunas
- `pyproject.toml` materializado com thresholds absolutos (cobertura ≥50%, 0 erros críticos — DEC-018/DEC-022); `thresholds_source` é referência paramétrica para projetos-alvo futuros, nunca hardcode.
- **[LACUNA]** Persistência/SoT/event-log concreto (stack, storage, retenção) pendente de D-V0-01; `audit.event_log_ref` é lógico. *Impacto:* durabilidade/recuperação de runs não garantida.
- **[LACUNA]** Critério operacional exato de `completed` no sistema-alvo (`docs/10-produto-visao-v0.md` §3.2) — não definido; o esquema não modela `completed` como campo de agente (correto por design).
- **[RESOLVIDO]** `schema_version` reconciliado para `1.0.0` (contrato canônico v1.0.0 — DEC-021, D-V0-05, Classe C, 2026-11-17; reconciliação materializada por DEC-025); migração aditiva (sem remoção/re-tipagem). Numeração ADR (D-V0-04) resolvida via ADR-001…ADR-008 (`accepted`, DEC-020). **Schema version 1.0.0 (DEC-021, 2026-11-17).**
- **[PREMISSA]** LangGraph como runtime proposto; reducers/checkpointer (memória/persistência) a definir após D-V0-01. Nenhum outro runtime descartado explicitamente.
- **[PREMISSA]** `specs/current_ads.md` (referenciado em `ads[].template_ref`) é proposta; `specs/` **não existe** neste repo e não foi criado.
- **[PREMISSA]** Human Review gate (t5) é o único ponto de escrita de `approved`; integra com Classe C (D-V0-03/D-V0-04).

## ✅ Próximas Ações
1. Validar este esquema com PO/TL/PM na reconciliação do baseline v0 (D-V0-05) — Dono: TL (R), PO/PM (C) — Prazo: F0 `[LACUNA]`.
2. Após D-V0-01 (stack), formalizar `AgentState` como `TypedDict`/Pydantic com reducers e testes de contrato — Dono: TL/Engenharia — Prazo: F1 `[LACUNA]`.
3. Submeter semântica `done/completed/approved` do estado a aceite do PO (Classe C) — Dono: TL (proposta) / PO (decisão) — Prazo: F0/F1.
4. Alimentar t2 (mapeamento gates/Makefile), t3 (prompts), t4 (loop de reparo) e t5 (grafo + Classe C) com este esquema — Dono: tech-lead (esta sessão/artefatos 41–45) — Prazo: esta entrega.

```json
{
  "decision_id": "01M7JCD6AXPFPJ0HHF6GBQ6KC1",
  "papel": "tech-lead",
  "classe_autonomia": "B",
  "decision_type": "arquitetura",
  "adr_ref": "none",
  "status": "condicional",
  "evidencia": ["docs/10-produto-visao-v0.md §3 (semântica canônica)", "docs/30 §Contratos/Estados", "docs/00 §5 (D-V0-05)"],
  "premissas_validadas": ["done != completed != approved", "aprovados só via Human Review", "specs/ inexistente"],
  "lacunas": ["pyproject.toml materializado (cobertura ≥50%, 0 erros críticos — DEC-018/DEC-022)", "persistência/SoT concreta pendente de D-V0-01", "critério operacional de completed [LACUNA]", "schema_version 1.0.0 adotado (DEC-021)"],
  "proximas_acoes": [{"acao": "Reconciliar esquema com contrato canônico v1.0.0 (D-V0-05)", "dono": "TL + PO + PM"}, {"acao": "Formalizar AgentState tipado após D-V0-01", "dono": "TL/Engenharia"}],
  "schema_version": "1.0"
}
```

## Resumo do Subagente
- objetivo: Definir o esquema de estado tipado (`AgentState`) proposto para LangGraph, com `global_context`, `ads`, `tasks`, `errors` e distinção estrutural entre `done` (técnico) e `approved` (valor/PO).
- ação executada: Leitura integral dos canônicos (00/10/20/30/40/README); especificação documental do estado com campos tipados, invariantes, semântica de transições, rastreabilidade por ids/correlação e bloco JSON_STRICT validável; explicitação de lacunas (thresholds, persistência, critério de `completed`).
- resultado/artefato: `docs/41-agentstate-esquema-v0.md` (este documento), contendo o bloco JSON_STRICT do `AgentState` (§3) e as tabelas de transições/invariantes.
- evidência: Canônicos citados acima (lidos 2026-11-16); bloco JSON validado localmente com `python3 -m json.tool`; verificação cruzada README ↔ canônicos realizada após edição do índice (nesta mesma entrega).
- status: done
- bloqueios/riscos: Nenhum bloqueio de execução documental. Risco: esquema pode conflitar com contrato canônico v1.0.0 (D-V0-05) — registrado como `[LACUNA]`, não resolvido silenciosamente.
- decisão pendente: Aprovação humana (Classe C) da semântica de estados e do `schema_version` do contrato; stack LangGraph (D-V0-01); thresholds (D-V0-06).
- próxima ação recomendada: Executar t2 (mapeamento gates↔Makefile) consumindo este esquema; em seguida submeter à reconciliação do baseline v0.
