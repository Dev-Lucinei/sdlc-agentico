---
title: "DEC-004 — LICENSE: nenhuma por ora"
date: "2026-11-16"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-004 — LICENSE: nenhuma por ora (CR-003)

- **Contexto:** `LICENSE` ausente no repo (verificado em 2026-11-16; adendo §8.2 do painel). A auditoria externa tratou a ausência como falha objetiva; não é: é decisão explícita do Mantenedor.
- **Decisão:** **nenhuma LICENSE por ora**. O repositório mantém a proteção padrão de copyright — **todos os direitos reservados**. Qualquer licenciamento futuro exige nova decisão Classe C do Mantenedor.
- **Alternativas consideradas:**
  - (a) MIT / Apache-2.0 / GPL / outra licença permissiva ou copyleft — todas rejeitadas por ora (decisão explícita de não licenciar).
  - (b) Arquivo `LICENSE` com texto proprietário/"todos os direitos reservados" — rejeitada: redundante; o default legal já opera sem arquivo.
  - (c) Licenciar apenas docs vs. código futuro separadamente — rejeitada por ora: sem stack/repo-alvo de código (D-V0-01 adiado), não há o que licenciar em separado.
- **Consequências:** terceiros não têm permissão de uso, cópia ou distribuição; o repo permanece documental/privado na prática; nenhuma mudança de arquivo é necessária; se/quando houver release público ou contribuição externa, será necessária nova decisão Classe C (e provável D-V0-01 resolvida antes).
- **Evidência:** verificação de ausência de `LICENSE` em 2026-11-16 (registrada no adendo §8.2 de `docs/00`); decisão explícita do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C, decisão explícita).
