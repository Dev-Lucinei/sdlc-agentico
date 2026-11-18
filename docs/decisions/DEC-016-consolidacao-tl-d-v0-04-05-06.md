---
title: "DEC-016 — Consolidação TL das pautas D-V0-04/05/06 (proposta)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "aprovado (Classe C, 2026-11-16) — materializado em docs/adr/core/ADR-001…ADR-007 + Makefile/pyproject.toml"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-016 — Consolidação TL das pautas D-V0-04/05/06, CR-008-C, CR-009-C, arquitetura e dívida técnica (proposta; Classe B — registro)

- **Contexto:** pendências bloqueantes da especialidade TL: D-V0-04 (aprovação da baseline técnica e ADRs iniciais A–G + convenção/numeração canônica de ADRs), D-V0-05 (consolidação do contrato canônico v1.0.0), D-V0-06 (política unificada de gates/evidência/thresholds), CR-008-C (unificação de gates), CR-009-C (LangGraph — dormente, condicional a D-V0-01), arquitetura (dispatcher+agregador, SoT/event-log, idempotência, contratos versionados, estados/autonomia A/B/C, qualidade incremental, observabilidade/segurança) e dívida técnica. Aplicou-se grill-with-docs em 2 rodadas × 3 perguntas para lacunas de peso 5 (numeração ADR, thresholds, convenção ADR, dívida documental, CR-008-C). **Nenhuma decisão Classe C final foi tomada; nenhuma promoção a `approved`/`completed`; nenhum ADR numerado; nenhum diretório/Makefile/pyproject.toml criado.** Materialização de artefatos (ADRs numerados, contrato adotado, Makefile, pyproject.toml) **não** executada — aguarda aprovação explícita do Mantenedor via subagente de escrita (Classe B apenas neste registro).

- **Respostas do grill (Mantenedor, 2026-11-16):**
  - Rodada 1:
    1. **Numeração ADR:** reiniciar local (ADR-001…) — namespace isolado ao repo `sdlc-agentico`; citação por caminho (ADR-009) evita ambiguidade prática. NÃO continuar da árvore compartilhada (019+).
    2. **Thresholds:** `[LACUNA]` + parametrização (fail-closed, exit_code 6) até o projeto-alvo existir; thresholds lidos do `pyproject.toml` do projeto-alvo quando existir; "no new errors" sobre baseline declarada. NÃO adotar default conservador hardcoded.
    3. **Kickoff D-V0-01:** reabrir antes da semana 1 (conforme DEC-014) com escopo mínimo (stack condicional LangGraph, repo-alvo este repo, CI nenhuma, gates G0–G3 propostos). LangGraph permanece condicional até decisão formal de D-V0-01; F-ÚNICO-1 bloqueada até kickoff + D-V0-03/04/05/06.
  - Rodada 2:
    4. **Convenção ADR:** confirmada conforme `docs/30` — status `proposed|accepted|superseded|rejected`, data, contexto, decisão, alternativas, trade-offs, consequências, evidências; slug kebab-case.
    5. **Dívida técnica:** registrada como dívida documental (drift, lacunas, riscos R1–R12) em `docs/DECISIONS.md`; sem backlog separado (tracking = `docs/`). Criar `docs/tech/debt.md` exigiria decisão Classe C (estrutura de diretórios pendente).
    6. **CR-008-C:** unificação feita agora (documental) — G0–G3 × exit_code → AgentState × contrato v1.0.0 registrada como proposta (Classe B); materialização (Makefile) somente após D-V0-06 decidida + projeto-alvo existente.

