---
title: "Loop de Feedback Coding-TDD-QA — Grafo de Estados e Transições (v0, proposta)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead (subagente; classe B; t4 da demanda de design dos itens de execução agêntica)"
status: "condicional"
---
> **Change Control:** inclusão condicional na baseline v0 autorizada por CR-002 / DEC-003 (`docs/DECISIONS.md`) — o conteúdo permanece `condicional`; isto NÃO aprova o conteúdo nem inicia implementação.

**Classe de autonomia declarada:** B (proposta documental reversível; nenhuma ação Classe C executada; nenhum `approved` declarado).

> **Aviso obrigatório:** Proposta de design — **não é implementação aprovada**; stack LangGraph condicional (CR-009-C); D-V0-06 APROVADO E MATERIALIZADO (DEC-022, 2026-11-17) — thresholds absolutos cobertura ≥50%, 0 erros críticos; nenhum `approved` declarado.

## 🔧 Decisão / Conclusão
Propõe-se um loop de feedback determinístico **`coding → tdd → qa_unit → qa_integration → (pr_gate)`** com retorno forçado a `coding` em qualquer falha de validação (`make test-unit` / `make test-integration`, t2), TDD **anterior** à validação unitária, processamento de **uma tarefa por vez** e geração de PR **condicionada** às chaves `integration_test_output == "success"` **e** `pr_ready == true` (definidas neste documento e no `AgentState` de t1; alimentadas pelos exit codes de t2). **Trade-off assumido:** serialização estrita (uma tarefa em voo, sem paralelismo de execução) em detrimento de throughput — correto para MVP de baixo risco e para a regra canônica de reparo de 3 strikes.

## 🗂️ Artefato

### 1) Bloco `JSON_STRICT` — grafo de estados/transições + pseudocódigo (validável)

