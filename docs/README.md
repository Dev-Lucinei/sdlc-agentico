# Índice de Documentação — `docs/`

- **Data da última atualização:** 2026-11-16
- **Projeto:** `sdlc-agentico`
- **Contexto:** baseline v0 **condicional** (definição/agregação), repositório reiniciado (sem baseline operacional anterior). Foi observado subdiretório `.git` em `docs/` (estado ambíguo); **nenhuma ação git** (init/add/commit/movimentação) foi executada nesta ação.
- **Estado observado:** baseline v0 **não consolidado** (pendente reconciliação formal e validações/aprovações); execução de implementação não iniciada. Ver `00-painel-gerencial-consolidado.md`.

## Política canônica (estado atual)

> ### Fonte canônica
> - **Canônicos (mantidos em `docs/`):** os 13 numerados (`00/10/20/30/40/41..48-*.md`; design de execução agêntica t1–t5, ata de kickoff, roadmap único e Contrato v1.0.0-proposta) e este `README.md` e o log `DECISIONS.md` (conteúdo integral dos numerados, com sessões/fontes/status explícitos, base para reconciliação do baseline v0). Os canônicos 41–45 são **proposta documental de design** (não implementação), conforme observação de governança abaixo.
> - **Não canônicos (`baseline-v0-*.md`):** foram **removidos do diretório `docs/` em 2026-11-13** para eliminar ambiguidade. Tratavam-se de duplicata do painel e registros parciais sem o corpo completo (conteúdo integral não fornecido na persistência nos registros parciais). Não devem ser recriados como fonte de verdade; para rastreabilidade histórica, o registro desta remoção consta neste índice.

## Artefatos canônicos (fonte de referência)

| Arquivo | Título/Conteúdo (breve) | Fonte / Sessão | Status |
|---|---|---|---|
| `00-painel-gerencial-consolidado.md` | Painel gerencial consolidado do baseline v0: semáforo, delegações/evidências, convergências, pontos a reconciliar, decisões pendentes, riscos, próximos passos e estado machine-readable. | `orchestrator` (agregação). Subagentes: PO `ses_e292deeacffeDISULhsnAjsxBi`, PM `ses_e292deea9ffecJ3wI1b7obkWGp`, TL `ses_e292deea6ffeFHtGus1wUTHx1E`. | `condicional` |
| `10-produto-po-visao-mvp-baseline-v0.md` | Produto (PO): visão, problema, personas, proposta de valor; escopo MVP (MoSCoW+WSJF); backlog E1–E4 com critérios Given/When/Then e DoR; semântica canônica de estados (execução/operação/valor); KPIs e mecanismo de feedback/aceite; premissas/lacunas/riscos. | `gerente-produto` (sessão `ses_e292deeacffeDISULhsnAjsxBi`, classe B). | `partial/condicional` |
| `20-governanca-pm-plano-baseline-v0.md` | Governança (PM): roadmap F0–F2 e marcos; RACI; cadência/semáforo; riscos R1–R7 e premissas P1–P5; baseline documental canônico, backlog/tracking, DoR/DoD e change control; plano I1–I2 (PERT+30%) e critério de baseline v0 pronto. | `gerente-projeto` (sessão `ses_e292deea9ffecJ3wI1b7obkWGp`, classe B). | `partial/condicional` |
| `30-arquitetura-tech-lead-baseline-v0.md` | Arquitetura (TL): componentes/fluxos (dispatcher+agregador, SoT/event-log, idempotência), contratos/envelopes e mapeamento de estados; ADRs iniciais A–G (propostos); DoD técnico e gates incrementais G0–G3; plano F0–F5; riscos/lacunas. | `tech-lead` (sessão `ses_e292deea6ffeFHtGus1wUTHx1E`, classe B). | `done/condicional` (execução da proposta) |
| `40-operacao-raci-repo-v0.md` | Operação do repositório (PO): matriz RACI das operações documentais do repo (edição de canônicos, índice, AGENTS.md, git, Classe C, lacunas); complementar ao RACI de produto do `20-*`. | `gerente-produto` (sessão orquestradora delegante; classe B). | `vigente` |
| `DECISIONS.md` | Log canônico de decisões (DEC-001…DEC-008; kickoff D-V0-01/02; CRs 001–013). Fonte de verdade para Classe C. | `gerente-projeto` + Mantenedor (Lucinei, 2026-11-16) | `vigente` |
| `46-ata-kickoff-d-v0-01-02-v0.md` | Ata do kickoff D-V0-01/02 (2026-11-16): D-V0-01 adiado; repo-alvo este repo; sem CI por ora; mantenedor único; cadência sob demanda sem SLA; docs como trilha de tracking. Baseline v0 NÃO pronta. | `gerente-projeto` + Mantenedor | `vigente` |
| `47-roadmap-unico-fundacao-mvp-evolucao-v0.md` | Roadmap único Fundação→MVP→Evolução; funde M1–M3 ↔ F0–F2 ↔ F0–F5; F-ÚNICO-1 bloqueada por D-V0-01 adiada (DEC-006, R8). | `tech-lead` (proposta condicional) | `condicional` |
| `48-contrato-canonico-v1-0-0-proposta-v0.md` | Contrato Canônico v1.0.0-PROPOSTA: envelope/resumo/estados/exit codes; unifica `schema_version 0.1.0-draft→1.0.0`; `completed`≠`approved`. Adoção pendente D-V0-05 (Classe C). | `tech-lead` (proposta condicional) | `condicional` |
| `41-agentstate-esquema-v0.md` | Design (TL) t1: esquema de estado tipado `AgentState` proposto para LangGraph (`global_context`/`ads`/`tasks`/`errors`, `approvals[]`, `integration_test_output`, `pr_ready`); semântica `done`≠`completed`≠`approved`; semântica de transições e rastreabilidade por correlação; JSON_STRICT validável. Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t1). | `condicional` |
| `42-mapeamento-gates-makefile-v0.md` | Design (TL) t2: mapeamento Design/Arquitetura/Coding/QA → `make lint-ads` / `make test-unit` / `make test-integration` (assinaturas de entrada/saída); tabela obrigatória `exit_code → AgentState` para reparo automático; explicita que o `Makefile` **não existe** neste repo. Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t2). | `condicional` |
| `43-prompts-design-arquitetura-v0.md` | Design (TL) t3: prompts estruturados do Design Agent (ADS + Mermaid, template `specs/current_ads.md` — inexistente; proposta) e do Architecture Agent (gate de validação; inconsistência = `[LACUNA]` + bloqueio de avanço para Coding); injeção de `global_context`; variáveis, guardrails e formato de saída. Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t3). | `condicional` |
| `44-loop-feedback-coding-tdd-qa-v0.md` | Design (TL) t4: loop Coding→TDD→QA (uma tarefa por vez; TDD antes da validação unitária; retorno forçado a Coding em falha unitária/integração; PR só com `integration_test_output=success` e `pr_ready=TRUE`); grafo de 7 nós + pseudocódigo em JSON_STRICT. Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t4). | `condicional` |
| `45-grafo-langgraph-classe-c-v0.md` | Design (TL) t5: grafo LangGraph proposto (skeleton Python ilustrativo, **não executável**) com Human Review gate explícito para Classe C (único escritor de `approved`, com evidência de interação humana) e `pr_generation` bloqueado por threshold de cobertura lido do `pyproject.toml` (**inexistente**; parametrizado, nunca hardcoded). Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t5). | `condicional` |
| `README.md` | Este índice: política canônica, inventário dos artefatos canônicos e registro de rastreabilidade da remoção dos não canônicos. | Atualização documental (2026-11-16). | `done` |

