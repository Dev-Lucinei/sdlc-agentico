---
title: "Governança (PM) — Plano e Baseline v0"
date: "2026-11-13"
project: "sdlc-agentico"
source: "gerente-projeto (sessão ses_e292deea9ffecJ3wI1b7obkWGp, status partial/condicional, classe B)"
status: "partial/condicional"
---

**Classe de autonomia declarada:** B (decisão/plano reversível, documentado, sujeito a revisão; nenhuma ação irreversível, aceite de valor ou aprovação de arquitetura executada). `[LACUNA]` Skill de apoio `~/.agents/skills/project-manager/SKILL.md` e políticas/standards em `/home/lucinei/Projetos/.agents/*` não encontrados no ambiente; regras aplicadas com base nas diretrizes fornecidas no prompt e em `~/.opencode/references/{contrato-resumo-subagentes.md,autonomia-e-estados.md}`.

## 0. Reconciliação F-ÚNICO-0 (MU-0.3, 2026-11-16) — bloco aditivo

Bloco aditivo — não apaga histórico. Mapeamento da trilha de governança (F0–F2 / I1–I2) para a trilha única de `docs/47`:

| Trilha única (`docs/47`) | PM (`docs/20`) | Leitura |
|---|---|---|
| **F-ÚNICO-0 — Fundação** | F0 — Fundação Contratual & Governança (M0.1–M0.3; I1–I2); cadência/change control/RACI | Base documental/contratual; reconciliação em andamento (MU-0.3) |
| **F-ÚNICO-1 — MVP Controlado** | F1 — MVP Controlado (M1.1–M1.3) | **Concluída (DEC-024, 2026-11-17):** implementação (SQLite, validador, segredos, máquina de estados, 65 testes, 74,84% cobertura); gates G0→G1 verdes; F-ÚNICO-2 iniciada |
| **F-ÚNICO-2 — Evolução** | F2 — Evolução & Escala (M2.1–M2.2) | Depende de F-ÚNICO-1; change control obrigatório |

**Cadência (DEC-006(v)):** sob demanda, sem SLA formal — substitui a `[PREMISSA-P1]` quinzenal (marcada como substituída acima). Mantenedor único (DEC-006(iv)); tracking = `docs/` (DEC-006(vi)).

**Normativos externos (vivos, referenciados por caminho+sha256 completo — DEC-003; pin exato):**
- `~/.opencode/references/contrato-resumo-subagentes.md` — sha256 `163e0aad7654d0a60930e90388afa9b9474ee727f119e94a62337d8321442a60`
- `~/.opencode/references/autonomia-e-estados.md` — sha256 `776af494ee702cf4d3db8837f2b1c0c23450844f9b54e376a052d7adbc42c78a`

**Evidências (DEC-005):** `docs/evidence/` **rejeitado** — evidências permanecem embutidas nos canônicos ou referenciadas por link/caminho+hash; nenhum diretório paralelo de SoT.

**Status honesto:** `partial/condicional` — nenhuma promoção a `approved`/`completed`; D-V0-01 **RESOLVIDO** (DEC-018, 2026-11-17); D-V0-03/04/05/06 aprovados e materializados (DEC-009…DEC-012); baseline v0 **publicada** (DEC-024, 2026-11-17); F-ÚNICO-1 concluída; F-ÚNICO-2 iniciada.

## 📋 Decisão / Diagnóstico
Proposta de **governança e entrega em 3 fases** (Fundação Contratual → MVP Controlado → Evolução/Escala) para um SDLC agêntico reiniciado, com baseline documental canônico, RACI explícito, gates e change control como pré-condições de execução. **Trade-off (triângulo de ferro):** prioriza-se **qualidade/rastreabilidade e controle de escopo** sobre velocidade inicial, dado `[LACUNA]` de capacidade, prazo, orçamento, repositório-alvo e cadência; estimativas e datas são condicionais (`[PREMISSA]`). “Execução concluída” ≠ “Valor entregue/aceito” (aceite pendente do PO).

