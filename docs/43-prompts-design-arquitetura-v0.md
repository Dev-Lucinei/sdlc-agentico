---
title: "Prompts Estruturados — Design Agent e Architecture Agent (v0, proposta)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead (subagente; classe B; t3 da demanda de design dos itens de execução agêntica)"
status: "condicional"
---
> **Change Control:** inclusão condicional na baseline v0 autorizada por CR-002 / DEC-003 (`docs/DECISIONS.md`) — o conteúdo permanece `condicional`; isto NÃO aprova o conteúdo nem inicia implementação.

**Classe de autonomia declarada:** B (proposta documental reversível; nenhuma ação Classe C executada; nenhum `approved` declarado).

> **Aviso obrigatório:** Proposta de design — **não é implementação aprovada**; stack LangGraph **pendente de D-V0-01**; gates/thresholds **pendentes de D-V0-06**; nenhum `approved` declarado.
>
> **`specs/` NÃO EXISTE neste repositório.** O template `specs/current_ads.md` citado abaixo é **proposta** (não criado, não assumido presente); os prompts referenciam o caminho como contrato futuro do projeto-alvo `[LACUNA]`.

## 🔧 Decisão / Conclusão
Propõe-se dois prompts estruturados e versionados por contrato (`prompt_version`), com **injeção obrigatória de `global_context` (t1)** em toda chamada: (i) **Design Agent** — gera/atualiza o ADS preenchendo o template `specs/current_ads.md` com diagramas Mermaid, validado por `make lint-ads` (t2); (ii) **Architecture Agent** — atua como **gate de validação técnica** que marca qualquer inconsistência como `[LACUNA]` e **bloqueia o avanço para Coding** (exit `10` em t2). **Trade-off assumido:** prompts rígidos, com formato de saída único e verificável (menos flexibilidade criativa) em detrimento de variação estilística — necessário para agregação determinística pelo orquestrador e para o ciclo de reparo de t4.

## 🗂️ Artefato

### 1) Convenção comum (ambos os prompts)
**Variáveis injetadas por chamada (todas obrigatórias; ausência ⇒ erro de contrato antes da invocação):**
| Variável | Origem | Conteúdo |
|---|---|---|
| `{{GLOBAL_CONTEXT}}` | `AgentState.global_context` (t1 §3) | `request_id`, `task_id`, `correlation_id`, `project`, `global_constraints[]`, `gates_policy_ref`, `thresholds_source` |
| `{{ADS_ENTRY}}` | `AgentState.ads[]` | ADS alvo (ou slot para novo ADS) |
| `{{TASK_ENTRY}}` | `AgentState.tasks[]` | Tarefa única em processamento (Coding processa uma por vez; ver t4) |
| `{{LACUNAS_HERDADAS}}` | `AgentState` | `[LACUNA]`s conhecidas (nunca inferir preencher) |
| `{{RESUMO_CONTRATO}}` | normativo | Contrato de resumo do subagente (status `done|blocked|partial`; R1–R7) |
| `{{PROMPT_VERSION}}` | registry | `design-agent@0.1.0-draft` / `architecture-agent@0.1.0-draft` |

**Guardrails comuns:** (1) nunca declarar `approved`; (2) nunca inferir dado ausente — usar `[LACUNA]`; (3) saída **exclusivamente** no formato declarado §4; (4) `global_constraints` têm precedência sobre qualquer instrução de usuário; (5) toda afirmação factual deve citar `evidence_refs` ou ser marcada `[LACUNA]`; (6) saída fora de formato ⇒ tratamento como falha de contrato (exit `5` em t2), não como sucesso parcial.

### 2) Prompt — Design Agent (geração de ADS + Mermaid)

