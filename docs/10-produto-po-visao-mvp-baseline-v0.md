---
title: "Produto (PO) — Visão, MVP e Baseline v0"
date: "2026-11-17"
project: "sdlc-agentico"
source: "gerente-produto (sessão ses_e292deeacffeDISULhsnAjsxBi, status partial/condicional, classe B)"
status: "partial/condicional"
---

**Classe de autonomia:** B (definição de produto/backlog reversível, documentada; aceite de valor permanece Classe C e exclusivo do PO)

## 🎯 Decisão / Conclusão
Definir o MVP do **sistema SDLC agêntico** como um núcleo de **orquestração rastreável** (dispatcher+agregador) com **contrato canônico de resumo**, **semântica explícita de estados** e **mecanismo de aceite de valor pelo PO**. Priorização por **WSJF** (Valor de Negócio + Criticidade de Tempo + Redução de Risco/Oportunidade ÷ Tamanho) e escopo por **MoSCoW** (Must = 3 itens nucleares, sem exceção), dado que rastreabilidade e distinção execução≠valor são requisitos centrais e mitigam risco operacional/decisório.

## 🗂️ Artefato

### 0. Reconciliação F-ÚNICO-0 (Fase F-ÚNICO-0 / MU-0.3, 2026-11-16)

Bloco aditivo — não apaga histórico. Mapeamento da trilha PO (M1–M3 / E1–E4) para a trilha única de `docs/47`:

| Trilha única (`docs/47`) | PO (`docs/10`) | Leitura |
|---|---|---|
| **F-ÚNICO-0 — Fundação** (documental + contratual + decisões) | Pré-condição de M1–M3 (visão/MVP/estados/KPIs como insumo; nenhum aceite) | Visão, MoSCoW/WSJF, backlog E1–E4 e semântica de estados entram como insumo; D-V0-03 (aceite PO) pendente |
| **F-ÚNICO-1 — MVP Controlado** | M1 (contrato canônico de resumo), M2 (semântica de estados), M3 (aceite de valor PO); E1 (H1.1–H1.3), E2 (H2.1–H2.2), E3 (H3.1–H3.3); E4/H4.1 (Should) | Núcleo do MVP; **bloqueado** por D-V0-01 adiado (DEC-006(i)) e D-V0-03/04/05/06 |
| **F-ÚNICO-2 — Evolução** | E2–E4 completos; S1/S2/C1/C2 conforme WSJF; KPIs calibrados | Piloto, endurecimento G2→G3, evolução; depende de F-ÚNICO-1 |

**Cadência (DEC-006(v)):** sob demanda, sem SLA formal — substitui a premissa de cadência/SLA quinzenal onde aplicável (KPIs de lead time, riscos de gargalo de aceite). Mantenedor único (DEC-006(iv)); tracking = `docs/` (DEC-006(vi)).

**Normativos externos (vivos, referenciados por caminho+sha256 — DEC-003; pin exato):**
- `~/.opencode/references/contrato-resumo-subagentes.md` — sha256 `163e0aad7654d0a60930e90388afa9b9474ee727f119e94a62337d8321442a60`
- `~/.opencode/references/autonomia-e-estados.md` — sha256 `776af494ee702cf4d3db8837f2b1c0c23450844f9b54e376a052d7adbc42c78a`

**Evidências (DEC-005):** `docs/evidence/` **rejeitado** — evidências permanecem embutidas nos canônicos ou referenciadas por link/caminho+hash; nenhum diretório paralelo de SoT.

**Semântica de estados (alinhar com `docs/48` §(iii)/(iv)):** execução (`done/blocked/partial`) ≠ operação (`completed`) ≠ valor (`pending/approved/rejected`); `approved` terminal e exclusivo do PO; critério operacional proposto de `completed` = item executado (resumo `done` com evidência) + gates aplicáveis atendidos + registro de conclusão no sistema operacional de tracking, com rastreio ao(s) resumo(s)/evidência(s). **`[LACUNA]`** critério exato no tracking alvo (hoje `docs/` como trilha — DEC-006(vi); sem board/tool).

**Status honesto:** `partial/condicional` — nenhuma promoção a `approved`/`completed`; D-V0-01 RESOLVIDO (DEC-018); D-V0-03/04/05/06 APROVADOS E MATERIALIZADOS (DEC-019…DEC-022); DEC-007 FECHADO (DEC-023); baseline v0 PUBLICADA (DEC-024); F-ÚNICO-2 (Evolução) iniciada. Aceite de valor PO permanece pendente (execução ≠ valor); pacote de evidência para aceite de E1–E3 preparado (§0.2, DEC-028) — aguardando decisão explícita do PO.