## 🗂️ Artefato

### 1) Roadmap, fases, marcos e dependências (trilhas)
| Fase | Objetivo | Marcos (M) | Trilhas e dependências | Saída principal |
|---|---|---|---|---|
| **F0 — Fundação Contratual & Governança** | Estabelecer baseline, contratos e operação mínima | M0.1 Contratos/RACI/DoR-DoD aprovados (processo) · M0.2 Baseline documental canônico v0 · M0.3 Backlog/gates/change-control operacionais | **Governança (PM, líder):** depende de insumos iniciais de Produto e Técnico. **Produto (PO):** Visão/MVP/Backlog priorizado → alimenta F0. **Técnico (TL):** Arquitetura/ADRs/Contratos/Gates → alimenta F0. **PM:** consolida baseline, riscos, RACI, cadência. *Dependência cruzada:* backlog e critérios de aceite (PO) + contratos/gates (TL) antes de declarar baseline pronto. | Baseline v0, registro de riscos, plano de iteração |
| **F1 — MVP Controlado** | Entregar incremento mínimo com rastreabilidade e aceite | M1.1 Incrementos com evidência e gates verdes · M1.2 Validação técnica (TL) · M1.3 Aceite de valor (PO) | **Execução (especialistas):** depende de F0 concluída (DoR atendido). **Técnico:** implementação conforme ADRs/contratos. **Produto:** valida valor/aceite por incremento. **Governança:** monitora status, riscos e mudanças. *Execução concluída ≠ aceito.* | Incrementos do MVP, evidências, decisões de aceite |
| **F2 — Evolução & Escala** | Ampliar escopo com melhoria contínua e controle | M2.1 Retrospectivas/gates ajustados · M2.2 Novos incrementos priorizados | Depende de aprendizados/evidências de F1 e capacidade confirmada `[LACUNA]`. Change control obrigatório para expansão de escopo. | Backlog evolutivo, métricas, ADRs/contratos atualizados |

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
| Ritual/Checkpoint | Frequência `[PREMISSA]` | Participantes | Saída | Semáforo |
|---|---|---|---|---|
| **Checkpoint de status** | 2x/semana (ajustar à cadência real) | PM, PO, TL, Orchestrator (síncrono/assíncrono) | Status por trilha, riscos, bloqueios, decisões pendentes | 🟢 no trilho · 🟡 risco/atraso gerenciável · 🔴 bloqueio/impacto crítico (escala) |
| **Revisão de backlog & DoR** | Início de cada iteração | PO, PM, TL | Itens prontos para execução, dependências claras | — |
| **Revisão técnica/gates** | Por incremento / fim de iteração | TL, especialistas, PM (visibilidade) | Evidências, dívida, go/no-go técnico | — |
| **Review de valor & aceite** | Fim de iteração/incremento | PO, PM, TL | Decisão de aceite (approved/rejeitado/pendente) | — |
| **Change Control Board (leve)** | Sob demanda | PM, PO, TL, Sponsor/Operador (se impacto) | Aprovação/rejeição de mudança + impacto no triângulo de ferro | — |
| **Revisão de riscos** | Semanal + sob gatilho | PM (dono), demais conforme risco | Registro atualizado, ações de mitigação | — |

> **Cadência vigente (DEC-006(v), 2026-11-16):** sob demanda, sem SLA formal — substitui a frequência quinzenal da `[PREMISSA-P1]`; Mantenedor único (DEC-006(iv)); tracking = `docs/` (DEC-006(vi)). As frequências acima (2x/semana, semanal, por incremento) são referência histórica não vigente; aplicar sob demanda até nova decisão.

