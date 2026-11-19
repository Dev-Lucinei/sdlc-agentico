---
title: "DEC-035 — Aceite do piloto manual mínimo + proposta de faixa de KPIs (Classe C)"
date: "2026-11-18"
project: "sdlc-agentico"
source: "Mantenedor Lucinei (sessão OpenCode 2026-11-18, perguntas interativas — 'Sim, aceito o piloto'; 'Propor instrumentação mínima')"
status: "vigente"
classe: "C"
decided_by: "Lucinei (Mantenedor)"
human_interaction_ref: "sessão OpenCode 2026-11-18 (perguntas interativas — aceite do piloto; faixa de KPIs proposta)"
---

## DEC-035 — Aceite do piloto manual mínimo + proposta de faixa de KPIs (Classe C)

- **Data:** 2026-11-18
- **Classe:** C
- **Decisão:** o Mantenedor (Lucinei) decidiu explicitamente, em sessão OpenCode 2026-11-18 (perguntas interativas), **"Sim, aceito o piloto"** (aceite do resultado do piloto manual mínimo) e **"Propor instrumentação mínima"** (faixa de KPIs proposta — NÃO aprovada, nada implementado).

### a) Contexto

DEC-034 (2026-11-18, Classe C) desbloqueou o piloto manual mínimo, determinando que "o registro pós-execução (tempo de revisão, retrabalho e aceite) será feito no fechamento da sessão, sob decisão do Mantenedor". O piloto foi executado **nesta sessão** (2026-11-18): a própria resolução dos **gaps 2.1–2.4 da crítica externa** (demanda real do Mantenedor).

### b) Registro do piloto (dados literais)

- **Janela:** sessão 2026-11-18 (~21:24–22:35 -03).
- **Demanda real do Mantenedor:** "Resolver os gaps identificados" (gaps 2.1–2.4) da crítica externa.
- **Execução:** subagentes code-implementer (correções A→D), quality-gate-scaffold (`tests/test_status_drift.py`), session-commit.
- **Gates:** `make audit` exit 0 antes e depois; suíte 100 → 104 testes (novos 4 de drift); cobertura 79,02% ≥ fail_under=50; `make lint` exit 0.
- **Commits locais (sem push):** `92a17ec` (docs gaps 2.1/2.3), `17f8297` (teste guarda drift), `7193647` (DEC-034 piloto desbloqueado).
- **Retrabalho:** 1 iteração de lint (E501 no teste novo — corrigido na mesma sessão pelo quality-gate-scaffold).
- **Falha(s):** 1 (E501, tipo flaky/ambiente trivial).
- **Desvio estrutural:** o gate canônico `~/.agents/AGENTS.md`/`~/.agents/orchestrator.py` NÃO existe no ambiente — verificações substituídas pelos gates nativos do repo (`make lint`/`make test`/`make audit`). Compliance-audit indisponível (caminho da skill inexistente) — não invocado.
- **Trechos stale detectados pela revisão pós-tarefa** (painel §8; contagens) — corrigidos no fechamento (DEC-034).
- **Aceite do resultado do piloto:** Mantenedor Lucinei, 2026-11-18, pergunta interativa ("Sim, aceito o piloto"). O aceite **NÃO** promove valor/E4/KPIs/nenhum artefato (semântica de estados mantida).

### c) Aceite

O Mantenedor (Lucinei), em 2026-11-18, na sessão OpenCode 2026-11-18 (pergunta interativa), **aceitou o resultado do piloto manual mínimo**. O aceite aplica-se **exclusivamente ao resultado do piloto** (registro acima). **Nenhuma execução/artefato é promovido a `completed`/`approved` por esta decisão**; aceite de valor permanece ato exclusivo do PO; E4 e demais artefatos seguem não aprovados (DEC-030). Semântica de estados mantida: execução ≠ `completed` ≠ `approved`.

### d) Proposta mínima de KPIs instrumentáveis (NÃO APROVADA)

**Nada implementado agora.** Proposta enviada para **Classe C própria na próxima sessão**; até a decisão, KPIs seguem lacuna (DEC-026/DEC-030).

KPIs propostos:

1. **tempo de revisão humana por demanda** (min);
2. **nº de iterações de retrabalho por entrega**;
3. **taxa de aceite pelo PO** (aceitas/rejeitadas);
4. **lead time demanda→entrega** (dias).

**Instrumentação proposta:** reuso da telemetria local existente (`src/observability.py` — JSON logs + `Metrics` in-memory; `correlation_id`) + git/log de decisões — **SEM ferramenta/plataforma externa e SEM processo novo** (consistente com DEC-029).

**Custo estimado:** 1–1,5 dia. **Classe C ao decidir; Classe B ao implementar, se aprovado.**

### e) O que NÃO muda (todos inalterados)

KPIs seguem **lacuna** até a decisão (Classe C própria, próxima sessão); E4; G3; CR-009-C; CR-010-C; DRAFT critério `completed`; LAC-IDEMP-02..05; adoção de ferramenta de tracking (externa) — todos inalterados. `docs/48-contrato-canonico-v1-0-0.md` intocado. `docs/decisions/DEC-001…034` e `arquivo-2026-11-16.md` **NÃO reescritos** (append-only).

- **Decisão tomada em:** sessão OpenCode 2026-11-18 pelo Mantenedor (respostas interativas — "Sim, aceito o piloto"; "Propor instrumentação mínima").
