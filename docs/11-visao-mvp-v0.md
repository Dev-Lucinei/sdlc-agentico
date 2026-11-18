---
title: "Visão/MVP (PO) — v0"
date: "2026-11-17"
project: "sdlc-agentico"
source: "gerente-produto"
status: "condicional"
---
> **Change Control:** materializado por aprovação Classe C (DEC-009/DEC-015, 2026-11-16). Conteúdo permanece `condicional`; isto NÃO declara `approved`/`completed` nem inicia implementação (F-ÚNICO-1 bloqueada por D-V0-01 adiado — DEC-006(i)). Modo documental (F-ÚNICO-0) em 1 semana.

**Classe de autonomia:** B/C — proposta de produto materializada (aceite de valor permanece Classe C e exclusivo do PO; nenhum `approved` declarado).

## Visão

Tornar o SDLC agêntico **previsível, auditável e orientado a valor**, onde cada execução técnica é rastreável ponta a ponta e nenhum resultado é tratado como valor entregue sem aceite explícito do PO.

## Problema

Em sistemas multiagente, saídas técnicas ambíguas (`done` confundido com entregue/aceito), falta de evidência padronizada e ausência de trilha de decisão geram retrabalho, risco de falsa conclusão e baixa confiança dos stakeholders.

## Proposta de valor (MVP)

1. Contrato único de delegação/resumo para verificação.
2. Estados canônicos separando execução técnica, conclusão operacional e aceite de valor.
3. Fluxo mínimo de aceite/feedback do PO com evidência obrigatória.
4. Visibilidade de lacunas, riscos e próxima ação.

**Resultado esperado:** redução de ambiguidade decisória, aumento de auditabilidade e aceleração de ciclos de refinamento/aceite com critérios objetivos.

## MVP MoSCoW + WSJF

Premissas de estimativa WSJF: escala relativa 1–13; capacidade/timebox `[LACUNA]`. Ordenação por maior WSJF (desempate: maior Redução de Risco). MoSCoW Must = exatamente 3 itens (sem exceção).

| ID | Iniciativa | MoSCoW | BV | TC | RR/OE | Tam. | WSJF | Justificativa |
|---|---|---|---:|---:|---:|---:|---:|---|
| M1 | Contrato canônico de resumo + validação de completude | **Must** | 13 | 13 | 13 | 5 | **7,8** | Base de rastreabilidade e verificação |
| M2 | Semântica canônica de estados (execução vs operação vs valor/PO) | **Must** | 13 | 13 | 13 | 3 | **13,0** | Elimina ambiguidade central |
| M3 | Fluxo de aceite de valor do PO (Decision/Acceptance) com evidência | **Must** | 13 | 8 | 13 | 5 | **6,8** | Materializa entrega de valor |
| S1 | Registro/auditoria ponta a ponta (trilha de decisões, artefatos, evidências) | **Should** | 8 | 8 | 8 | 5 | **4,8** | Aumenta auditabilidade |
| S2 | Dashboard/visão consolidada de status, lacunas e riscos | **Should** | 8 | 5 | 8 | 5 | **4,2** | Melhora visibilidade |
| C1 | Métricas automatizadas e alertas de conformidade (resumo/evidência) | **Could** | 5 | 5 | 5 | 5 | **3,0** | Otimiza operação após núcleo |
| C2 | Catálogo de templates por domínio de subagente | **Could** | 5 | 3 | 5 | 3 | **4,3** | Acelera adoção |
| W1 | Automação avançada de remediação/retry cross-agente | **Won't (MVP)** | 3 | 2 | 3 | 8 | **1,0** | Alto custo; validar núcleo primeiro |

## Backlog E1–E4

- **E1 (Must, M1)** — Contrato canônico de resumo e verificação: H1.1, H1.2, H1.3.
- **E2 (Must, M2)** — Semântica canônica de estados: H2.1, H2.2.
- **E3 (Must, M3)** — Aceite de valor pelo PO (Decision/Acceptance): H3.1, H3.2, H3.3.
- **E4 (Should, S1)** — Rastreabilidade ponta a ponta: H4.1. **Adiado para F-ÚNICO-2** (depende de IDs correlacionáveis — `[LACUNA]`).

Modo documental (F-ÚNICO-0) em 1 semana: E1+E2+E3 cabem como refinamento documental; E4 adiado.

## Semântica de estados (3 camadas)

