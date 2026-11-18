# Índice de Documentação — `docs/`

- **Data da última atualização:** Atualizado 2026-11-18 — ver `docs/DECISIONS.md`.
- **Projeto:** `sdlc-agentico`
- **Contexto:** baseline v0 PUBLICADA (DEC-024); Fase 1 done; E1–E3 approved (DEC-030); F-ÚNICO-2 em andamento.
- **Estado observado:** baseline v0 **publicada** (6/6 critérios PASS, DEC-024); F-ÚNICO-1 concluída (65 testes, 75,00% cobertura medida 2026-11-17 — DEC-028); F-ÚNICO-2 (Evolução) iniciada; **aceite de valor E1–E3 APROVADO (DEC-030, 2026-11-18, Classe C — decided_by Lucinei)**; E4 fora do escopo e não aprovado; KPIs não instrumentáveis (lacuna mantida). Ver `00-painel-gerencial-consolidado.md`. Telemetria volátil (capacidade/alocação): **`docs/00` §0 "Status dinâmico" é a fonte única** (DEC-029).

## Política canônica (estado atual)

> ### Fonte canônica
> - **Canônicos (mantidos em `docs/`):** 14 artefatos numerados (00,10,20,21,30,40,41,42,43,44,45,46,47,48) mais o log `DECISIONS.md` e este `README.md` — cobertura `00–48` + `DECISIONS.md` + `46`. `47/48` adotados como baseline (D-V0-05/DEC-021); baseline v0 publicada (DEC-024). `docs/ONBOARDING.md` é **não canônico** (fachada de entrada, DEC-029). Fusão `docs/10`+`docs/11` → `docs/10-produto-visao-v0.md` (DEC-029, 2026-11-18).
> - **Não canônicos (`baseline-v0-*.md`):** foram **removidos do diretório `docs/` em 2026-11-13** para eliminar ambiguidade. Tratavam-se de duplicata do painel e registros parciais sem o corpo completo (conteúdo integral não fornecido na persistência nos registros parciais). Não devem ser recriados como fonte de verdade; para rastreabilidade histórica, o registro desta remoção consta neste índice.

## Artefatos canônicos (fonte de referência)