```json
{
  "schema_name": "sdlc.loop.coding_tdd_qa",
  "schema_version": "0.1.0-draft",
  "proposal_status": "condicional",
  "stack_proposal": "langgraph (pendente D-V0-01)",
  "references": {
    "t1_agentstate": "docs/41-agentstate-esquema-v0.md",
    "t2_makefile_gates": "docs/42-mapeamento-gates-makefile-v0.md",
    "t3_prompts": "docs/43-prompts-design-arquitetura-v0.md"
  },
  "state_keys": {
    "integration_test_output": {
      "type": "string|null",
      "values": ["success", "failure", null],
      "defined_in": "t1 §3 (AgentState.integration_test_output)",
      "set_by": "qa_integration node apos make test-integration (t2 §2: exit 0 => success; exit 3 => failure)",
      "required_for": ["pr_generation"]
    },
    "pr_ready": {
      "type": "boolean",
      "default": false,
      "defined_in": "t1 §3 (AgentState.pr_ready)",
      "set_by": "pr_gate node: true somente se integration_test_output=='success' E todos os gates aplicaveis verdes (t2 §4)",
      "required_for": ["pr_generation"]
    },
    "tasks_single_in_flight": {
      "type": "invariant",
      "rule": "no maximo 1 item de tasks[] com status=='in_progress' por run; Coding Agent processa UMA tarefa por vez"
    }
  },
  "nodes": [
    {"id": "coding", "agent": "coding-agent", "role": "implementacao/reparo", "entry_guard": "existe exatamente 1 task in_progress; architecture gate != BLOCKED (t3)", "effects": ["tasks[].attempts += 1 na entrada", "aplica patch na task ativa"], "exits": ["tdd"]},
    {"id": "tdd", "agent": "tdd-agent", "role": "geracao de testes e cobertura ANTES da validacao unitaria", "entry_guard": "coding concluido (patch aplicado)", "effects": ["gera/atualiza testes", "registra coverage_report_ref e evidencia em tasks[].evidence_refs", "tasks[].tdd_before_unit_validation=true"], "exits": ["qa_unit"], "note": "cobertura gerada ANTES de qualquer validacao unitaria; limiar lido do pyproject.toml do projeto-alvo [LACUNA]"},
    {"id": "qa_unit", "agent": "qa-agent", "role": "validacao unitaria via Makefile", "entry_guard": "tdd concluido com evidencia de testes", "command": "make test-unit (t2)", "exit_codes": {"0": "qa_integration", "2": "coding", "1": "coding", "4": "blocked"}, "exits": ["qa_integration", "coding", "blocked"]},
    {"id": "qa_integration", "agent": "qa-agent", "role": "validacao de integracao via Makefile", "entry_guard": "qa_unit exit 0", "command": "make test-integration (t2)", "exit_codes": {"0": "pr_gate", "3": "coding", "1": "coding", "4": "blocked"}, "effects_on_exit": {"0": "integration_test_output=success", "3": "integration_test_output=failure; pr_ready=false"}, "exits": ["pr_gate", "coding", "blocked"]},
    {"id": "pr_gate", "agent": "orchestrator/policy-gate", "role": "decisao de aptidao para PR", "entry_guard": "qa_integration exit 0", "rule": "pr_ready=true SOMENTE se integration_test_output=='success' E lint-ads/test-unit/test-integration verdes; senao pr_ready=false", "exits": ["pr_generation", "coding"]},
    {"id": "pr_generation", "agent": "coding-agent/orchestrator", "role": "geracao de PR", "entry_guard": "integration_test_output=='success' AND pr_ready==true", "blocked_unless": ["integration_test_output=='success'", "pr_ready==true"], "exits": ["end"]},
    {"id": "blocked", "agent": "orchestrator", "role": "estado terminal de reparo esgotado", "entry_guard": "tasks[].attempts>=3 na mesma validacao OU exit_code in {4,10,130} OU violacao de constraint", "effects": ["tasks[].status=blocked", "escalonamento humano com evidencia (errors[])"], "exits": ["human_review"]}
  ],
  "transitions": [
    {"from": "coding", "to": "tdd", "guard": "patch aplicado e task ainda in_progress"},
    {"from": "tdd", "to": "qa_unit", "guard": "testes gerados; coverage_report_ref registrado"},
    {"from": "qa_unit", "to": "qa_integration", "guard": "exit_code==0", "effect": "pr_ready permanece false ate pr_gate"},
    {"from": "qa_unit", "to": "coding", "guard": "exit_code in {1,2}", "effect": "errors[]+={source_gate:'make test-unit', exit_code}; tasks[].attempts+=1; RETORNO FORCADO"},
    {"from": "qa_unit", "to": "blocked", "guard": "exit_code==4 OU tasks[].attempts>=3", "effect": "errors[]+={error_class:'ambiente'|...}; escalonamento humano"},
    {"from": "qa_integration", "to": "pr_gate", "guard": "exit_code==0", "effect": "integration_test_output='success'"},
    {"from": "qa_integration", "to": "coding", "guard": "exit_code in {1,3}", "effect": "integration_test_output='failure'; pr_ready=false; errors[]+={source_gate:'make test-integration', exit_code}; tasks[].attempts+=1; RETORNO FORCADO"},
    {"from": "qa_integration", "to": "blocked", "guard": "exit_code==4 OU tasks[].attempts>=3", "effect": "escalonamento humano"},
    {"from": "pr_gate", "to": "pr_generation", "guard": "integration_test_output=='success' AND pr_ready==true", "effect": "pr.pr_id/pr_url preenchidos; audit event 'pr.generated'"},
    {"from": "pr_gate", "to": "coding", "guard": "NOT (integration_test_output=='success' AND pr_ready==true)", "effect": "pr_ready=false; errors[]+={error_class:'lacuna', message:'pr_gate negou: pre-condicoes de PR nao atendidas'}"},
    {"from": "*", "to": "blocked", "guard": "exit_code==130 (critico) OU 1 critica OU violacao de global_constraints", "effect": "parada imediata; escala humana"}
  ],
  "failure_semantics": {
    "max_attempts_same_validation": 3,
    "on_threshold_exceeded": "tasks[].status='blocked' + escalonamento humano (3 strikes, docs/30 §Tratamento de falhas)",
    "critical_failure": "1 ocorrencia => parada imediata (exit 130)",
    "forced_return_nodes": ["qa_unit->coding", "qa_integration->coding", "pr_gate->coding"]
  },
  "pseudocode": "function run_loop(state):\n  assert count(t for t in state.tasks if t.status=='in_progress') == 1, 'Coding processa UMA tarefa por vez'\n  loop:\n    task = the_single_in_progress_task(state)\n    state = coding_agent(state, task)            # patch\n    state = tdd_agent(state, task)               # cobertura ANTES da validacao unitaria\n    assert task.tdd_before_unit_validation == true\n    rc_unit = exec('make test-unit', TASK_ID=task.task_id)   # t2\n    if rc_unit == 0:\n      pass\n    elif rc_unit in (1,2):\n      state = record_error(state, 'make test-unit', rc_unit)\n      task.attempts += 1\n      if task.attempts >= 3: return blocked(state, task)\n      continue                                  # RETORNO FORCADO a coding\n    else:  # 4 ou critico\n      return blocked(state, task, reason=rc_unit)\n    rc_int = exec('make test-integration', TASK_ID=task.task_id)  # t2\n    if rc_int == 0:\n      state.integration_test_output = 'success'\n    elif rc_int in (1,3):\n      state.integration_test_output = 'failure'\n      state.pr_ready = False\n      state = record_error(state, 'make test-integration', rc_int)\n      task.attempts += 1\n      if task.attempts >= 3: return blocked(state, task)\n      continue                                  # RETORNO FORCADO a coding\n    else:\n      return blocked(state, task, reason=rc_int)\n    state.pr_ready = (state.integration_test_output == 'success') and all_gates_green(state)  # t2 §4\n    if state.integration_test_output == 'success' and state.pr_ready is True:\n      return pr_generation(state, task)         # unico caminho para PR\n    else:\n      state.pr_ready = False\n      continue                                  # pr_gate nega; retorno a coding",
  "pr_preconditions": {
    "required": ["integration_test_output=='success'", "pr_ready==true"],
    "on_violation": "pr_generation NAO emite PR; loga errors[] (error_class='lacuna'); retorna a coding ou blocked conforme attempts",
    "note": "pr_ready NUNCA true com integration_test_output!='success'; coberto por teste de contrato no projeto-alvo [LACUNA]"
  },
  "done_vs_approved": {
    "note": "Este loop termina em PR gerado (execucao), NUNCA em 'approved'. Aceite de valor (PO/Classe C) ocorre apos Human Review (t5). done != completed != approved (t1 §4; docs/10 §3)."
  }
}
```