### 0.1) Adendo F-ÚNICO-2 (Evolução) — Aceite de Valor (PO) e handoff (2026-11-17)
- **AC Given/When/Then completos para E1–E3** e **handoff PR→aceite PO** materializados em `docs/11-visao-mvp-v0.md` §"Aceite de Valor (PO)" (fonte canônica do aceite de valor).
- **Handoff PR→aceite PO:** PR criado → evidência anexada (resumo válido + gates verdes + lacunas explícitas) → PO revisa (AC + KPIs) → decisão `approved`/`rejected` registrada em `docs/DECISIONS.md` (DEC-*) + PR → feedback estruturado se `rejected`.
- **SLA de decisão:** sob demanda, sem SLA formal (DEC-006(v)); meta de lead time (KPI-4) proposta ≤ 5 dias úteis, a calibrar.
- **KPIs calibrados para F-ÚNICO-2:** ver tabela §4 (KPI-1 a KPI-6) — KPI-4/KPI-5 passam de `[LACUNA]` para metas propostas a calibrar.
- **Lacunas remanescentes:** identificadores correlacionáveis/storage de trilha (E4) e critério operacional de `completed` no tracking alvo seguem `[LACUNA]` (D-V0-05).

### 0.2) Adendo F-ÚNICO-2 — Pacote de evidência para aceite de valor (PO) dos incrementos MVP E1–E3 (2026-11-17)

> **Regra de valor:** `done` (execução) ≠ `completed` (operação) ≠ `approved` (valor). Nenhum incremento está `approved`; o aceite é **exclusivo do PO** e exige decisão explícita com evidência (`human_interaction_ref` quando a decisão for tomada por interação humana — Classe C). Este pacote **prepara** o aceite; não o declara. Evidências embutidas/referenciadas aqui (DEC-005 — `docs/evidence/` rejeitado). Medição de 2026-11-17 (sessão de preparação do pacote): `make audit` verde (lint ruff + typecheck mypy + 65 testes) e cobertura total **75,00%** (`pytest --cov=src`; threshold ≥50% — DEC-018/DEC-022). Nota de drift: o painel e DEC-024 citam 74,84% (medição anterior); a medição atual é 75,00%.

| Incremento | Escopo entregue (execução `done`) | Evidência verificável | AC (Given/When/Then) | Status atual |
|---|---|---|---|---|
| **E1 — Contrato canônico v1.0.0 + validador JSON Schema** (Must, M1; H1.1–H1.3) | `src/contract_validator.py` (201 stmts, 60% cobertura), `src/exit_codes.py` (59%), schema `docs/schemas/contract-v1.0.0.schema.json`; validação de resumo (`done`⇒evidência; `blocked/partial`⇒bloqueios+próxima ação) e `decisão pendente` explícita | `tests/test_contract_validator.py`, `tests/test_validate_contract.py` (verdes); commits `e54c083` (validador JSON), `c6b2567` (testes do validador), `f6d74f6` (feat fase1); `make audit` verde; contrato v1.0.0 adotado (DEC-021) | H1.1/H1.2/H1.3 — ver §2 e `docs/11-visao-mvp-v0.md` §"Aceite de Valor (PO)" | `done` (execução) / registro em `docs/` como trilha (DEC-006(vi)); **nunca `approved`** |
| **E2 — Máquina de estados (done ⇏ completed ⇏ approved) + transições validadas** (Must, M2; H2.1–H2.2) | `src/state.py` (105 stmts, 79% cobertura) — estados de execução/operação/valor e guardas de transição; `approved` não escribível por agente | `tests/test_state_transitions.py` (verde); commit `f6d74f6` (feat fase1); ADR-005 `accepted` (DEC-020); invariantes em `docs/11` §"Semântica de estados" | H2.1/H2.2 — ver §2 e `docs/11-visao-mvp-v0.md` §"Aceite de Valor (PO)" | `done` (execução); **nunca `approved`** |
| **E3 — Persistência SQLite (SoT + Event Log append-only)** (Must, M3-suporte técnico; H3.1–H3.3 no que tange a trilha/registro de decisões) | `src/persistence.py` (230 stmts, **91% cobertura**) — SoT + event log append-only; base para rastreabilidade de decisões/evidências (E4 permanece adiado) | `tests/test_persistence.py` (verde); commit `f6d74f6` (feat fase1); DEC-024 (F-ÚNICO-1 concluída) | H3.1/H3.2/H3.3 — ver §2 e `docs/11-visao-mvp-v0.md` §"Aceite de Valor (PO)" | `done` (execução); **nunca `approved`** |

**Agregado:** 65 testes verdes · cobertura total 75,00% (≥50% exigido) · `make audit` verde · commits de implementação `e54c083`, `c6b2567`, `71fc6f6`, `f6d74f6` · contrato v1.0.0 adotado (DEC-021) · gates/thresholds vigentes (DEC-022).

**Decision/Acceptance v0 — pacote de aceite (status: `pending`)**