### Execução técnica (dono: subagente/agente) — `status` do Resumo do Subagente
| Estado | Significado | Regras |
|---|---|---|
| `done` | Execução técnica concluída no escopo pedido. | Exige evidência verificável. Não implica `completed` nem `approved`. |
| `blocked` | Execução parada por impedimento/falha/lacuna crítica. | Exige `bloqueios/riscos` e `próxima ação recomendada` não vazios. |
| `partial` | Execução parcialmente concluída/interrompida. | Exige bloqueios, próxima ação e lacunas explícitas (`[LACUNA]`). |

### Conclusão operacional (dono: OPS/sistema de orquestração)
| Estado | Significado |
|---|---|
| `completed` | Task/unidade marcada como concluída no sistema operacional de tracking (hoje `docs/` — DEC-006(vi)). Critério operacional proposto: item executado (`done` com evidência) + gates aplicáveis da fase atendidos + registro de conclusão com rastreio explícito. Não implica `approved`. `[LACUNA]` critério exato no tracking alvo (sem board/tool; D-V0-05). |

### Aceite de valor (dono: PO) — Decision/Acceptance v0
| Estado | Significado | Regras |
|---|---|---|
| `pending` | Aguardando avaliação/decisão do PO. | Estado inicial ou retorno de `rejected` somente com nova evidência. |
| `approved` | Valor aceito pelo PO. | Terminal. Exige `evidence`, `decided_by=PO`, `decided_at`. Não pode ser inferido de `done/completed`. |
| `rejected` | Valor não aceito pelo PO. | Exige `rationale`, `decided_by=PO`, `decided_at`. Transita para `pending` apenas com nova evidência. |

**Invariantes:** `done` → habilita avaliação; `completed` → organiza fluxo; `approved` → confirma valor. Nenhuma seta implica a próxima automaticamente. `approved` somente via PO com evidência; agente nunca escreve `approved`.

## KPIs (calibrados para F-ÚNICO-2 — Evolução)

<!-- (tabela KPI — cabeçalho corrigido 2026-11-17: removido token espúrio) -->
| KPI | Definição | Meta F-ÚNICO-1 (gate binário, 1 semana) | Meta F-ÚNICO-2 (calibrada) | Instrumentação / Fonte | Observação |
|---|---|---|---|---|---|
| KPI-1 Conformidade de resumo | % de delegações com “Resumo do Subagente” válido (campos + regras R1–R7) | ≥ 95% | ≥ 98% (sustentado em 2 iterações consecutivas) | Validador de contrato (`docs/schemas/contract-v1.0.0.schema.json`) + auditoria manual de resumos | Gate de qualidade; baseline F-ÚNICO-1 = 65 testes verdes |
| KPI-2 Clareza de evidência | % de `done` com evidência verificável; % de `approved` com evidência | 100% (gate) | 100% (gate mantido; zero tolerância) | Auditoria de resumos/decisões (DECISIONS.md + docs/) | Gate de qualidade, não meta estatística |
| KPI-3 Distinção de estados preservada | Nº de ocorrências em que `done/completed` foi tratado como `approved` sem decisão do PO | 0 | 0 (zero tolerância mantida) | Revisão/auditoria de agregações | Métrica de risco/governança |
| KPI-4 Lead time até decisão do PO | Tempo (dias úteis) entre incremento “pronto para aceite” (evidência + critérios) e decisão `pending→approved/rejected` | `[LACUNA]` (sem SLA — DEC-006(v)) | Meta inicial proposta: ≤ 5 dias úteis (a calibrar após 2 iterações de F-ÚNICO-2; medir em dias) | Registro de decisões em `docs/DECISIONS.md` + data de “pronto para aceite” no PR/handoff | Depende de capacidade do PO (mantenedor único — DEC-006(iv)); cadência de aceite sob demanda, sem SLA formal (DEC-006(v)) |
| KPI-5 Taxa de retrabalho pós-decisão | % de `rejected` que retornam a `pending` e exigem nova execução | `[LACUNA]` (não mensurável em 1 semana) | Meta inicial proposta: ≤ 20% das decisões `rejected` retornam com nova evidência | Trilha de decisões em `docs/DECISIONS.md` (Decision/Acceptance v0) | Indica qualidade de critérios/evidência; calibrar após acúmulo de ≥10 decisões |
| KPI-6 Visibilidade de lacunas | % de respostas com incertezas marcadas como `[LACUNA]` quando aplicável (vs inferência silenciosa) | 100% esperado | 100% esperado (mantido) | Amostragem/auditoria de resumos | Proxy de confiabilidade |

