---
title: "DEC-027 — D-V0-02 — Capacidade real e tracking (F-ÚNICO-2)"
date: "2026-11-17"
project: "sdlc-agentico"
status: "registrado (Classe B, 2026-11-17) — D-V0-02 resolvido para a escala atual"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-027 — D-V0-02: Capacidade real e ferramenta de tracking (F-ÚNICO-2, 2026-11-17)

**Nota de numeração:** a pauta original previa "DEC-025"; DEC-025 (reconciliação docs/41/45, Classe B) e DEC-026 (aceite de valor PO, Classe C) já existiam. Este registro assume o número livre seguinte, **DEC-027** — consistente com `docs/20-*` §0.1, que já referencia DEC-027 para a resolução de D-V0-02.

- **Contexto:** D-V0-02 (stakeholders/capacidade/capacidade/cadência/tracking) permaneceu **parcialmente resolvido** desde DEC-006(iv)-(vi) (2026-11-16; Mantenedor único; cadência sob demanda sem SLA; tracking = `docs/`). Em 2026-11-17, na fase F-ÚNICO-2 (Evolução), a sessão delegante demandou o fechamento de D-V0-02: capacidade real estimada para o projeto e recomendação de ferramenta de tracking para suporte à escala. Referências: DEC-006 (kickoff), DEC-014 ([PREMISSA-P7]/PR-02 — 40h/sem, full-time MVP de 1 semana, grill 2026-11-16), DEC-024 (baseline v0 publicada; F-ÚNICO-2 iniciada), `docs/20` §0.1, `docs/21`, `docs/40`, `docs/47` §(vi).
- **Decisão (Classe B — registro + recomendação; decided_by NÃO humano; nenhuma decisão Classe C tomada por este registro):**
  1. **Capacidade real (estimada, F-ÚNICO-2):** **Mantenedor único (Lucinei), ~4–8 horas/semana para o projeto** (projeto paralelo à atividade principal; não 40h/sem). **Cadência mantida:** sob demanda, sem SLA formal (DEC-006(v)); revisão RACI/checkpoints semanal (DEC-014 [PREMISSA-P8]) mantida. **Buffer PERT+30% mantido:** `E = ((O + 4×M + P)/6) × 1.3`; **não prometer prazo sem buffer** (Regra 4). **Orçamento monetário:** zero (DEC-014 [PREMISSA-P7]).
  2. **`[PREMISSA]` de divergência (registrar, não resolver silenciosamente):** a estimativa ~4–8h/sem **diverge** de DEC-014 [PREMISSA-P7]/PR-02 e de `docs/20` §0.1 (P9: 40h/sem, 8h/dia × 5d — premissa do MVP de 1 semana full-time). P7/P9 permanecem no histórico como registro do contexto de 2026-11-16; para F-ÚNICO-2, a referência vigente passa a ser **[PREMISSA-P10]** (este DEC): capacidade estimada ~4–8h/semana, sem SLA, buffer 30%, revisão RACI semanal. Estimativa **não confirmada com o Mantenedor** nesta data — tratar como `[PREMISSA]` até confirmação explícita.
  3. **Implicação de cronograma:** itens F2.x com esforço equivalente ~3,9d (F2.1+F2.2, `docs/20` §0.1.3) não cabem mais em 1 semana (~4–8h/sem ≈ 0,5–1d útil/semana); ao ritmo atual, ~4–8 semanas de calendário. Replanejamento rolling-wave; re-baseline sob demanda; **nenhum prazo prometido sem buffer e sem confirmação de capacidade**.
  4. **Tracking — análise das opções:**
     | Opção | Descrição | Avaliação |
     |---|---|---|
     | A | `docs/` como trilha (atual, DEC-006(vi)) | Suficiente para mantenedor único hoje; disciplina documental exigida; sem notificações; sem visão kanban; sem IDs correlacionáveis nativos |
     | B | **GitHub Issues** (gratuito, integrado ao repositório) | **Recomendado para escala**: notificações, templates, IDs correlacionáveis (`#n`), busca, referência cruzada PR↔issue↔decisão; custo operacional baixo |
     | C | **GitHub Projects** (kanban) | **Recomendado como complemento a B** para visualização (colunas ready→in_progress→done→accepted); não substitui B |
     | D | Manter `docs/` (sem ferramenta externa) | Mais simples; sem notificações; aceito como status quo por DEC-006(vi) |
  5. **Recomendação (Classe B; NÃO adotada por este registro):** adotar **Opção B (GitHub Issues), complementada pela Opção C (GitHub Projects)**, quando iniciar escala (ex.: ≥ 2 contribuidores, ou necessidade de notificações/rastreio de issues fora dos canônicos, ou volume de itens > capacidade de curadoria manual em `docs/`). **Até decisão Classe C do Mantenedor, a trilha vigente permanece `docs/` (DEC-006(vi))** — nenhuma issue externa é criada; CR-010-C permanece dormente.
  6. **Pré-condições para adoção de B/C (não executadas):** decisão Classe C do Mantenedor (CR-010-C); **remote configurado** (repo hoje **sem remote** — DEC-006(iii), `docs/40` linha 14); custos nulos (plano gratuito); migração aditiva (docs/ continua como SoT documental; issues = trilha operacional); atualizar `docs/40` (linha 14), `docs/20` §0.1.2, `docs/00` §5 e README no change set da adoção.
  7. **R10 (bus factor 1) permanece aberto** — mantenedor único; mitigação vigente: decisões no log, artefatos autossuficientes, tracking em `docs/` (ou Issues, se adotada).
