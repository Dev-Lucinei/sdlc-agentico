---
title: "Visão/MVP (PO) — v0"
date: "2026-11-16"
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

## KPIs

| KPI | Definição | Meta inicial (MVP) | Observação |
|---|---|---|---|
| KPI-1 Conformidade de resumo | % de delegações com “Resumo do Subagente” válido (campos + regras R1–R7) | ≥ 95% | Gate binário em 1 semana (auditoria manual) |
| KPI-2 Clareza de evidência | % de `done` com evidência verificável; % de `approved` com evidência | 100% (gate) | Gate binário em 1 semana |
| KPI-3 Distinção de estados preservada | Nº de ocorrências em que `done/completed` foi tratado como `approved` sem decisão do PO | 0 | Gate binário em 1 semana |
| KPI-4 Lead time até decisão do PO | Tempo entre incremento “pronto para aceite” e decisão `pending→approved/rejected` | `[LACUNA]` (sem SLA — DEC-006(v)) | Parcialmente mensurável; calibrar após 2 iterações |
| KPI-5 Taxa de retrabalho pós-decisão | % de `rejected` que retornam a `pending` e exigem nova execução | Tendência decrescente `[LACUNA]` | NÃO mensurável em 1 semana; adiado para F-ÚNICO-2 |
| KPI-6 Visibilidade de lacunas | % de respostas com incertezas marcadas como `[LACUNA]` quando aplicável | 100% esperado | Gate binário em 1 semana |

Metas de 1 semana (gates binários): KPI-1, KPI-2, KPI-3, KPI-6. KPI-4 e KPI-5 permanecem `[LACUNA]` com tracking manual.

## Aceite de valor (Decision/Acceptance v0)

- `pending|approved|rejected`.
- `approved` terminal: exige `evidence`, `decided_by=PO`, `decided_at`.
- `rejected`: exige `rationale`, `decided_by=PO`, `decided_at`.
- `rejected → pending` somente com nova evidência.
- Handoff PR→aceite PO inexistente: registrado como `[LACUNA]` a materializar em F-ÚNICO-1 (não bloqueia a proposta).

## Mecanismo de feedback/aceite (5 passos)

1. **Pronto para aceite:** subagente(s) entregam `status=done` com evidência verificável + critérios de aceite atendidos; orquestrador agrega e marca “Valor pendente de aceite do PO” (`decisão pendente: Aceite do PO`).
2. **Avaliação do PO:** valida critérios Given/When/Then e evidências; emite decisão Decision/Acceptance (`pending|approved|rejected`) com campos obrigatórios (v0).
3. **Feedback estruturado:** se `rejected`, registra `rationale` acionável (gap vs critério) e condição para nova submissão (nova evidência).
4. **Ciclo de aprendizado:** revisão periódica `[LACUNA]` (ex.: a cada iteração) de rejeições, lacunas recorrentes e conformidade de resumo para refinar DoR, critérios e backlog.
5. **Registro:** toda decisão e evidência vinculada a identificadores rastreáveis `[LACUNA]` (demanda/incremento/artefato).

## Lacunas persistentes

- `[LACUNA]` D-V0-01 adiado (DEC-006(i)): stack/CI/repo-alvo indefinidos ⇒ F-ÚNICO-1 bloqueada; MVP de 1 semana = modo documental (F-ÚNICO-0).
- D-V0-03 APROVADO E MATERIALIZADO (DEC-019, 2026-11-17): visão/MVP/estados/KPIs materializados; `approved` de valor permanece pendente de aceite explícito do PO (execução ≠ valor).
- D-V0-04 APROVADO E MATERIALIZADO (DEC-020, 2026-11-17): ADR-001…ADR-008 promovidos para `accepted`.
- D-V0-05 APROVADO E MATERIALIZADO (DEC-021, 2026-11-17): contrato v1.0.0 adotado.
- D-V0-06 APROVADO E MATERIALIZADO (DEC-022, 2026-11-17): política de gates/thresholds; thresholds absolutos cobertura ≥50%, 0 erros críticos.
- `[LACUNA]` Handoff PR→aceite PO inexistente (revisão PO); AC Given/When/Then ausentes nos designs t1–t5.
- `[LACUNA]` KPIs não instrumentáveis (revisão PO); métricas baseline inexistentes.
- `[LACUNA]` Identificadores correlacionáveis e storage de trilha/evidências/decisões (E4 adiado).
- `[LACUNA]` Critério operacional exato de `completed` no tracking alvo (`docs/` como trilha, sem board/tool).
- `[LACUNA]` Capacidade real por dia (total estimado 117% da capacidade — sobrecarga; re-planejar).
- `[LACUNA]` DEC-007 (política de segredos) permanece aberta.

## Premissas

- **P1:** MVP M1–M3 entregue em 1 semana com 40h/sem — teste: escopo documental (F-ÚNICO-0) cabe em 5d×8h com buffer 30% (~30h úteis); F-ÚNICO-1 bloqueada por D-V0-01 (R8) — não prometer código.
- **P2:** KPIs mensuráveis sem infra externa (`docs/`) — teste: KPI-1/2/3/6 auditáveis manualmente em 1 semana; KPI-4/5 `[LACUNA]`.
- **P7 (DEC-014):** orçamento monetário = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada.
- **P8 (DEC-014):** cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A).

## Riscos

R1 (ambiguidade contratual), R2 (rastreabilidade), R4 (capacidade), R7 (gargalo de aceite PO), R8 (D-V0-01 adiado ⇒ F-ÚNICO-1 bloqueada), R10 (bus factor 1), R11 (drift documental), R12 (MVP de 1 semana inviável sem kickoff D-V0-01 — Crítico). Mitigações ativas conforme DEC-014/DEC-016.

### Conflitos registrados (não resolvidos silenciosamente)
- DIV-1 (roadmap PM F0–F2 × TL F0–F5 × PO M1–M3) — mapa em `docs/47` §1; em andamento.
- DIV-2 (`schema_version 0.1.0-draft` × v1.0.0) — proposta em `docs/48`; em andamento.
- Divergência revisão PO: KPIs não instrumentáveis / AC ausentes nos designs — registrada como `[LACUNA]`, não resolvida.
