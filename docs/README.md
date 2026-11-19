# Índice de Documentação — `docs/`

- **Data da última atualização:** Atualizado 2026-11-18 — ver `docs/DECISIONS.md`.
- **Projeto:** `sdlc-agentico`
- **Contexto:** baseline v0 PUBLICADA (DEC-024); Fase 1 done; E1–E3 approved (DEC-030); F-ÚNICO-2 em andamento.
- **Estado observado:** baseline v0 **publicada** (6/6 critérios PASS, DEC-024); F-ÚNICO-1 concluída (65 testes, 75,00% cobertura medida 2026-11-17 — DEC-028); F-ÚNICO-2 (Evolução) iniciada; **aceite de valor E1–E3 APROVADO (DEC-030, 2026-11-18, Classe C — decided_by Lucinei)**; E4 fora do escopo e não aprovado; KPIs não instrumentáveis (lacuna mantida). Ver `00-painel-gerencial-consolidado.md`. Telemetria volátil (capacidade/alocação): **`docs/00` §0 "Status dinâmico" é a fonte única** (DEC-029).

## Política canônica (estado atual)

> ### Fonte canônica
> - **Canônicos (mantidos em `docs/`):** 7 artefatos numerados (00,10,20,30,40,42,48) mais o log `DECISIONS.md` e este `README.md` — cobertura `00–48` com 7 itens arquivados em `docs/historico/` (ver seção própria). `47/48` adotados como baseline (D-V0-05/DEC-021); baseline v0 publicada (DEC-024). `docs/ONBOARDING.md` é **não canônico** (fachada de entrada, DEC-029). Fusão `docs/10`+`docs/11` → `docs/10-produto-visao-v0.md` (DEC-029, 2026-11-18).
> - **Não canônicos (`baseline-v0-*.md`):** foram **removidos do diretório `docs/` em 2026-11-13** para eliminar ambiguidade. Tratavam-se de duplicata do painel e registros parciais sem o corpo completo (conteúdo integral não fornecido na persistência nos registros parciais). Não devem ser recriados como fonte de verdade; para rastreabilidade histórica, o registro desta remoção consta neste índice.

## Artefatos canônicos (fonte de referência)