- **Proposta consolidada (Classe B, reversível):**

  1. **ADRs A–G (D-V0-04):** manter como proposta (`status: proposed`), **sem número atribuído**, até D-V0-04 decidida. Convenção canônica (proposta): `docs/adr/core/ADR-<NNN>-<slug-kebab>.md`, **numeração local reiniciando em ADR-001** (namespace isolado ao repo; citação por caminho conforme ADR-009 do ecossistema); status `proposed|accepted|superseded|rejected`; campos: data, contexto, decisão, alternativas consideradas, trade-offs, consequências, evidências. **Sem criar diretório `docs/adr/` nem ADRs numerados sem decisão Classe C** (AGENTS.md regra dura; DEC-008 bloqueia publicação). Atribuição de `adr_ref` permanece `none` até D-V0-04.
  2. **Contrato canônico v1.0.0 (D-V0-05):** manter `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` como proposta até D-V0-05 decidida. Migração aditiva `0.1.0-draft → 1.0.0` (sem remoção/re-tipagem de campos; minor aditivo; major exige migração explícita). `completed` ≠ `approved`; `approved` terminal e exclusivo do PO (com `evidence` + `decided_by` + `decided_at`); agente nunca escreve `approved`. Sem efeito normativo até adoção (Classe C). `machine_readable.schema_version` ("1.0") × `schema_version` de contrato ("1.0.0") permanece decisão de D-V0-05.
  3. **Gates (D-V0-06 + CR-008-C):** política unificada registrada como proposta (Classe B, agora): G0 (schema/contrato, lint/format de artefatos normativos, checagem de links/paths), G1 (testes do núcleo + smoke dispatcher→agregação + correlação/lineage), G2 (cobertura mínima lida do `pyproject.toml` do projeto-alvo + análise estática/tipos + SAST básico + SLOs), G3 (performance/carga se aplicável + revisão de ADRs + auditoria periódica) × `exit_code → AgentState` (docs/42 §2, incluindo linha 6 fail-closed) × contrato v1.0.0 (docs/48 §v). Thresholds: `[LACUNA]` + parametrização (fail-closed, exit_code 6) até o projeto-alvo existir; "no new errors" sobre baseline declarada; thresholds numéricos lidos do `pyproject.toml` do projeto-alvo quando existir (nunca hardcoded). **Materialização (Makefile/pyproject.toml) somente após D-V0-06 decidida + projeto-alvo existente**; não criar sem decisão Classe C (DEC-006(i) mantém D-V0-01 adiado).
  4. **LangGraph / CR-009-C:** reabrir kickoff D-V0-01 antes da semana 1 (conforme DEC-014 PR-01) com escopo mínimo (stack condicional LangGraph, repo-alvo este repo — DEC-006(ii), CI nenhuma — DEC-006(iii), gates G0–G3 propostos, thresholds lidos do alvo — D-V0-06). LangGraph permanece **condicional** até decisão formal de D-V0-01 (Classe C); F-ÚNICO-1 bloqueada até kickoff + D-V0-03/04/05/06. CR-009-C permanece dormente hoje (sem efeito até D-V0-01 decidida).
  5. **Arquitetura (ADRs A–G):** manter como proposta até D-V0-04: ADR-A (orquestrador dispatcher+agregador, sem domínio), ADR-B (SoT central + event log append-only), ADR-C (idempotência + ingestão at-least-once com dedupe), ADR-D (contratos versionados, envelope + resumo + JSON, validação na borda), ADR-E (modelo de estados e autonomia, execução vs aceite, A/B/C), ADR-F (qualidade incremental por gates e evidência, "no new errors"), ADR-G (observabilidade e segurança mínima by design). Status `proposed`; sem número; sem promoção.
  6. **Dívida técnica (documental):** registrada em `docs/DECISIONS.md` (esta entrada + R1–R12, DIV-1…DIV-6). Itens vigentes: DIV-1 (roadmap PM F0–F2 × TL F0–F5 × PO M1–M3) — em andamento; DIV-2 (`schema_version 0.1.0-draft` × v1.0.0) — em andamento; DIV-3 (ata 46 existente) — fechado; DIV-4 (exit_code 6) — fechado; DIV-5 (inclusão condicional 41–45) — fechado (inclusão condicional vigente); DIV-6 (índice README) — fechado. Riscos vigentes R1–R12 (R8 D-V0-01 adiado, R10 bus factor 1, R11 drift documental, R12 MVP de 1 semana inviável sem kickoff). Sem código neste repo ⇒ sem dívida de código; dívida é documental (drift, lacunas, inconsistências). Sem backlog separado (tracking = `docs/`).