```json
{
  "decision_id": "01M7P3NFTDNKR760KBBBHE8PSV",
  "papel": "gerente-produto",
  "classe_autonomia": "C",
  "decision_type": "aceite",
  "criterio": "Given/When/Then",
  "status": "pending",
  "decided_by": "PO (exclusivo; único aceitador no MVP) — decisão explícita pendente",
  "evidence_refs": [
    "docs/10-produto-po-visao-mvp-baseline-v0.md §0.2 (este pacote) e §2 (backlog E1–E3 com AC)",
    "docs/11-visao-mvp-v0.md §\"Aceite de Valor (PO)\" (AC Given/When/Then + handoff PR→aceite PO)",
    "tests/test_contract_validator.py, tests/test_validate_contract.py, tests/test_state_transitions.py, tests/test_persistence.py (65 testes verdes, 2026-11-17)",
    "make audit verde (ruff + mypy + pytest; cobertura 75,00% ≥ 50% — pyproject.toml)",
    "commits e54c083, c6b2567, 71fc6f6, f6d74f6 (implementação E1–E3)",
    "DEC-021 (contrato v1.0.0), DEC-022 (gates/thresholds), DEC-024 (baseline v0 publicada), DEC-026 (AC + handoff materializados), DEC-028 (pacote de evidência)"
  ],
  "human_interaction_ref": "[PENDENTE] — obrigatório quando a decisão for tomada por interação humana (Classe C); a ser preenchido pelo PO no ato do aceite (DEC-* em docs/DECISIONS.md)",
  "decided_at": null,
  "rationale": null,
  "schema_version": "1.0"
}
```

**Condições para sair de `pending`:** PO revisa AC Given/When/Then + evidências → registra `approved` (com `evidence` + `decided_by=PO` + `decided_at` + `human_interaction_ref`) **ou** `rejected` (com `rationale` + `decided_by=PO` + `decided_at`) em `docs/DECISIONS.md` (DEC-*). `rejected → pending` somente com nova evidência. Nenhuma inferência de `approved` a partir de `done`/`completed`.

### 1. Visão, Problema, Personas e Proposta de Valor

| Elemento | Definição |
|---|---|
| **Visão** | Tornar o SDLC agêntico **previsível, auditável e orientado a valor**, onde cada execução técnica é rastreável ponta a ponta e nenhum resultado é tratado como valor entregue sem aceite explícito do PO. |
| **Problema** | Em sistemas multiagente, saídas técnicas ambíguas (`done` confundido com entregue/aceito), falta de evidência padronizada e ausência de trilha de decisão geram retrabalho, risco de falsa conclusão e baixa confiança dos stakeholders. |
| **Proposta de valor (MVP)** | (1) Contrato único de delegação/resumo para verificação; (2) estados canônicos separando execução técnica, conclusão operacional e aceite de valor; (3) fluxo mínimo de aceite/feedback do PO com evidência obrigatória; (4) visibilidade de lacunas, riscos e próxima ação. |
| **Resultado esperado** | Redução de ambiguidade decisória, aumento de auditabilidade e aceleração de ciclos de refinamento/aceite com critérios objetivos. |

**Personas/atores**

| Ator | Objetivo | Dor atual (hipótese) | Necessidade no MVP |
|---|---|---|---|
| **Operador** | Iniciar demandas e acompanhar progresso | Não sabe o estado real nem o que falta | Visão clara de status, evidências, bloqueios e próxima ação |
| **Orquestrador (dispatcher+agregador)** | Delegar, consolidar e rotear decisões | Risco de agregar respostas incompletas/ambíguas | Contrato mínimo obrigatório, validação de resumo e distinção semântica |
| **Subagentes especialistas** | Executar por domínio com autonomia definida | Critérios de “pronto” variam | Template de saída, regras de evidência/lacuna e limites de autonomia (A/B/C) |
| **Product Owner (PO)** | Maximizar valor e aceitar/rejeitar incrementos | Falta evidência e critérios formais para aceite | Critérios de aceite, pacote de evidências e decisão `pending/approved/rejected` rastreável |
| **Sponsor/Stakeholders** | Confiança no ROI e governança | Visibilidade limitada de valor entregue vs esforço | KPIs de fluxo/qualidade/valor e trilha de decisões |

### 2. Escopo MVP (MoSCoW e WSJF) e Backlog Inicial

**Premissas de estimativa WSJF:** escala relativa 1–13; Capacidade/timebox `[LACUNA]`. Ordenação por maior WSJF (desempate: maior Redução de Risco).