- **Alternativas consideradas:**
  - (a) Adotar GitHub Issues imediatamente (Opção B) — **rejeitada por este registro**: DEC-006(vi) é decisão Classe C vigente (tracking = `docs/`); substituí-la exige decisão Classe C do Mantenedor; mudança não autorizada seria violação de change control (`docs/20` §5).
  - (b) Manter `docs/` para sempre (Opção D) — **rejeitada como recomendação de escala**: sem notificações/visão; aceitável como status quo até a escala exigir.
  - (c) GitHub Projects isolado (Opção C) sem Issues — rejeitada: Projects referencia issues; sem B, o kanban fica vazio de conteúdo rastreável.
  - (d) Jira/Linear/similar — rejeitada: custo/complexidade injustificados para mantenedor único; viola "mínimo necessário".
  - (e) Registrar capacidade 40h/sem (manter P7) — rejeitada: incompatível com a estimativa ~4–8h/sem fornecida para F-ÚNICO-2; manter P7 silenciosamente seria inventar/retificar dado sem registro.
- **Consequências:**
  - D-V0-02 passa de "parcialmente resolvido" para **resolvido para a escala atual** (Mantenedor único, ~4–8h/sem, docs/ tracking), com **pendência Classe C** apenas para a adoção de ferramenta externa em escala (CR-010-C).
  - `docs/20` §0.1, `docs/21`, `docs/40`, `docs/47`, `docs/00` atualizados para refletir DEC-027 (mesmo change set).
  - P7/P9 marcadas como divergentes/supersedidas para o contexto de F-ÚNICO-2; histórico preservado; [PREMISSA-P10] registrada; confirmação do Mantenedor pendente.
  - Nenhuma promoção a `approved`/`completed`; nenhuma mudança de DEC-006(vi); nenhum remote criado; nenhuma issue criada.
- **Evidência:** ata `docs/46`; DEC-006 (kickoff), DEC-014 ([PREMISSA-P7]/PR-02, [PREMISSA-P8]), DEC-018, DEC-024, DEC-025, DEC-026; `docs/00` §5 (D-V0-02); `docs/20` §0.1 (P9/F2.1–F2.5); `docs/21` (capacidade/P7); `docs/40` (lacuna tracking; linha 14); `docs/47` §3/§Premissas (D-V0-02); demanda da sessão delegante (2026-11-17).
- **Status final:** **registrado — D-V0-02 resolvido para a escala atual (Classe B, 2026-11-17)**; recomendação de tracking para escala (Opções B/C) **pendente de decisão Classe C do Mantenedor** (CR-010-C); [PREMISSA-P10] pendente de confirmação explícita do Mantenedor.