### 2) Leitura do grafo (resumo)
- Caminho feliz: `coding → tdd → qa_unit(0) → qa_integration(0) → pr_gate → pr_generation`.
- Qualquer não-zero em `test-unit`/`test-integration` (exceto `4`/`130`) ⇒ **retorno forçado a `coding`** com `attempts += 1`.
- `tasks[].attempts >= 3` na mesma validação ⇒ `blocked` + escala humana (3 strikes).
- `4` (ambiente) e `130` (crítico) nunca retentam: bloqueio/parada imediatos.
- `pr_generation` só é alcançável com `integration_test_output=="success"` **e** `pr_ready==true` — ambos definidos em t1 (`AgentState`) e setados conforme exit codes de t2.

### 3) Regra dos 3 Strikes (formalizada)

**Definição.** Após **3 falhas consecutivas no mesmo nó do loop** (Coding→TDD→QA) — i.e., `tasks[].attempts >= 3` na mesma validação (`make test-unit` ou `make test-integration`) — o loop **escala** em vez de retentar. A contagem é por validação e por tarefa ativa; reset ocorre apenas quando a validação passa (`exit 0`) ou quando a tarefa é substituída. Consistente com `docs/30-arquitetura-tech-lead-baseline-v0.md` §Tratamento de falhas e com a tabela de exit codes de `docs/42` §2.