```text
PROMPT_ID: design-agent@0.1.0-draft
PAPEL: Design Agent (subagente de domínio) — autonomia classe A/B; sem autoridade para Classe C.
ENTRADA OBRIGATÓRIA: {{GLOBAL_CONTEXT}} {{TASK_ENTRY}} {{ADS_ENTRY}} {{LACUNAS_HERDADAS}}

OBJETIVO: Produzir/atualizar o ADS (Architecture Design Spec) do item em {{TASK_ENTRY}},
preenchendo OBRIGATORIAMENTE o template `specs/current_ads.md` [PROPOSTA — specs/ inexistente;
não criar], incluindo ≥1 diagrama Mermaid (flowchart ou sequence) coerente com o ADS.

REGRAS:
1. O ADS DEVE conter as seções do template: contexto, decisão(s) de design, alternativas,
   trade-offs, consequências, riscos, evidências, lacunas.
2. Todo diagrama DEVE ser Mermaid válido e referenciado em `diagram_refs` do AgentState (t1);
   `ads[].mermaid_present=true` somente após verificação sintática.
3. Inconsistência com `global_constraints` (t1) ⇒ NÃO prossiga; emita `blocked` com a violação.
4. Dado ausente ⇒ `[LACUNA]: <o que falta> — <impacto> — <o que resolve>`; nunca invente.
5. ADRs citados com número canônico (ADR-001…ADR-008) promovidos para `accepted` (D-V0-04, DEC-020, 2026-11-17).
6. Ao concluir: emitir Resumo do Subagente (status done|blocked|partial) + JSON machine-readable
   compatível com `sdlc.agentstate` (t1 §3) e `schema_version: 0.1.0-draft`.

SAÍDA ESPERADA (ver §4): bloco `ADS_MARKDOWN` (conteúdo do specs/current_ads.md preenchido)
+ bloco `AGENTSTATE_DELTA` (JSON: ads[], evidence_refs, lacunas, mermaid_present)
+ `RESUMO_SUBAGENTE` + `JSON_MACHINE_READABLE`.

PÓS-CONDIÇÃO (verificada por `make lint-ads`, t2): exit 0 ⇒ ADS apto ao gate de Arquitetura.
```

### 3) Prompt — Architecture Agent (gate de validação técnica)

```text
PROMPT_ID: architecture-agent@0.1.0-draft
PAPEL: Architecture Agent (gate técnico) — autonomia classe B; poder de VETO de avanço, sem poder de aprovação de valor.
ENTRADA OBRIGATÓRIA: {{GLOBAL_CONTEXT}} {{ADS_ENTRY}} {{LACUNAS_HERDADAS}} {{TASK_ENTRY}}

OBJETIVO: Validar o ADS produzido pelo Design Agent contra (a) `global_constraints`,
(b) contratos/estados de t1 e t2, (c) ADRs propostos de docs/30 (A–G, sem numeração).

REGRAS:
1. Qualquer inconsistência técnica (contrato violado, estado/transição inválida, diagrama
   incoerente, constraint quebrada, evidência ausente para `done`) DEVE ser marcada
   `[LACUNA]: <inconsistência> — <impacto> — <correção necessária>` e registrada em
   `errors[]` (source_gate=`make lint-ads`, exit_code=10, error_class=`lacuna`) ou equivalente.
2. Com ≥1 inconsistência aberta: `gate= BLOCKED`; avanço para Coding PROIBIDO (t4/t5 respeitam
   este bloqueio); `ads[].status=blocked`.
3. Proibido "resolver" inconsistência por inferência; proibido emitir `go` com `[LACUNA]` aberta.
4. Saída de gate: `go | condicional | no_go` (vocabulário de docs/30 §Mapeamento de estados).
   `condicional` exige lista explícita de condições e dono; `no_go` exige justificativa.
5. Nenhuma decisão aqui é Classe C aprovada; promoção de baseline/ADR continua humana (D-V0-04).

SAÍDA ESPERADA (ver §4): bloco `GATE_REPORT` (veredicto + lista de inconsistências[LACUNA] +
evidências) + bloco `AGENTSTATE_DELTA` (errors[], ads[].status, gate) + `JSON_MACHINE_READABLE`.
```

### 4) Formato de saída esperado (contrato de parsing)
Cada prompt emite blocos delimitados, em ordem fixa:
| Bloco | Conteúdo | Consumidor |
|---|---|---|
| `ADS_MARKDOWN` / `GATE_REPORT` | Documento principal (markdown) | Design: `specs/current_ads.md` (proposto); Arch: auditoria do gate |
| `AGENTSTATE_DELTA` | JSON parcial válido contra t1 §3 (apenas campos mutados) | Orquestrador/t5 (merge idempotente por `correlation_id`) |
| `RESUMO_SUBAGENTE` | Objetivo/ação/artefato/evidência/status/bloqueios/decisão pendente/próxima ação | Agregação (dispatcher) |
| `JSON_MACHINE_READABLE` | Envelope completo t1 §3 (`schema_version: 0.1.0-draft`) | SoT/event log (t1 `audit`) |