| Arquivo | Título/Conteúdo (breve) | Fonte / Sessão | Status |
|---|---|---|---|
| `00-painel-gerencial-consolidado.md` | Painel gerencial consolidado do baseline v0: semáforo, delegações/evidências, convergências, pontos a reconciliar, decisões pendentes, riscos, próximos passos (estado machine-readable extraído para `docs/schemas/painel-status.json` em 2026-11-18). | `orchestrator` (agregação). Subagentes: PO `ses_e292deeacffeDISULhsnAjsxBi`, PM `ses_e292deea9ffecJ3wI1b7obkWGp`, TL `ses_e292deea6ffeFHtGus1wUTHx1E`. | `condicional` |
| `10-produto-visao-v0.md` | Produto (PO) — fusão DEC-029 (2026-11-18) de `10-produto-po-visao-mvp-baseline-v0.md` + `11-visao-mvp-v0.md`: visão, problema, personas, proposta de valor (fonte prioritária: docs/11); escopo MVP (MoSCoW+WSJF); backlog E1–E4 com critérios Given/When/Then e DoR; semântica canônica de estados; KPIs; mecanismo de feedback/aceite; **pacote de evidência de aceite E1–E3 (§0.2, DEC-028) — aceite APROVADO por DEC-030 (2026-11-18, Classe C)**; Decision/Acceptance v0; premissas/lacunas/riscos (P7 40h/sem depreciada/histórica — DEC-029). | `gerente-produto` (fusão por DEC-029; fontes classe B). | `partial/condicional` (aceite E1–E3 `approved` por DEC-030; documento/visão como um todo não promovidos) |
| `20-governanca-pm-plano-baseline-v0.md` | Governança (PM): trilha única F-ÚNICO-0/1/2; cronograma F-ÚNICO-2 (F2.1–F2.5); RACI; riscos R1–R12; DoR/DoD; change control. | `gerente-projeto` (sessão `ses_e292deea9ffecJ3wI1b7obkWGp`, classe B). | `partial/condicional` |
| `30-arquitetura-tech-lead-baseline-v0.md` | Arquitetura (TL): componentes/fluxos (dispatcher+agregador, SoT/event-log, idempotência), contratos/envelopes e mapeamento de estados; ADRs iniciais A–G (propostos); DoD técnico e gates incrementais G0–G3; plano F0–F5; riscos/lacunas. | `tech-lead` (sessão `ses_e292deea6ffeFHtGus1wUTHx1E`, classe B). | `done/condicional` (execução da proposta) |
| `40-operacao-raci-repo-v0.md` | Operação do repositório (PO): matriz RACI das operações documentais do repo (edição de canônicos, índice, AGENTS.md, git, Classe C, lacunas); complementar ao RACI de produto do `20-*`. | `gerente-produto` (sessão orquestradora delegante; classe B). | `vigente` |
| `DECISIONS.md` | Log canônico de decisões — **índice vigente** (DEC-035, 2026-11-18): regra de ouro condensada + declaração de leitura obrigatória (~4k tokens) + tabela-índice DEC-001…DEC-035 + ponteiros. Corpos append-only em `docs/decisions/DEC-NNN-<slug>.md`; arquivo congelado `docs/decisions/arquivo-2026-11-16.md` (seções stale de 2026-11-16). Fonte de verdade para Classe C. | `gerente-projeto` + Mantenedor (Lucinei, 2026-11-18) | `vigente` |
| `decisions/` | 36 arquivos: 35 corpos append-only `DEC-NNN-<slug>.md` (DEC-001…DEC-035, extração byte a byte de 2026-11-18 + DEC-033, 2026-11-18 + DEC-034, 2026-11-18 + DEC-035, 2026-11-18) + `arquivo-2026-11-16.md` (quarentena verbatim de seções stale: Decisões pendentes, nota DEC-016, Propagação pendente, Adendo trio, Rodapé). Append-only; nunca reescrever; seções stale não referenciar como estado vigente. | `gerente-projeto` + Mantenedor (Lucinei, 2026-11-18; DEC-031/DEC-032/DEC-033/DEC-034/DEC-035) | `vigente` |
| `48-contrato-canonico-v1-0-0.md` | Contrato Canônico v1.0.0: envelope/resumo/estados/exit codes; unifica `schema_version 0.1.0-draft→1.0.0`; `completed`≠`approved`. **Adotado como v1.0.0 por DEC-021 (D-V0-05, Classe C, 2026-11-17)**; sufixo `-proposta-` removido do nome (renomeação 2026-11-18); validador `docs/schemas/contract-v1.0.0.schema.json`. | `tech-lead` (proposta adotada; Classe B) | `condicional` |
| `42-mapeamento-gates-makefile-v0.md` | Design (TL) t2: mapeamento Design/Arquitetura/Coding/QA → `make lint-ads` / `make test-unit` / `make test-integration` (assinaturas de entrada/saída); §2 reduzido a ponteiro para a tabela canônica (`docs/48 §(v)` + `src/exit_codes.py`, E1/DEC-030); Makefile criado (parametrizado); thresholds reais: D-V0-06 materializado (DEC-022). Proposta de design, não implementação. | `tech-lead` (subagente; classe B; t2). | `condicional` |
| `README.md` | Este índice: política canônica, inventário dos artefatos canônicos e registro de rastreabilidade da remoção dos não canônicos. | Atualização documental (2026-11-18 — extração `schemas/painel-status.json`). | `done` |

## `docs/historico/` — propostas v0 superseded (não canônicos)