**Critérios de escalação.**

| Falha (exit code) | Tipo de falha | Agente notificado | Ação automática |
|---|---|---|---|
| `1` (lint-ads design/arch) | `logica` | Architecture Agent + Tech Lead | Pausar nó de origem; registrar `[LACUNA]` se inconsistência técnica; aguardar correção dirigida |
| `2` (test-unit) | `logica` ou `flaky` | Coding Agent + Tech Lead (após 3 strikes) | Pausar loop; `tasks[].status=blocked`; abrir revisão humana |
| `3` (test-integration) | `logica` ou `ambiente` | QA Agent + Tech Lead (após 3 strikes) | Pausar loop; `integration_test_output=failure`; `pr_ready=false`; revisão humana |
| `4` (ferramenta/ambiente ausente) | `ambiente` | Tech Lead + Operador/Infra | **Bloquear imediatamente** (sem retry); intervenção de infraestrutura |
| `5` (lint-ads contrato/schema) | `logica` | Design Agent + Tech Lead | Bloquear avanço para Coding; corrigir ADS |
| `6` (cobertura abaixo do threshold) | `lacuna` | Tech Lead + PO (decisão de threshold) | Bloquear `pr_generation`; elevar cobertura ou decidir threshold (D-V0-06) |
| `10` (inconsistência de arquitetura) | `lacuna` | Tech Lead | Bloquear avanço para Coding; registrar `[LACUNA]` |
| `130` (SIGINT/crítico) | `critico` | Tech Lead + Mantenedor | **Parada total imediata** (1 ocorrência basta); escala humana |
| `>=64` (não mapeado) | `lacuna` | Tech Lead | Tratar como `[LACUNA]`; **nunca** inferir sucesso; escalar |

**Regra de parada antecipada.** Falha `critico` (`exit 130`) para na **1ª ocorrência** (autonomia-e-estados: 1 crítico ⇒ stop), independentemente de `attempts`. Falha `ambiente` (`exit 4`) não retenta cegamente.

**Referência à taxonomia de falhas (AGENTS.md / `docs/30`).** As classes de `errors[].error_class` seguem a taxonomia canônica: `flaky` (intermitente/ambiente), `ambiente` (tooling/infra ausente), `logica` (defeito de código/teste), `degradado` (performance/qualidade abaixo do aceitável), `critico` (falha bloqueante/segurança). A classe `lacuna` é extensão documental para inconsistência não resolvida (exit 6/10/≥64). Toda falha é registrada em `errors[]` com `source_gate`, `exit_code` e `error_class` antes de qualquer retry (t2 §2).

**KPI proposto.** **KPI-7 = "taxa de sucesso do loop"** = (iterações até passar) / (total de iterações) por tarefa, agregado por fase. Mede eficiência do ciclo Coding→TDD→QA e a eficácia da regra de 3 strikes (meta inicial a calibrar no piloto F-ÚNICO-2; baseline "no new errors" sobre a baseline declarada). Instrumentação depende de F-ÚNICO-1 (D-V0-01/06). Consistente com KPIs de fluxo do PO (`docs/10`/`docs/11`) e com o roadmap (`docs/47`).

## Evidências
- `docs/41-agentstate-esquema-v0.md` (t1; chaves `integration_test_output`, `pr_ready`, `tasks[].attempts`, `errors[]`).
- `docs/42-mapeamento-gates-makefile-v0.md` (t2; alvos `make test-unit`/`make test-integration`, exit codes 0/1/2/3/4/130, fluxo §3).
- `docs/43-prompts-design-arquitetura-v0.md` (t3; bloqueio do Architecture Agent pré-Coding; guardrails).
- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Tratamento de falhas (3 strikes / 1 crítico) e §Mapeamento de estados.
- Verificação local: bloco JSON validado com `python3 -m json.tool` no momento da criação (ver Protocolo de Retorno).