## Artefatos não canônicos removidos (rastreabilidade)

Em 2026-11-13 foram removidos de `docs/` os seguintes arquivos (não canônicos):

| Arquivo (removido) | Conteúdo observado anteriormente | Motivo |
|---|---|---|
| `baseline-v0-painel-consolidado.md` | Cópia do conteúdo do painel consolidado (sem front matter/metadata explícita de título/fonte/status presente no canônico). | **Duplicata** do painel; gerava ambiguidade. Referência: `00-painel-gerencial-consolidado.md`. |
| `baseline-v0-po-gerente-produto.md` | Registro **parcial** (metadados + resumo consolidado); conteúdo integral não fornecido na persistência. | **Parcial, sem corpo completo**; não substituía `10-produto-po-visao-mvp-baseline-v0.md`. |
| `baseline-v0-pm-gerente-projeto.md` | Registro **parcial** (metadados + resumo consolidado); conteúdo integral não fornecido na persistência. | **Parcial, sem corpo completo**; não substituía `20-governanca-pm-plano-baseline-v0.md`. |
| `baseline-v0-tl-tech-lead.md` | Registro **parcial** (metadados + resumo consolidado); conteúdo integral não fornecido na persistência. | **Parcial, sem corpo completo**; não substituía `30-arquitetura-tech-lead-baseline-v0.md`. |

## Observações de governança

- **Regras de valor/estado (referência):** “Execução concluída” (técnica) ≠ “Valor entregue/aceito (pendente de aceite do PO)”. `done/blocked/partial` (execução) ≠ `completed` (OPS) ≠ `approved` (valor/PO). Detalhes nos artefatos canônicos.
- **Rastreabilidade:** este índice registra a consolidação do diretório `docs/` nos canônicos e a remoção dos não canônicos em 2026-11-13; decisões de promoção/aprovação (Classe C) permanecem pendentes conforme painel.
- **RACI de operação do repo:** `40-operacao-raci-repo-v0.md` (criado em 2026-11-13) propõe a matriz RACI das operações deste repositório (não duplica o RACI de produto do `20-*` §2); status `vigente` (validação Classe C do Mantenedor em 2026-11-16, DEC-002; ver `docs/DECISIONS.md`). Nenhum `approved` inferido.
- **Canônicos de design t1–t5 (`41/42/43/44/45-*.md`, 2026-11-16):** são **proposta documental de design condicional** do ciclo de execução agêntica (AgentState, gates↔Makefile, prompts Design/Architecture, loop Coding-TDD-QA e grafo LangGraph com gate Classe C) — **não são implementação**; a stack LangGraph está pendente de D-V0-01, os gates/thresholds de D-V0-06 (inexistência de `Makefile`/`pyproject.toml`/`specs/` explicitada nos canônicos) e nenhum `approved` foi declarado. Promoção a baseline/aceite exige validação humana (Classe C) e reconciliação do baseline v0.
- **Log de decisões:** `docs/DECISIONS.md` é a fonte de verdade para Classe C (DEC-001…008); normativos externos citados por caminho+sha256; publicação do baseline bloqueada por D-V0-03/04/05/06 (DEC-008); baseline v0 NÃO pronta (6 critérios avaliados — 2 PASS parciais, 4 FAIL, ver painel §8.3).
- **Ações não realizadas nesta atualização:** nenhuma ação git (init/add/commit) e nenhuma criação de estrutura de arquivamento adicional.