- **Lacunas persistentes (registradas, não resolvidas silenciosamente):**
  - [LACUNA] D-V0-01 adiado (DEC-006(i)): stack/CI/repo-alvo indefinidos ⇒ F-ÚNICO-1 bloqueada; implementação não iniciada; kickoff reaberto antes da semana 1 (DEC-014/DEC-016) mas decisão formal (Classe C) pendente.
  - [LACUNA] D-V0-03 pendente (Classe C): aceite do PO sobre visão/MVP/estados/KPIs; este registro é proposta, não aceite; `approved` exclusivo do PO com evidência.
  - [LACUNA] D-V0-04 pendente (Classe C): baseline técnica/ADRs A–G sem número; `adr_ref="none"`; convenção de numeração (local ADR-001…) proposta mas não adotada.
  - [LACUNA] D-V0-05 pendente (Classe C): contrato v1.0.0 não adotado; `0.1.0-draft` vigente nos designs.
  - [LACUNA] D-V0-06 pendente (Classe C): política de gates/thresholds; "no new errors" sem baseline; thresholds numéricos inexistentes (sem `pyproject.toml`).
  - [LACUNA] CR-008-C: unificação registrada como proposta (Classe B); materialização (Makefile) após D-V0-06 + projeto-alvo.
  - [LACUNA] CR-009-C: LangGraph dormente; sem efeito até D-V0-01 decidida.
  - [LACUNA] CR-013-publicação: baseline v0 não publicado; bloqueada por D-V0-03/04/05/06 + DEC-008.
  - [LACUNA] Critério operacional exato de `completed` no tracking alvo (`docs/` como trilha, sem board/tool) — D-V0-05.
  - [LACUNA] Identificadores correlacionáveis e storage de trilha/evidências/decisões (E4 adiado para F-ÚNICO-2).
  - [LACUNA] Capacidade real por dia (total estimado 117% da capacidade — sobrecarga; re-planejar).
  - [LACUNA] DEC-007 (política de segredos) permanece aberta (gatilho: D-V0-01 resolvido).
  - [LACUNA] Handoff PR→aceite PO inexistente; AC Given/When/Then ausentes nos designs t1–t5 (revisão PO).
  - [LACUNA] KPIs não instrumentáveis (revisão PO); métricas baseline inexistentes.

- **Conflitos registrados (não resolvidos silenciosamente):**
  - DIV-1 (roadmap PM F0–F2 × TL F0–F5 × PO M1–M3) — mapa em `docs/47` §1; em andamento.
  - DIV-2 (`schema_version 0.1.0-draft` × v1.0.0) — proposta em `docs/48`; em andamento.
  - Divergência revisão PO: KPIs não instrumentáveis / AC ausentes nos designs — registrada como [LACUNA], não resolvida.

- **Premissas operacionais (vigentes, com teste correspondente):**
  - P1: MVP M1–M3 entregue em 1 semana com 40h/sem — teste: escopo documental (F-ÚNICO-0) cabe em 5d×8h com buffer 30% (~30h úteis); F-ÚNICO-1 bloqueada por D-V0-01 (R8) — não prometer código.
  - P2: KPIs mensuráveis sem infra externa (docs/) — teste: KPI-1/2/3/6 auditáveis manualmente em 1 semana; KPI-4/5 [LACUNA].
  - [PREMISSA-P7] (DEC-014): orçamento monetário = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada.
  - [PREMISSA-P8] (DEC-014): cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A).
  - P3 (DEC-016): numeração de ADRs reinicia local em ADR-001 (namespace isolado ao repo; citação por caminho). Teste: nenhum id nu citado sem caminho (ADR-009).
  - P4 (DEC-016): thresholds parametrizados (fail-closed exit_code 6) até projeto-alvo existir. Teste: nenhum número de cobertura/lint/types hardcoded em justificativa.
  - P5 (DEC-016): kickoff D-V0-01 reaberto antes da semana 1 (escopo mínimo). Teste: F-ÚNICO-1 permanece bloqueada até decisão formal.

- **Riscos vigentes (topo):** R1 (ambiguidade contratual), R2 (rastreabilidade), R3 (gates), R4 (capacidade), R6 (dependências), R7 (gargalo de aceite PO), R8 (D-V0-01 adiado ⇒ F-ÚNICO-1 bloqueada), R9 (drift DECISIONS×change control), R10 (bus factor 1), R11 (drift documental), R12 (MVP de 1 semana inviável sem kickoff D-V0-01 — Crítico). Mitigações ativas conforme DEC-014/DEC-016.