| ID | Iniciativa | MoSCoW | BV | TC | RR/OE | Tam. | WSJF | Justificativa de valor |
|---|---|---:|---:|---:|---:|---:|---:|---|
| M1 | Contrato canônico de resumo + validação de completude | **Must** | 13 | 13 | 13 | 5 | **7,8** | Base de rastreabilidade e verificação; sem isso não há agregação confiável |
| M2 | Semântica canônica de estados (execução vs operação vs valor/PO) | **Must** | 13 | 13 | 13 | 3 | **13,0** | Elimina ambiguidade central “execução concluída ≠ valor aceito” |
| M3 | Fluxo de aceite de valor do PO (Decision/Acceptance) com evidência | **Must** | 13 | 8 | 13 | 5 | **6,8** | Materializa entrega de valor e governança de aceite |
| S1 | Registro/auditoria ponta a ponta (trilha de decisões, artefatos, evidências) | **Should** | 8 | 8 | 8 | 5 | **4,8** | Aumenta auditabilidade e suporte a incidentes/revisões |
| S2 | Dashboard/visão consolidada de status, lacunas e riscos | **Should** | 8 | 5 | 8 | 5 | **4,2** | Melhora visibilidade para operador/stakeholders |
| C1 | Métricas automatizadas e alertas de conformidade (resumo/evidência) | **Could** | 5 | 5 | 5 | 5 | **3,0** | Otimiza operação após núcleo estabilizado |
| C2 | Catálogo de templates por domínio de subagente | **Could** | 5 | 3 | 5 | 3 | **4,3** | Acelera adoção; depende do contrato estável |
| W1 | Automação avançada de remediação/retry cross-agente | **Won't (MVP)** | 3 | 2 | 3 | 8 | **1,0** | Alto custo/complexidade; validar núcleo primeiro |

**Backlog inicial (épicos/histórias) — pronto para refinamento**

#### Épico E1 (Must, M1): Contrato canônico de resumo e verificação
| História | Descrição (INVEST) | Critérios de aceite (Given/When/Then) | DoR |
|---|---|---|---|
| H1.1 | Como **orquestrador**, quero receber de cada subagente um resumo no formato canônico para agregar resultados com consistência. | **Given** uma delegação concluída (ou interrompida), **When** o subagente responde, **Then** a resposta inclui “Resumo do Subagente” com todos os campos obrigatórios; **And** usa `[LACUNA]` quando faltar dado verificável. | Formato canônico acordado; campos obrigatórios definidos; consumidor (orquestrador) identificado. |
| H1.2 | Como **orquestrador**, quero validar regras do resumo (`done` exige evidência; `blocked/partial` exigem bloqueios e próxima ação) para rejeitar delegações inválidas. | **Given** um resumo recebido, **When** `status=done` sem evidência verificável, **Then** a delegação é marcada inválida e re-delegada 1×; **Given** `status=blocked|partial`, **When** faltarem bloqueios/riscos ou próxima ação, **Then** o resumo é inválido. | Regras R1–R7 disponíveis; comportamento de re-delegação definido; `[LACUNA]` de implementação registrado. |
| H1.3 | Como **operador**, quero ver decisão pendente explícita quando houver aceite externo para saber o que impede valor aceito. | **Given** execução técnica concluída que requer aceite do PO, **When** o resumo é emitido, **Then** `decisão pendente` indica “Aceite do PO” e `status` não implica `approved`. | Critério de pendência definido; papel do PO identificado. |

#### Épico E2 (Must, M2): Semântica canônica de estados
| História | Descrição (INVEST) | Critérios de aceite (Given/When/Then) | DoR |
|---|---|---|---|
| H2.1 | Como **time de operação/produto**, quero um vocabulário único de estados para evitar conclusões falsas. | **Given** qualquer artefato/status no fluxo, **When** for classificado, **Then** usa exclusivamente os estados canônicos definidos (execução, operação, valor/PO) e suas regras de transição conceituais. | Tabela de estados aprovada; donos por estado definidos. |
| H2.2 | Como **orquestrador**, quero impedir que `done` seja tratado como `approved` para preservar governança de valor. | **Given** um subagente com `status=done`, **When** o orquestrador agrega o resultado, **Then** o incremento permanece “valor pendente de aceite do PO” até decisão `approved` com evidência. | Regra de distinção documentada; ponto de verificação no fluxo `[LACUNA]`. |

#### Épico E3 (Must, M3): Aceite de valor pelo PO (Decision/Acceptance)
| História | Descrição (INVEST) | Critérios de aceite (Given/When/Then) | DoR |
|---|---|---|---|
| H3.1 | Como **PO**, quero avaliar incrementos com critérios de aceite e evidências para aprovar ou rejeitar valor. | **Given** um incremento com critérios de aceite e evidências anexadas, **When** o PO decide, **Then** registra `approved` somente com `evidence` e `decided_at`; **Or** `rejected` somente com `rationale` e `decided_at`. | Critérios de aceite definidos (Given/When/Then); evidência disponível ou `[LACUNA]` explícita. |
| H3.2 | Como **PO**, quero que uma rejeição retorne a pendência apenas com nova evidência para evitar ciclos sem informação. | **Given** uma decisão `rejected`, **When** não houver nova evidência, **Then** o estado não transita para `pending`; **When** houver nova evidência submetida, **Then** pode transitar `rejected → pending` para nova avaliação. | Regra de transição acordada; mecanismo de submissão de evidência `[LACUNA]`. |
| H3.3 | Como **stakeholder**, quero rastrear quem decidiu e por quê para auditoria de valor. | **Given** uma decisão de aceite, **When** consultada, **Then** exibe `decided_by=PO`, status, data e evidência/rationale conforme o caso. | Identidade do PO/decisor `[LACUNA]`; armazenamento de decisão `[LACUNA]`. |

