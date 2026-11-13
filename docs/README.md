# Índice de Documentação — `docs/`

- **Data da última atualização:** 2026-11-13
- **Projeto:** `sdlc-agentico`
- **Contexto:** baseline v0 **condicional** (definição/agregação), repositório reiniciado (sem baseline operacional anterior). Foi observado subdiretório `.git` em `docs/` (estado ambíguo); **nenhuma ação git** (init/add/commit/movimentação) foi executada nesta ação.
- **Estado observado:** baseline v0 **não consolidado** (pendente reconciliação formal e validações/aprovações); execução de implementação não iniciada. Ver `00-painel-gerencial-consolidado.md`.

## Política canônica (estado atual)

> ### Fonte canônica
> - **Canônicos (mantidos em `docs/`):** os 5 arquivos `00/10/20/30-*.md` e este `README.md` (conteúdo integral dos numerados, com sessões/fontes/status explícitos, base para reconciliação do baseline v0).
> - **Não canônicos (`baseline-v0-*.md`):** foram **removidos do diretório `docs/` em 2026-11-13** para eliminar ambiguidade. Tratavam-se de duplicata do painel e registros parciais sem o corpo completo (conteúdo integral não fornecido na persistência nos registros parciais). Não devem ser recriados como fonte de verdade; para rastreabilidade histórica, o registro desta remoção consta neste índice.

## Artefatos canônicos (fonte de referência)

| Arquivo | Título/Conteúdo (breve) | Fonte / Sessão | Status |
|---|---|---|---|
| `00-painel-gerencial-consolidado.md` | Painel gerencial consolidado do baseline v0: semáforo, delegações/evidências, convergências, pontos a reconciliar, decisões pendentes, riscos, próximos passos e estado machine-readable. | `orchestrator` (agregação). Subagentes: PO `ses_e292deeacffeDISULhsnAjsxBi`, PM `ses_e292deea9ffecJ3wI1b7obkWGp`, TL `ses_e292deea6ffeFHtGus1wUTHx1E`. | `condicional` |
| `10-produto-po-visao-mvp-baseline-v0.md` | Produto (PO): visão, problema, personas, proposta de valor; escopo MVP (MoSCoW+WSJF); backlog E1–E4 com critérios Given/When/Then e DoR; semântica canônica de estados (execução/operação/valor); KPIs e mecanismo de feedback/aceite; premissas/lacunas/riscos. | `gerente-produto` (sessão `ses_e292deeacffeDISULhsnAjsxBi`, classe B). | `partial/condicional` |
| `20-governanca-pm-plano-baseline-v0.md` | Governança (PM): roadmap F0–F2 e marcos; RACI; cadência/semáforo; riscos R1–R7 e premissas P1–P5; baseline documental canônico, backlog/tracking, DoR/DoD e change control; plano I1–I2 (PERT+30%) e critério de baseline v0 pronto. | `gerente-projeto` (sessão `ses_e292deea9ffecJ3wI1b7obkWGp`, classe B). | `partial/condicional` |
| `30-arquitetura-tech-lead-baseline-v0.md` | Arquitetura (TL): componentes/fluxos (dispatcher+agregador, SoT/event-log, idempotência), contratos/envelopes e mapeamento de estados; ADRs iniciais A–G (propostos); DoD técnico e gates incrementais G0–G3; plano F0–F5; riscos/lacunas. | `tech-lead` (sessão `ses_e292deea6ffeFHtGus1wUTHx1E`, classe B). | `done/condicional` (execução da proposta) |
| `README.md` | Este índice: política canônica, inventário dos artefatos canônicos e registro de rastreabilidade da remoção dos não canônicos. | Atualização documental (2026-11-13). | `done` |

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
- **Ações não realizadas nesta atualização:** nenhuma ação git (init/add/commit) e nenhuma criação de estrutura de arquivamento adicional.