## Premissas e Lacunas
- **[LACUNA]** Execução real do loop depende de LangGraph + Makefile + `pyproject.toml` no projeto-alvo — nenhum existe neste repo (D-V0-01/06).
- **[LACUNA]** Critério objetivo de "cobertura gerada" antes de `qa_unit`: depende de linter/coverage tooling do projeto-alvo (limiar lido de `pyproject.toml`, nunca hardcode).
- **[LACUNA]** Heurística de classificação `flaky` vs `logica` em `make test-unit` (exit 2) não definida; proposta assume classificação humana inicial.
- **[LACUNA]** `pr_generation` real (criação de PR em forge/git) depende de repo-alvo e permissões — hoje no-op (`git` sem remote; AGENTS.md).
- **[PREMISSA]** Serialização de 1 tarefa em voo é deliberada; paralelismo futuro exigiria revisão deste grafo (change control).
- **[PREMISSA]** `pr_gate` é nó de política/orquestrador, não de agente de domínio; não concede `approved`.

## ✅ Próximas Ações
1. Acoplar este grafo ao grafo completo com Human Review gate Classe C (t5) — Dono: tech-lead — Prazo: esta entrega.
2. Implementar no projeto-alvo: reducer de `tasks[].attempts`, asserção "1 tarefa in_progress" e testes de contrato das pré-condições de PR — Dono: Engenharia/TL — Prazo: F2 `[LACUNA]`.
3. Definir política de flake e thresholds no `pyproject.toml` do projeto-alvo — Dono: TL + PM — Prazo: F1/F3.
4. Medir taxa de reparo (loop iterations/PR) como KPI de fluxo após piloto — Dono: PM/TL — Prazo: F4.

```json
{
  "decision_id": "01M7JCD6AYK6X6DA8RDN5VN3WQ",
  "papel": "tech-lead",
  "classe_autonomia": "B",
  "decision_type": "arquitetura",
  "adr_ref": "none",
  "status": "condicional",
  "evidencia": ["docs/41 (chaves integration_test_output/pr_ready)", "docs/42 (exit codes/fluxo reparo)", "docs/30 §3 strikes"],
  "premissas_validadas": ["1 tarefa in_progress por run", "TDD antes de test-unit", "retorno forçado a coding em falha", "PR exige success+pr_ready"],
  "lacunas": ["tooling LangGraph/Makefile/pyproject inexistentes", "heurística flaky indefinida", "pr_generation sem repo-alvo", "threshold de cobertura [LACUNA]"],
  "proximas_acoes": [{"acao": "Integrar grafo ao t5 com Human Review Classe C", "dono": "tech-lead"}, {"acao": "Implementar reducers/asserções no projeto-alvo", "dono": "TL/Engenharia"}],
  "schema_version": "1.0"
}
```

## Resumo do Subagente
- objetivo: Especificar a lógica do loop Coding→TDD→QA com retorno forçado a Coding em falhas e pré-condições formais para geração de PR.
- ação executada: Definição das chaves `integration_test_output`/`pr_ready` (referenciando t1/t2), do grafo de 7 nós com guards/efeitos, das transições com exit codes e do pseudocódigo determinístico, incluindo asserção de unicidade de tarefa e regra de 3 strikes.
- resultado/artefato: `docs/44-loop-feedback-coding-tdd-qa-v0.md` (este documento).
- evidência: Bloco JSON validado com `python3 -m json.tool` nesta entrega; `docs/41`, `docs/42`, `docs/43` (lidos); `docs/30` §Tratamento de falhas.
- status: done
- bloqueios/riscos: Bloqueio de execução real (sem tooling no repo) — `[LACUNA]` aceito por design. Risco: divergência entre pseudocódigo e implementação LangGraph futura — mitigado por testes de contrato propostos.
- decisão pendente: D-V0-01 resolvido (DEC-018); D-V0-06 adotado (DEC-022); eventual promoção deste grafo a canônico de implementação (Classe C).
- próxima ação recomendada: Prosseguir para t5 (grafo LangGraph + gate Classe C), incorporando este loop como subgrafo.
