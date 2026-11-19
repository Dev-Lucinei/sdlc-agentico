---
title: "Governança (PM) — Plano e Baseline v0"
date: "2026-11-18"
project: "sdlc-agentico"
source: "gerente-projeto (sessão ses_e292deea9ffecJ3wI1b7obkWGp, status partial/condicional, classe B)"
status: "partial/condicional"
---

**Classe de autonomia declarada:** B (decisão/plano reversível, documentado, sujeito a revisão; nenhuma ação irreversível, aceite de valor ou aprovação de arquitetura executada). `[LACUNA]` Skill de apoio `~/.agents/skills/project-manager/SKILL.md` e políticas/standards em `/home/lucinei/Projetos/.agents/*` não encontrados no ambiente; regras aplicadas com base nas diretrizes fornecidas no prompt e em `~/.opencode/references/{contrato-resumo-subagentes.md,autonomia-e-estados.md}`.

### 0.1) Capacidade e Tracking (resolução de D-V0-02, F-ÚNICO-2, DEC-027)

**Premissa P10/capacidade (1 linha):** `[PREMISSA-P10]` (DEC-027, 2026-11-17; **CONFIRMADA pelo Mantenedor em DEC-032, 2026-11-18, Classe C**) — capacidade do Mantenedor único; **valor vigente em `docs/00` §0** (DEC-029; telemetria volátil); cadência sob demanda sem SLA; buffer PERT+30%.

### 0.1.3) Cronograma F-ÚNICO-2 (Evolução)

Modo documental/técnico com change control obrigatório. Capacidade: ver `docs/00` §0 "Status dinâmico" ([PREMISSA-P10], DEC-027/DEC-029); buffer PERT+30%. Sob demanda, sem SLA (DEC-006(v)).

| Item | Descrição | Dono (R) | Aprovador (A) | Est. PERT E (×1.3) | Status |
|---|---|---|---|---|---|
| F2.1 | Reconciliar backlog E1–E4 com estados/IDs e DoR/DoD (tracking = `docs/`) | PM (R) | Mantenedor (A) | 1d→1.3d | `ready` (E1–E3) |
| F2.2 | Resolver lacunas de peso 5 — **remanescente (Onda 2, DEC-032):** KPIs instrumentáveis (KPI-4/KPI-5) + IDs correlacionáveis (E4) + correção deste stale; handoff PR→aceite PO e AC Given/When/Then **já materializados** (DEC-026, 2026-11-17; aceite formal DEC-030, 2026-11-18) | PM + TL + PO | Mantenedor (A) | 2d→2.6d | `in_progress` |
| F2.3 | E4 (rastreabilidade ponta a ponta) — adiado de MVP | TL (R) | Mantenedor + PO | 2d→2.6d | `todo` (F-ÚNICO-2) |
| F2.4 | Revisão de riscos e change control (semanal) | PM (R) | Mantenedor (A) | contínuo | `in_progress` |
| F2.5 | Aceite de valor (PO) sobre incrementos concluídos | PO (A/R) | PO | sob demanda | `todo` (aguarda `done`) |

**Total estimado (F2.1+F2.2):** ~3,9d equivalente **não cabe em 1 semana** ao ritmo de capacidade vigente (`docs/00` §0; ≈0,5–1 dia útil/semana ⇒ ~4–8 semanas de calendário para F2.1+F2.2) — **re-planejar com janela realista ou reduzir escopo**; re-baseline rolling-wave sob demanda; nenhum prazo prometido sem buffer. E4 (F2.3) entra em iteração seguinte.

**Dependências críticas (não bloqueantes):** handoff PR→aceite PO e AC Given/When/Then — **materializados** (DEC-026, 2026-11-17; aceite formal DEC-030, 2026-11-18, Classe C); KPIs instrumentáveis (KPI-4/KPI-5) e IDs correlacionáveis (E4) permanecem `[LACUNA]`, com plano de resolução em F2.2 (Onda 2). **Escopo F2.2 pós-DEC-032 (Onda 1 = F2.1+F2.4; Onda 2 = F2.2 remanescente — KPI-4/KPI-5 e E4/IDs correlacionáveis): ver DEC-032 (2026-11-18, Classe C).**

