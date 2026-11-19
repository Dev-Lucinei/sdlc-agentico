---
title: "DEC-002 — docs/40 RACI validado como vigente (CR-001)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-002 — `docs/40-operacao-raci-repo-v0.md` validado como vigente (CR-001)

- **Contexto:** `docs/40` criado em 2026-11-13 com status `condicional`, explicitamente pendente de validação do Mantenedor (suas "Próximas Ações" #1). A divergência índice↔painel (40 ausente do painel) foi corrigida no adendo §8.2 de `docs/00` (painel passou a referenciar `docs/40`).
- **Decisão:** validar `docs/40-operacao-raci-repo-v0.md` como **vigente** (Classe C, decided_by Lucinei, 2026-11-16). A matriz RACI das operações do repo passa a ser referência vigente para operação documental.
- **Alternativas consideradas:**
  - (a) Manter `condicional` — rejeitada: a validação do Mantenedor foi concedida nesta data.
  - (b) Migrar o conteúdo para `AGENTS.md` ("Fontes de verdade") e remover `docs/40` — rejeitada por ora: `AGENTS.md` fora do escopo de alteração desta sessão; permanece como opção futura (40 §Próximas Ações #2/#3).
  - (c) Remover o arquivo — rejeitada: artefato válido e referenciado.
- **Consequências:** `docs/40` vigente para operação do repo; linhas 9, 10 e 12–14 continuam exigindo humano (Classe C); nenhuma linha autoriza inferir `approved`. **Propagação pendente:** o front matter de `docs/40` ainda exibe `status: "condicional"`, e o índice/painel ainda o descrevem como condicional — a atualização desses três pontos exige change set designado (fora do escopo desta sessão). Ver "Propagação pendente".
- **Evidência:** `docs/40-operacao-raci-repo-v0.md` (conteúdo integral lido em 2026-11-16); `docs/README.md` (linha do índice); `docs/00` §8.2 (adendo que referencia `docs/40`); decisão do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C). Nota honesta: o canônico `docs/40` em si ainda não foi editado para refletir a vigência — ver "Propagação pendente".
