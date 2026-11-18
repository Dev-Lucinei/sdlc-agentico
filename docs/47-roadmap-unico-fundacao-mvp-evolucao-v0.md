---
title: "Roadmap Unificado — Fundação → MVP → Evolução (v0, proposta)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead (subagente; classe B; proposta documental condicional; D-V0-01/03/04/05/06 pendentes)"
status: "condicional"
---

**Classe de autonomia declarada:** B (artefato documental reversível; nenhuma ação Classe C executada; nenhum `approved` declarado; nenhuma baseline promovida).

> **Aviso obrigatório:** este roadmap é **proposta condicional**, exigindo validação do **Mantenedor humano** (Lucinei; mantenedor único). Este documento apenas **registra o mapa de correspondência**; a reconciliação textual dos canônicos antigos (`docs/10-*`, `docs/20-*`, `docs/30-*`) fica pendente de D-V0-05/D-V0-06 — e da publicação do baseline sob DEC-008 (`docs/DECISIONS.md`, bloqueada por D-V0-03/04/05/06). Nenhuma fase além de F-ÚNICO-0 é executável hoje.
>
> **Sincronia com o log canônico de decisões:** as decisões do Mantenedor de 2026-11-16 estão vigentes em `docs/DECISIONS.md` (DEC-001…DEC-008) e na ata `docs/46-ata-kickoff-d-v0-01-02-v0.md`. Este roadmap **não** cria, altera nem promove decisões desse log; em caso de divergência entre este documento e o log/ata, **o log e a ata prevalecem** e a divergência deve ser registrada como `[LACUNA]`/DIV neste arquivo.

## 🔧 Decisão / Conclusão

Fica proposta a **fusão dos 3 roadmaps divergentes** hoje registrados em `docs/10-*` (M1–M3/E1–E4, trilha PO), `docs/20-*` (F0–F2/I1–I2, trilha PM) e `docs/30-*` (F0–F5, trilha TL) em uma **única trilha linear de 3 fases** — **F-ÚNICO-0 Fundação → F-ÚNICO-1 MVP Controlado → F-ÚNICO-2 Evolução** — com marcos, critérios de entrada/saída (DoR/DoD) e riscos compartilhados. **Trade-off assumido:** linearidade e rastreabilidade entre trilhas em detrimento da granularidade original de cada plano (os planos antigos permanecem válidos como histórico, não como fonte de verdade). **Decisão estrutural condicionada ao Mantenedor:** a decisão de 2026-11-16 **adiou D-V0-01** (stack indefinida; LangGraph condicional; implementação não iniciada; repo-alvo = este repo; CI nenhuma por ora; cadência sob demanda sem SLA; `docs/` como trilha de tracking; LICENSE nenhuma por ora; `docs/evidence/` rejeitado) — registrada como **DEC-006** em `docs/DECISIONS.md` (Classe C, decided_by Lucinei, 2026-11-16) e na ata `docs/46-ata-kickoff-d-v0-01-02-v0.md`. Consequência direta: **F-ÚNICO-1 está bloqueada** (risco **R8** de `docs/20-*`); **F-ÚNICO-0 é a única fase executável hoje** (baixo risco, documental); qualquer avanço além dela exige D-V0-03/04/05/06 decididas e registradas no log. Estimativas PERT+30% **não são declaradas** — capacidade é Mantenedor único (DEC-006(iv)) e comprometimento sob demanda sem SLA (DEC-006(v)); estimar dias-homem sem capacidade seria inventar número.

## 🗂️ Artefato

### 1) Mapa de correspondência (trilhas antigas → trilha única)