### 4) Registro inicial de riscos e premissas (P×I, mitigação, dono)
| ID | Tipo | Descrição | P | I | Nível | Mitigação / Resposta | Dono | Gatilho |
|---|---|---|---|---|---|---|---|---|
| R1 | Contratual | Ambiguidade de contratos entre papéis/artefatos (entradas, saídas, “done”) | M | A | Alto | Baseline contratual v0, templates, distinção explícita done/completed/approved, revisão cruzada PO-TL-PM | PM + TL/PO | Divergência de interpretação em entrega |
| R2 | Rastreabilidade | Falta de vínculo requisito↔decisão↔artefato↔evidência↔aceite | M | A | Alto | IDs únicos, matriz de rastreabilidade, backlog/task tracking obrigatório, evidência em todo “done” | PM | Artefato sem evidência ou sem origem |
| R3 | Qualidade/Gates | Gates insuficientes ou ignorados geram débito/defeitos | M | A | Alto | Definição de gates por TL, DoD com evidência, bloqueio de promoção sem gate verde `[PREMISSA]` | TL | Gate falho/ausente em incremento |
| R4 | Capacidade | Capacidade/equipe desconhecida `[LACUNA]` inviabiliza compromissos | A | A | Crítico | `[PREMISSA]` de capacidade mínima, planejamento rolling-wave, replanejamento por iteração, não prometer prazo sem buffer | PM + Sponsor | Compromisso sem alocação confirmada |
| R5 | Change control | Mudanças sem avaliação quebram escopo/prazo/qualidade | M | M | Médio | Processo formal de change request, análise de impacto no triângulo de ferro, decisão registrada | PM | Solicitação fora do baseline |
| R6 | Dependências externas | Repositório-alvo, ferramentas, acessos ou decisões pendentes `[LACUNA]` | M | A | Alto | Registrar dependências, donos e datas-alvo; status `condicional/bloqueado` quando impeditivo | PM | Dependência sem dono/prazo |
| R7 | Desalinhamento de aceite | Confusão entre execução concluída e valor aceito | M | M | Médio | Critérios de aceite explícitos (PO), checkpoints de review, comunicação de semântica no status | PO + PM | Entrega “done” sem decisão de aceite |
| R8 | Governança/Decisão | D-V0-01 adiado (stack indefinida) — F-ÚNICO-1/MVP bloqueada; implementação não iniciável; risco de estagnação do baseline | A | A | Alto | **MITIGADO** por DEC-018 (2026-11-17): stack mínima definida (Python 3.12 + pytest + ruff + mypy, sem CI externo); F-ÚNICO-1 desbloqueada; thresholds absolutos (cobertura ≥50%, 0 erros críticos). LangGraph permanece condicional (CR-009-C). | Sponsor/Mantenedor | Kickoff/decisão D-V0-01 contornada ou F1 iniciada sem decisão |
| R9 | Change control | `docs/DECISIONS.md` como log único pode divergir do change control de `20-*` §5 se o processo não apontar consistentemente para este log | M | M | Médio | Manter referência cruzada (change control ↔ DECISIONS.md) nos próximos change sets; revisar no próximo checkpoint | PM + Orchestrator | Change set sem referência cruzada para DECISIONS.md |
| R10 | Capacidade | Mantenedor único (bus factor = 1) — ponto único de decisão e de falha do baseline | A | M | Alto | Documentar todas as decisões no log (feito); manter artefatos autossuficientes; evitar dependência de contexto oral | Mantenedor | Decisão tomada sem registro no log ou artefato dependente de contexto oral |
| R11 | Rastreabilidade | Roadmap único (`47`) e Contrato v1.0.0 (`48`) são propostas condicional — risco de drift com `10/20/30` enquanto não reconciliados | M | A | Alto | Tratar como proposta; sincronizar após D-V0-05/06; não usar para execução | TL + PM | Divergência detectada entre `47`/`48` e `10/20/30` |