Arquivamento de propostas/kickoff v0 **superseded** pela Fase 1 (`src/`, DEC-030), preservadas via `git log` (caminho antigo preservado no histórico). **Não recriar nos caminhos antigos; não promover estados.**

| Arquivo | Conteúdo (breve) | Status |
|---|---|---|
| `historico/41-agentstate-esquema-v0.md` | Design (TL) t1: esquema de estado tipado `AgentState` (proposta; não implementação). | `condicional` |
| `historico/43-prompts-design-arquitetura-v0.md` | Design (TL) t3: prompts do Design/Architecture Agent (proposta; `specs/` inexistente). | `condicional` |
| `historico/44-loop-feedback-coding-tdd-qa-v0.md` | Design (TL) t4: loop Coding→TDD→QA (proposta; pseudocódigo JSON_STRICT). | `condicional` |
| `historico/45-grafo-langgraph-classe-c-v0.md` | Design (TL) t5: grafo LangGraph + Human Review gate Classe C (proposta; skeleton não executável). | `condicional` |
| `historico/46-ata-kickoff-d-v0-01-02-v0.md` | Ata do kickoff D-V0-01/02 (2026-11-16): DEC-006; D-V0-01 resolvido (DEC-018). | `vigente` |
| `historico/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` | Roadmap único F-ÚNICO-0/1/2; F-ÚNICO-1 concluída (DEC-024); F-ÚNICO-2 iniciada. | `condicional` |
| `historico/21-cronograma-raci-riscos-v0.md` | Cronograma/RACI/riscos (PM) 1 semana, modo documental; riscos R1–R12. | `condicional` |

## Documentos de entrada (não canônicos)

| Arquivo | Título/Conteúdo (breve) | Fonte / Sessão | Status |
|---|---|---|---|
| `ONBOARDING.md` | Porta de entrada human-friendly: visão, fluxo humano (orquestrador como dispatcher+agregador), visão conceitual do grafo em 7 nós, responsabilidades humano vs. máquina, setup local e FAQ. Sem jargão de processo e sem IDs internos. | `gerente-produto` (2026-11-18, decisão do Mantenedor — fachada de entrada). | `condicional` |

## Artefatos derivados (machine-readable, não canônicos)

| Arquivo | Título/Conteúdo (breve) | Fonte / Sessão | Status |
|---|---|---|---|
| `schemas/painel-status.json` | Estado machine-readable derivado (`aggregation_status`, `lacunas_consolidadas`, `decisoes_pendentes`, `no_go_flags`, `proxima_acao_recomendada`). Derivado de `docs/DECISIONS.md` (`derived: true`) — regenerar a cada DEC; não editar como fonte. Não é canônico e não promove nenhum status. | Derivado (2026-11-18) | `derivado` (não canônico) |

## ADRs (docs/adr/core/)

ADR-001…008 = accepted (DEC-020) — ver `docs/adr/core/` (ADR-003 adendado por DEC-033, 2026-11-18 — dedupe atômico; corpo accepted intacto)
DRAFT-criterio-completed-e-dod-g2-g3.md = `draft — não aprovado` (DEC-032 F2.7-téc, 2026-11-18); NÃO numerado; promoção a ADR `accepted` = Classe C futura; não altera ADR-005/ADR-006 nem o Contrato v1.0.0 — ver `docs/adr/core/DRAFT-criterio-completed-e-dod-g2-g3.md`

## Artefatos não canônicos removidos (rastreabilidade)

- `baseline-v0-*.md` removidos em 2026-11-13 (duplicatas/parciais, DEC-029); ver `git log`.

## Observações de governança

- Semântica done≠completed≠approved → `AGENTS.md` / `docs/48 §(iii)`.
- Log de decisões (Classe C) → `docs/DECISIONS.md`.
- DEC-030 (aceite de valor E1–E3) → `docs/DECISIONS.md` + `docs/10 §0.2`.