| Arquivo | Título/Conteúdo (breve) | Fonte / Sessão | Status |
|---|---|---|---|
| `00-painel-gerencial-consolidado.md` | Painel gerencial consolidado do baseline v0: semáforo, delegações/evidências, convergências, pontos a reconciliar, decisões pendentes, riscos, próximos passos (estado machine-readable extraído para `docs/schemas/painel-status.json` em 2026-11-18). | `orchestrator` (agregação). Subagentes: PO `ses_e292deeacffeDISULhsnAjsxBi`, PM `ses_e292deea9ffecJ3wI1b7obkWGp`, TL `ses_e292deea6ffeFHtGus1wUTHx1E`. | `condicional` |
| `10-produto-visao-v0.md` | Produto (PO) — fusão DEC-029 (2026-11-18) de `10-produto-po-visao-mvp-baseline-v0.md` + `11-visao-mvp-v0.md`: visão, problema, personas, proposta de valor (fonte prioritária: docs/11); escopo MVP (MoSCoW+WSJF); backlog E1–E4 com critérios Given/When/Then e DoR; semântica canônica de estados; KPIs; mecanismo de feedback/aceite; **pacote de evidência de aceite E1–E3 (§0.2, DEC-028) — aceite APROVADO por DEC-030 (2026-11-18, Classe C)**; Decision/Acceptance v0; premissas/lacunas/riscos (P7 40h/sem depreciada/histórica — DEC-029). | `gerente-produto` (fusão por DEC-029; fontes classe B). | `partial/condicional` (aceite E1–E3 `approved` por DEC-030; documento/visão como um todo não promovidos) |
| `20-governanca-pm-plano-baseline-v0.md` | Governança (PM): roadmap F0–F2 e marcos; RACI; cadência/semáforo; riscos R1–R7 e premissas P1–P5; baseline documental canônico, backlog/tracking, DoR/DoD e change control; plano I1–I2 (PERT+30%) e critério de baseline v0 pronto. | `gerente-projeto` (sessão `ses_e292deea9ffecJ3wI1b7obkWGp`, classe B). | `partial/condicional` |
| `30-arquitetura-tech-lead-baseline-v0.md` | Arquitetura (TL): componentes/fluxos (dispatcher+agregador, SoT/event-log, idempotência), contratos/envelopes e mapeamento de estados; ADRs iniciais A–G (propostos); DoD técnico e gates incrementais G0–G3; plano F0–F5; riscos/lacunas. | `tech-lead` (sessão `ses_e292deea6ffeFHtGus1wUTHx1E`, classe B). | `done/condicional` (execução da proposta) |
| `40-operacao-raci-repo-v0.md` | Operação do repositório (PO): matriz RACI das operações documentais do repo (edição de canônicos, índice, AGENTS.md, git, Classe C, lacunas); complementar ao RACI de produto do `20-*`. | `gerente-produto` (sessão orquestradora delegante; classe B). | `vigente` |
| `DECISIONS.md` | Log canônico de decisões (DEC-001…DEC-030; kickoff D-V0-01/02; pautas D-V0-03/04/05/06 como DEC-009…DEC-012/DEC-019…DEC-022; reconciliação MU-0.3 como DEC-013; grill-with-docs PM/PO/TL como DEC-014/DEC-015/DEC-016; DEC-017 registra mudança de identidade do repo; DEC-018 resolve D-V0-01 (Opção B); DEC-019 formaliza D-V0-03; DEC-020 formaliza D-V0-04 e promove ADR-001…ADR-008 para `accepted`; DEC-021 formaliza D-V0-05 (contrato v1.0.0); DEC-022 formaliza D-V0-06 (gates/thresholds); DEC-023 fecha DEC-007 (política de segredos); DEC-024 consolida baseline v0 publicada e inicia F-ÚNICO-2; DEC-025 reconcilia docs/41 e docs/45 para contrato v1.0.0; DEC-026 materializa trilha de aceite de valor do PO (AC + handoff + KPIs); DEC-027 registra D-V0-02 resolvido para a escala atual (Classe B); DEC-028 registra pacote de evidência de aceite E1–E3 (Classe B; supersedido por DEC-030); DEC-029 reestrutura SoT + escalona governança (fusão docs/10+11; telemetria volátil em `docs/00` §0; P7 depreciada/histórica); **DEC-030 registra aceite de valor E1–E3 APROVADO (Classe C, 2026-11-18 — Lucinei; E4 fora do escopo e não aprovado)**; CRs 001–013). Fonte de verdade para Classe C. | `gerente-projeto` + Mantenedor (Lucinei, 2026-11-17/18) | `vigente` |
| `46-ata-kickoff-d-v0-01-02-v0.md` | Ata do kickoff D-V0-01/02 (2026-11-16): D-V0-01 resolvido (DEC-018); repo-alvo este repo; sem CI por ora; mantenedor único; cadência sob demanda sem SLA; docs como trilha de tracking. Baseline v0 publicada (DEC-024). | `gerente-projeto` + Mantenedor | `vigente` |
| `47-roadmap-unico-fundacao-mvp-evolucao-v0.md` | Roadmap único Fundação→MVP→Evolução; funde M1–M3 ↔ F0–F2 ↔ F0–F5; F-ÚNICO-1 concluída (DEC-024); F-ÚNICO-2 iniciada. | `tech-lead` (proposta condicional) | `condicional` |
| `48-contrato-canonico-v1-0-0-proposta-v0.md` | Contrato Canônico v1.0.0: envelope/resumo/estados/exit codes; unifica `schema_version 0.1.0-draft→1.0.0`; `completed`≠`approved`. **Adotado como v1.0.0 por DEC-021 (D-V0-05, Classe C, 2026-11-17)**; arquivo mantém o sufixo `-proposta-` por rastreabilidade; validador `docs/schemas/contract-v1.0.0.schema.json`. | `tech-lead` (proposta adotada; Classe B) | `condicional` |
| `41-agentstate-esquema-v0.md` | Design (TL) t1: esquema de estado tipado `AgentState` proposto para LangGraph (`global_context`/`ads`/`tasks`/`errors`, `approvals[]`, `integration_test_output`, `pr_ready`); semântica `done`≠`completed`≠`approved`; semântica de transições e rastreabilidade por correlação; JSON_STRICT validável. `schema_version 1.0.0` (DEC-021/DEC-025). Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t1). | `condicional` |
| `42-mapeamento-gates-makefile-v0.md` | Design (TL) t2: mapeamento Design/Arquitetura/Coding/QA → `make lint-ads` / `make test-unit` / `make test-integration` (assinaturas de entrada/saída); tabela obrigatória `exit_code → AgentState` para reparo automático; Makefile criado (parametrizado); thresholds reais: D-V0-06 materializado (DEC-022). Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t2). | `condicional` |
| `43-prompts-design-arquitetura-v0.md` | Design (TL) t3: prompts estruturados do Design Agent (ADS + Mermaid, template `specs/current_ads.md` — inexistente; proposta) e do Architecture Agent (gate de validação; inconsistência = `[LACUNA]` + bloqueio de avanço para Coding); injeção de `global_context`; variáveis, guardrails e formato de saída. Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t3). | `condicional` |
| `44-loop-feedback-coding-tdd-qa-v0.md` | Design (TL) t4: loop Coding→TDD→QA (uma tarefa por vez; TDD antes da validação unitária; retorno forçado a Coding em falha unitária/integração; PR só com `integration_test_output=success` e `pr_ready=TRUE`); grafo de 7 nós + pseudocódigo em JSON_STRICT (`sdlc.loop.coding_tdd_qa`, `schema_version 1.0.0` — DEC-021/DEC-025). Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t4). | `condicional` |
| `45-grafo-langgraph-classe-c-v0.md` | Design (TL) t5: grafo LangGraph proposto (skeleton Python ilustrativo, **não executável**) com Human Review gate explícito para Classe C (único escritor de `approved`, com evidência de interação humana) e `pr_generation` bloqueado por threshold de cobertura lido do `pyproject.toml` (materializado, parametrizado, fail-closed; thresholds absolutos cobertura ≥50%, 0 erros críticos — DEC-022). `schema_version 1.0.0` (DEC-021/DEC-025). Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t5). | `condicional` |
| `21-cronograma-raci-riscos-v0.md` | Cronograma/RACI/riscos (PM): cronograma 1 semana (5d + pre-S1 kickoff, modo documental); RACI por papéis (PM R / Mantenedor A); riscos R1–R12; premissas P1–P8 (P7 orçamento zero, P8 cadência semanal); lacunas persistentes. Materializado por aprovação Classe C (DEC-014). | `gerente-projeto` (proposta aprovada, Classe C, 2026-11-16). | `condicional` |
| `README.md` | Este índice: política canônica, inventário dos artefatos canônicos e registro de rastreabilidade da remoção dos não canônicos. | Atualização documental (2026-11-18 — extração `schemas/painel-status.json`). | `done` |

