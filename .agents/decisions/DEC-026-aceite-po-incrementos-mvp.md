---
title: "DEC-026 — Aceite de valor PO — incrementos MVP (E1–E3)"
date: "2026-11-17"
project: "sdlc-agentico"
status: "Materializado (Classe C, 2026-11-17)"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-026 — Aceite de valor do PO para incrementos MVP (Classe C, 2026-11-17)

- **Contexto:** F-ÚNICO-2 (Evolução) exige formalização do aceite de valor do PO para os incrementos MVP (E1–E3), com critérios de aceite (AC Given/When/Then) completos e handoff PR→aceite PO documentado. A revisão PO dos designs t1–t5 (`ses_e1b33e791ffeK0gwIR9QY7Y7z5`) apontou como lacunas: handoff PR→aceite PO inexistente, AC Given/When/Then ausentes nos designs e KPIs não instrumentáveis. DEC-024 consolidou a baseline v0 e iniciou F-ÚNICO-2; D-V0-03 aprovado e materializado (DEC-019) mantém `approved` de valor pendente de aceite explícito do PO (execução ≠ valor).
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **MATERIALIZAR o aceite de valor do PO para incrementos MVP** como trilha documental e de governança, sem declarar `approved` de nenhum incremento:
  1. **AC Given/When/Then completos para E1–E3** registrados em `docs/11-visao-mvp-v0.md` §"Aceite de Valor (PO)" (fonte canônica do aceite de valor) e referenciados em `docs/10-produto-po-visao-mvp-baseline-v0.md` §4/§0.1.
  2. **Handoff PR→aceite PO** documentado (PR criado → evidência anexada → PO revisa → decisão `approved`/`rejected` → feedback estruturado), com SLA sob demanda sem SLA formal (DEC-006(v)).
  3. **KPIs (KPI-1 a KPI-6) calibrados para F-ÚNICO-2** em `docs/10` e `docs/11` (KPI-4/KPI-5 passam de `[LACUNA]` para metas propostas a calibrar).
  4. **`approved` é exclusivo do PO com evidência** — nenhum agente (orquestrador, PO-as-proposta, PM, TL, subagentes) pode inferir ou declarar `approved`; a transição `pending → approved` exige `evidence` verificável e `human_interaction_ref` quando a decisão for tomada por interação humana (Classe C). `rejected → pending` somente com nova evidência.
  5. **Decision/Acceptance v0** preservado: `pending | approved | rejected`; `approved` terminal (exige `evidence` + `decided_by=PO` + `decided_at`); `rejected` exige `rationale` + `decided_by=PO` + `decided_at`.
- **Nota:** `approved` de valor permanece pendente de aceite formal de execução — a materialização documental (AC + handoff + KPIs) não equivale a `approved` de nenhum incremento. A transição `pending → approved` exige evidência verificável e `human_interaction_ref` (Classe C).
- **Evidência:** AC Given/When/Then definidos (docs/11 §"Aceite de Valor (PO)" — E1 H1.1–H1.3, E2 H2.1–H2.2, E3 H3.1–H3.3); handoff PR→aceite PO documentado (docs/11 §C); KPIs calibrados (docs/10 §4, docs/11 §KPIs); revisão PO dos designs t1–t5 (`ses_e1b33e791ffeK0gwIR9QY7Y7z5`); DEC-019 (D-V0-03 materializado); DEC-024 (baseline v0 publicada, F-ÚNICO-2 iniciada).
- **Lacuna:** aceite formal pendente de execução (pending → approved) — nenhum incremento MVP (E1–E3) foi declarado `approved`; a transição exige evidência verificável e `human_interaction_ref` (Classe C), a ser registrada em `docs/DECISIONS.md` como DEC-* quando ocorrer. Identificadores correlacionáveis/storage de trilha (E4) e critério operacional de `completed` no tracking alvo permanecem `[LACUNA]`.
- **Referência:** DEC-019 (D-V0-03), DEC-024 (baseline v0/F-ÚNICO-2), DEC-006 (iv)-(vi) (mantenedor único, cadência sob demanda, tracking = docs/), docs/10, docs/11, docs/48 (semântica de estados).
- **Status final:** **Materializado (Classe C, 2026-11-17)** — trilha documental/governança do aceite de valor do PO; nenhum incremento declarado `approved`; `approved` permanece exclusivo do PO com evidência.