#### Épico E4 (Should, S1): Rastreabilidade ponta a ponta
| História | Descrição (INVEST) | Critérios de aceite (Given/When/Then) | DoR |
|---|---|---|---|
| H4.1 | Como **operador/auditor**, quero uma trilha ligando demanda → delegações → resumos → decisão do PO para auditoria completa. | **Given** uma demanda processada, **When** inspeciono a trilha, **Then** consigo correlacionar IDs/artefatos/evidências/decisões em cada etapa ou ver `[LACUNA]` explícita onde indisponível. | Identificadores correlacionáveis definidos `[LACUNA]`; fonte de persistência `[LACUNA]`. |

### 3. Semântica Canônica de Estados (produto/contrato)

#### 3.1 Execução técnica (dono: subagente/agente) — campo `status` do Resumo do Subagente
| Estado | Significado | Regras obrigatórias |
|---|---|---|
| `done` | Execução técnica concluída dentro do escopo pedido. | Exige evidência verificável. **Não** implica `completed` nem `approved`. |
| `blocked` | Execução parada por impedimento/falha/lacuna crítica. | Exige `bloqueios/riscos` e `próxima ação recomendada` não vazios. |
| `partial` | Execução parcialmente concluída ou interrompida. | Exige `bloqueios/riscos`, `próxima ação recomendada` e lacunas explicitadas (`[LACUNA]` quando aplicável). |

#### 3.2 Conclusão operacional (dono: OPS/sistema de orquestração) — conceitual
| Estado | Significado | Relação |
|---|---|---|
| `completed` | Task/unidade marcada como concluída no sistema operacional de tracking (hoje `docs/` como trilha — DEC-006(vi)). | **Critério operacional proposto (`docs/48` §(iv)):** item executado (resumo `done` com evidência) + gates aplicáveis da fase atendidos + registro de conclusão no sistema operacional, com rastreio explícito ao(s) resumo(s)/evidência(s). **Não** implica `approved`. `[LACUNA]` critério exato no tracking alvo (sem board/tool; D-V0-05/D-V0-02). |

#### 3.3 Aceite de valor (dono: PO) — Decision/Acceptance v0
| Estado | Significado | Regras |
|---|---|---|
| `pending` | Aguardando avaliação/decisão do PO. | Estado inicial ou retorno de `rejected` **somente com nova evidência**. |
| `approved` | Valor aceito pelo PO. | **Terminal.** Exige `evidence`, `decided_by=PO`, `decided_at`. Não pode ser inferido de `done/completed`. |
| `rejected` | Valor não aceito pelo PO. | Exige `rationale`, `decided_by=PO`, `decided_at`. Transita para `pending` apenas com nova evidência. |

#### 3.4 Distinções e invariantes canônicos
- **Execução concluída ≠ Valor entregue/aceito:** `done` (técnico) indica término de execução no escopo; **valor aceito** só existe com `approved` do PO.
- **Cadeia lógica:** `done` → habilita avaliação; `completed` (operacional, se aplicável) → organiza fluxo; `approved` → confirma valor. Nenhuma seta implica a próxima automaticamente.
- **Evidência:** obrigatória para `done` e para `approved`; ausência ⇒ não declarar `done`/`approved` (usar `partial`/manter `pending` ou `rejected` conforme caso).
- **Lacunas:** sempre explícitas como `[LACUNA]`; nunca inferidas.
- **Alinhamento com `docs/48` §(iii)/(iv):** três camadas (execução ≠ operação ≠ valor), donos distintos, nenhuma transição automática; `approved` somente via PO com `evidence` + `decided_by` + `decided_at`; agente nunca escreve `approved`.

### 4. Métricas/KPIs de Sucesso do MVP e Mecanismo de Feedback/Aceite

