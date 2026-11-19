---
title: "DEC-037 — Reorganização do SoT de agente para `.agents/`"
date: "2026-11-19"
project: "sdlc-agentico"
source: "Mantenedor Lucinei (Classe C, decidido em sessão 2026-11-19)"
status: "vigente"
classe: "C"
decided_by: "Lucinei (Mantenedor)"
human_interaction_ref: "sessão 2026-11-19 (Classe C; registro desta entrada)"
---

## DEC-037 — Reorganização do SoT de agente para `.agents/`

- **Data:** 2026-11-19
- **Classe:** C
- **Decisão:** o Mantenedor (Lucinei) decidiu, em sessão 2026-11-19, reorganizar o SoT (Source of Truth) de agente do repo: a documentação consumida/produzida por agentes passa a residir em **`.agents/`** (padrão de mercado), separando-a da documentação voltada ao público humano (`docs/`). Esta é a decisão Classe C que formaliza a reorganização (Opção A, aprovada).

### a) Contexto

- **Necessidade:** separar público humano (`docs/`) de agente (`.agents/`) — padrão de mercado para repositórios com agentic SDLC.
- **Mapa de referências (pré-migração) mostrou:** gate de teste com paths hard-coded (`docs/DECISIONS.md`, `docs/decisions/`, `docs/schemas/painel-status.json`); `tools/` com default schema path; **158 refs textuais** distribuídas pelo repo.
- **Aprovação:** o Mantenedor Lucinei, em sessão 2026-11-19, aprovou a reorganização (Opção A). Esta DEC-037 formaliza a execução.

### b) Decisão (Opção A aprovada)

1. **Movimentos (com `git mv`, preservando histórico):**
   - `docs/DECISIONS.md` → `.agents/DECISIONS.md`
   - `docs/decisions/` → `.agents/decisions/`
   - `docs/schemas/` → `.agents/schemas/`
   - `docs/examples/` → `.agents/examples/`
2. **Stubs não-canônicos** nos caminhos antigos mais citados: `docs/DECISIONS.md` (stub) e `docs/decisions/README.md` (stub) — redirecionantes; não são fonte de verdade; não editar.
3. **Reescrita path-only** de refs em arquivos editáveis (AGENTS.md, docs/ vivos, ADRs vivos, ONBOARDING, testes, tools, `src` — `DEFAULT_SCHEMA_PATH` path-only).
4. **Imutáveis intocados:** `docs/historico/**` e os corpos `.agents/decisions/DEC-*.md` — refs stale aceitas **por design** (append-only / histórico imutável).
5. **Gate verificado VERDE (fatia anterior, 2026-11-19):** `make audit-g2` **exit 0** (ruff + mypy `src` + pytest com cobertura ≥ `fail_under` lido do `pyproject.toml` + SAST `ruff --select S src/`) — **177 testes**, **cobertura 93,94%**.
6. **Nenhuma promoção adicional de status:** E4, KPIs, G3, DRAFT `completed`, CR-009-C/CR-010-C permanecem intocados.

### c) Evidência

- **`git status`** (fatia anterior): renames staged `R`/`RM` para `.agents/DECISIONS.md`, `.agents/decisions/**`, `.agents/schemas/painel-status.json` (e demais schemas/examples); stubs `docs/DECISIONS.md` e `docs/decisions/README.md` criados.
- **`make audit-g2` exit 0** — 177 testes, cobertura 93,94% (≥ fail_under=80, lido do `pyproject.toml`).
- **Grep residual:** nenhuma ref a `docs/DECISIONS.md` / `docs/decisions/` / `docs/schemas/` / `docs/examples/` fora das categorias permitidas (stubs redirecionantes; corpos `.agents/decisions/DEC-*.md` append-only; `docs/historico/**` imutável; `historico_commits.log` — log histórico, não canônico).
- **[LACUNA]:** identificador formal de interação (ex.: `decision_id`/`human_interaction_ref` estruturado) não consta no registro disponível; a decisão está ancorada na sessão 2026-11-19 (Classe C) informada pelo Mantenedor. Horário exato da sessão: [LACUNA].

### d) Consequências

- `.agents/DECISIONS.md`: índice atualizado para DEC-001…DEC-037 (tabela-índice, cabeçalho, ponteiros); front matter `date` → 2026-11-19.
- `.agents/schemas/painel-status.json` (derivado): `decisions_log` atualizado para DEC-001..037 (+ entrada DEC-037); `proxima_acao_recomendada` acrescenta nota de DEC-037; fatos históricos mantidos.
- `docs/README.md`: contagens (`DEC-001…DEC-037`; `37 corpos`; `38 arquivos`) e menções de índice vigente atualizadas para DEC-037; linha do índice referente a `.agents/DECISIONS.md`/`decisions/` menciona DEC-037.
- `AGENTS.md`: menções de "índice vigente"/contagens atualizadas para DEC-037.
- Índice e derivados consistentes com DEC-001…DEC-037.
- **Nada mais promovido:** nenhum outro artefato/status foi alterado ou promovido por esta decisão.

### e) Regra de ouro (mantida)

Execução ≠ `completed` ≠ `approved`. Esta DEC-037 **não** promove E4, KPIs, G3, CR-009-C, CR-010-C, DRAFT `completed`, nem nenhum outro artefato/status. Aceite de valor permanece ato exclusivo do PO (E1–E3, DEC-030). KPIs seguem lacuna; demais bloqueios mantidos. Entradas anteriores do log (DEC-001…DEC-036) **NÃO reescritas** (append-only).

- **Decisão tomada em:** sessão 2026-11-19 pelo Mantenedor Lucinei (Classe C).
