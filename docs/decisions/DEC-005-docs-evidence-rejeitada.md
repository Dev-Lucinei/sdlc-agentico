---
title: "DEC-005 — Criação de docs/evidence/ REJEITADA (CR-004)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-005 — Criação de `docs/evidence/` REJEITADA (CR-004)

- **Contexto:** a auditoria externa propôs `docs/evidence/` como repositório de evidências de execução/aceite. A proposta criaria uma **segunda source-of-truth** paralela ao painel/índice/canônicos, antes de existirem contrato canônico (D-V0-05) e política de gates/thresholds (D-V0-06). A convergência PO/PM/TL (adendo §8.2) foi de recusa.
- **Decisão:** **rejeitar a criação de `docs/evidence/`** (decisão Classe C, decided_by Lucinei, 2026-11-16). Evidências permanecem **embutidas nos artefatos canônicos** (seções de evidência) ou **referenciadas por link rastreável** a partir do item/decisão. Reavaliação somente junto de D-V0-05/D-V0-06 e por nova decisão humana.
- **Alternativas consideradas:**
  - (a) Criar `docs/evidence/` agora — rejeitada: segunda SoT; sem contrato/gates não há critério do que é evidência canônica.
  - (b) `docs/governance/evidence/` ou similar — rejeitada: mesma classe de problema; estrutura de diretórios indefinida (`[PREMISSA]` pendente de Classe C).
  - (c) Evidências embutidas/por link (escolhida) — consistente com DoD do `docs/20` §DoD ("sem evidência não há `done`") e com o painel.
- **Consequências:** nenhum diretório novo é criado; todo `done`/aceite deve carregar evidência embutida ou link rastreável no próprio artefato; auditorias futuras não podem exigir `docs/evidence/`; risco de evidências dispersas mitigado por rastreabilidade item↔decisão↔evidência (quando tracking existir — DEC-006(vi)).
- **Evidência:** `docs/00` §8.2 (vereditos convergentes PO/PM/TL; recusa registrada); `docs/20` §5 (DoD/change control); decisão do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C — rejeição).
