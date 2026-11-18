---
title: "DEC-015 — Consolidação PO da pauta D-V0-03 (proposta)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "aprovado (Classe C, 2026-11-16) — materializado em docs/11-visao-mvp-v0.md"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-015 — Consolidação PO da pauta D-V0-03 (proposta; Classe B — registro)

- **Contexto:** D-V0-03 (painel `docs/00` §5) exige aceite do PO sobre visão, escopo MVP (M1–M3), semântica de estados e metas/KPIs iniciais. É decisão de **valor (Classe C no efeito de aceite)** — exclusiva do PO; nenhum agente pode inferir `approved`. Este registro consolida a proposta do PO (docs/10 §1–§4 + revisão PO dos designs t1–t5) com as premissas operacionais vigentes (capacidade 40h/semana — DEC-014 [PREMISSA-P7]; prazo 1 semana MVP — DEC-014 PR-06; mantenedor único; tracking = docs/ — DEC-006(vi); cadência sob demanda sem SLA para aceite — DEC-006(v); revisão RACI semanal — DEC-014). **Nenhuma decisão Classe C final é tomada; nenhum `approved`/`completed` é declarado; nenhum ADR numerado; nenhum diretório criado; backlog/visão NÃO materializados (aguarda aprovação explícita do Mantenedor).**

- **Proposta consolidada (Classe B — reversível):**

  1. **Visão** (docs/10 §1): SDLC agêntico previsível, auditável e orientado a valor; execução técnica rastreável ponta a ponta; nenhum resultado tratado como valor entregue sem aceite explícito do PO. (Sem alteração de substância.)
  2. **MVP (MoSCoW + WSJF)** (docs/10 §2): Must = M1 (contrato canônico de resumo + validação), M2 (semântica canônica de estados), M3 (fluxo de aceite de valor PO). Should = S1 (rastreabilidade ponta a ponta), S2 (dashboard). Could = C1 (métricas automatizadas), C2 (catálogo de templates). Won't (MVP) = W1 (automação avançada cross-agente). WSJF: M2=13,0 (maior), M1=7,8, M3=6,8. MoSCoW Must = exatamente 3 itens (sem exceção), conforme docs/10.
  3. **Backlog (épicos/histórias)** (docs/10 §2): E1 (Must, M1) H1.1–H1.3; E2 (Must, M2) H2.1–H2.2; E3 (Must, M3) H3.1–H3.3; E4 (Should, S1) H4.1. **Modo documental (F-ÚNICO-0) em 1 semana:** E1+E2+E3 cabem como refinamento documental; E4 (H4.1) adiado para F-ÚNICO-2 (depende de IDs correlacionáveis — [LACUNA]).
  4. **Semântica de estados** (docs/10 §3, docs/48 §iii/iv): três camadas — execução (`done/blocked/partial`), operação (`completed`), valor (`pending/approved/rejected`). `done` ⇏ `completed` ⇏ `approved`; `approved` terminal, exclusivo do PO, exige `evidence`+`decided_by`+`decided_at`; agente nunca escreve `approved`. Critério operacional proposto de `completed` = "item executado (resumo `done` com evidência) + gates aplicáveis da fase atendidos + registro de conclusão no sistema operacional de tracking, com rastreio explícito" — semântica aceita como conceitual; ferramenta exata permanece [LACUNA] (tracking = docs/, sem board/tool — DEC-006(vi)/D-V0-05).
  5. **KPIs mensuráveis em 1 semana (tracking=docs/, sem infra externa)** (docs/10 §4, calibrados para 40h/sem):
     - KPI-1 Conformidade de resumo ≥95% — mensurável por auditoria manual de resumos em 1 semana (gate binário).
     - KPI-2 Clareza de evidência 100% (gate) — mensurável por auditoria.
     - KPI-3 Distinção de estados preservada = 0 ocorrências de `done/completed` tratado como `approved` sem decisão do PO — mensurável por revisão.
     - KPI-4 Lead time até decisão do PO — parcialmente mensurável (requer registro de datas; [LACUNA] baseline); meta inicial [LACUNA] (sem SLA — DEC-006(v)); calibrar após 2 iterações.
     - KPI-5 Taxa de retrabalho pós-decisão — NÃO mensurável em 1 semana (tendência); adiado para F-ÚNICO-2.
     - KPI-6 Visibilidade de lacunas 100% em casos aplicáveis — mensurável por auditoria.
     - Metas de 1 semana (gates binários): KPI-1, KPI-2, KPI-3, KPI-6. KPI-4 e KPI-5 permanecem [LACUNA] com tracking manual.
  6. **Aceite de valor (Decision/Acceptance v0)** (docs/10 §3.3, docs/48): `pending|approved|rejected`; `approved` terminal, exige `evidence`+`decided_by=PO`+`decided_at`; `rejected` exige `rationale`; `rejected→pending` somente com nova evidência. Handoff PR→aceite PO inexistente (lacuna da revisão PO) — registrado como [LACUNA] a materializar em F-ÚNICO-1 (não bloqueia a proposta).
  7. **Mecanismo de feedback/aceite (MVP)** (docs/10 §4): pronto para aceite (done+evidência+critérios) → orquestrador marca "valor pendente de aceite do PO" → PO valida Given/When/Then + evidências → decisão registrada → se rejected, rationale acionável + condição de nova submissão → revisão periódica de rejeições/lacunas/conformidade.

