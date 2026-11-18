---
title: "Cronograma/RACI/Riscos (PM) — v0"
date: "2026-11-16"
project: "sdlc-agentico"
source: "gerente-projeto"
status: "condicional"
---
> **Change Control:** materializado por aprovação Classe C (DEC-014, 2026-11-16). Conteúdo permanece `condicional`; isto NÃO declara `approved`/`completed` nem inicia implementação (F-ÚNICO-1 bloqueada por D-V0-01 adiado — DEC-006(i)). Modo documental (F-ÚNICO-0) em 1 semana.

**Classe de autonomia:** B/C — proposta de governança materializada (nenhum `approved` declarado).

## Cronograma 1 semana

Modo documental (sem código) até kickoff D-V0-01 resolvido. Condicionado ao kickoff D-V0-01 (antes da semana 1). 5 dias úteis (40h) com buffer 30% (PERT) — capacidade P7 conforme grill 2026-11-16. **Nota (DEC-027, 2026-11-17):** para F-ÚNICO-2 a capacidade estimada vigente é **~4–8h/semana** ([PREMISSA-P10]); o cronograma abaixo reflete o contexto full-time do MVP (histórico).

| Dia | Atividade | Dono (R) | Aprovador (A) | Est. PERT E (×1.3) |
|---|---|---|---|---|
| pré-S1 (D-2…D-1) | Kickoff D-V0-01 (stack/CI/gates) — gate bloqueante | Mantenedor (A/R) | Mantenedor | — (decisão humana) |
| D1 | Revisão RACI semanal + atualização `docs/40`/`docs/20` §3 | PM (R) | Mantenedor (A) | 0.5d→0.65d |
| D2 | Consolidação contrato v1.0.0 (proposta) + semântica de estados (PO/PM/TL) | TL (R) | Mantenedor+PO+PM | 1d→1.3d |
| D3 | Cronograma PERT+30% + DoR/DoD + change control registro | PM (R) | Mantenedor (A) | 1d→1.3d |
| D4 | Reconciliação `docs/10/20/30` + painel + README + DECISIONS | PM (R) + TL/PO (C) | Mantenedor (A) | 1.5d→1.95d |
| D5 | Review de valor (PO) + semáforo + checkpoint + riscos | PO (R) + PM (C) | Mantenedor (A) | 0.5d→0.65d |

**Total estimado:** ~5.85d equivalente sobre 5d úteis (117% da capacidade) — **sobrecarga**; re-planejar ou reduzir escopo. Marcar `[PREMISSA]` e `[LACUNA]` de capacidade real por dia.

**Bloqueio:** se kickoff D-V0-01 não concluído antes da semana 1, toda a semana 1 permanece em F-ÚNICO-0 documental (sem MVP) — R12 ativo.

## RACI

Papéis, não pessoas. Mantenedor único = PO+PM+Sponsor (DEC-006(iv)). Consistente com `docs/40` (RACI de operação do repo, complementar).

| Atividade / Decisão | Orchestrator | PO (gerente-produto) | PM (gerente-projeto) | TL (tech-lead) | Subagentes especialistas | Operador/Sponsor |
|---|---|---|---|---|---|---|
| Visão, valor, MVP, priorização e critérios de aceite | I | **A/R** | C | C | C | I |
| Arquitetura, ADRs, contratos técnicos, quality gates | I | C | C | **A/R** | C/R (insumos) | I |
| Plano, cronograma, RACI, riscos, governança, status | I | C | **A/R** | C | I | C/I |
| Dispatch de tarefas e agregação de resultados | **A/R** | I | I | I | R (execução) | I |
| Execução técnica/conteúdo especializado | I | I | I | C | **R** | I |
| Aceite de valor (`approved`) | I | **A/R** | I | C | I | I |
| Validação técnica/gates (evidência) | I | I | C | **A/R** | R | I |
| Change control (escopo/tempo/custo/qualidade) | I | C | **A/R** | C | I | **A** (impactos relevantes) `[PREMISSA]` |
| Resolução de bloqueios de capacidade/orçamento/prazo | I | C | R | C | I | **A/R** |

Legenda: R=Responsável, A=Aprovador, C=Consultado, I=Informado.

**Cadência de revisão RACI/checkpoints:** semanal (1x/semana), PM delegado (R) com aprovação do Mantenedor (A) (P8). Demais rituais (revisão de backlog/DoR, review de valor/aceite, change control) permanecem sob demanda sem SLA (DEC-006(v)) até nova decisão.

## Riscos R1–R12