**Premissas explícitas**
- `[PREMISSA-P1]` *(SUBSTITUÍDA por DEC-006(v), 2026-11-16)* Cadência inicial quinzenal (2 semanas) até definição real `[LACUNA]` — **não vigente**. Premissa operacional vigente: `[PREMISSA-P6]` "sob demanda, sem SLA formal" (DEC-006(v), decided_by Lucinei).
- `[PREMISSA-P2]` Capacidade inicial mínima de 1 agente/especialista por trilha ativa, alocação parcial `[LACUNA]`; ajustar após confirmação.
- `[PREMISSA-P3]` Repositório-alvo e ferramenta de tracking serão definidos no kickoff; até lá, baseline mantido em estrutura documental acordada `[LACUNA]`.
- `[PREMISSA-P4]` Buffer de planejamento **30%** aplicado via PERT: `E = ((O + 4×M + P)/6) × 1.3`.
- `[PREMISSA-P5]` Sponsor/Operador disponível para decisões de impacto (C/autorização de mudança relevante) em até 2 dias úteis.
- `[PREMISSA-P6]` [DECISÃO 2026-11-16] Mantenedor único (Lucinei); cadência sob demanda, sem SLA formal — substitui P1/P5 como premissa operacional vigente; tracking = docs/ (sem ferramenta externa).

### 5) Baseline documental canônico, backlog/task tracking, DoR/DoD e change control

**Estratégia de baseline documental canônico (v0)**
| Elemento | Localização canônica `[PREMISSA]` | Dono | Controle |
|---|---|---|---|
| Visão, MVP, critérios de aceite, backlog priorizado | `docs/product/` (ex.: `VISION.md`, `MVP.md`, `BACKLOG.md`) | PO | Versionado; mudanças via change control; ID de itens |
| Arquitetura, ADRs, contratos técnicos, definição de gates | `docs/tech/` (ex.: `ARCHITECTURE.md`, `adrs/`, `CONTRACTS.md`, `GATES.md`) | TL | ADR numerado; contratos versionados |
| Plano, RACI, riscos, status, governança, atas/decisões | `docs/governance/` (ex.: `PLAN.md`, `RACI.md`, `RISK_REGISTER.md`, `STATUS.md`, `DECISIONS.md`) | PM | Atualização por checkpoint; log de mudanças |
| Evidências de execução/aceite | `docs/evidence/` ou links rastreáveis por item | Especialistas/TL/PO | Referência obrigatória para “done” e aceite |

- **Regra:** um artefato é canônico apenas na localização acordada e versionada; duplicatas são referências, não fonte de verdade. Divergência doc vigente × legado → registrada em lacunas/riscos.

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

### 6) Plano das próximas 1–2 iterações (estimativas 3 pontos, PERT E=((O+4M+P)/6)*1.3)
`[PREMISSA-P1/P4]` iteração = 2 semanas; unidade = dias úteis de esforço equivalente.

| It. | Ação | Dono | Dependências | O | M | P | E (×1.3) | Entregável |
|---|---|---|---|---|---|---|---|---|
| I1 | Kickoff de alinhamento: confirmar lacunas (capacidade, prazo, orçamento, repo, cadência, ferramenta) e nomear sponsor/operador | PM (R), PO/TL/Sponsor (C/A) | Disponibilidade stakeholders `[LACUNA]` | 0.5 | 1 | 2 | **1.4d** | Ata de kickoff, lacunas atualizadas |
| I1 | Consolidar Visão/MVP/Backlog inicial priorizado com critérios de aceite | PO (A/R), PM/TL (C) | Kickoff | 1 | 2 | 4 | **2.8d** | `docs/product/*` (rascunho v0) |
| I1 | Definir Arquitetura inicial, ADRs-chave, contratos e quality gates | TL (A/R), PO/PM (C) | Visão/MVP draft | 1 | 3 | 5 | **3.9d** | `docs/tech/*` (rascunho v0) |
| I1 | Estabelecer baseline documental canônico, RACI, DoR/DoD, change control e setup de tracking | PM (A/R), PO/TL (C) | Insumos produto+técnico | 1 | 2 | 3 | **2.6d** | `docs/governance/*`, board inicial |
| I1 | Montar registro de riscos v0 e plano de comunicação/semáforos | PM (A/R), PO/TL (C) | Kickoff | 0.5 | 1 | 2 | **1.4d** | `RISK_REGISTER.md`, `STATUS.md` |
| I2 | Revisão cruzada e reconciliação dos entregáveis paralelos (produto/técnico/governança) | PM (R), PO/TL (A por domínio) | Saídas I1 completas | 1 | 2 | 4 | **2.8d** | Baseline integrado, gaps resolvidos/registrados |
| I2 | Validar operacionalmente DoR/DoD, gates e rastreabilidade em itens-piloto | TL/PM (R), especialistas (C) | Baseline integrado, tracking ativo | 1 | 2 | 4 | **2.8d** | Evidência de processo, ajustes |
| I2 | Selecionar/refinar fatia MVP “ready” e planejar I3 com capacidade confirmada | PO (A/R), PM/TL (C) | Capacidade `[LACUNA]` reduzida; reconciliação | 0.5 | 1 | 2 | **1.4d** | Backlog ready para execução, plano I3 |