- **Grill-with-docs aplicado (2 rodadas × 3 perguntas, lacunas de peso 5):**
  - Rodada 1:
    - Q1 (KPIs mensuráveis): Quais dos 6 KPIs são mensuráveis em 1 semana com tracking=docs/? → Resposta: KPI-1/2/3/6 mensuráveis por auditoria manual; KPI-4 parcial; KPI-5 não mensurável em 1 semana. Ação: metas de 1 semana = KPI-1/2/3/6 como gates binários; KPI-4/5 = [LACUNA] com tracking manual, calibrar em F-ÚNICO-2.
    - Q2 (semântica de estados): O critério operacional proposto de `completed` deve ser aceito como canônico ou permanecer [LACUNA]? → Resposta: aceitar a semântica conceitual; ferramenta exata permanece [LACUNA] (tracking=docs/, sem board/tool; D-V0-05). Não promover baseline sem D-V0-05.
    - Q3 (handoff PR→aceite): O pacote mínimo de evidência é suficiente ou falta o handoff? → Resposta: lacuna confirmada (revisão PO ses_e1b33e791ffeK0gwIR9QY7Y7z5: handoff PR→aceite PO inexistente; AC Given/When/Then ausentes nos designs; KPIs não instrumentáveis). Ação: adicionar à DoR de H3.1/H3.2 o campo "handoff: PR/entrega → pacote de evidência → fila de aceite do PO" como [LACUNA] a materializar em F-ÚNICO-1. Não bloqueia a proposta de valor.
  - Rodada 2:
    - Q4 (capacidade/backlog): Com 40h/sem e 1 semana (modo documental, sem código), quais histórias cabem? → Resposta: E1+E2+E3 cabem como refinamento documental (≈3d/24h com buffer 30% sobre 40h); E4 (H4.1) adiado para F-ÚNICO-2. Estimativa PERT: 40h = 5d×8h; buffer 30% ⇒ ~30h úteis.
    - Q5 (rastreabilidade): E4/H4.1 pode entrar no MVP de 1 semana sem IDs correlacionáveis? → Resposta: Não. Manter E4 como Should (S1); [LACUNA] "identificadores correlacionáveis e storage de trilha" registrada. E4 entra em F-ÚNICO-2.
    - Q6 (cadência de aceite): Lead time viável com mantenedor único + revisão semanal? → Resposta: lead time KPI-4 permanece [LACUNA] (sem SLA de decisão — DEC-006(v) para aceite; revisão semanal cobre RACI/checkpoints, não aceite). Proposta: medir em dias entre "pronto para aceite" e decisão; meta inicial [LACUNA] a calibrar após 2 iterações. Risco R7 mitigado por pacote mínimo de evidência + cadência sob demanda.

- **Lacunas persistentes (registradas, não resolvidas silenciosamente):**
  - [LACUNA] D-V0-01 adiado (DEC-006(i)): stack/CI/repo-alvo indefinidos ⇒ F-ÚNICO-1 bloqueada; implementação não iniciada; MVP de 1 semana = modo documental (F-ÚNICO-0).
  - [LACUNA] D-V0-03 pendente (Classe C): este registro é proposta, não aceite; `approved` exclusivo do PO com evidência.
  - [LACUNA] D-V0-04 pendente (Classe C): baseline técnica/ADRs A–G sem número; `adr_ref="none"`.
  - [LACUNA] D-V0-05 pendente (Classe C): contrato v1.0.0 não adotado; `0.1.0-draft` vigente nos designs.
  - [LACUNA] D-V0-06 pendente (Classe C): política de gates/thresholds; "no new errors" sem baseline.
  - [LACUNA] Handoff PR→aceite PO inexistente (revisão PO); AC Given/When/Then ausentes nos designs t1–t5.
  - [LACUNA] KPIs não instrumentáveis (revisão PO); métricas baseline inexistentes.
  - [LACUNA] Identificadores correlacionáveis e storage de trilha/evidências/decisões (E4 adiado).
  - [LACUNA] Critério operacional exato de `completed` no tracking alvo (docs/ como trilha, sem board/tool).
  - [LACUNA] Capacidade real por dia (total estimado 117% da capacidade — sobrecarga; re-planejar).
  - [LACUNA] DEC-007 (política de segredos) permanece [LACUNA] aberta.