| Trilha única | PO (`docs/10-*`) | PM (`docs/20-*`) | TL (`docs/30-*`) | Design (`docs/41`–`45`) |
|---|---|---|---|---|
| **F-ÚNICO-0 — Fundação** (documental + contratual + decisões) | Pré-condição de M1–M3 (visão/MVP/estados/KPIs como insumo; nenhum aceite) | F0 — Fundação Contratual & Governança (M0.1–M0.3; I1–I2) | F0 — Alinhamento & baseline; F1 — Contratos & modelo de dados (parcial: validação documental) | Canônicos 41–45 como *insumo documental* de F-ÚNICO-1; revisão cruzada |
| **F-ÚNICO-1 — MVP Controlado** (contratos + fluxo mínimo rastreável + gates G0→G1) | M1 (contrato canônico de resumo), M2 (semântica de estados), M3 (aceite de valor PO); épicos E1 (H1.1–H1.3), E2 (H2.1–H2.2), E3 (H3.1–H3.3); E4/H4.1 como Should | F1 — MVP Controlado (M1.1–M1.3) | F1 — Contratos & modelo de dados; F2 — Núcleo dispatcher+agregação (MVP); gates G0→G1 | Consumo de 41–45 como spec de design (não como implementação aprovada) |
| **F-ÚNICO-2 — Evolução** (piloto, endurecimento G2→G3, evolução) | E2–E4 completos; S1/S2/C1/C2 conforme WSJF; KPIs calibrados | F2 — Evolução & Escala (M2.1–M2.2) | F3 — Gates/observabilidade/segurança; F4 — Piloto multi-papel & endurecimento; F5 — Evolução contínua; gates G2→G3 | Revisão/evolução de 41–45 conforme decisões D-V0-01/06 |

**Leitura:** cada fase F-ÚNICO-* *agrega* (não substitui retroativamente) as correspondentes fases antigas. Os textos dos canônicos antigos **não são editados por este documento**; a reconciliação formal fica pendente de D-V0-05 (contrato único) e D-V0-06 (política única de gates).

### 2) Fases da trilha única

#### F-ÚNICO-0 — Fundação (documental + contratual + decisões)

| Elemento | Definição |
|---|---|
| **Objetivo** | Consolidar baseline documental canônico, contratos propostos e decisões pendentes **antes** de qualquer implementação; reduzir ambiguidade contratual (R1) e de rastreabilidade (R2). |
| **Escopo** | (i) Reconciliação documental dos canônicos 00–45 (mapa de divergências; sem editar canônicos antigos por este artefato); (ii) proposta de Contrato Canônico v1.0.0 (ver `docs/48-contrato-canonico-v1-0-0-proposta-v0.md`); (iii) registro formal das decisões pendentes D-V0-03/04/05/06 como pauta de Classe C para o Mantenedor; (iv) índice/registro de ADRs como convenção proposta (numeração **não atribuída**; ADR-016/017 já existem no namespace `~/.agents/adr/core/`; ADR nº 018 existe em árvore externa — numeração reconciliada na Fase B, fora deste repo de ação). |
| **Marcos** | **MU-0.1** Mapa de divergências registrado (este documento + `docs/48`); **MU-0.2** Decisões D-V0-03/04/05/06 despachadas pelo Mantenedor (registro em `docs/DECISIONS.md` como DEC-009+; D-V0-01/02 já decididas por DEC-006); **MU-0.3** Baseline documental v0 reconciliado (ou gaps formalmente registrados); publicação só sob **DEC-008** (bloqueada por D-V0-03/04/05/06). |
| **Dependências** | Nenhuma técnica (documental). Decisão humana do Mantenedor para Classe C. **Não depende de D-V0-01.** |
| **DoR (entrada)** | Canônicos 00–45 lidos e íntegros; Mantenedor disponível para decisão (cadência sob demanda); escopo F-ÚNICO-0 aceito como documental/Classe B. |
| **DoD (saída)** | Mapa de divergências publicado; contrato v1.0.0-PROPOSTA publicado; CRs/decisões pendentes registrados e despachados; riscos R1/R2/R6 atualizados com dono; **nenhuma** promoção a `approved`/`completed`. |
| **Riscos associados** | R1 (ambiguidade contratual — mitiga por `docs/48`), R2 (rastreabilidade — mitiga por mapa único), R5 (change control — CRs devem referenciar `docs/DECISIONS.md`; ver R9), R6 (dependência externa: D-V0-01 **resolvido** por DEC-018 — gatilho atendido), R7 (desalinhamento de aceite — sem aceite nesta fase), **R8** (D-V0-01 adiado ⇒ F-ÚNICO-1 bloqueada — **MITIGADO** por DEC-018, 2026-11-17), **R9** (drift `DECISIONS.md` × change control `docs/20-*` §5), **R10** (bus factor = 1; mantenedor único), **R11** (drift `47`/`48` × `10/20/30` enquanto não reconciliados). |
| **Estimativa PERT+30%** | **[LACUNA]** — não estimável sem capacidade confirmada (D-V0-02). Não inventar dias-homem. Referência histórica (não vigente): plano I1–I2 de `docs/20-*` §6. |
| **Executável hoje?** | **SIM** — única fase executável (baixo risco, Classe B, reversível). |

