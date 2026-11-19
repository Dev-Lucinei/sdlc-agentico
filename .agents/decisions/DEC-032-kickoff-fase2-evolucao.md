---
title: "DEC-032 — Kickoff formal da Fase 2 (F-ÚNICO-2, Evolução)"
date: "2026-11-18"
project: "sdlc-agentico"
status: "vigente"
classe: "C"
decided_by: "Lucinei (Mantenedor)"
human_interaction_ref: "sessão OpenCode 2026-11-18 (pergunta interativa — 3 respostas: P10 confirmada; fatia Classe B autorizada; DEC-032 de baseline)"
source: "sessão OpenCode 2026-11-18 (pergunta interativa do Mantenedor)"
---

## DEC-032 — Kickoff formal da Fase 2 (F-ÚNICO-2, Evolução)

- **Data:** 2026-11-18
- **Classe:** C
- **Decisão:** kickoff formal da trilha de Evolução (F-ÚNICO-2) registrado como decisão Classe C do Mantenedor.

### a) [PREMISSA-P10] CONFIRMADA

Capacidade do Mantenedor **CONFIRMADA**: ~4–8h/sem (≈ 0,5–1 dia útil/sem), cadência sob demanda, **sem SLA**. DEC-027 e DEC-029 permanecem vigentes.

### b) Escopo autorizado agora (Classe B)

- **Onda 1:** F2.1 (reconciliar backlog E1–E4, tracking `docs/`) + F2.4 (riscos/change control).
- **Onda 2:** F2.2 remanescente (calibrar KPI-4/KPI-5 com dados reais ≥2 iterações ou re-registrar lacuna; corrigir stale de F2.2 em `docs/20`).
- **Fatia técnica Classe B:**
  - F2.0 — corrigir `docs/00` §1 linha 39 (stale × DEC-025).
  - F2.1-téc — `make audit-g2` parametrizado, thresholds lidos do `pyproject.toml`.
  - F2.2-téc — SQLite hardening: WAL/busy_timeout/foreign_keys + `verify_chain()` + testes de corrupção.
  - F2.4-téc — idempotência/dedupe e2e.
  - F2.3-téc — observabilidade mínima: logs JSON + `correlation_id`, sem backend externo.
  - F2.5-téc — mypy incremental endurecido por módulo + limpeza de aliases de `quality_gates.py`; **SEM alterar `fail_under`**.
  - F2.7-téc — ADR draft **NÃO numerado** sobre critério operacional de `completed` + DoD G2→G3 (promoção a `accepted` = Classe C futura).

### c) Gates de saída propostos

- **G-F2-1 (processo):** F2.1 + F2.2 remanescente `done` com evidência.
- **G-F2-2 (qualidade):** `make audit` + `audit-g2` exit 0; cobertura ≥ `fail_under` do `pyproject.toml`; 0 erros críticos.
- **G-F2-3 (valor):** F2.5 Decision/Acceptance do PO por incremento — nunca por inferência.
- **G-F2-4 (fechamento):** painel §0/§1 + `docs/schemas/painel-status.json` + `docs/README.md` consistentes.

Gates têm efeito de governança; **promoção de status do semáforo é decisão humana**.

### d) EXPLICITAMENTE FORA DE ESCOPO (bloqueados até nova decisão Classe C)

- E4/F2.3 (DEC-030);
- G3 verde/operacional e piloto multi-papel como marco;
- LangGraph (CR-009-C, DEC-018);
- CI externo (DEC-018);
- adoção de tracking externo GitHub Issues/Projects (CR-010-C, DEC-027);
- alteração de thresholds (`fail_under=50`, DEC-018/DEC-022);
- promoção de KPIs/metas a `approved`;
- promoção de visão/MVP;
- LICENSE;
- `docs/evidence/` (DEC-005).

### e) Calendário honesto

Sem E4: ~4–8 semanas; com a fatia técnica completa: ~9–18 semanas (≈37 dias-esforço PERT+30%). Nenhuma data prometida; rolling-wave com re-baseline por checkpoint.

### f) Governança escalonada (DEC-029)

Classe B reversível sem cerimônia adicional; Classe C sempre humana e registrada.

- **Decisão tomada em:** sessão OpenCode 2026-11-18 pelo Mantenedor (resposta interativa — 3 respostas: P10 confirmada; fatia Classe B autorizada; DEC-032 de baseline).
- **Autorização:** execução da fatia Classe B autorizada; itens da seção (d) permanecem bloqueados.