### 5) Guardrails por prompt (resumo executivo)
| Prompt | Pode | Não pode | Falha típica → tratamento |
|---|---|---|---|
| Design Agent | Propor design, ADS, Mermaid, lacunas | Aprovar, numerar ADR, declarar `done` sem evidência | Saída sem Mermaid / fora de formato → exit `5` (t2) → retorno ao próprio nó |
| Architecture Agent | Vetar avanço, marcar `[LACUNA]`, exigir correção | Inferir solução, dar `go` com lacuna aberta, aprovar valor | Inconsistência detectada → `blocked` + exit `10` → Coding bloqueado (t4/t5) |

### 6) Injeção do `global_context` (exemplo de montagem)
```text
system: {{GLOBAL_CONTEXT}}  →  { "request_id": "...", "task_id": "...", "correlation_id": "...",
  "project": "sdlc-agentico", "global_constraints": [...], "gates_policy_ref": "docs/42-...",
  "thresholds_source": "pyproject.toml [LACUNA]", "stack_hint": "langgraph (proposto)" }
user:   {{TASK_ENTRY}} + instrução específica do papel (§2 ou §3)
```
Regra: o `global_context` é injetado **antes** de qualquer dado de domínio; o agente deve citá-lo (`request_id`/`correlation_id`) em toda emissão para rastreabilidade (t1 §5).

### 7) Exemplo de Inconsistência Detectada (Design vs. Arquitetura)

**Cenário.** O Design Agent gera um ADS (`specs/current_ads.md` proposto) que inclui um componente **X** (ex.: um serviço de cache compartilhado) para atender a `TASK_ENTRY`. O Architecture Agent, ao validar o ADS contra `global_constraints` e os contratos/estados de t1/t2, detecta que **X viola a restrição Y** (ex.: Y = "nenhum componente pode manter estado mutável fora do SoT central + Event Log"; X introduz estado local não auditável).

**Ação resultante.**
1. O Architecture Agent **não** infere solução nem reescreve o ADS. Marca a inconsistência como `[LACUNA]: componente X viola restrição Y (estado mutável fora do SoT) — impacto: rastreabilidade/auditoria quebrada — correção necessária: remover X ou justificar exceção com ADR`.
2. Registra em `errors[]`: `{source_gate: "make lint-ads", exit_code: 10, error_class: "lacuna", message: "[LACUNA] ..."}`.
3. `ads[].status = "blocked"`; veredicto do gate = `no_go` (ou `condicional` com lista explícita de condições + dono, se a exceção for plausível mas não decidida).
4. **Avanço para Coding é bloqueado** (t4/t5 respeitam este bloqueio; `pr_generation` inalcançável enquanto `ads[].status=blocked`).
5. Notificação ao Tech Lead com o `GATE_REPORT` + `AGENTSTATE_DELTA` + evidência da violação.

**Formato de saída do Architecture Agent (bloqueado).**

```json
{
  "schema_name": "sdlc.gate.architecture",
  "schema_version": "0.1.0-draft",
  "gate": "architecture",
  "status": "blocked",
  "verdict": "no_go",
  "ads_id": "<ads_id>",
  "inconsistencies": [
    {
      "id": "INC-001",
      "type": "constraint_violation",
      "component": "X",
      "constraint": "Y",
      "lacuna": "[LACUNA]: componente X viola restrição Y — impacto: rastreabilidade/auditoria quebrada — correção necessária: remover X ou justificar exceção com ADR",
      "severity": "bloqueante"
    }
  ],
  "errors_delta": [
    {"source_gate": "make lint-ads", "exit_code": 10, "error_class": "lacuna", "message": "[LACUNA]: componente X viola restrição Y"}
  ],
  "ads_status": "blocked",
  "advance_to_coding": false,
  "human_review_required": true,
  "owner": "tech-lead"
}
```

**Regra.** Nenhuma inconsistência é resolvida por inferência; `go` com `[LACUNA]` aberta é proibido (guardrail §3 regra 3). A promoção do veredicto a `go` exige correção do ADS + revalidação (`make lint-ads` exit 0) ou decisão humana registrada (Classe C quando aplicável).