## 📋 Decisão / Diagnóstico
Proposta de **governança e entrega em 3 fases** (Fundação Contratual → MVP Controlado → Evolução/Escala) para um SDLC agêntico reiniciado, com baseline documental canônico, RACI explícito, gates e change control como pré-condições de execução. **Trade-off (triângulo de ferro):** prioriza-se **qualidade/rastreabilidade e controle de escopo** sobre velocidade inicial, dado `[LACUNA]` de capacidade, prazo, orçamento, repositório-alvo e cadência; estimativas e datas são condicionais (`[PREMISSA]`). “Execução concluída” ≠ “Valor entregue/aceito” (aceite pendente do PO).

## 🗂️ Artefato

### 1) Roadmap, fases, marcos e dependências (trilhas)

Trilha única F-ÚNICO-0/1/2 — ver `docs/10-produto-visao-v0.md`, `docs/00-painel-gerencial-consolidado.md` §0, `docs/historico/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` e `docs/DECISIONS.md`.

### 2) RACI detalhado
| Atividade / Decisão | Orchestrator | PO (gerente-produto) | PM (gerente-projeto) | TL (tech-lead) | Subagentes especialistas | Operador/Sponsor |
|---|---|---|---|---|---|---|
| Visão, valor, MVP, priorização e critérios de aceite | I | **A/R** | C | C | C | I |
| Arquitetura, ADRs, contratos técnicos, quality gates | I | C | C | **A/R** | C/R (insumos) | I |
| Plano, cronograma, RACI, riscos, governança, status | I | C | **A/R** | C | I | C/I |
| Dispatch de tarefas e agregação de resultados | **A/R** | I | I | I | R (execução) | I |
| Execução técnica/conteúdo especializado | I | I | I | C | **R** | I |
| Aceite de valor (“approved”) | I | **A/R** | I | C | I | I |
| Validação técnica/gates (evidência) | I | I | C | **A/R** | R | I |
| Change control (escopo/tempo/custo/qualidade) | I | C | **A/R** | C | I | **A** (impactos relevantes) `[PREMISSA]` |
| Resolução de bloqueios de capacidade/orçamento/prazo | I | C | R | C | I | **A/R** |

**Legenda:** R=Responsável, A=Aprovador, C=Consultado, I=Informado.

### 3) Cadência de governança e status

Cadência sob demanda (DEC-006(v)).

