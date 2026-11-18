---
title: "DEC-014 — Registro de grill-with-docs (pendências bloqueantes PM)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "aprovado (Classe C, 2026-11-16) — materializado em docs/21-cronograma-raci-riscos-v0.md"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-014 — Registro de grill-with-docs (pendências bloqueantes PM) e propostas de resolução (Classe B — registro)

- **Contexto:** sessão `sdlc-agentico-pm-pendencias-bloqueantes` (gerente-projeto, 2026-11-16) consolidou as pendências bloqueantes da especialidade PM: D-V0-01 (restante: infra/CI/gates), D-V0-02 (restante: orçamento formal e cadência de revisão RACI), roadmap F-ÚNICO, riscos, cronograma de 1 semana e tracking em `docs/`. Aplicou grill-with-docs em 2 rodadas × 3 perguntas para lacunas de peso 5 (orçamento formal, cadência de revisão RACI, timing do kickoff D-V0-01). **Nenhuma decisão Classe C final foi tomada; nenhuma promoção a `approved`/`completed`; nenhum ADR numerado; nenhum diretório criado.** Materialização de artefatos (cronograma, RACI, riscos) **não** executada — aguarda aprovação explícita do Mantenedor via subagente de escrita (Class B apenas neste registro).
- **Respostas do grill (Mantenedor, 2026-11-16):**
  1. **Orçamento formal:** sem orçamento monetário; MVP sustentado exclusivamente pelo esforço do Mantenedor (40h/semana). → `[PREMISSA-P7]` (operacional): capacidade = 40h/semana do Mantenedor único; nenhum custo externo; não prometer prazo sem buffer.
  2. **Cadência de revisão RACI/checkpoints:** semanal (1x/semana), fixa. → substitui a cadência "sob demanda" (DEC-006(v)) **apenas** para a revisão RACI/checkpoints semanais; demais decisões permanecem sob demanda sem SLA (DEC-006(v) vigente para aceite/decisão).
  3. **Dono da revisão RACI:** PM delegado (R) com aprovação do Mantenedor (A) — consistente com `docs/40` RACI (PM A/R em governança; Mantenedor A em impactos relevantes).
  4. **Timing do kickoff D-V0-01:** **antes da semana 1** (bloqueia MVP até decisão). → F-ÚNICO-1 permanece bloqueada até kickoff concluído; semana 1 não inicia MVP sem kickoff resolvido.
  5. **D-V0-01 para o MVP de 1 semana:** reabrir kickoff de stack/CI antes do MVP (decisão do Mantenedor no grill) — **não** é resolução de D-V0-01 (continua adiado até kickoff); apenas autoriza a reabertura. Requer decisão Classe C formal (D-V0-01) + registro em `docs/DECISIONS.md` como DEC-015+ quando ocorrer.