**Metas de F-ÚNICO-2 (gates binários):** KPI-1, KPI-2, KPI-3, KPI-6 mantidos como gates binários. KPI-4 e KPI-5 passam de `[LACUNA]` para **metas propostas a calibrar** com dados reais de F-ÚNICO-1/F-ÚNICO-2 (tracking manual em `docs/` — DEC-006(vi)); revisão a cada iteração. Nenhuma meta de KPI-4/KPI-5 é declarada `approved` sem medição verificável (regra “sem evidência, não há done”).

## Aceite de Valor (PO) — critérios, handoff e Decision/Acceptance v0

### A. Decision/Acceptance v0 (semântica)
- Estados: `pending | approved | rejected`.
- `approved`: **terminal**. Exige `evidence`, `decided_by=PO`, `decided_at`. Não pode ser inferido de `done`/`completed`.
- `rejected`: exige `rationale`, `decided_by=PO`, `decided_at`.
- `rejected → pending` **somente** com nova evidência submetida.
- `decided_by` = PO (único aceitador no MVP); `decisão pendente` explícita quando houver aceite externo.

### B. Critérios de aceite (AC Given/When/Then) por épico — MVP E1–E3

#### Épico E1 (Must, M1): Contrato canônico de resumo e verificação
| História | AC (Given/When/Then) |
|---|---|
| H1.1 | **Given** uma delegação concluída (ou interrompida), **When** o subagente responde, **Then** a resposta inclui “Resumo do Subagente” com todos os campos obrigatórios; **And** usa `[LACUNA]` quando faltar dado verificável. |
| H1.2 | **Given** um resumo recebido, **When** `status=done` sem evidência verificável, **Then** a delegação é marcada inválida e re-delegada 1×; **Given** `status=blocked|partial`, **When** faltarem bloqueios/riscos ou próxima ação, **Then** o resumo é inválido. |
| H1.3 | **Given** execução técnica concluída que requer aceite do PO, **When** o resumo é emitido, **Then** `decisão pendente` indica “Aceite do PO” e `status` não implica `approved`. |

#### Épico E2 (Must, M2): Semântica canônica de estados
| História | AC (Given/When/Then) |
|---|---|
| H2.1 | **Given** qualquer artefato/status no fluxo, **When** for classificado, **Then** usa exclusivamente os estados canônicos (execução, operação, valor/PO) e suas regras de transição conceituais. |
| H2.2 | **Given** um subagente com `status=done`, **When** o orquestrador agrega o resultado, **Then** o incremento permanece “valor pendente de aceite do PO” até decisão `approved` com evidência. |

#### Épico E3 (Must, M3): Aceite de valor pelo PO (Decision/Acceptance)
| História | AC (Given/When/Then) |
|---|---|
| H3.1 | **Given** um incremento com critérios de aceite e evidências anexadas, **When** o PO decide, **Then** registra `approved` somente com `evidence` e `decided_at`; **Or** `rejected` somente com `rationale` e `decided_at`. |
| H3.2 | **Given** uma decisão `rejected`, **When** não houver nova evidência, **Then** o estado não transita para `pending`; **When** houver nova evidência submetida, **Then** pode transitar `rejected → pending` para nova avaliação. |
| H3.3 | **Given** uma decisão de aceite, **When** consultada, **Then** exibe `decided_by=PO`, status, data e evidência/rationale conforme o caso. |

### C. Handoff PR → aceite PO (fluxo F-ÚNICO-2)

Fluxo canônico (materializado; antes `[LACUNA]`):
1. **PR criado** — implementação/alteração concluída com `status=done` + evidência verificável; PR referencia o incremento/épico (E1–E3) e os AC Given/When/Then atendidos.
2. **Evidência anexada** — pacote mínimo de evidência no PR: (a) resumo do subagente válido (campos + regras R1–R7); (b) saída de gates (lint/typecheck/test/build/audit) verdes ou baseline “no new errors”; (c) referência a artefatos/commits; (d) lacunas explícitas (`[LACUNA]`) quando aplicável.
3. **PO revisa** — valida AC Given/When/Then e evidências; verifica distinção `done ≠ approved`; checa KPIs relevantes (KPI-1/2/3/6 gates binários).
4. **Decisão** — PO registra `approved` (com `evidence` + `decided_by=PO` + `decided_at`) **ou** `rejected` (com `rationale` + `decided_by=PO` + `decided_at`); `rejected → pending` somente com nova evidência.
5. **Feedback estruturado** — se `rejected`, `rationale` acionável (gap vs critério) + condição para nova submissão (nova evidência); registro em `docs/DECISIONS.md` (DEC-*) e no PR.