- **Alternativas consideradas:**
  - (a) Numerar ADRs continuando da árvore compartilhada (019+) — rejeitada pelo Mantenedor (grill #1): namespace isolado ao repo é suficiente; citação por caminho evita ambiguidade.
  - (b) Adotar default conservador de cobertura (ex.: ≥ 80%) hardcoded — rejeitada pelo Mantenedor (grill #2): violaria regra "thresholds lidos do projeto-alvo"; parametrização + fail-closed é a política.
  - (c) Manter D-V0-01 adiado indefinidamente — rejeitada pelo Mantenedor (grill #3): kickoff antes da semana 1 (DEC-014) autorizado; LangGraph permanece condicional.
  - (d) Criar backlog separado de dívida técnica (`docs/tech/debt.md`) — rejeitada pelo Mantenedor (grill #5): tracking = `docs/`; DECISIONS.md é o log canônico; criar diretório exige decisão Classe C (estrutura pendente).
  - (e) Aguardar D-V0-06 para registrar CR-008-C — rejeitada pelo Mantenedor (grill #6): unificação documental (Classe B) pode ser registrada agora; materialização (Makefile) após D-V0-06 + projeto-alvo.
  - (f) Declarar D-V0-04/05/06 aprovados agora — rejeitada: viola regra dura (Classe C, aprovação humana explícita; execução ≠ `approved`).
  - (g) Materializar ADRs numerados/contrato/Makefile/pyproject.toml agora — rejeitada: exige aprovação explícita do Mantenedor via subagente de escrita; não concedida.
  - (h) Resolver lacunas de peso 5 silenciosamente — rejeitada: regra R2/R8; registradas como [LACUNA].

- **Consequências:** proposta consolidada e registrada (Classe B, reversível); nenhuma promoção a `approved`/`completed`; D-V0-04/05/06 permanecem pendentes (Classe C) aguardando decisão do Mantenedor; ADRs A–G permanecem sem número (`adr_ref="none"`); contrato v1.0.0 permanece proposta (sem efeito normativo); gates permanecem propostos (sem Makefile/pyproject.toml); LangGraph permanece condicional; dívida técnica documental registrada (sem backlog separado); publicação do baseline bloqueada (DEC-008/CR-013-publicação); baseline v0 permanece `condicional`/não pronta (2 PASS parciais, 4 FAIL — painel §8.3). Propagação para `docs/30`, `docs/47`, `docs/48`, `docs/00` §8 e `docs/README.md` pendente no próximo change set autorizado.

- **Decisão Recomendada (proposta do TL, 2026-11-16):** **Sim** — aceitar a proposta consolidada TL (ADRs A–G como proposta com convenção de numeração local ADR-001…; contrato v1.0.0 como proposta com migração aditiva; política de gates unificada documentalmente com thresholds parametrizados; LangGraph condicional com kickoff antes da semana 1; arquitetura dispatcher+agregador/SoT/idempotência/contratos/estados/qualidade/observabilidade como proposta; dívida técnica documental registrada em DECISIONS.md) condicionada ao modo documental (sem código) até D-V0-01 resolvido, com resolução das lacunas registradas. Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).

- **Ressalvas:** TL — consenso condicional de substância com PO/PM; PO — aceite de valor reservado ao PO; PM — consenso condicional, divergência residual de ritmo; Mantenedor — decisão Classe C pendente para D-V0-04/05/06/CR-008-C/CR-009-C/CR-013-publicação; aceite de valor permanece exclusivo do PO.

- **Evidência:** `docs/30-arquitetura-tech-lead-baseline-v0.md` (ADRs A–G, gates G0–G3, contratos, riscos/lacunas); `docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` (F-ÚNICO-0/1/2, bloqueios, DIV-1…DIV-6); `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (contrato v1.0.0, semântica de estados, exit codes); `docs/42-mapeamento-gates-makefile-v0.md` §2 (exit_code 6 fail-closed); `docs/00-painel-gerencial-consolidado.md` §5/§8 (D-V0-04/05/06, lacunas, bloqueios); `docs/DECISIONS.md` (DEC-001…DEC-015); `docs/10-produto-po-visao-mvp-baseline-v0.md` (semântica de estados, KPIs); `docs/20-governanca-pm-plano-baseline-v0.md` (R1–R12, P1–P8, PR-01…PR-07); `docs/README.md` (índice canônicos); AGENTS.md (regras duras, precedência); `~/.opencode/references/contrato-resumo-subagentes.md` (sha256 `163e0aad…`); `~/.opencode/references/autonomia-e-estados.md` (sha256 `776af494…`); `~/.agents/adr/core/INDEX.md` (convenção de numeração, ADR-016/017/018 existentes, citação por caminho — ADR-009); grill-with-docs 2×3 (respostas registradas acima).

- **Status final:** **registrado — proposta (Classe B)** (consolidação TL de D-V0-04/05/06, CR-008-C, CR-009-C, arquitetura e dívida técnica; nenhuma aprovação inferida; nenhuma promoção a `approved`/`completed`; nenhum ADR numerado; nenhum diretório/Makefile/pyproject.toml criado; materialização aguarda aprovação explícita do Mantenedor via subagente de escrita; propagação para `docs/30`/`docs/47`/`docs/48`/`docs/00`/`docs/README.md` pendente no próximo change set autorizado). [ATUALIZADO 2026-11-16: materialização Classe C concluída — ADR-001…ADR-007 (status proposed) em docs/adr/core/; Makefile e pyproject.toml na raiz (parametrizados, fail-closed). Nenhuma promoção a approved/completed.]