### 4) Registro inicial de riscos e premissas (P×I, mitigação, dono)
| ID | Tipo | Descrição | P | I | Nível | Mitigação / Resposta | Dono | Gatilho |
|---|---|---|---|---|---|---|---|---|
| R1 | Contratual | Ambiguidade de contratos entre papéis/artefatos (entradas, saídas, “done”) | M | A | Médio | **MITIGADO (DEC-021):** contrato canônico v1.0.0 adotado (`docs/48`); validador `docs/schemas/contract-v1.0.0.schema.json`; distinção `done`≠`completed`≠`approved` fixada; 65 testes verdes. Monitorar em change sets futuros. | PM + TL/PO | Divergência de interpretação em entrega |
| R2 | Rastreabilidade | Falta de vínculo requisito↔decisão↔artefato↔evidência↔aceite | M | A | Médio | **MITIGADO (DEC-027):** tracking = `docs/` (DEC-006(vi)); convenção de estados `todo→ready→in_progress→done→accepted/rejected` formalizada; IDs E/H/T; evidência obrigatória no DoD. E4 (IDs correlacionáveis) adiado para F-ÚNICO-2. | PM | Artefato sem evidência ou sem origem |
| R3 | Qualidade/Gates | Gates insuficientes ou ignorados geram débito/defeitos | M | A | Médio | **MITIGADO (DEC-022):** política unificada de gates adotada (G0–G3, exit_code 6 fail-closed); thresholds absolutos (cobertura ≥50%, 0 erros críticos); `make lint/test/typecheck/build/audit` parametrizados. | TL | Gate falho/ausente em incremento |
| R4 | Capacidade | Capacidade/equipe (Mantenedor único) — compromissos inviáveis sem alocação confirmada | A | M | Alto | **MITIGADO (DEC-027, 2026-11-17):** capacidade estimada do Mantenedor único = `[PREMISSA-P10]` (valor vigente em `docs/00` §0 "Status dinâmico" — DEC-029); divergência registrada com DEC-014 [PREMISSA-P7] (40h/sem full-time MVP — **depreciada/histórica**, DEC-029); buffer PERT+30% mantido; planejamento rolling-wave sob demanda; não prometer prazo sem buffer. Probabilidade de sobrecarga **aumentou** vs. premissa 40h/sem — monitorar em checkpoint semanal. | PM + Sponsor | Compromisso sem alocação confirmada |
| R5 | Change control | Mudanças sem avaliação quebram escopo/prazo/qualidade | M | M | Médio | Processo formal de change request, análise de impacto no triângulo de ferro, decisão registrada | PM | Solicitação fora do baseline |
| R6 | Dependências externas | Repositório-alvo, ferramentas, acessos ou decisões pendentes | M | M | Médio | **MITIGADO (DEC-018/DEC-027):** repo-alvo = este repo (DEC-006(ii)); stack mínima definida (DEC-018); tracking = `docs/` (DEC-006(vi)/DEC-027); ferramentas de gates (ruff/mypy/pytest) disponíveis localmente. Dependências restantes (IDs correlacionáveis/E4) registradas como lacuna não bloqueante para F-ÚNICO-2. | PM | Dependência sem dono/prazo |
| R7 | Desalinhamento de aceite | Confusão entre execução concluída e valor aceito | M | M | Médio | **MITIGADO (DEC-019/DEC-021):** semântica de estados fixada (`done`≠`completed`≠`approved`); `approved` terminal/exclusivo do PO; contrato v1.0.0 adotado. Handoff PR→aceite PO permanece `[LACUNA]` (F-ÚNICO-2). | PO + PM | Entrega “done” sem decisão de aceite |
| R8 | Governança/Decisão | D-V0-01 adiado (stack indefinida) — F-ÚNICO-1/MVP bloqueada; risco de estagnação do baseline | A | A | Alto | **MITIGADO** por DEC-018 (2026-11-17): stack mínima definida (Python 3.12 + pytest + ruff + mypy, sem CI externo); F-ÚNICO-1 concluída (65 testes, 74,84% cobertura); thresholds absolutos (cobertura ≥50%, 0 erros críticos). LangGraph permanece condicional (CR-009-C). **R8 fechado.** | Sponsor/Mantenedor | Kickoff/decisão D-V0-01 contornada ou F1 iniciada sem decisão |
| R9 | Change control | `docs/DECISIONS.md` como log único pode divergir do change control de `20-*` §5 se o processo não apontar consistentemente para este log | M | M | Médio | Manter referência cruzada (change control ↔ DECISIONS.md) nos próximos change sets; revisar no próximo checkpoint | PM + Orchestrator | Change set sem referência cruzada para DECISIONS.md |
| R10 | Capacidade | Mantenedor único (bus factor = 1) — ponto único de decisão e de falha do baseline | A | M | Médio | **MITIGADO (DEC-027):** decisões registradas no log (DEC-001…DEC-027); artefatos autossuficientes; tracking = `docs/` (sem dependência de contexto oral); capacidade `[PREMISSA-P10]` — valor em `docs/00` §0 (DEC-029). Risco residual: sobrecarga do Mantenedor em F-ÚNICO-2 (mitigação: escopo sob demanda, buffer 30%, change control, re-baseline rolling-wave). | Mantenedor | Decisão tomada sem registro no log ou artefato dependente de contexto oral |
| R11 | Rastreabilidade | Roadmap único (`47`) e Contrato v1.0.0 (`48`) — risco de drift com `10/20/30` | M | M | Médio | **MITIGADO (DEC-024):** baseline v0 publicada (6/6 critérios §8.3 PASS); D-V0-03/04/05/06 aprovados e materializados (DEC-019…DEC-022); contratos/rastreabilidade reconciliados. Monitorar divergência em change sets futuros (R9). | TL + PM | Divergência detectada entre `47`/`48` e `10/20/30` |
| R12 | Governança/Execução | MVP de 1 semana inviável sem kickoff D-V0-01 resolvido (bloqueio ativo) | A | A | Alto | **MITIGADO (DEC-018/DEC-024):** D-V0-01 resolvido (stack mínima); F-ÚNICO-1 concluída; F-ÚNICO-2 iniciada. R12 fechado para execução. | Mantenedor/PM | Kickoff D-V0-01 não concluído antes da semana 1 |

