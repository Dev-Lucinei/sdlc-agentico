---
title: "DEC-031 — Bifurcação do log de decisões"
date: "2026-11-18"
project: "sdlc-agentico"
status: "vigente (Classe C, 2026-11-18)"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-031 — Bifurcação do log de decisões (índice vigente + corpos append-only)

- **Data:** 2026-11-18
- **Classe:** C
- **Decisão:** bifurcar `docs/DECISIONS.md` em índice vigente (`docs/DECISIONS.md`, contendo apenas regra de ouro condensada + tabela-índice + ponteiros) + corpos append-only em `docs/decisions/DEC-NNN-<slug>.md` + quarentena `docs/decisions/arquivo-2026-11-16.md` (seções stale preservadas verbatim).
- **Contexto:** auditoria de complexidade documental (respostas do Mantenedor 2026-11-18; Fases A/B aprovadas e executadas). O log monouso havia crescido a ~704 linhas / ~21–24k tokens, estourando o contexto de 8k.
- **Alternativas rejeitadas:**
  - (a) Manter log monouso (status quo — estoura o contexto de 8k).
  - (b) Apagar seções stale (viola append-only).
  - (c) Promover corpos a status vigente (Classe C requer decisão própria).
- **Consequências:** leitura obrigatória cai de ~21–24k para ~4k tokens; rastreabilidade via `git log --follow` + `docs/decisions/arquivo-2026-11-16.md`; corpos permanecem append-only em `docs/decisions/`; o contrato de leitura do repo é preservado (`docs/DECISIONS.md` continua o arquivo citado por tudo no repo); seções stale congeladas em `docs/decisions/arquivo-2026-11-16.md` (não usar como referência de estado vigente).
- **Decisão tomada em:** sessão OpenCode 2026-11-18 pelo Mantenedor (resposta interativa).
- **Autorização:** execução condicionada a `make audit` = exit 0.
