---
title: "DEC-007 — Política de segredos permanece [LACUNA] (CR-011)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "registrado — `[LACUNA]` aberta"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-007 — Política de segredos permanece `[LACUNA]`; reavaliar após D-V0-01 (CR-011)

- **Contexto:** a fila de CRs pós-auditoria (`docs/00` §8.2) inclui política de segredos. Sem stack/infra/repo-alvo de código definidos (D-V0-01 adiado — DEC-006(i)), não há o que escanear, rotacionar ou isolar; fixar política agora seria inventar contexto.
- **Decisão (registro, não aprovação):** nenhuma política de segredos é adotada. Permanece **`[LACUNA]`**. **Gatilho de reavaliação: decisão futura de D-V0-01** (quando a stack for definida) ou decisão explícita do Mantenedor, o que ocorrer primeiro.
- **Alternativas consideradas:**
  - (a) Adotar já `.env.example` + secret scanning + rotação — rejeitada: sem stack/código; teatro de segurança sem alvo.
  - (b) Declarar "não há segredos neste repo" como política — rejeitada sem decisão Classe C; e a afirmação seria frágil (credenciais locais/futuro código).
  - (c) `[LACUNA]` com gatilho explícito (escolhida).
- **Consequências:** risco residual registrado (segredo commitado por engano permanece possível — mitigação atual: revisão humana em todo commit, linha 12 do `docs/40`); nenhum controle automatizado existe hoje; a decisão definitiva exige Classe C quando D-V0-01 ocorrer.
- **Evidência:** `docs/00` §8.2 (fila de CRs, CR-011); DEC-006(i); `docs/40` linha 12.
- **Status final:** **registrado — `[LACUNA]` aberta** (Classe B — registro; **não** é decisão de aprovação; nenhuma política em vigor).
