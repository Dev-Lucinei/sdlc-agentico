---
title: "Grafo de Estados LangGraph + Gate Classe C (v0, proposta, skeleton não executável)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead (subagente; classe B; t5 da demanda de design dos itens de execução agêntica)"
status: "condicional"
---
> **HISTÓRICO/SUPERSEDED** — documento de design/kickoff condicional, não executável como está; a implementação vigente é a Fase 1 em `src/` (65 testes, 75,00% cobertura; E1–E3 approved por DEC-030). Registrado como histórico; dúvidas → `docs/DECISIONS.md` e `git log`.

> **Migração aditiva (DEC-021, 2026-11-17 — D-V0-05, Classe C):** `schema_version` do contrato reconciliado `0.1.0-draft → 1.0.0` (contrato canônico v1.0.0; validador `docs/schemas/contract-v1.0.0.schema.json`). Migração **aditiva** — sem remoção/re-tipagem de campos; versões de prompt (`@0.1.0-draft`) permanecem como identificadores de prompt e não são `schema_version` de contrato. **Schema version 1.0.0 (DEC-021, 2026-11-17).**
> **Change Control:** inclusão condicional na baseline v0 autorizada por CR-002 / DEC-003 (`docs/DECISIONS.md`) — o conteúdo permanece `condicional`; isto NÃO aprova o conteúdo nem inicia implementação.

**Classe de autonomia declarada:** B (proposta documental reversível; nenhuma ação Classe C executada; nenhum `approved` declarado).

> **Aviso obrigatório:** Proposta de design — **não é implementação aprovada**; stack mínima definida (Python 3.12, DEC-018, 2026-11-17) — LangGraph permanece **condicional** (CR-009-C) e pode ser adotado ou substituído por máquina de estados Python pura (já implementada em `src/`); D-V0-06 APROVADO E MATERIALIZADO (DEC-022, 2026-11-17) — thresholds absolutos cobertura ≥50%, 0 erros críticos; baseline v0 publicada (DEC-024, 2026-11-17); F-ÚNICO-1 concluída; F-ÚNICO-2 iniciada; nenhum `approved` declarado.
>
> **`pyproject.toml` MATERIALIZADO (parametrizado, fail-closed).** O threshold de cobertura citado abaixo é **materializado** neste repo (`fail_under=50`; D-V0-06 materializado (DEC-022)) e é **parametrizado** — lido do `pyproject.toml` do projeto-alvo (`tool.coverage[.report].fail_under` ou equivalente); **nunca hardcoded**. O skeleton Python abaixo é **ilustrativo, NÃO executável** (imports hipotéticos, sem runtime, sem dependências instaladas) e vive apenas como bloco de proposta dentro deste documento.

## 🔧 Decisão / Conclusão
Propõe-se um grafo de estados LangGraph (proposta) com o ciclo `design → architecture → [subgrafo coding/tdd/qa — t4] → pr_generation → human_review → end`, em que (i) **decisões Classe C NUNCA transitam para `approved` sem evidência de interação humana** — o nó `human_review` é gate explícito e único escritor de `approvals[].status=approved` (com `human_interaction_ref`), e (ii) o nó final `pr_generation` é **bloqueado** quando a cobertura medida está abaixo do threshold **parametrizado** do `pyproject.toml` do projeto-alvo. **Trade-off assumido:** acoplamento do merge/aceite a um humano síncrono no grafo (latência de fila de aprovação) em detrimento de automação total — exigência não negociável do modelo Classe C (`docs/00` §5; `AGENTS.md`).

## 🗂️ Artefato