**SLA de decisão:** sob demanda, sem SLA formal (DEC-006(v)); mantenedor único (DEC-006(iv)); cadência de aceite sob demanda. Meta de lead time (KPI-4) proposta ≤ 5 dias úteis, a calibrar após 2 iterações de F-ÚNICO-2.

**Identidade do decisor:** `decided_by = PO` (único aceitador no MVP); `human_interaction_ref` obrigatório quando a decisão for tomada por interação humana (Classe C). A transição `pending → approved` exige evidência verificável — nunca “ok”.

### D. Mecanismo de feedback/aceite (MVP) — 5 passos
1. **Pronto para aceite:** subagente(s) entregam `status=done` com evidência verificável + critérios de aceite atendidos; orquestrador agrega e marca “Valor pendente de aceite do PO” (`decisão pendente: Aceite do PO`).
2. **Avaliação do PO:** valida critérios Given/When/Then e evidências; emite decisão Decision/Acceptance (`pending|approved|rejected`) com campos obrigatórios (v0).
3. **Feedback estruturado:** se `rejected`, registra `rationale` acionável (gap vs critério) e condição para nova submissão (nova evidência).
4. **Ciclo de aprendizado:** revisão periódica de rejeições, lacunas recorrentes e conformidade de resumo para refinar DoR, critérios e backlog.
5. **Registro:** toda decisão e evidência vinculada a identificadores rastreáveis (demanda/incremento/artefato) em `docs/DECISIONS.md` e no PR.

**Lacunas remanescentes (honestas):** identificadores correlacionáveis e storage de trilha/evidências/decisões (E4) permanecem `[LACUNA]` — adiado para F-ÚNICO-2; critério operacional exato de `completed` no tracking alvo (`docs/` como trilha, sem board/tool) segue `[LACUNA]` (D-V0-05).>

## Mecanismo de feedback/aceite (5 passos)

1. **Pronto para aceite:** subagente(s) entregam `status=done` com evidência verificável + critérios de aceite atendidos; orquestrador agrega e marca “Valor pendente de aceite do PO” (`decisão pendente: Aceite do PO`).
2. **Avaliação do PO:** valida critérios Given/When/Then e evidências; emite decisão Decision/Acceptance (`pending|approved|rejected`) com campos obrigatórios (v0).
3. **Feedback estruturado:** se `rejected`, registra `rationale` acionável (gap vs critério) e condição para nova submissão (nova evidência).
4. **Ciclo de aprendizado:** revisão periódica `[LACUNA]` (ex.: a cada iteração) de rejeições, lacunas recorrentes e conformidade de resumo para refinar DoR, critérios e backlog.
5. **Registro:** toda decisão e evidência vinculada a identificadores rastreáveis `[LACUNA]` (demanda/incremento/artefato).

## Incrementos MVP implementados (E1–E3) — referências (2026-11-17)

Implementação concluída tecnicamente (F-ÚNICO-1 concluída, DEC-024); aceite de valor **pendente** do PO (execução ≠ valor; `docs/10` §0.2 — pacote de evidência; DEC-028). Medição 2026-11-17: **65 testes verdes · cobertura 75,00% (≥50%) · `make audit` verde**. Drift registrado: painel/DEC-024 citam 74,84% (medição anterior).

| Incremento | Artefatos | Evidência | AC | Status |
|---|---|---|---|---|
| **E1** Contrato canônico v1.0.0 + validador JSON Schema | `src/contract_validator.py`, `src/exit_codes.py`, `docs/schemas/contract-v1.0.0.schema.json` | `tests/test_contract_validator.py`, `tests/test_validate_contract.py`; commits `e54c083`, `c6b2567`, `f6d74f6`; DEC-021 | H1.1–H1.3 (§B) | `done`; nunca `approved` |
| **E2** Máquina de estados (done ⇏ completed ⇏ approved) + transições validadas | `src/state.py` | `tests/test_state_transitions.py`; commit `f6d74f6`; ADR-005 `accepted` (DEC-020) | H2.1–H2.2 (§B) | `done`; nunca `approved` |
| **E3** Persistência SQLite (SoT + Event Log append-only) | `src/persistence.py` | `tests/test_persistence.py`; commit `f6d74f6`; DEC-024 | H3.1–H3.3 (§B) | `done`; nunca `approved` |