**Critério de “baseline v0 pronto para execução”** (todos obrigatórios)
1. **Documental canônico:** Visão/MVP/Backlog (PO), Arquitetura/ADRs/Contratos/Gates (TL) e Plano/RACI/Riscos/Governança (PM) publicados em local canônico versionado e reconciliados.
2. **Contratos e rastreabilidade:** papéis, entradas/saídas, distinção `done`≠`accepted` e vínculo item↔decisão↔evidência definidos.
3. **Processo operacional:** RACI, cadência, semáforo, DoR/DoD e change control aprovados (processualmente) e conhecidos pelos papéis.
4. **Tracking ativo:** backlog com IDs, estados e ao menos uma fatia MVP em estado `ready` (DoR atendido).
5. **Riscos/premissas registrados:** riscos críticos com mitigação/dono e lacunas `[LACUNA]` explicitadas com plano de resolução.
6. **Dependências críticas:** sem bloqueio crítico não mitigado para iniciar I3 (ou decisão explícita de iniciar com risco aceito e registrado).

## ⚠️ Riscos e Premissas
- `[RISCO][R1-R11]` Ver registro acima (P×I, mitigação, dono e gatilho definidos).
- `[PREMISSA][P1-P6]` Cadência quinzenal, capacidade mínima presumida, local/ferramenta de baseline/tracking a confirmar, buffer PERT 30%, disponibilidade de sponsor em 2 dias úteis.
- `[LACUNA]` Equipe/capacidade real, prazo-alvo, orçamento, repositório-alvo e cadência oficial não informados — **não prometer prazo sem buffer e sem dependências resolvidas**; plano permanece `condicional`.
- `[LACUNA]` Skill/políticas/standards de apoio indicados no ambiente não acessíveis; validação final deve cruzar com esses artefatos quando disponíveis.

## ✅ Próximas Ações
1. **Realizar kickoff e fechar lacunas críticas** (capacidade, prazo, orçamento, repo, cadência, sponsor, ferramenta) — Dono: **PM** (R), **Sponsor/Operador** (A), PO/TL (C) — Prazo: I1/D1-D2 `[PREMISSA]`.
2. **Entregar e reconciliar Visão/MVP/Backlog + Arquitetura/ADRs/Contratos/Gates + Baseline de governança (v0)** — Dono: **PO** (produto), **TL** (técnico), **PM** (governança/consolidação) — Prazo: fim de I1 `[PREMISSA]`.
3. **Ativar tracking, validar DoR/DoD/gates em piloto e declarar baseline v0 pronto (ou gaps formais)** — Dono: **PM + TL** (R), **PO** (aceite de processo/produto conforme domínio) — Prazo: fim de I2 `[PREMISSA]`.
4. **Revisão de riscos e change requests** em cadência definida — Dono: **PM** — Prazo: contínuo (semanal/sob gatilho).