### 1) `CODE_SNIPPET` — skeleton ilustrativo (NÃO executável)
```python
# -*- coding: utf-8 -*-
"""
SKELETON ILUSTRATIVO — NÃO EXECUTÁVEL — CONDICIONAL (D-V0-06).
Stack mínima definida (Python 3.12, DEC-018, 2026-11-17); LangGraph permanece CONDICIONAL (CR-009-C) e pode ser adotado ou substituído por máquina de estados Python pura (src/). pyproject.toml MATERIALIZADO (thresholds absolutos: cobertura ≥50%, 0 erros críticos — DEC-018).
Nenhuma transição para `approved` sem Human Review com evidência de interação humana.
Conteúdo vive apenas neste documento; nenhum .py é criado no repositório.
"""
from typing import Annotated, Any, Literal, TypedDict, NotRequired  # ilustrativo
# import langgraph / tenacity / etc.  # [LACUNA: dependências não instaladas; stack pendente D-V0-01]

THRESHOLD_SOURCE = "pyproject.toml (materializado, thresholds absolutos DEC-018)::tool.coverage.report.fail_under = 50 (cobertura ≥50%, 0 erros críticos)"
# schema_version do contrato: 1.0.0 (reconciliado de 0.1.0-draft; migração aditiva — DEC-021, D-V0-05, Classe C, 2026-11-17; validador docs/schemas/contract-v1.0.0.schema.json)

class LacunaError(Exception):
    """Sinaliza lacuna bloqueante: NUNCA inferir threshold/aprovação."""

def load_coverage_threshold(pyproject_path: str) -> float:
    """Parametriza o limiar a partir do pyproject.toml do projeto-alvo.
    NUNCA hardcode: se o arquivo não existir ou a chave estiver ausente,
    levanta LacunaError e o nó pr_generation permanece BLOQUEADO."""
    try:
        ...  # tomllib.load(...) -> cfg["tool"]["coverage"]["report"]["fail_under"]
    except FileNotFoundError as exc:
        raise LacunaError(f"pyproject.toml ausente em {pyproject_path}; threshold indefinido (fail-closed, D-V0-06)") from exc
    # validar tipo/intervalo; qualquer ambiguidade => LacunaError (nunca default mágico)

def gate_pr_generation(state: "AgentState", measured_coverage: float, pyproject_path: str) -> Literal["allow", "block"]:
    threshold = load_coverage_threshold(pyproject_path)   # [LACUNA] até existir no projeto-alvo
    if measured_coverage < threshold:
        state.errors.append({"source_gate": "coverage", "exit_code": 6, "error_class": "lacuna",
                             "message": f"cobertura {measured_coverage} < limiar {threshold} (fonte: {THRESHOLD_SOURCE})"})
        state.pr_ready = False
        return "block"                                     # pr_generation NÃO executa
    if state.integration_test_output != "success" or state.pr_ready is not True:
        return "block"                                     # pré-condições de t4/t2
    return "allow"

def human_review_gate(state: "AgentState") -> "AgentState":
    """ÚNICO nó com permissão de escrever approvals[].status='approved'.
    Exige evidência de interação humana (ata, session_id, decided_by, decided_at).
    Sem isso: status permanece 'pending' e NENHUMA promoção ocorre."""
    decision = interrupt_for_human(state)                  # interrupt() do LangGraph — pausa o grafo
    state.approvals.append({
        "decision_id": new_ulid(), "kind": "classe_c",
        "subject_ref": state.ads[-1]["ads_id"] if state.ads else state.tasks[-1]["task_id"],
        "status": "approved" if decision.verdict == "approved" else "rejected",
        "decided_by": decision.human_id,                   # humano identificável
        "decided_at": now_iso(),
        "evidence_refs": decision.evidence_refs,           # obrigatório não-vazio para approved
        "human_interaction_ref": decision.interaction_ref, # ata/sessão — prova de interação humana
        "rationale": decision.rationale,
    })
    return state

def architecture_block_guard(state: "AgentState") -> Literal["coding", "blocked"]:
    """Architecture Agent (t3): inconsistência = [LACUNA] => bloqueio; Coding nunca é alcançado."""
    if any(e.get("error_class") == "lacuna" and e.get("source_gate") == "make lint-ads" for e in state.errors):
        return "blocked"                                    # errors[] exit_code=10 (t2)
    return "coding"

# --- Construção do grafo (ilustrativa; requer LangGraph instalado no projeto-alvo) ---
# graph = StateGraph(AgentState)                      # reducers por campo (t1 §1; errors/ads com append)
# graph.add_node("design", design_agent_node)          # t3: prompt design-agent@0.1.0-draft
# graph.add_node("architecture", architecture_agent_node)  # t3: gate; emite BLOCKED em inconsistência
# graph.add_node("coding_tdd_qa", compile_subgraph(t4_loop))   # t4: coding→tdd→qa_unit→qa_integration→pr_gate
# graph.add_node("pr_generation", pr_generation_node)  # executa SOMENTE com gate_pr_generation == 'allow'
# graph.add_node("human_review", human_review_gate)    # Classe C; interrupt(); único escritor de 'approved'
# graph.add_node("blocked", blocked_escalation_node)
# graph.set_entry_point("design")
# graph.add_edge("design", "architecture")
# graph.add_conditional_edges("architecture", architecture_block_guard, {"coding": "coding_tdd_qa", "blocked": "blocked"})
# graph.add_edge("coding_tdd_qa", "pr_generation")     # pr_generation se autobloqueia via gate_pr_generation
# graph.add_edge("pr_generation", "human_review")
# graph.add_conditional_edges("human_review", classe_c_outcome, {"approved": "end", "rejected": "coding_tdd_qa", "pending": "blocked"})
# graph.add_edge("blocked", END)                       # escala humana; nunca 'approved'
```

