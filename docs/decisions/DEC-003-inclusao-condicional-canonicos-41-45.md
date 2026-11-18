---
title: "DEC-003 — Inclusão condicional dos canônicos 41–45 + normativos por caminho+sha256"
date: "2026-11-16"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-003 — Inclusão condicional dos canônicos 41–45 na baseline v0 + normativos externos por caminho+sha256 (CR-002B + CR-005B)

- **Contexto:** os canônicos de design t1–t5 (`docs/41`–`docs/45`, criados em 2026-11-16) receberam 5× `concordo_com_ressalvas` (PO e PM) e permanecem proposta documental condicional. O change request de inclusão na baseline v0 estava pendente desde o adendo §8.1 do painel. A auditoria externa chegou a propor **cópia física** de normativos externos para dentro do repo — proposta recusada (criaria drift / segunda SoT).
- **Decisão (dois pontos, ambos Classe C, decided_by Lucinei, 2026-11-16):**
  1. **Inclusão condicional** dos canônicos `41`–`45` na baseline v0. *Inclusão ≠ aprovação de conteúdo.* O conteúdo permanece proposta de design condicional (stack LangGraph não aprovada — ver DEC-006(i) e D-V0-01; gates/thresholds — D-V0-06). Promoção de conteúdo exige D-V0-04 (baseline técnica) e demais decisões Classe C.
  2. **Normativos externos referenciados por caminho+sha256 abreviado, sem cópia física** no repo. Registrados:
     - `~/.opencode/references/contrato-resumo-subagentes.md` — sha256 abreviado `163e0aad…` `[PREMISSA]`
     - `~/.opencode/references/autonomia-e-estados.md` — sha256 abreviado `776af494…` `[PREMISSA]`
     - *Nota:* os hashes completos **não** são fixados nesta data; devem ser recalculados pelo TL no próximo change set se o Mantenedor quiser pin exato. Verificação de 2026-11-16 (`sha256sum`): os prefixos acima conferem com os arquivos vivos no ambiente.
- **Alternativas consideradas:**
  - (a) Cópia física dos normativos no repo — rejeitada: drift garantido, segunda SoT, viola decisão do Mantenedor.
  - (b) Vendoring via submódulo/pacote — rejeitada: sem remote configurado; complexidade injustificada para 2 arquivos de referência.
  - (c) Excluir 41–45 da baseline v0 — rejeitada: são proposta condicional válida, revisada com ressalvas; exclusão perderia rastreabilidade.
  - (d) Aprovar o conteúdo/stack junto com a inclusão — rejeitada: exigiria D-V0-01 (adiado — DEC-006(i)) e D-V0-04; `inclusão ≠ aprovação`.
- **Consequências:** a baseline v0 passa a **incluir como propostas condicionais** os canônicos 00–45 (mais `DECISIONS.md` e a ata `docs/46`); nenhuma promoção de conteúdo é inferida; normativos permanecem vivos fora do repo, com risco de drift mitigado por referência+hash abreviado (pin exato pendente de decisão); qualquer mudança nos normativos externos invalida a referência até re-registro.
- **Evidência:** `docs/41`–`docs/45`; `docs/00` §8.1 (revisões PO/PM, 5× concordo_com_ressalvas) e §8.2 (recusa de cópia física); `docs/README.md` (índice 41–45); `sha256sum` local em 2026-11-16 (prefixos `163e0aad…` e `776af494…` conferem); decisão do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C) — para a *inclusão condicional* e a *política de referência por caminho+sha256*; o conteúdo de 41–45 permanece **condicional**.