## Documentos de entrada (não canônicos)

| Arquivo | Título/Conteúdo (breve) | Fonte / Sessão | Status |
|---|---|---|---|
| `ONBOARDING.md` | Porta de entrada human-friendly: visão, fluxo humano (orquestrador como dispatcher+agregador), visão conceitual do grafo em 7 nós, responsabilidades humano vs. máquina, setup local e FAQ. Sem jargão de processo e sem IDs internos. | `gerente-produto` (2026-11-18, decisão do Mantenedor — fachada de entrada). | `condicional` |

## Artefatos derivados (machine-readable, não canônicos)

| Arquivo | Título/Conteúdo (breve) | Fonte / Sessão | Status |
|---|---|---|---|
| `schemas/painel-status.json` | Estado machine-readable derivado (`aggregation_status`, `lacunas_consolidadas`, `decisoes_pendentes`, `no_go_flags`, `proxima_acao_recomendada`). Derivado de `docs/DECISIONS.md` (`derived: true`) — regenerar a cada DEC; não editar como fonte. Não é canônico e não promove nenhum status. | Derivado (2026-11-18) | `derivado` (não canônico) |

## ADRs (docs/adr/core/)

ADR-001…008 = accepted (DEC-020) — ver `docs/adr/core/`

## Artefatos não canônicos removidos (rastreabilidade)

- `baseline-v0-*.md` removidos em 2026-11-13 (duplicatas/parciais, DEC-029); ver `git log`.

## Observações de governança

- Semântica done≠completed≠approved → `AGENTS.md` / `docs/48 §(iii)`.
- Log de decisões (Classe C) → `docs/DECISIONS.md`.
- DEC-030 (aceite de valor E1–E3) → `docs/DECISIONS.md` + `docs/10 §0.2`.