- **Propostas de resolução (Class B, reversíveis; não aprovadas):**
  - **PR-01 (D-V0-01 restante — infra/CI/gates):** manter D-V0-01 adiado (DEC-006(i)) como baseline; reabrir kickoff antes da semana 1 (conforme grill #4/#5) com escopo mínimo: stack (condicional LangGraph), repo-alvo (este repo — DEC-006(ii)), CI (nenhuma por ora — DEC-006(iii)) e gates (G0–G3 propostos, thresholds lidos do alvo — D-V0-06). Sem kickoff resolvido, F-ÚNICO-1 permanece bloqueada (R8). **Não criar Makefile/pyproject.toml sem decisão Classe C.**
  - **PR-02 (D-V0-02 restante — orçamento formal):** orçamento monetário = zero (grill #1); capacidade = 40h/semana do Mantenedor único; PERT+30% aplicável sobre capacidade confirmada (40h/sem ≈ 8h/dia, 5 dias). Estimativas declaráveis apenas como `[PREMISSA]` com buffer 30%: `E = ((O+4M+P)/6) × 1.3`. **Não prometer prazo sem buffer** (regra vigente).
  - **PR-03 (D-V0-02 restante — cadência de revisão RACI):** revisão RACI/checkpoints **semanal** (grill #2), PM delegado (R) com aprovação do Mantenedor (A) (grill #3). Atualizar `docs/20` §3 e `docs/40` no próximo change set autorizado (propagação pendente). Demais rituais (revisão de backlog/DoR, review de valor/aceite, change control) permanecem sob demanda sem SLA (DEC-006(v)) até nova decisão.
  - **PR-04 (roadmap F-ÚNICO):** manter `docs/47` (proposta condicional) como mapa vigente; F-ÚNICO-0 executável (documental, baixo risco); F-ÚNICO-1 bloqueada até kickoff D-V0-01 + D-V0-03/04/05/06; F-ÚNICO-2 depende de F-ÚNICO-1. Sem PERT declarável para F-ÚNICO-1/2 (depende de D-V0-01/02).
  - **PR-05 (riscos):** manter R1–R11 (`docs/20`) vigentes; reavaliar R8 (D-V0-01 adiado) após kickoff; R4/R10 (capacidade/bus factor) mitigados parcialmente pela confirmação de 40h/sem + cadência semanal; R9 (drift DECISIONS×change control) e R11 (drift 47/48×10/20/30) permanecem abertos até reconciliação. Novo risco registrado: **R12** — "MVP de 1 semana inviável sem kickoff D-V0-01 resolvido (bloqueio ativo)" | A×A (Crítico) | mitigação: kickoff antes da semana 1; modo documental F-ÚNICO-1 | Mantenedor/PM.
  - **PR-06 (cronograma de 1 semana):** condicional ao kickoff D-V0-01 (antes da semana 1). Proposta de 5 dias úteis (40h) com buffer 30% (PERT), modo documental (sem código) até kickoff resolvido:
    | Dia | Atividade | Dono (R) | Aprovador (A) | Est. PERT E (×1.3) |
    |---|---|---|---|---|
    | pré-S1 (D-2…D-1) | Kickoff D-V0-01 (stack/CI/gates) — gate bloqueante | Mantenedor (A/R) | Mantenedor | — (decisão humana) |
    | D1 | Revisão RACI semanal + atualização `docs/40`/`docs/20` §3 | PM (R) | Mantenedor (A) | 0.5d→0.65d |
    | D2 | Consolidação contrato v1.0.0 (proposta) + semântica de estados (PO/PM/TL) | TL (R) | Mantenedor+PO+PM | 1d→1.3d |
    | D3 | Cronograma PERT+30% + DoR/DoD + change control registro | PM (R) | Mantenedor (A) | 1d→1.3d |
    | D4 | Reconciliação `docs/10/20/30` + painel + README + DECISIONS | PM (R) + TL/PO (C) | Mantenedor (A) | 1.5d→1.95d |
    | D5 | Review de valor (PO) + semáforo + checkpoint + riscos | PO (R) + PM (C) | Mantenedor (A) | 0.5d→0.65d |
    - **Total estimado:** ~5.85d equivalente sobre 5d úteis (117% da capacidade) — **sobrecarga**; re-planejar ou reduzir escopo. Marcar `[PREMISSA]` e `[LACUNA]` de capacidade real por dia.
    - **Bloqueio:** se kickoff D-V0-01 não concluído antes da semana 1, toda a semana 1 permanece em F-ÚNICO-0 documental (sem MVP) — R12 ativo.
  - **PR-07 (tracking em `docs/`):** manter `docs/` como trilha (DEC-006(vi)); estados/IDs nos canônicos e no log; critério operacional de `completed` segue `[LACUNA]` (D-V0-05). Cadência de revisão RACI agora semanal (PR-03). Sem board/issue tracker externo.
- **Riscos e premissas:**
  - `[RISCO] R12` (novo) | A×A (Crítico) | MVP de 1 semana inviável sem kickoff D-V0-01 resolvido | mitigação: kickoff antes da semana 1; modo documental F-ÚNICO-1 | Mantenedor/PM
  - `[RISCO] R4/R10` (capacidade/bus factor) | A×M (Alto) | Mantenedor único 40h/sem; cadência semanal pode sobrecarregar | mitigação: reduzir escopo; delegar PM (R) com aprovação (A); re-planejar se total > 100% capacidade | PM/Mantenedor
  - `[RISCO] R9/R11` (drift documental) | M×A (Alto) | DECISIONS×change control; 47/48×10/20/30 | mitigação: propagação pendente registrada; revisão semanal | PM
  - `[PREMISSA-P7]` (nova, operacional) Orcamento monetario = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada; sem custo externo. Teste: capacidade 40h/sem (S08).
  - `[PREMISSA-P8]` (nova, operacional) Cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A). Teste: checkpoint semanal realizado.
  - `[LACUNA]` Capacidade real por dia (não confirmada); total estimado 117% da capacidade (sobrecarga) — re-planejar.
  - `[LACUNA]` Critério operacional de `completed` no tracking alvo (`docs/`) — D-V0-05.
  - `[LACUNA]` Stack/CI/gates (D-V0-01) — kickoff antes da semana 1; não resolvido.
  - `[LACUNA]` Thresholds de gates (D-V0-06) — lidos do projeto-alvo (inexistente).
- **Alternativas consideradas:**
  - (a) Manter D-V0-01 adiado sem kickoff (status quo) — rejeitada pelo Mantenedor no grill (#4/#5); manteria F-ÚNICO-1 bloqueada indefinidamente.
  - (b) Orcamento monetario > 0 — rejeitada pelo Mantenedor no grill (#1); MVP sem custo externo.
  - (c) Cadência "sob demanda" (DEC-006(v)) para RACI — rejeitada pelo Mantenedor no grill (#2); fixar semanal.
  - (d) Materializar cronograma/RACI/riscos como arquivos novos agora — rejeitada: exige aprovação explícita do Mantenedor via subagente de escrita (regra vigente); apenas registro Class B aqui.
  - (e) Marcar DEC-014 como decisão Classe C — rejeitada: este registro é Class B (proposta/reversível); formalização Classe C ocorre quando o Mantenedor confirmar via DEC-015+.
- **Evidência:** grill-with-docs (2 rodadas × 3 perguntas) realizado em 2026-11-16 (respostas do Mantenedor registradas acima); `docs/00` §5/§8; `docs/20` (R1–R11, P1–P6, §3, §6); `docs/40` (RACI, status vigente DEC-002); `docs/47` (F-ÚNICO-0/1/2, bloqueios); `docs/48` (contrato v1.0.0-PROPOSTA); `docs/DECISIONS.md` (DEC-001…DEC-013); AGENTS.md (regras duras); `~/.opencode/references/contrato-resumo-subagentes.md` e `autonomia-e-estados.md` (normativos).
- **Status final:** **registrado — proposta (Class B)** (grill-with-docs concluído; nenhuma aprovação inferida; nenhuma promoção a `approved`/`completed`; materialização de artefatos aguarda aprovação explícita do Mantenedor; propagação para `docs/20` §3, `docs/40`, `docs/00` §8 e `docs/README.md` pendente no próximo change set autorizado).