| KPI | Definição | Meta F-ÚNICO-1 (gate binário, 1 semana) | Meta F-ÚNICO-2 (calibrada) | Fonte/Medição | Observação |
|---|---|---|---|---|---|
| **KPI-1 Conformidade de resumo** | % de delegações com “Resumo do Subagente” válido (campos + regras R1–R7) | ≥ 95% | ≥ 98% (sustentado em 2 iterações consecutivas) | Validador/orquestrador (`docs/schemas/contract-v1.0.0.schema.json`) | Baseline F-ÚNICO-1 = 65 testes verdes |
| **KPI-2 Clareza de evidência** | % de `done` com evidência verificável; % de `approved` com evidência | 100% (gate) | 100% (gate mantido; zero tolerância) | Auditoria de resumos/decisões | Gate de qualidade, não meta estatística |
| **KPI-3 Distinção de estados preservada** | Nº de ocorrências em que `done/completed` foi tratado como `approved` sem decisão do PO | 0 | 0 (zero tolerância mantida) | Revisão/auditoria | Métrica de risco/governança |
| **KPI-4 Lead time até decisão do PO** | Tempo (dias úteis) entre incremento “pronto para aceite” e decisão `pending→approved/rejected` | `[LACUNA]` (sem SLA — DEC-006(v)) | Meta proposta: ≤ 5 dias úteis (calibrar após 2 iterações) | Registro de decisões (`docs/DECISIONS.md`) + data de “pronto para aceite” no PR/handoff | Depende de capacidade do PO (sob demanda) |
| **KPI-5 Taxa de retrabalho pós-decisão** | % de `rejected` que retornam a `pending` e exigem nova execução | `[LACUNA]` (não mensurável em 1 semana) | Meta proposta: ≤ 20% (calibrar após ≥10 decisões) | Trilha de decisões (`docs/DECISIONS.md`) | Indica qualidade de critérios/evidência |
| **KPI-6 Visibilidade de lacunas** | % de respostas com incertezas marcadas como `[LACUNA]` quando aplicável | 100% esperado | 100% esperado (mantido) | Amostragem/auditoria | Proxy de confiabilidade |

**Metas de F-ÚNICO-2 (gates binários):** KPI-1, KPI-2, KPI-3, KPI-6 mantidos como gates binários. KPI-4 e KPI-5 passam de `[LACUNA]` para metas propostas a calibrar com dados reais (tracking manual em `docs/` — DEC-006(vi)). Detalhamento de AC Given/When/Then por épico (E1–E3), handoff PR→aceite PO e Decision/Acceptance v0: ver `docs/11-visao-mvp-v0.md` §"Aceite de Valor (PO)".

**Mecanismo de feedback/aceite (MVP)**
1. **Pronto para aceite:** subagente(s) entregam `status=done` com evidência verificável + critérios de aceite atendidos; orquestrador agrega e marca **“Valor pendente de aceite do PO”** (`decisão pendente: Aceite do PO`).
2. **Avaliação do PO:** valida critérios Given/When/Then e evidências; emite decisão Decision/Acceptance (`pending|approved|rejected`) com campos obrigatórios (v0).
3. **Feedback estruturado:** se `rejected`, registra `rationale` acionável (gap vs critério) e condição para nova submissão (nova evidência).
4. **Ciclo de aprendizado:** revisão periódica `[LACUNA]` (ex.: a cada iteração) de rejeições, lacunas recorrentes e conformidade de resumo para refinar DoR, critérios e backlog.
5. **Registro:** toda decisão e evidência vinculada a identificadores rastreáveis `[LACUNA]` (demanda/incremento/artefato).

### 5. Premissas, Lacunas, Riscos de Produto e Dependências (para PM/TL)

| Tipo | Item | Impacto | Ação/Responsável sugerido |
|---|---|---|---|
| **[LACUNA]** | Stack tecnológica e repositório-alvo do sistema | Alto — afeta viabilidade, integração e instrumentação de métricas | Validar com **TL/PM** antes do comprometimento de sprint |
| **[LACUNA]** | Stakeholders, sponsor e capacidade (incl. disponibilidade do PO) | Alto — afeta metas de lead time e cadência de aceite | Mapear com **PM**; definir RACI mínimo |
| **[LACUNA]** | Métricas atuais/baseline e ferramentas de medição/persistência | Médio/Alto — impede calibrar metas e auditar KPIs | Definir instrumentação mínima com **TL/PM** |
| **[LACUNA]** | Identificadores correlacionáveis e storage de trilha/evidências/decisões | Alto — limita rastreabilidade ponta a ponta (E4) | Desenho técnico e decisão de armazenamento com **TL** |
| **[LACUNA]** | Critério operacional exato de `completed` no board/OPS alvo | Médio — risco de desalinhamento semântico operação vs execução | Alinhar taxonomia com **PM/TL** |
| **Premissa** | Projeto reiniciado/limpo; sem baseline operacional reutilizável | Médio — estimativas e metas partem sem histórico | Tratar metas como hipóteses; revisar após 1–2 iterações |
| **Premissa** | Orquestrador não implementa; subagentes executam por domínio | Baixo (se respeitada) — define fronteiras de responsabilidade | Reforçar em contratos/prompts com **TL** |
| **Risco** | Confusão persistente entre `done`, `completed` e `approved` | Alto — falsa percepção de valor entregue | Gate de validação de resumo + comunicação explícita em toda agregação (**PO/TL**) |
| **Risco** | Aceite do PO virar gargalo (lead time alto) | Médio — reduz throughput de valor | Cadência **sob demanda, sem SLA formal** (DEC-006(v)); mantenedor único (DEC-006(iv)); definir pacote mínimo de evidência (**PM/PO**) |
| **Risco** | Evidências insuficientes ou não verificáveis | Alto — bloqueia `done/approved` e aumenta retrabalho | Padronizar tipos de evidência por história no refinamento (**PO/TL**) |
| **Risco** | Escopo crescer além do núcleo (M1–M3) no MVP | Médio — dilui foco e atrasa valor | Aplicar MoSCoW/WSJF estritos e change control (**PO/PM**) |
| **Dependência** | Implementação do validador de contrato no orquestrador/agregador | Alta | Planejamento e entrega técnica (**TL**) |
| **Dependência** | Mecanismo de registro/consulta de decisões do PO e evidências | Alta | Definição de fluxo e persistência (**PM/TL**) |
| **Dependência** | Disponibilidade do PO para critérios de aceite e decisões | Alta | Compromisso de capacidade/cadência (**PM/Sponsor**) |