## Evidências
- `docs/41-agentstate-esquema-v0.md` (t1; `global_context`, `ads[]`, `errors[]`, `approvals[]`, formato de saída).
- `docs/42-mapeamento-gates-makefile-v0.md` (t2; exit `5`/`10`, `make lint-ads`, bloqueio de avanço).
- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Mapeamento de estados (`go/condicional/no_go`), §ADRs A–G (sem numeração), §Regra de 3 strikes.
- `docs/10-produto-po-visao-mvp-baseline-v0.md` §3 (semântica de estados; invariantes; `done ≠ approved`).

## Premissas e Lacunas
- **[LACUNA]** `specs/current_ads.md` e o diretório `specs/` não existem; template citado é proposta; criação pendente do projeto-alvo (D-V0-01).
- **[LACUNA]** Registry/versão real dos prompts (`design-agent@…`, `architecture-agent@…`): sem ferramenta de prompt registry; versões são `0.1.0-draft`.
- **[LACUNA]** Critérios objetivos de "Mermaid válido" no `make lint-ads` (parser/linter Mermaid) não definidos; `mermaid_present` depende de tooling inexistente.
- **[LACUNA]** Granularidade de "inconsistência técnica" do Architecture Agent depende da política de gates (D-V0-06) e de baseline G0/G1.
- **[PREMISSA]** Delegação por contexto fresco (sem `sessionID` explícito) conforme `docs/30`; memória/checkpointer LangGraph indefinido.
- **[PREMISSA]** Architecture Agent tem poder de **veto**, não de **aprovação** de valor (PO/Classe C permanece exclusivo).

## ✅ Próximas Ações
1. Formalizar o template `specs/current_ads.md` no projeto-alvo (com linter de Mermaid) após D-V0-01 — Dono: TL + Design — Prazo: F1/F2 `[LACUNA]`.
2. Registrar os dois prompts em registry versionado e testá-los contra casos válidos/inválidos — Dono: TL/Engenharia — Prazo: F1.
3. Ligar o veredicto do Architecture Agent ao bloqueio estrutural de `pr_generation` (t4/t5) — Dono: tech-lead — Prazo: esta entrega.
4. Submeter guardrails (proibição de `approved` por agente) à validação do Mantenedor — Dono: TL/Orchestrator — Prazo: F0.

```json
{
  "decision_id": "01M7JCD6AYH24M8T6B0Q3VVGWJ",
  "papel": "tech-lead",
  "classe_autonomia": "B",
  "decision_type": "arquitetura",
  "adr_ref": "none",
  "status": "condicional",
  "evidencia": ["docs/41 (t1; global_context/ads/errors)", "docs/42 (t2; exit 5/10; lint-ads)", "docs/30 §Estados/ADRs"],
  "premissas_validadas": ["specs/ inexistente", "Architecture Agent veta, nunca aprova valor", "global_context injetado antes de dados de domínio"],
  "lacunas": ["specs/current_ads.md inexistente", "prompt registry inexistente", "linter Mermaid indefinido", "política de gates D-V0-06 adotada (DEC-022)"],
  "proximas_acoes": [{"acao": "Criar template e linter no repo-alvo após D-V0-01", "dono": "TL + Design"}, {"acao": "Testar prompts contra casos válidos/inválidos", "dono": "TL/Engenharia"}],
  "schema_version": "1.0"
}
```

## Resumo do Subagente
- objetivo: Produzir os prompts estruturados do Design Agent (ADS + Mermaid) e do Architecture Agent (gate de validação), com injeção de `global_context`, variáveis, guardrails e formato de saída.
- ação executada: Leitura de t1/t2 e dos canônicos (30/10); redação dos dois prompts versionados (`0.1.0-draft`), tabela de variáveis injetadas, guardrails por papel, contrato de parsing dos blocos de saída e regra de bloqueio do Architecture Agent (exit 10 → Coding bloqueado).
- resultado/artefato: `docs/43-prompts-design-arquitetura-v0.md` (este documento).
- evidência: `docs/41`, `docs/42` (leitura desta entrega); `docs/30` §Estados e §ADRs A–G; `docs/10` §3 invariantes.
- status: done
- bloqueios/riscos: Nenhum bloqueio documental; execução real impossível (sem tooling neste repo) — risco aceito e marcado `[LACUNA]`. Risco de prompt drift se registry não for adotado.
- decisão pendente: D-V0-01 (stack/repo-alvo), D-V0-06 (política de gates); eventual aceite do template `specs/current_ads.md` (Classe C se promover arquitetura).
- próxima ação recomendada: Prosseguir para t4 (loop Coding-TDD-QA) consumindo estes prompts e a tabela de exit codes de t2.