### 2) Pontos arquiteturais não negociáveis (Classe C)
| Invariante | Onde vive | Garantia |
|---|---|---|
| `approved` só via `human_review` com `human_interaction_ref` + `evidence_refs` não vazio | nó `human_review_gate` | Escrita de `approved` impossível em qualquer outro nó |
| Classe C rejeitada/pendente ⇒ sem merge/aceite; retorno com nova evidência | `classe_c_outcome` | `docs/10-produto-visao-v0.md` §3.3 (`rejected → pending` só com nova evidência) |
| `pr_generation` bloqueado por cobertura < limiar (parametrizado) | `gate_pr_generation` | Lê `pyproject.toml` (materializado, parametrizado); threshold numérico real ausente ⇒ `LacunaError` ⇒ **block** (fail-closed) |
| `pr_generation` bloqueado sem `integration_test_output=="success"` e `pr_ready==true` | `gate_pr_generation` | Herda t4; nunca contorna `pr_gate` |
| `architecture` com inconsistência ⇒ Coding inatingível | `architecture_block_guard` | Herda t3 (exit `10`, t2) |
| 1 crítico ⇒ parada imediata; 3 strikes ⇒ bloqueado + humano | `blocked` node / t4 `failure_semantics` | `docs/30` §Tratamento de falhas |

### 2.1) Exit codes → ação automática

Tabela canônica: `docs/48 §(v)` + `src/exit_codes.py` (implementação E1, DEC-030).

Regra dos 3 strikes: `attempts >= 3` na mesma validação ⇒ `blocked` + escala humana (exceto `critico`: parada na 1ª). Thresholds lidos do `pyproject.toml` do projeto-alvo (cobertura ≥50%, 0 erros críticos — DEC-018/DEC-022); ausência ⇒ `LacunaError` ⇒ `block` (fail-closed).

### 2.2) Gates G2/G3 com thresholds do `pyproject.toml`

- **G0 (schema/contrato):** lint/format de artefatos normativos, checagem de links/paths. Exit codes `0`/`1`/`5`/`10`.
- **G1 (núcleo):** testes do núcleo + smoke dispatcher→agregação + correlação/lineage. Exit codes `0`/`2`/`3`/`4`.
- **G2 (qualidade):** cobertura mínima lida do `pyproject.toml` do projeto-alvo (`fail_under`) + análise estática/tipos (mypy) + SAST básico + SLOs. Exit code `6` (fail-closed) quando cobertura < limiar ou `pyproject.toml` ausente. Thresholds absolutos do MVP: cobertura ≥50%, 0 erros críticos (DEC-018/DEC-022).
- **G3 (evolução/auditoria):** performance/carga se aplicável + revisão de ADRs + auditoria periódica. Exit codes `0`/`130`/`>=64`.

Política: "no new errors" sobre baseline declarada; thresholds numéricos **nunca hardcoded** em justificativa de decisão — sempre lidos do `pyproject.toml` do projeto-alvo (parametrizado para projetos-alvo futuros).