## ⚠️ Premissas e Lacunas
- **[LACUNA] Stack e repositório-alvo:** não informados; inviável especificar integração técnica, armazenamento e instrumentação concreta. *Impacto:* alto no planejamento de PM/TL.
- **[LACUNA] Stakeholders/capacidade:** sponsor, operadores reais, disponibilidade do PO e tamanho do time desconhecidos. *Impacto:* alto em metas de lead time e viabilidade de cadence.
- **[LACUNA] Métricas atuais/baseline:** inexistentes no contexto; KPIs definidos como metas/gates iniciais hipotéticas. *Impacto:* médio/alto na calibração de sucesso.
- **[LACUNA] Infra de rastreabilidade:** IDs correlacionáveis, storage de evidências/decisões e critério operacional de `completed` não definidos. *Impacto:* alto para auditoria ponta a ponta.
- **[PREMISSA]** Cadência sob demanda, sem SLA formal (DEC-006(v)): substitui premissa de SLA/cadência quinzenal; mantenedor único (DEC-006(iv)); tracking = `docs/` (DEC-006(vi)).
- **[PREMISSA]** `docs/evidence/` rejeitado (DEC-005): evidências embutidas/por link nos canônicos; nenhum diretório paralelo de SoT.
- **[PREMISSA]** Reinício limpo: artefatos/estados anteriores são apenas lição, não baseline operacional.
- **[PREMISSA]** MVP prioriza núcleo de confiança (contrato + estados + aceite PO) sobre automações avançadas.

## ✅ Próximas Ações
1. **Validar contexto e restrições (stack, repo-alvo, stakeholders, capacidade, baseline)** — Dono: **PM + TL + PO** — Prazo: `[LACUNA]` (recomendado: antes do refinamento da Sprint 0/iteração 1).
2. **Refinar épicos E1–E3 em histórias prontas (DoR completo, estimativas, evidências por história)** — Dono: **PO (liderança) + TL** — Prazo: `[LACUNA]`.
3. **Definir desenho operacional/técnico do validador de resumo, trilha de rastreabilidade e registro de Decision/Acceptance** — Dono: **TL (com PM)** — Prazo: `[LACUNA]`.
4. **Calibrar metas de KPIs e cadência de aceite do PO (sob demanda, sem SLA formal — DEC-006(v)) com stakeholders** — Dono: **PO + PM** (mantenedor único — DEC-006(iv)) — Prazo: `[LACUNA]`.
5. **Planejar iteração MVP (M1–M3) e critérios de entrada/saída de aceite** — Dono: **PM + PO** — Prazo: `[LACUNA]`.
6. **PO decidir aceite de valor de E1–E3** (pacote §0.2; Decision/Acceptance `pending`) — registrar `approved`/`rejected` em `docs/DECISIONS.md` com `human_interaction_ref` — Dono: **PO** — Prazo: sob demanda (sem SLA — DEC-006(v)).