### 5) Backlog/task tracking, DoR/DoD e change control

**Backlog & task tracking**
- Hierarquia: **Épico → História/Item → Tarefa** com ID único, dono, dependências, critérios de aceite, estimativa e estado.
- Estados mínimos: `todo` → `ready` (DoR) → `in_progress` → `done` (execução + evidência) → `accepted` (PO) / `rejected`.
- Rastreabilidade obrigatória: item ↔ ADR/contrato ↔ evidência ↔ decisão de aceite. Ferramenta `[LACUNA]` (board/issue tracker) a definir no M0.1.

**DoR (Definition of Ready) — processo**
- Item priorizado pelo PO com valor/objetivo e critérios de aceite claros.
- Dependências identificadas e sem bloqueio crítico (ou risco aceito).
- Contratos/gates técnicos aplicáveis definidos ou referenciados (TL).
- Estimativa e dono atribuídos; cabe na iteração `[PREMISSA]`.
- Sem ambiguidade contratual impeditiva (ou lacuna registrada).

**DoD (Definition of Done) — processo**
- Trabalho executado conforme escopo do item e contratos aplicáveis.
- Evidência verificável anexada/referenciada (testes, logs, diffs, checks) — sem evidência não há `done`.
- Gates de qualidade aplicáveis atendidos/registrados (TL).
- Documentação/artefatos atualizados quando aplicável.
- **Atenção:** `done` (execução) ≠ `accepted/approved` (valor aceito pelo PO).

**Change control (triângulo de ferro: escopo/tempo/custo/qualidade)**
1. **Solicitação:** registrar change request (descrição, solicitante, motivação, item afetado).
2. **Análise de impacto (PM+TL+PO):** efeito em escopo, prazo, custo/capacidade e qualidade/riscos; opções e trade-off.
3. **Decisão:** PM consolida; aprovação conforme impacto (`[PREMISSA]` Sponsor para alto impacto). Decisão registrada em `docs/DECISIONS.md`.
4. **Execução:** atualizar baseline/backlog/planos; comunicar em checkpoint.
5. **Sem aprovação registrada não há mudança de baseline.**

## ⚠️ Riscos e Premissas
- `[RISCO][R1-R12]` Ver registro acima (P×I, mitigação, dono e gatilho definidos).
- `[PREMISSA][P10]` Capacidade do Mantenedor único — valor vigente em `docs/00` §0 (DEC-029); cadência sob demanda sem SLA (DEC-006(v)); buffer PERT 30%.
- `[LACUNA]` KPIs não instrumentáveis (KPI-4/KPI-5); IDs correlacionáveis (E4) — remanescentes de F2.2 (Onda 2, DEC-032). Handoff PR→aceite PO e AC Given/When/Then **materializados** (DEC-026; aceite formal DEC-030).

## ✅ Próximas Ações
1. **F-ÚNICO-2 (Evolução) em andamento** — kickoff formal **DEC-032** (2026-11-18, Classe C; Onda 1 = F2.1+F2.4; Onda 2 = F2.2 remanescente: KPI-4/KPI-5 + E4/IDs correlacionáveis); F2.2 (lacunas de peso 5 remanescentes) e F2.4 (revisão de riscos/change control) `in_progress`; F2.1 `ready`; F2.3 `todo`; F2.5 (aceite de valor, PO) aguarda `done` dos incrementos. Rolling-wave sob demanda, sem SLA (DEC-006(v)). — Dono: PM/TL — Prazo: sob demanda.
2. **Revisão contínua de riscos e change requests** (F2.4) — Dono: **PM** — Prazo: contínuo (sob demanda/gatilho).
3. **AÇÃO final [aguardando]** — encerramento de F-ÚNICO-2 e decisão de valor do PO sobre os incrementos (F2.5); aguarda `done` + evidência verificável. Aceite de valor é ato exclusivo do PO; nenhuma promoção por inferência. — Prazo: sob demanda, sem SLA (DEC-006(v)).