| Risco | P×I | Mitigação | Dono |
|---|---|---|---|
| R1 Ambiguidade de contratos entre papéis/artefatos | M×A (Alto) | Baseline contratual v0, templates, distinção explícita done/completed/approved, revisão cruzada PO-TL-PM | PM + TL/PO |
| R2 Falta de vínculo requisito↔decisão↔artefato↔evidência↔aceite | M×A (Alto) | IDs únicos, matriz de rastreabilidade, backlog/task tracking obrigatório, evidência em todo `done` | PM |
| R3 Gates insuficientes ou ignorados | M×A (Alto) | Definição de gates por TL, DoD com evidência, bloqueio de promoção sem gate verde `[PREMISSA]` | TL |
| R4 Capacidade/equipe desconhecida (LACUNA) | A×A (Crítico) | Capacidade estimada ~4–8h/sem (DEC-027 [PREMISSA-P10]); [PREMISSA] de capacidade mínima; planejamento rolling-wave, replanejamento por iteração, não prometer prazo sem buffer | PM + Sponsor |
| R5 Mudanças sem avaliação (change control) | M×M (Médio) | Processo formal de change request, análise de impacto no triângulo de ferro, decisão registrada | PM |
| R6 Dependências externas (repo-alvo, ferramentas, acessos, decisões pendentes) | M×A (Alto) | Registrar dependências, donos e datas-alvo; status `condicional/bloqueado` quando impeditivo | PM |
| R7 Desalinhamento de aceite (execução concluída vs valor aceito) | M×M (Médio) | Critérios de aceite explícitos (PO), checkpoints de review, comunicação de semântica no status | PO + PM |
| R8 D-V0-01 adiado (stack indefinida) — F-ÚNICO-1/MVP bloqueada | A×A (Alto) | Manter F-ÚNICO-0 documental (baixo risco); reabrir D-V0-01 só com kickoff explícito; não iniciar F1 sem decisão | Sponsor/Mantenedor |
| R9 Drift `docs/DECISIONS.md` × change control de `20-*` §5 | M×M (Médio) | Manter referência cruzada (change control ↔ DECISIONS.md) nos próximos change sets; revisar no próximo checkpoint | PM + Orchestrator |
| R10 Bus factor = 1 (Mantenedor único) | A×M (Alto) | Documentar todas as decisões no log; manter artefatos autossuficientes; evitar dependência de contexto oral | Mantenedor |
| R11 Drift documental (roadmap único `47` × contrato v1.0.0 `48` × `10/20/30`) | M×A (Alto) | Tratar como proposta; sincronizar após D-V0-05/06; não usar para execução | TL + PM |
| R12 MVP de 1 semana inviável sem kickoff D-V0-01 resolvido | A×A (Crítico) | Kickoff antes da semana 1; modo documental F-ÚNICO-1 | Mantenedor/PM |

## Premissas P1–P8

- **P1 (SUBSTITUÍDA por DEC-006(v), 2026-11-16):** cadência inicial quinzenal — **não vigente**. Premissa operacional vigente: P6 (sob demanda, sem SLA formal).
- **P2:** capacidade inicial mínima de 1 agente/especialista por trilha ativa, alocação parcial `[LACUNA]`; ajustar após confirmação.
- **P3:** repositório-alvo e ferramenta de tracking serão definidos no kickoff; até lá, baseline mantido em estrutura documental acordada `[LACUNA]`.
- **P4:** buffer de planejamento **30%** aplicado via PERT: `E = ((O + 4×M + P)/6) × 1.3`.
- **P5:** Sponsor/Operador disponível para decisões de impacto em até 2 dias úteis.
- **P6 (DEC-006(v)):** Mantenedor único (Lucinei); cadência sob demanda, sem SLA formal — substitui P1/P5 como premissa operacional vigente; tracking = `docs/` (sem ferramenta externa).
- **P7 (DEC-014):** orçamento monetário = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada; sem custo externo. **[ATUALIZADA para F-ÚNICO-2 por DEC-027, 2026-11-17 — divergência registrada]:** referência vigente passa a ser **[PREMISSA-P10]** (~4–8h/sem, sem SLA, buffer 30%); P7 permanece como registro histórico do MVP full-time (grill 2026-11-16); não usar 40h/sem para novos compromissos.
- **P8 (DEC-014):** cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A).
- **P10 (DEC-027, 2026-11-17):** capacidade estimada **~4–8h/semana** para o projeto (Mantenedor único, projeto paralelo); cadência sob demanda sem SLA; revisão RACI semanal mantida; buffer PERT+30%; **não confirmada explicitamente com o Mantenedor** — tratar como `[PREMISSA]` até confirmação; re-baseline rolling-wave se divergir.

## Lacunas persistentes

- `[LACUNA]` Capacidade real por dia (não confirmada); total estimado 117% da capacidade (sobrecarga) — re-planejar. **Atualização (DEC-027, 2026-11-17):** capacidade estimada ~4–8h/sem ([PREMISSA-P10]); F2.x de `docs/20` §0.1.3 (~3,9d) ≈ 4–8 semanas de calendário — re-planejar; estimativa não confirmada com o Mantenedor.
- `[LACUNA]` Critério operacional de `completed` no tracking alvo (`docs/`) — D-V0-05.
- `[LACUNA]` Stack/CI/gates (D-V0-01) — kickoff antes da semana 1; não resolvido.
- `[LACUNA]` Thresholds de gates (D-V0-06) — lidos do projeto-alvo (inexistente).
- `[LACUNA]` Handoff PR→aceite PO inexistente; AC Given/When/Then ausentes nos designs t1–t5.
- `[LACUNA]` KPIs não instrumentáveis; métricas baseline inexistentes.
- `[LACUNA]` Identificadores correlacionáveis e storage de trilha/evidências/decisões (E4 adiado).
- `[LACUNA]` DEC-007 (política de segredos) permanece aberta.
- `[RESOLVIDO — DEC-027, 2026-11-17]` Ferramenta de tracking/backlog: trilha vigente = `docs/` (DEC-006(vi), Classe C); recomendação de adoção GitHub Issues/Projects para escala **pendente de decisão Classe C do Mantenedor** (CR-010-C); `docs/40` (linha 14) e `docs/20` §0.1.2 atualizados.