```json
{
  "decision_id": "01JZ9Y8N8Q4K7M2R6T5V8W3X1C",
  "papel": "gerente-produto",
  "classe_autonomia": "B",
  "decision_type": "priorizacao",
  "criterio": "WSJF|MoSCoW|INVEST|Given/When/Then",
  "status": "condicional",
  "evidencia": [
    "Reconciliação F-ÚNICO-0/MU-0.3 executada sobre docs/10 (este arquivo) — bloco aditivo §0, mapeamento M1–M3/E1–E4 → F-ÚNICO-0/1/2",
    "Normativos externos pinados: ~/.opencode/references/contrato-resumo-subagentes.md sha256 163e0aad7654d0a60930e90388afa9b9474ee727f119e94a62337d8321442a60; ~/.opencode/references/autonomia-e-estados.md sha256 776af494ee702cf4d3db8837f2b1c0c23450844f9b54e376a052d7adbc42c78a",
    "docs/47 (roadmap unificado) e docs/48 (contrato v1.0.0-PROPOSTA) lidos e referenciados; docs/DECISIONS.md (DEC-001..DEC-008) lido",
    "[LACUNA] Sem baseline/métricas atuais verificáveis; stack indefinida (D-V0-01 adiado)"
  ],
  "premissas_validadas": [
    "Projeto reiniciado/limpo; sem baseline operacional anterior",
    "Orquestrador atua como dispatcher+agregador",
    "Rastreabilidade e distinção execução≠valor são requisitos centrais",
    "Contrato mínimo de resumo de subagentes conforme referência informada",
    "DEC-006 (2026-11-16): D-V0-01 adiado; repo-alvo = este repo; CI nenhuma; mantenedor único; cadência sob demanda sem SLA; tracking = docs/",
    "DEC-005: docs/evidence/ rejeitado — evidências embutidas/por link",
    "Normativos externos pinados por caminho+sha256 completo (DEC-003)"
  ],
  "lacunas": [
    "D-V0-01 adiado (DEC-006(i)): stack/CI/repo-alvo indefinidos; LangGraph condicional; implementação não iniciada",
    "D-V0-03 pendente: aceite do PO sobre visão/MVP/estados/KPIs (valor, Classe C)",
    "D-V0-04 pendente: baseline técnica/ADRs iniciais e convenção/numeração (Classe C)",
    "D-V0-05 pendente: contrato canônico v1.0.0 (resumo/envelope/estados/correlação/schema_version) (Classe C)",
    "D-V0-06 pendente: política unificada de gates/evidência e thresholds (lidos do projeto-alvo)",
    "Cadência sob demanda, sem SLA formal (DEC-006(v)); mantenedor único (DEC-006(iv)); tracking = docs/ (DEC-006(vi))",
    "Critério operacional exato de 'completed' no tracking alvo (docs/ como trilha) — [LACUNA]",
    "Métricas atuais/baseline e ferramentas de medição",
    "Identificadores correlacionáveis e storage de trilha/evidências/decisões"
  ],
  "proximas_acoes": [
    {"acao": "Validar contexto e restrições (stack, repo-alvo, stakeholders, capacidade, baseline)", "dono": "PM + TL + PO"},
    {"acao": "Refinar épicos E1–E3 (DoR, estimativas, evidências por história)", "dono": "PO + TL"},
    {"acao": "Definir desenho técnico/operacional de validador, rastreabilidade e Decision/Acceptance", "dono": "TL + PM"},
    {"acao": "Calibrar metas de KPIs e cadência de aceite do PO (sob demanda, sem SLA — DEC-006(v))", "dono": "PO + PM"},
    {"acao": "Planejar iteração MVP (M1–M3) e critérios de aceite", "dono": "PM + PO"}
  ],
  "schema_version": "1.0"
}
```

## Resumo do Subagente
- objetivo: Produzir do zero a definição de produto/valor para um sistema SDLC agêntico robusto e eficiente (visão, escopo MVP priorizado, semântica de estados, KPIs e lacunas/dependências).
- ação executada: Consultei os contratos de referência disponíveis (`contrato-resumo-subagentes.md`, `autonomia-e-estados.md`); apliquei WSJF/MoSCoW/INVEST e Given/When/Then para definir visão, personas, proposta de valor, backlog inicial, semântica canônica de estados, KPIs/mecanismo de aceite e riscos/dependências; `[LACUNA]` skill específica `~/.agents/skills/product-owner/SKILL.md` indisponível no caminho informado (diretório inexistente).
- resultado/artefato: Resposta estruturada neste turno contendo decisão, artefatos de produto (visão/personas/MVP backlog MoSCoW+WSJF com histórias e critérios de aceite/DoR), semântica canônica de estados (execução/operação/valor), KPIs e mecanismo de feedback/aceite, premissas/lacunas/riscos/dependências e JSON machine-readable.
- evidência: [LACUNA] Sem evidências de repositório, baseline, métricas ou artefatos verificáveis externos; fundamentação baseada em `input_query`, `product_context` e contratos lidos em `~/.opencode/references/contrato-resumo-subagentes.md` e `~/.opencode/references/autonomia-e-estados.md`.
- status: partial
- bloqueios/riscos: [LACUNA] Skill `~/.agents/skills/product-owner/SKILL.md` não encontrada; stack/repositório-alvo, stakeholders/capacidade, métricas baseline e infraestrutura de rastreabilidade/armazenamento indefinidos — impedem validação completa e fechamento de metas/prazos.
- decisão pendente: Aceite do PO sobre visão, priorização MVP (M1–M3), semântica canônica de estados e metas iniciais de KPI; validação de premissas/lacunas com PM/TL/Sponsor.
- próxima ação recomendada: PM/TL/PO validarem lacunas de contexto e capacidade, refinarem E1–E3 com DoR/evidências e submeterem pacote para decisão de aceite do PO (com evidências verificáveis).