Status do aceite de valor: **`pending`** (Decision/Acceptance v0 — `decision_id` `01M7P3NFTDNKR760KBBBHE8PSV`, `decided_by`=PO explícito pendente, `human_interaction_ref` a preencher no ato). Nenhum incremento declarado `approved`.

## Lacunas persistentes

- ~~`[LACUNA]` D-V0-01 adiado~~ — **RESOLVIDO** (DEC-018, 2026-11-17): stack mínima Python 3.12 + pytest + ruff + mypy; F-ÚNICO-1 concluída.
- ~~`[LACUNA]` Capacidade real por dia (117% — sobrecarga)~~ — **ATUALIZADO** (DEC-027, 2026-11-17): capacidade estimada **~4–8h/sem** ([PREMISSA-P10], pendente confirmação do Mantenedor); divergência com DEC-014 [PREMISSA-P7] (40h/sem) registrada, não silenciada.
- ~~`[LACUNA]` DEC-007 (política de segredos) permanece aberta~~ — **FECHADA** (DEC-023, 2026-11-17): segredos via `os.environ`, nunca hardcode; mascaramento em logs; `src/secrets.py`.
- D-V0-03 APROVADO E MATERIALIZADO (DEC-019, 2026-11-17): visão/MVP/estados/KPIs materializados; `approved` de valor permanece pendente de aceite explícito do PO (execução ≠ valor).
- D-V0-04 APROVADO E MATERIALIZADO (DEC-020, 2026-11-17): ADR-001…ADR-008 promovidos para `accepted`.
- D-V0-05 APROVADO E MATERIALIZADO (DEC-021, 2026-11-17): contrato v1.0.0 adotado.
- D-V0-06 APROVADO E MATERIALIZADO (DEC-022, 2026-11-17): política de gates/thresholds; thresholds absolutos cobertura ≥50%, 0 erros críticos.
- ~~[LACUNA] Handoff PR→aceite PO inexistente; AC Given/When/Then ausentes nos designs t1–t5~~ — **MATERIALIZADO** (DEC-026, 2026-11-17): AC E1–E3 completos neste arquivo §B; handoff PR→aceite PO §C. KPIs KPI-4/KPI-5 passaram de `[LACUNA]` a metas propostas a calibrar (DEC-026). Aceite formal (`pending→approved`) segue **pendente do PO** (DEC-028).
- `[LACUNA]` Identificadores correlacionáveis e storage de trilha/evidências/decisões (E4 adiado).
- `[LACUNA]` Critério operacional exato de `completed` no tracking alvo (`docs/` como trilha, sem board/tool).

## Premissas

- **P1:** MVP M1–M3 entregue em 1 semana com 40h/sem — teste: escopo documental (F-ÚNICO-0) cabe em 5d×8h com buffer 30% (~30h úteis); F-ÚNICO-1 bloqueada por D-V0-01 (R8) — não prometer código.
- **P2:** KPIs mensuráveis sem infra externa (`docs/`) — teste: KPI-1/2/3/6 auditáveis manualmente em 1 semana; KPI-4/5 `[LACUNA]`.
- P1, P7, P8 (2026-11-16) — **histórico**: P1 (referia-se a F-ÚNICO-1 bloqueada por D-V0-01 — hoje RESOLVIDO por DEC-018); P7 (40h/sem — diverge de DEC-027 [PREMISSA-P10], ~4–8h/sem; ambas registradas, divergência não silenciada); P8 (revisão RACI semanal — mantida). Ver DEC-018/DEC-027.
- **P7 (DEC-014):** orçamento monetário = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada.
- **P8 (DEC-014):** cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A).

## Riscos

R1 (ambiguidade contratual), R2 (rastreabilidade), R4 (capacidade), R7 (gargalo de aceite PO), R8 (D-V0-01 — **mitigado** por DEC-018), R10 (bus factor 1), R11 (drift documental), R12 (MVP de 1 semana inviável — **mitigado** por DEC-018; F-ÚNICO-1 concluída). Mitigações ativas conforme DEC-014/DEC-016/DEC-018/DEC-027.

### Conflitos registrados (não resolvidos silenciosamente)
- DIV-1 (roadmap PM F0–F2 × TL F0–F5 × PO M1–M3) — mapa em `docs/47` §1; em andamento.
- DIV-2 (`schema_version 0.1.0-draft` × v1.0.0) — proposta em `docs/48`; em andamento.
- Divergência revisão PO: KPIs não instrumentáveis / AC ausentes nos designs — registrada como `[LACUNA]`, não resolvida.