### 3) Estados terminais do grafo
| Terminal | Significado | Semântica canônica |
|---|---|---|
| `end` (após `approved`) | Fluxo aceito pelo humano | `approved` = valor aceito (PO/humano), **nunca** inferido de execução |
| `blocked` | Reparo esgotado / crítico / lacuna | `blocked` (execução); escala humana |
| `pending` (revisão) | Aguardando decisão humana | `approvals[].status=pending`; sem promoção |

## Evidências
- `docs/historico/41-agentstate-esquema-v0.md` (t1; `approvals[]`, `integration_test_output`, `pr_ready`, `errors[]`, invariantes §4).
- `docs/42-mapeamento-gates-makefile-v0.md` (t2; exit `0/10/130`, bloqueio fail-closed).
- `docs/historico/43-prompts-design-arquitetura-v0.md` (t3; Architecture Agent veta Coding em inconsistência).
- `docs/historico/44-loop-feedback-coding-tdd-qa-v0.md` (t4; subgrafo coding↔tdd↔qa; pré-condições de PR).
- `docs/00-painel-gerencial-consolidado.md` §5 (D-V0-01/04/06; Classe C exige aprovação humana) e `docs/10-produto-visao-v0.md` §3.3 (transições `pending/approved/rejected`).
- Verificação local: nenhum arquivo `.py` criado; `pyproject.toml`/`Makefile` materializados (parametrizados, fail-closed); bloco Python é texto dentro deste `.md`.
- Contrato canônico v1.0.0 adotado por DEC-021 (2026-11-17); validador de referência `docs/schemas/contract-v1.0.0.schema.json`; reconciliação deste canônico registrada por DEC-025 (2026-11-17). **Schema version 1.0.0 (DEC-021, 2026-11-17).**

## Premissas e Lacunas
- **[RESOLVIDO]** `pyproject.toml` materializado (thresholds absolutos definidos por DEC-018/DEC-022: cobertura ≥50%, 0 erros críticos); fail_under = 50 (aplicado; 65 testes verdes, 74,84% cobertura). *Impacto:* `pr_generation` libera quando cobertura medida ≥ 50% e gates verdes.
- **[LACUNA]** LangGraph (API `StateGraph`, `interrupt()`, reducers, checkpointer) não instalado/aprovado; skeleton ilustrativo; stack mínima definida (Python 3.12, DEC-018) — LangGraph permanece condicional (CR-009-C) e pode ser substituído por máquina de estados Python pura (já implementada em `src/`).
- **[LACUNA]** `interrupt_for_human`, `new_ulid`, `now_iso`, `_exists` são placeholders sem implementação; definição depende do projeto-alvo.
- **[LACUNA]** Mapeamento "nó final `pr_generation`" vs merge em forge: merge real exige remote/forge (hoje inexistente; AGENTS.md) — decisão humana.
- **[PREMISSA]** `human_review` pode abranger tanto aceite de valor (PO) quanto promoção Classe C arquitetural; o campo `approvals[].kind` distingue (`valor` vs `classe_c`).
- **[PREMISSA]** Subgrafo t4 é embarcado inline; versionamento independente do prompt (`@0.1.0-draft`) é mantido no registry proposto.
- **[PREMISSA]** Fail-closed como política: ausência de dado/threshold/aprovação ⇒ bloqueio, nunca "assumir ok".

## ✅ Próximas Ações
1. Aprovar (Classe C humana) o grafo e os invariantes como baseline técnico, se/quando D-V0-01/04/06 forem decididas — Dono: Mantenedor/PO/TL — Prazo: F0/F1.
2. Implementar no projeto-alvo: `AgentState` tipado (t1), subgrafo t4, `gate_pr_generation` lendo `pyproject.toml` real — Dono: TL/Engenharia — Prazo: F2/F3.
3. `fail_under` definido no `pyproject.toml` (cobertura ≥50%, 0 erros críticos) — D-V0-06 APROVADO (DEC-022, 2026-11-17).
4. Testar deterministicamente os 3 ramos de `classe_c_outcome` (approved/rejected/pending) com fixtures de interação humana — Dono: Engenharia/TL — Prazo: F2.
5. Auditar que nenhum caminho de código fora de `human_review` escreve `approved` (lint custom/policy SoT) — Dono: TL/DevEx — Prazo: F3.