- **Conflitos registrados (não resolvidos silenciosamente):**
  - DIV-1 (roadmap PM F0–F2 × TL F0–F5 × PO M1–M3) — mapa em docs/47 §1; em andamento.
  - DIV-2 (`schema_version 0.1.0-draft` × v1.0.0) — proposta em docs/48; em andamento.
  - Divergência revisão PO: KPIs não instrumentáveis / AC ausentes nos designs — registrada como [LACUNA], não resolvida.

- **Premissas operacionais (vigentes, com teste correspondente):**
  - P1: MVP M1–M3 entregue em 1 semana com 40h/sem — teste: escopo documental (F-ÚNICO-0) cabe em 5d×8h com buffer 30% (~30h úteis); F-ÚNICO-1 bloqueada por D-V0-01 (R8) — não prometer código.
  - P2: KPIs mensuráveis sem infra externa (docs/) — teste: KPI-1/2/3/6 auditáveis manualmente em 1 semana; KPI-4/5 [LACUNA].
  - [PREMISSA-P7] (DEC-014): orçamento monetário = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada.
  - [PREMISSA-P8] (DEC-014): cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A).

- **Riscos de produto (vigentes):** R1 (ambiguidade contratual), R2 (rastreabilidade), R4 (capacidade), R7 (gargalo de aceite PO), R8 (D-V0-01 adiado ⇒ F-ÚNICO-1 bloqueada), R10 (bus factor 1), R11 (drift documental), R12 (MVP de 1 semana inviável sem kickoff D-V0-01 — Crítico).

- **Alternativas consideradas:**
  - (a) Declarar D-V0-03 aprovado agora — rejeitada: viola regra dura (aceite de valor é Classe C, exclusivo do PO, com evidência; nenhum agente infere `approved`).
  - (b) Materializar backlog/visão em arquivos novos (docs/product/*) — rejeitada: exige aprovação explícita do Mantenedor via subagente de escrita; não concedida.
  - (c) Promover ADR/baseline — rejeitada: D-V0-04 pendente (Classe C).
  - (d) Resolver lacunas de peso 5 silenciosamente — rejeitada: regra R2/R8; registradas como [LACUNA].
  - (e) Criar diretórios/ADRs numerados — rejeitada: sem decisão Classe C (AGENTS.md regra dura).

- **Consequências:** proposta consolidada e registrada (Classe B, reversível); nenhuma promoção a `approved`/`completed`; D-V0-03 permanece pendente (Classe C) aguardando decisão do Mantenedor; backlog/visão permanecem não materializados; publicação do baseline bloqueada (DEC-008/CR-013-publicação); baseline v0 permanece `condicional`/não pronta.

- **Decisão Recomendada (proposta do PO, 2026-11-16):** **Sim** — aceitar a proposta consolidada (visão/MVP M1–M3, semântica de estados, KPIs mensuráveis em 1 semana como gates binários KPI-1/2/3/6, aceite de valor, backlog E1–E4 com E4 adiado) condicionada ao modo documental (sem código) até D-V0-01 resolvido, com resolução das lacunas registradas (handoff PR→aceite, AC Given/When/Then, KPIs instrumentáveis, IDs correlacionáveis). Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).

- **Ressalvas:** PO — no-go para aceite/implementação até D-V0-03/04/05/06; PM — consenso condicional, divergência residual de ritmo; TL — consenso condicional de substância. Aceite de valor permanece exclusivo do PO.

- **Evidência:** `docs/10-*` §1–§4; `docs/00` §5/§8 (D-V0-03; revisão PO ses_e1b33e791ffeK0gwIR9QY7Y7z5); `docs/20-*` (R1–R11, P1–P6, PR-01…PR-07); `docs/30-*` (ADRs A–G, gates G0–G3); `docs/47-*` (F-ÚNICO-0/1/2, bloqueios, DIV-1/2); `docs/48-*` (semântica de estados, critério de `completed`, exit codes); `docs/DECISIONS.md` (DEC-001…DEC-014); `docs/README.md`; AGENTS.md (regras duras); `~/.opencode/references/contrato-resumo-subagentes.md` (sha256 `163e0aad…`); `~/.opencode/references/autonomia-e-estados.md` (sha256 `776af494…`); grill-with-docs 2×3 (respostas registradas acima).

- **Status final:** **registrado — proposta (Classe B)** (consolidação PO de D-V0-03; nenhuma aprovação inferida; nenhuma promoção a `approved`/`completed`; materialização de backlog/visão aguarda aprovação explícita do Mantenedor via subagente de escrita; propagação para `docs/10`/`docs/00`/`docs/README.md` pendente no próximo change set autorizado).
