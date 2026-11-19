---
title: "DEC-036 — Ratificação docs/00 vigente + fail_under=80 no gate de cobertura"
date: "2026-11-19"
project: "sdlc-agentico"
source: "Mantenedor Lucinei (Classe C, decidido em sessão 2026-11-19)"
status: "vigente"
classe: "C"
decided_by: "Lucinei (Mantenedor)"
human_interaction_ref: "sessão 2026-11-19 (ratificação Classe C; registro desta entrada)"
---

## DEC-036 — Ratificação docs/00 vigente + fail_under=80 no gate de cobertura

- **Data:** 2026-11-19
- **Classe:** C
- **Decisão:** o Mantenedor (Lucinei) ratificou explicitamente, em sessão 2026-11-19, dois itens: (1) `docs/00-painel-gerencial-consolidado.md` = **vigente**; (2) `pyproject.toml` `tool.coverage.report.fail_under = 80` (e `--cov-fail-under=80` em `addopts`) = **ratificado**, substituindo o fail_under=50 de DEC-018/DEC-022.

### a) Contexto

- **Divergência detectada (fatia Classe B de 2026-11-18/19):** o front matter de `docs/00-painel-gerencial-consolidado.md` declarava `status: "vigente"` (e `last_reviewed: "2026-11-18"`), enquanto o índice `docs/README.md` listava o mesmo artefato com status `condicional`. Divergência registrada; desempate exige decisão humana Classe C (proibição de resolver silenciosamente).
- **`pyproject.toml` pré-modificado:** na sessão 2026-11-19, o `pyproject.toml` já se encontrava com `fail_under = 80` (`[tool.coverage.report]`) e `addopts = "-ra --cov=src --cov-report=term-missing --cov-fail-under=80"` (`[tool.pytest.ini_options]`), com comentário de ratificação Classe C apontando para esta DEC-036 — a alteração estava pendente de ratificação explícita do Mantenedor.
- **Aprovação:** o Mantenedor Lucinei, em sessão 2026-11-19, ratificou ambos os itens (Classe C). Esta é a decisão Classe C que formaliza a ratificação.

### b) Decisão (2 itens)

1. **`docs/00-painel-gerencial-consolidado.md` = `vigente`** — reconcilia a divergência (front matter `vigente` × índice `docs/README.md` `condicional`). O índice (`docs/README.md`) passa a refletir `vigente` para este artefato.
2. **`pyproject.toml` `fail_under = 80`** (`tool.coverage.report.fail_under`) **e** `--cov-fail-under=80` em `addopts` — **ratificados**; substituem o fail_under=50 estabelecido por DEC-018/DEC-022. O gate de cobertura do repo passa a exigir ≥ 80%.

### c) Evidência

- **Gate verificado VERDE nesta sessão (2026-11-19):** `make audit-g2` **exit 0** (ruff + mypy `src` + pytest com cobertura ≥ `fail_under` lido do `pyproject.toml` + SAST `ruff --select S src/`).
- **Suíte:** **177 testes** passando; **cobertura 93,94%** (≥ fail_under=80).
- **Diff `pyproject.toml`:** `fail_under` 50 → 80 em `[tool.coverage.report]`; `--cov-fail-under=80` em `addopts`; cabeçalho do arquivo (`cobertura >= 80%`); comentário de ratificação Classe C (2026-11-19, DEC-036) junto a `[tool.mypy]`.
- **Testes novos:** `tests/test_coverage_boost.py` (fatia de testes escrita por subagente; nenhum `src/` alterado; teste acoplado `test_stubs_sqlite_and_pyproject` (em `tests/test_phase1_langgraph.py`) tornado threshold-agnostic — lê o `fail_under` real do `pyproject.toml`).
- **[LACUNA]:** identificador formal de interação (ex.: `decision_id`/`human_interaction_ref` estruturado) não consta no registro disponível; a decisão está ancorada na sessão 2026-11-19 (Classe C) informada pelo Mantenedor. Horário exato da sessão: [LACUNA].

### d) Consequências

- `docs/README.md`: índice atualizado — `00-painel-gerencial-consolidado.md` passa a `vigente`; contagens de corpos/índice (`DECISIONS.md` e `decisions/`) atualizadas para DEC-036; data da última atualização → 2026-11-19.
- `docs/DECISIONS.md`: índice atualizado para DEC-036 (tabela-índice, cabeçalho, ponteiros); data do front matter → 2026-11-19.
- `docs/00-painel-gerencial-consolidado.md`: banner `> **O que é:** ...` atualizado — documento `vigente` no índice (ratificado pelo Mantenedor 2026-11-19 — DEC-036). Nenhum outro trecho alterado.
- `docs/schemas/painel-status.json`: rederivado/atualizado de forma coerente (derivado; `derivation_note` inalterada) — `decisions_log` (DEC-001..036 + entrada DEC-036), `aggregation_status.phase` (177 testes, 93,94%) e `proxima_acao_recomendada` (estado atual) atualizados; fatos históricos de DEC-030/DEC-033/DEC-035 mantêm os números originais.
- `AGENTS.md`: apenas menções de "índice vigente"/contagens de DEC atualizadas para DEC-036 (sem outras alterações).
- **Nada mais promovido:** nenhum outro artefato/status foi alterado ou promovido por esta decisão.

### e) Regra de ouro (mantida)

Execução ≠ `completed` ≠ `approved`. Esta DEC-036 **não** promove E4, KPIs, G3, CR-009-C, CR-010-C, DRAFT `completed`, nem nenhum outro artefato/status. Aceite de valor permanece ato exclusivo do PO; KPIs seguem lacuna; demais bloqueios mantidos. Entradas anteriores do log (DEC-001…DEC-035) **NÃO reescritas** (append-only).

- **Decisão tomada em:** sessão 2026-11-19 pelo Mantenedor Lucinei (Classe C).
