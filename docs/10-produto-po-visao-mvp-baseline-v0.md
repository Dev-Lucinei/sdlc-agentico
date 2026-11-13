---
title: "Produto (PO) — Visão, MVP e Baseline v0"
date: "2026-11-13"
project: "sdlc-agentico"
source: "gerente-produto (sessão ses_e292deeacffeDISULhsnAjsxBi, status partial/condicional, classe B)"
status: "partial/condicional"
---

**Classe de autonomia:** B (definição de produto/backlog reversível, documentada; aceite de valor permanece Classe C e exclusivo do PO)

## 🎯 Decisão / Conclusão
Definir o MVP do **sistema SDLC agêntico** como um núcleo de **orquestração rastreável** (dispatcher+agregador) com **contrato canônico de resumo**, **semântica explícita de estados** e **mecanismo de aceite de valor pelo PO**. Priorização por **WSJF** (Valor de Negócio + Criticidade de Tempo + Redução de Risco/Oportunidade ÷ Tamanho) e escopo por **MoSCoW** (Must = 3 itens nucleares, sem exceção), dado que rastreabilidade e distinção execução≠valor são requisitos centrais e mitigam risco operacional/decisório.

## 🗂️ Artefato

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
| `completed` | Task/unidade marcada como concluída no board/sistema operacional. | Pode decorrer de execução `done`, mas **não** implica `approved`. Requer rastreabilidade ao(s) resumo(s)/evidência(s). `[LACUNA]` critério operacional exato no repositório-alvo. |

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

### 4. Métricas/KPIs de Sucesso do MVP e Mecanismo de Feedback/Aceite

| KPI | Definição | Meta inicial (MVP) | Fonte/Medição | Observação |
|---|---|---|---|---|
| **Conformidade de resumo** | % de delegações com “Resumo do Subagente” válido (campos + regras R1–R7) | ≥ 95% | Validador/orquestrador `[LACUNA]` | Baseline atual `[LACUNA]` |
| **Clareza de evidência** | % de `done` com evidência verificável; % de `approved` com evidência | 100% (gate) | Auditoria de resumos/decisões `[LACUNA]` | Gate de qualidade, não meta estatística |
| **Distinção de estados preservada** | Nº de ocorrências em que `done/completed` foi tratado como `approved` sem decisão do PO | 0 | Revisão/auditoria `[LACUNA]` | Métrica de risco/governança |
| **Lead time até decisão do PO** | Tempo entre incremento “pronto para aceite” (evidência + critérios) e decisão `pending→approved/rejected` | `[LACUNA]` (definir com stakeholders) | Registro de decisões `[LACUNA]` | Depende de capacidade do PO |
| **Taxa de retrabalho pós-decisão** | % de `rejected` que retornam a `pending` e exigem nova execução | Tendência decrescente `[LACUNA]` | Trilha de decisões `[LACUNA]` | Indica qualidade de critérios/evidência |
| **Visibilidade de lacunas** | % de respostas com incertezas marcadas como `[LACUNA]` quando aplicável (vs inferência silenciosa) | 100% esperado em casos aplicáveis | Amostragem/auditoria `[LACUNA]` | Proxy de confiabilidade |

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
| **Risco** | Aceite do PO virar gargalo (lead time alto) | Médio — reduz throughput de valor | Definir SLA/cadência de aceite e pacote mínimo de evidência (**PM/PO**) |
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
- **[PREMISSA]** Reinício limpo: artefatos/estados anteriores são apenas lição, não baseline operacional.
- **[PREMISSA]** MVP prioriza núcleo de confiança (contrato + estados + aceite PO) sobre automações avançadas.

## ✅ Próximas Ações
1. **Validar contexto e restrições (stack, repo-alvo, stakeholders, capacidade, baseline)** — Dono: **PM + TL + PO** — Prazo: `[LACUNA]` (recomendado: antes do refinamento da Sprint 0/iteração 1).
2. **Refinar épicos E1–E3 em histórias prontas (DoR completo, estimativas, evidências por história)** — Dono: **PO (liderança) + TL** — Prazo: `[LACUNA]`.
3. **Definir desenho operacional/técnico do validador de resumo, trilha de rastreabilidade e registro de Decision/Acceptance** — Dono: **TL (com PM)** — Prazo: `[LACUNA]`.
4. **Calibrar metas de KPIs e cadência/SLA de aceite do PO com stakeholders** — Dono: **PO + PM + Sponsor** — Prazo: `[LACUNA]`.
5. **Planejar iteração MVP (M1–M3) e critérios de entrada/saída de aceite** — Dono: **PM + PO** — Prazo: `[LACUNA]`.

```json
{
  "decision_id": "01JZ9Y8N8Q4K7M2R6T5V8W3X1C",
  "papel": "gerente-produto",
  "classe_autonomia": "B",
  "decision_type": "priorizacao",
  "criterio": "WSJF|MoSCoW|INVEST|Given/When/Then",
  "status": "condicional",
  "evidencia": [
    "[LACUNA] Sem artefatos, baseline ou métricas atuais verificáveis no contexto; decisão baseada em input_query/product_context fornecidos"
  ],
  "premissas_validadas": [
    "Projeto reiniciado/limpo; sem baseline operacional anterior",
    "Orquestrador atua como dispatcher+agregador",
    "Rastreabilidade e distinção execução≠valor são requisitos centrais",
    "Contrato mínimo de resumo de subagentes conforme referência informada"
  ],
  "lacunas": [
    "Stack tecnológica e repositório-alvo",
    "Stakeholders, sponsor e capacidade (incl. disponibilidade do PO)",
    "Métricas atuais/baseline e ferramentas de medição",
    "Identificadores correlacionáveis e storage de trilha/evidências/decisões",
    "Critério operacional exato de 'completed' no sistema alvo"
  ],
  "proximas_acoes": [
    {"acao": "Validar contexto e restrições (stack, repo-alvo, stakeholders, capacidade, baseline)", "dono": "PM + TL + PO"},
    {"acao": "Refinar épicos E1–E3 (DoR, estimativas, evidências por história)", "dono": "PO + TL"},
    {"acao": "Definir desenho técnico/operacional de validador, rastreabilidade e Decision/Acceptance", "dono": "TL + PM"},
    {"acao": "Calibrar metas de KPIs e cadência/SLA de aceite do PO", "dono": "PO + PM + Sponsor"},
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