---
```json
{
  "decision_id": "01JZ8K3M7T9Q2V4X6B8N1C5D7E",
  "papel": "gerente-projeto",
  "classe_autonomia": "B",
  "status": "condicional",
  "criterio": "triangulo-de-ferro",
  "evidencia": [
    {
      "tipo": "input",
      "ref": "input_query/project_context fornecidos na sessão",
      "nota": "Plano elaborado a partir da demanda; sem artefatos de projeto versionados verificados"
    },
    {
      "tipo": "referencia",
      "ref": "~/.opencode/references/contrato-resumo-subagentes.md",
      "nota": "Contrato de resumo aplicado"
    },
    {
      "tipo": "referencia",
      "ref": "~/.opencode/references/autonomia-e-estados.md",
      "nota": "Autonomia/estados aplicados"
    }
  ],
  "premissas_validadas": [
    "Distinção Execução concluída ≠ Valor entregue/aceito (pendente de aceite PO) adotada",
    "Orquestrador como dispatcher+agregador; papéis PO/TL/PM conforme contexto",
    "PERT com buffer 30% aplicado nas estimativas (E=((O+4M+P)/6)*1.3)"
  ],
  "lacunas": [
    "Equipe/capacidade não definida",
    "Prazo-alvo não definido",
    "Orçamento não definido",
    "Repositório-alvo não definido",
    "Cadência oficial não definida",
    "Ferramenta de backlog/task tracking não definida",
    "Skill ~/.agents/skills/project-manager/SKILL.md não acessível no ambiente",
    "Políticas/standards /home/lucinei/Projetos/.agents/* não acessíveis no ambiente"
  ],
  "proximas_acoes": [
    {"acao": "Kickoff para fechar lacunas críticas e confirmar sponsor/ferramenta/cadência", "dono": "PM (R), Sponsor/Operador (A)"},
    {"acao": "Produzir e reconciliar baseline documental v0 (produto, técnico, governança)", "dono": "PO, TL, PM"},
    {"acao": "Ativar tracking e validar DoR/DoD/gates para declarar baseline v0 pronto", "dono": "PM, TL, PO"}
  ],
  "schema_version": "1.0"
}
```

## Resumo do Subagente
- objetivo: Produzir plano de governança e entrega do zero para um sistema SDLC agêntico robusto e eficiente.
- ação executada: Defini roadmap/fases/marcos e dependências; elaborei RACI e cadência de governança com semáforo; construí registro inicial de riscos/premissas (P×I, mitigação, dono); defini estratégia de baseline documental canônico, backlog/tracking, DoR/DoD e change control; propus plano de 1–2 iterações com estimativas 3 pontos (PERT+30%) e critério de baseline v0 pronto.
- resultado/artefato: Plano de governança e entrega (neste retorno) incluindo roadmap F0-F2, RACI, cadência, riscos R1-R11, premissas P1-P6, estrutura canônica, DoR/DoD, change control, plano I1-I2 e JSON machine-readable.
- evidência: Insumos da sessão (`input_query`, `project_context`) e referências lidas (`~/.opencode/references/contrato-resumo-subagentes.md`, `~/.opencode/references/autonomia-e-estados.md`). `[LACUNA]` Sem artefatos versionados no repositório, sem skill/políticas acessíveis e sem dados de capacidade/prazo/orçamento/repo/cadência.
- status: partial
- bloqueios/riscos: `[LACUNA]` capacidade, prazo, orçamento, repositório-alvo, cadência e ferramenta de tracking indefinidos; dependências entre trilhas (PO/TL/PM) ainda não materializadas em artefatos canônicos; skill/políticas de apoio não verificadas no ambiente. Riscos críticos R1-R4 (ambiguidade, rastreabilidade, gates, capacidade).
- decisão pendente: Aprovação processual do baseline/governança e definição das lacunas críticas por Sponsor/Operador, PO e TL; aceite de valor permanece exclusivo do PO em incrementos futuros.
- próxima ação recomendada: Realizar kickoff (I1) para fechar lacunas e consolidar/reconciliar artefatos canônicos v0 (produto, técnico, governança), ativar tracking e validar baseline v0 pronto para execução.