#### F-ÚNICO-1 — MVP Controlado (contratos + fluxo mínimo rastreável + gates G0→G1)

| Elemento | Definição |
|---|---|
| **Objetivo** | Entregar o núcleo mínimo verificável: contrato canônico validado, semântica de estados aplicada, fluxo dispatcher→subagente→agregação rastreável, gates G0→G1 passando. |
| **Escopo** | Implementação (fora deste repo documental, no repo-alvo decidido — hoje este repo, sem CI) dos artefatos de contrato: envelope/resumo/AgentState v1.0.0 validados; validador de resumo (H1.2); fluxo mínimo de aceite de valor (E3); gates G0 (schema/contrato) e G1 (testes do núcleo + smoke dispatcher→agregação); instrumentação mínima de KPIs (conformidade de resumo ≥ 95% como gate inicial, meta PO §4). |
| **Marcos** | **MU-1.1** Contratos v1.0.0 validados em casos válidos/inválidos; **MU-1.2** Fluxo mínimo ponta a ponta rastreável (1–2 papéis) com dedupe comprovado; **MU-1.3** Gate G1 verde + pacote de evidências submetido ao **aceite do PO** (D-V0-03) — aceite **nunca** inferido de execução. |
| **Dependências** | **D-V0-01 RESOLVIDO (DEC-018, 2026-11-17) ⇒ F-ÚNICO-1 DESBLOQUEADA.** Requer adicionalmente D-V0-05 (contrato adotado), D-V0-04 (baseline técnica/ADRs), D-V0-06 (política de gates), D-V0-03 (aceite de valor sobre visão/MVP). Capacidade (D-V0-02) `[LACUNA]`. |
| **DoR (entrada)** | F-ÚNICO-0 concluída (MU-0.1…MU-0.3); D-V0-01/03/04/05/06 decididas; repo-alvo com tooling mínimo; fatia MVP "ready" (DoR PO/PM atendido); baseline G0 declarada. |
| **DoD (saída)** | Incrementos com evidência verificável; gates G0→G1 verdes; rastreabilidade request→task→run→artifact→gate→decisão; decisão do PO registrada (`approved`/`pending`/`rejected`) com evidência; `done`≠`completed`≠`approved` preservado. |
| **Riscos associados** | R1 (contrato — mitigado por F-ÚNICO-0/`docs/48`), R2 (rastreabilidade), R3 (gates G0→G1), R4 (capacidade — decisão DEC-006(iv) não altera: 1 mantenedor), R6/**R8** (D-V0-01 **resolvido** por DEC-018 — mitigado), R7 (aceite PO como gargalo — SLA `[LACUNA]`; cadência sob demanda sem SLA — DEC-006(v)), R10 (mantenedor único), R11 (drift 47/48). |
| **Estimativa PERT+30%** | **[LACUNA]** — não estimável sem D-V0-01 (stack) e D-V0-02 (capacidade). Não inventar dias-homem. |
| **Executável hoje?** | **CONCLUÍDA (DEC-024, 2026-11-17) — F-ÚNICO-1 concluída (65 testes, 74,84% cobertura); F-ÚNICO-2 (Evolução) iniciada.** |

#### F-ÚNICO-2 — Evolução (piloto, endurecimento G2→G3, evolução)

| Elemento | Definição |
|---|---|
| **Objetivo** | Ampliar de MVP controlado para operação sustentada: piloto multi-papel, endurecimento de gates (G2→G3), escala de valor com controle de mudança. |
| **Escopo** | Piloto multi-papel com agregação paralela e tratamento de conflitos (TL F4); gates G2 (cobertura/estática/segurança — threshold **lido do `pyproject.toml` do projeto-alvo**, nunca hardcoded) e G3 (performance/auditoria/ADRs); E2–E4 completos (semântica de estados em produção, rastreabilidade ponta a ponta E4/H4.1, Decision/Acceptance operacional); KPIs calibrados com baseline real; retrospectivas e change control (PM F2). |
| **Marcos** | **MU-2.1** Piloto multi-papel agregado com decisões pendentes explícitas; **MU-2.2** G2/G3 verdes; **MU-2.3** Baseline v1 operacional com KPIs medidos; **MU-2.4** Evolução contínua (backlog E2–E4; ADRs operacionais). |
| **Dependências** | F-ÚNICO-1 concluída + aceite PO dos incrementos MVP; D-V0-02 (capacidade) e D-V0-06 (gates/thresholds) confirmadas; `pyproject.toml` (ou equivalente do alvo) existente para G2. |
| **DoR (entrada)** | F-ÚNICO-1 done com evidências; gates G1 verdes; PO com cadência de aceite mínima acordada (hoje: sob demanda, sem SLA — `[LACUNA]`). |
| **DoD (saída)** | G2/G3 verdes; trilha de auditoria periódica; KPIs com baseline medido; change control operante; dívida técnica registrada com plano. |
| **Riscos associados** | R3 (endurecimento de gates sem baseline — "no new errors" exige baseline declarada), R4/R10 (capacidade; mantenedor único), R5 (expansão de escopo — MoSCoW/WSJF estritos + change control com referência a `DECISIONS.md` — R9), R7 (gargalo de aceite PO — sem SLA, DEC-006(v)), R2 (escala de rastreabilidade), R11 (drift de artefatos não reconciliados). |
| **Estimativa PERT+30%** | **[LACUNA]** — não estimável; depende de F-ÚNICO-1 e D-V0-02/06. |
| **Executável hoje?** | **INICIADA (DEC-024, 2026-11-17) — depende da conclusão de F-ÚNICO-1 (atendida); evolução em andamento.** |

### 3) Dependências e bloqueios explícitos (decisões do Mantenedor, 2026-11-16)

Registro canônico: `docs/DECISIONS.md` (DEC-001…DEC-008) e ata `docs/46-ata-kickoff-d-v0-01-02-v0.md`.

| Decisão | Estado (2026-11-16) | Efeito no roadmap |
|---|---|---|
| **D-V0-01** (stack/CI/repo-alvo/gates técnicos) | **RESOLVIDO — DEC-018 (2026-11-17)** (stack mínima Python 3.12 + pytest + ruff + mypy, sem CI externo; thresholds absolutos cobertura ≥50%, 0 erros críticos) | **F-ÚNICO-1 desbloqueada** (R8 mitigado). F-ÚNICO-0 não depende dela. LangGraph permanece condicional (CR-009-C). |
| **D-V0-02** (stakeholders/capacidade/cadência) | **Decidida por DEC-006(iv)–(vi)**: Mantenedor único (Lucinei); cadência sob demanda sem SLA (substitui `[PREMISSA-P1]` quinzenal — `docs/20-*` `[PREMISSA-P6]`); tracking = `docs/` | Capacidade confirmada apenas como *mantenedor único sob demanda*; **PERT+30% não declarável**; R10 (bus factor 1) aberto. |
| **Repo-alvo** | **DEC-006(ii)**: este mesmo repositório (`sdlc-agentico`) | Documental; sem CI. |
| **CI** | **DEC-006(iii)**: nenhuma por ora; sem remote configurado | Sem gates executáveis; G0–G3 permanecem proposta. |
| **D-V0-03** (aceite PO: visão/MVP/estados/KPIs) | **APROVADO E MATERIALIZADO (DEC-019, 2026-11-17)** | F-ÚNICO-1 pode declarar valor após aceite explícito do PO. |
| **D-V0-04** (baseline técnica/ADRs/numeração) | **APROVADO E MATERIALIZADO (DEC-020, 2026-11-17)** | ADR-001…ADR-008 promovidos para `accepted`. |
| **D-V0-05** (contrato canônico v1.0.0) | **APROVADO E MATERIALIZADO (DEC-021, 2026-11-17)** | Contrato v1.0.0 adotado; validador `docs/schemas/contract-v1.0.0.schema.json`. |
| **D-V0-06** (política única de gates/thresholds) | **APROVADO E MATERIALIZADO (DEC-022, 2026-11-17)** | Thresholds absolutos cobertura ≥50%, 0 erros críticos. |
| **CR-009-C / CR-010-C** (stack/LangGraph; tracking externo) | **Dormentes** no log — só se kickoff futuro decidir | Sem efeito hoje (DEC-006). |
| **CR-013-publicação** (publicar baseline v0) | **Bloqueada** por D-V0-03/04/05/06 + DEC-008 | Nenhuma fase declara baseline publicado. |
| **LICENSE** | **DEC-004**: nenhuma por ora — todos os direitos reservados | Sem implicação de roadmap. |
| **`docs/evidence/`** | **DEC-005**: criação **rejeitada** | Evidências referenciadas por caminho/link/hash nos canônicos; não criar diretório. |

**Regra dura:** qualquer avanço além de F-ÚNICO-0 exige, no mínimo, D-V0-03 + D-V0-04 + D-V0-05 + D-V0-06 decididas e registradas em `docs/DECISIONS.md` (e D-V0-01 para qualquer implementação). A ata do kickoff é `docs/46-ata-kickoff-d-v0-01-02-v0.md` e o log canônico é `docs/DECISIONS.md` (DEC-006 registra as 6 decisões de 2026-11-16). Não criar novos canônicos, diretórios ou numeração sem decisão do Mantenedor.

### 4) DoR/DoD consolidado da trilha única

- **DoR transversal:** item priorizado com valor/objetivo e critérios Given/When/Then; dependências mapeadas sem bloqueio crítico (ou risco aceito registrado); contratos/gates aplicáveis definidos; estimativa e dono atribuídos; sem ambiguidade contratual impeditiva (ou `[LACUNA]` registrada).
- **DoD transversal:** escopo do item executado; **evidência verificável** anexada/referenciada; gates aplicáveis atendidos/registrados; documentação atualizada; `done` ≠ `completed` ≠ `approved` — nenhuma promoção implícita; lacunas explícitas.
- **Semântica de estados:** ver `docs/48` §Artefato(iii–iv) e `docs/10-*` §3.

### 5) Divergências registradas (não resolvidas silenciosamente)

| # | Divergência | Origem | Tratamento | Status (2026-11-16) |
|---|---|---|---|---|
| DIV-1 | Roadmap PM F0–F2/I1–I2 × TL F0–F5 × PO M1–M3/E1–E4 | `docs/10/20/30` | **Mapa em §1 deste documento.** Textos antigos não editados; reconciliação textual em andamento (F-ÚNICO-0/MU-0.3). `docs/30` reconciliado parcialmente em 2026-11-16 (bloco "Reconciliação F-ÚNICO-0" + mapeamento de fases + cadência DEC-006(v)). | **Em andamento** (mapa registrado; reconciliação textual em andamento) |
| DIV-2 | `schema_version 0.1.0-draft` (41/45) × v1.0.0 proposto (D-V0-05) | `docs/41`, `docs/45`, painel §8.1 | Proposta em `docs/48` (§(vi) migração aditiva); adoção = Classe C (D-V0-05). `docs/48` atualizado em 2026-11-16: normativos com hash completo; consistência com `docs/30` verificada. | **Em andamento** (proposta publicada; adoção pendente de Classe C) |
| DIV-3 | `docs/46` citada como inexistente na 1ª redação; na verdade criada em 2026-11-16 (sessão paralela) como ata do kickoff D-V0-01/02, status `vigente`; log canônico `docs/DECISIONS.md` também criado | ata `docs/46-ata-kickoff-d-v0-01-02-v0.md`; DEC-001…DEC-008 | Ata e log existem e são citados neste documento; a divergência de sincronia inicial está fechada por leitura direta. | **Fechado** |
| DIV-4 | `exit_code 6` adicionado ao `docs/42` após revisão PM (linha "coverage", fail-closed) | painel §8.1; `docs/42` §2 | Incorporado ao contrato em `docs/48` §v; divergência t2×t5 fechada no canônico 42. | **Fechado** |
| DIV-5 | CR de inclusão dos canônicos 41–45 **resolvido condicionalmente** por DEC-003 (inclusão ≠ aprovação de conteúdo); normativos externos por caminho+sha256 abreviado (sem cópia física) | painel §8.1/§8.2; `docs/DECISIONS.md` DEC-003 | Inclusão condicional vigente; conteúdo permanece condicional até D-V0-04. Normativos pinados com hash completo em `docs/30`/`docs/48` em 2026-11-16 (prefixos conferem; sem divergência). | **Fechado** (inclusão condicional vigente) |
| DIV-6 | Índice `docs/README.md` não atualizado para 47/48 neste change set | restrição da delegação | **Não tocado** por instrução explícita (somente 2 arquivos autorizados naquela entrega); atualização pendente no próximo change set autorizado. | **Pendente** (índice não atualizado) |

### 6) Critérios de Promoção de Fase (gate de saída)

**F-ÚNICO-0 → F-ÚNICO-1.** Todos os itens abaixo devem estar atendidos com evidência verificável antes de iniciar F-ÚNICO-1:
- D-V0-01 resolvido (stack/repo-alvo/CI/gates técnicos decididos e registrados em `docs/DECISIONS.md`) — **ATENDIDO por DEC-018 (2026-11-17)** (stack mínima Python 3.12 + pytest + ruff + mypy, sem CI externo; thresholds absolutos cobertura ≥50%, 0 erros críticos);
- Baseline v0 publicado (CR-013-publicação desbloqueada; DEC-008);
- Makefile funcional no repo-alvo (alvos de design `lint-ads`/`test-unit`/`test-integration` materializados com exit codes conforme `docs/42`);
- Primeiro incremento com evidência (contrato validado em casos válidos/inválidos; gates G0→G1 verdes; rastreabilidade request→task→run→artifact→gate→decisão);
- D-V0-03/04/05/06 decididas e registradas (aceite PO, baseline técnica/ADRs, contrato canônico v1.0.0, política de gates/thresholds);
- Tracking ativo com fatia MVP em `ready` (DoR atendido).

**F-ÚNICO-1 → F-ÚNICO-2.** Todos os itens abaixo:
- MVP validado (incrementos com evidência; gates G0→G1 verdes; aceite do PO registrado — `approved`/`pending`/`rejected` com evidência; `done`≠`completed`≠`approved` preservado);
- KPIs instrumentados (conformidade de resumo ≥ 95% como gate inicial; KPI-7 "taxa de sucesso do loop" medido; baseline "no new errors" declarada);
- Aceite PO registrado (D-V0-03 materializado; Decision/Acceptance operacional);
- Capacidade/cadência confirmadas (D-V0-02) ou risco aceito registrado;
- Gates G2 (cobertura/estática/segurança, threshold lido do `pyproject.toml` do projeto-alvo) prontos para endurecimento.

**Gatilho de desbloqueio de F-ÚNICO-1 (RESOLVIDO por DEC-018/DEC-024, 2026-11-17).** D-V0-01 foi resolvido (Opção B) e a sequência de desbloqueio abaixo foi ATENDIDA (itens 1–5); F-ÚNICO-1 concluída e F-ÚNICO-2 iniciada:
1. Registrar a decisão em `docs/DECISIONS.md` (nova DEC) e ata de kickoff (padrão `docs/46`);
2. Reconciliar `docs/30`/`docs/47`/`docs/48` (bloco de mapeamento + cadência) — change control `docs/20` §5;
3. Materializar Makefile/pyproject.toml (ou equivalente) no repo-alvo com alvos e exit codes conforme `docs/42`;
4. Declarar baseline G0 ("no new errors") sobre a baseline declarada;
5. Reavaliar DoR de F-ÚNICO-1 (fatia MVP `ready`) e, se atendido, autorizar início da implementação pelo Tech Lead (Classe C quando envolver arquitetura).

**Regra dura.** Nenhuma promoção de fase ocorre por inferência de execução; cada promoção exige evidência verificável e registro no log canônico (`docs/DECISIONS.md`). Baseline v0 permanece não publicada até CR-013-publicação desbloqueada.

## Evidências

- `docs/00-painel-gerencial-consolidado.md` §4 (pontos a reconciliar: fases/roadmap; contrato; `completed`; gates; cadência) e §5 (D-V0-01…D-V0-06); §8.1 (divergência roadmap e schema_version registrada; exit_code 6 corrigido no 42) — lido 2026-11-16.
- `docs/10-produto-po-visao-mvp-baseline-v0.md` (M1–M3; E1–E4; semântica de estados §3; KPIs §4) — lido 2026-11-16.
- `docs/20-governanca-pm-plano-baseline-v0.md` (F0–F2; I1–I2; riscos R1–R7; P1–P5; DoR/DoD §5; PERT+30% §6) — lido 2026-11-16.
- `docs/30-arquitetura-tech-lead-baseline-v0.md` (F0–F5; gates G0–G3; ADRs A–G sem numeração; `adr_ref="none"`) — lido 2026-11-16.
- `docs/46-ata-kickoff-d-v0-01-02-v0.md` (ata do kickoff D-V0-01/02; status `vigente`) e `docs/DECISIONS.md` (log canônico; DEC-001…DEC-008; DEC-006 registra as 6 decisões de 2026-11-16) — lidos em 2026-11-16, **após criação concorrente por sessão paralela no mesmo dia** (verificação inicial deste artefato, mais cedo no dia, não os encontrou; leitura atual confirma existência e conteúdo).
- `docs/20-governanca-pm-plano-baseline-v0.md` — leitura inicial (R1–R7, P1–P5) e leitura posterior (**R8–R11 e `[PREMISSA-P6]`**, adicionados por sessão concorrente em 2026-11-16; R8 = D-V0-01 adiado bloqueia F-ÚNICO-1; R11 = drift 47/48 × 10/20/30).
- `docs/41-agentstate-esquema-v0.md`, `docs/45-grafo-langgraph-classe-c-v0.md` (`schema_version 0.1.0-draft`); `docs/42-mapeamento-gates-makefile-v0.md` §2 (linha `exit_code 6` — gate de cobertura em `pr_generation`, fail-closed, adicionada 2026-11-16).
- **Reconciliação 2026-11-16 (F-ÚNICO-0/MU-0.3):** `docs/30` reconciliado (bloco de mapeamento F0–F5 → F-ÚNICO-*, cadência DEC-006(v), evidências embutidas por link/hash); `docs/48` verificado (normativos com hash completo). Hashes completos dos normativos externos pinados: `contrato-resumo-subagentes.md` = `163e0aad7654d0a60930e90388afa9b9474ee727f119e94a62337d8321442a60`; `autonomia-e-estados.md` = `776af494ee702cf4d3db8837f2b1c0c23450844f9b54e376a052d7adbc42c78a`. Prefixos conferem com DEC-003 (`163e0aad…`, `776af494…`); **nenhuma divergência detectada**. Divergência futura nos arquivos vivos invalida a referência até re-registro (DEC-003). `docs/evidence/` não criado (DEC-005): evidências embutidas/por link.
- Fatos do Mantenedor (2026-11-16), registrados em DEC-006: D-V0-01 adiado; repo-alvo = este repo; CI nenhuma; mantenedor único (Lucinei); cadência sob demanda sem SLA; docs/ = tracking; LICENSE nenhuma (DEC-004); `docs/evidence/` rejeitado (DEC-005).

## ⚠️ Premissas e Lacunas

- **[RESOLVIDO — DEC-018 (2026-11-17)] D-V0-01:** stack mínima definida (Python 3.12 + pytest + ruff + mypy, sem CI externo); thresholds absolutos (cobertura ≥50%, 0 erros críticos); F-ÚNICO-1 desbloqueada (R8 mitigado). LangGraph permanece condicional (CR-009-C). *Impacto:* roadmap deixa de ser puramente documental; implementação pode iniciar com infraestrutura real mínima.
- **[DECIDIDO — DEC-006(iv)–(vi)] D-V0-02:** mantenedor único (Lucinei); cadência sob demanda sem SLA (substitui `[PREMISSA-P1]` quinzenal; `docs/20-*` `[PREMISSA-P6]`); tracking = `docs/`. Capacidade real = 1 pessoa sob demanda ⇒ **PERT+30% não declarável**; qualquer número de dias-homem seria invenção. R10 (bus factor 1) aberto.
- **[RESOLVIDO] D-V0-03/04/05/06 APROVADOS E MATERIALIZADOS** (DEC-019…DEC-022, 2026-11-17): aceite PO (materializado), baseline técnica/ADRs (accepted), contrato v1.0.0 adotado, política de gates (thresholds absolutos). F-ÚNICO-1 tem DoR atendível; publicação do baseline permanece bloqueada por DEC-008/CR-013 (tracking + publicação).
- **[LACUNA] Critério operacional exato de `completed` no tracking alvo** (`docs/` como trilha, sem board/tool) — semântica proposta em `docs/48` §iv; ferramenta indefinida.
- **[LACUNA] Capacidade de revisão Classe C:** gargalo potencial de aceite/aprovação (ritmo sob demanda; mantenedor único).
- **[PREMISSA]** F-ÚNICO-0 é executável e de baixo risco (documental, Classe B, reversível) — coerente com D-V0-01 adiada (DEC-006) e com DEC-008 (reconciliação via roadmap único; publicação bloqueada).
- **[PREMISSA]** Os canônicos antigos (10/20/30) permanecem como histórico; sua reconciliação textual exige D-V0-05/06 e decisão do Mantenedor.
- **[PREMISSA]** `docs/evidence/` rejeitado ⇒ evidências são referências (caminho/URI/hash) nos próprios canônicos, nunca diretório paralelo de SoT.
- **[NOTA 2026-11-16 — F-ÚNICO-0/MU-0.3]** Reconciliação documental executada pelo tech-lead: `docs/30` reconciliado (mapeamento + cadência + hashes); `docs/48` verificado (hashes completos); `docs/47` DIV-1…DIV-6 atualizados (DIV-3/4/5 fechados; DIV-1/2 em andamento; DIV-6 pendente). Prefixos DEC-003 conferem; **nenhuma divergência de hash**. Nenhum canônico 10/20/40 editado; nenhum `approved`/`completed` promovido; nenhum ADR numerado.
- **[PREMISSA]** Divergência NÃO é licença para editar canônicos antigos neste change set (restrição da delegação: somente 47 e 48).

## ✅ Próximas Ações

1. **Mantenedor valida este roadmap (Classe B, reversível) e despacha D-V0-03/04/05/06** (registro em `docs/DECISIONS.md` como DEC-009+) — Dono: Mantenedor (Lucinei) — Prazo: sob demanda (sem SLA).
2. **Registrar referência cruzada deste roadmap no log/ata** (ou adendo em `docs/DECISIONS.md` apontando para `docs/47`) para fechar a rastreabilidade do DEC-008 ("roadmap único em elaboração em `docs/47`") — Dono: Mantenedor/Orchestrator — Prazo: próximo change set.
3. **Submeter `docs/48` (Contrato v1.0.0-PROPOSTA) à decisão D-V0-05** (CR-007-C no log) — Dono: TL (proposta) / Mantenedor+PO+PM (decisão) — Prazo: sob demanda.
4. **Atualizar `docs/README.md` (índice) com 47/48** no próximo change set autorizado (não tocado nesta entrega por restrição explícita) — Dono: Orchestrator/Mantenedor — Prazo: próximo change set.
5. **Reconciliação textual dos canônicos 10/20/30** (marcos, fases, PERT; P1 quinzenal já substituída por P6) após D-V0-05/06 — Dono: PM+TL+PO — Prazo: F-ÚNICO-0/MU-0.3.
6. **F-ÚNICO-1 concluída (DEC-024); F-ÚNICO-2 (Evolução) iniciada** — implementação entregue (SQLite, validador, segredos, máquina de estados, 65 testes, 74,84% cobertura); gates G0→G1 verdes; evolução em andamento — Dono: TL/Engenharia — Prazo: F-ÚNICO-2.

## Resumo do Subagente

- objetivo: Criar `docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` — roadmap unificado Fundação→MVP→Evolução, fundindo os 3 roadmaps divergentes (PO M1–M3/E1–E4, PM F0–F2, TL F0–F5) em trilha única linear, condicional à validação do Mantenedor.
- ação executada: Leitura integral de `docs/00` (§4/§5/§8.1/§8.2), `docs/10`, `docs/20`, `docs/30`, `docs/40`, `docs/41`, `docs/42` (§2 linha exit_code 6), `docs/45`, `docs/README.md`; **verificação concorrente**: `docs/46-ata-kickoff-d-v0-01-02-v0.md` e `docs/DECISIONS.md` (DEC-001…DEC-008) foram criados por sessão paralela em 2026-11-16 — este documento foi ajustado para citá-los (o log prevalece em divergência); redação do mapa de correspondência, das 3 fases (F-ÚNICO-0/1/2) com objetivo/escopo/marcos/dependências/DoR-DoD e riscos R1–R11, PERT+30% marcado `[LACUNA]` (não estimável sem capacidade), bloqueios explícitos (D-V0-01 adiado/DEC-006(i) ⇒ F-ÚNICO-1 bloqueada/R8) e Divergências DIV-1…DIV-6.
- resultado/artefato: `docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` (este documento), status `condicional`, classe B.
- evidência: Canônicos citados (lidos 2026-11-16); `docs/46-ata-kickoff-d-v0-01-02-v0.md` e `docs/DECISIONS.md` lidos após criação concorrente no mesmo dia; `docs/20-*` relido com R8–R11/P6; decisões do Mantenedor registradas em DEC-006 do log.
- status: done
- bloqueios/riscos: F-ÚNICO-1+ bloqueadas por D-V0-01 adiada (DEC-006(i); R8); PERT+30% não declarável; publicação do baseline bloqueada (DEC-008); índice README não atualizado para 47/48 (restrição da delegação); risco R11 (drift 47/48 × 10/20/30) até reconciliação.
- decisão pendente: Validação do roadmap pelo Mantenedor (Classe B); D-V0-03/04/05/06 materializados (DEC-019…DEC-022); publicação do baseline sob DEC-008.
- próxima ação recomendada: Mantenedor revisa 47/48 e despacha as decisões pendentes; nenhuma implementação iniciar.
