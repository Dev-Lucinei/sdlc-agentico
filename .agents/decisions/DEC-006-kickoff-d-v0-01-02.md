---
title: "DEC-006 — Kickoff D-V0-01/02 — 6 decisões Classe C"
date: "2026-11-16"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-006 — Kickoff D-V0-01/02 (realizado em 2026-11-16): 6 decisões Classe C (decided_by Lucinei, 2026-11-16)

- **Contexto:** lacunas D-V0-01 (stack/repo/infra/CI/gates) e D-V0-02 (stakeholders/capacidade/prazo/cadência/tracking) abertas desde a agregação inicial (`docs/00` §5). Kickoff realizado em 2026-11-16 — ata: `docs/46-ata-kickoff-d-v0-01-02-v0.md`. Todas as 6 decisões abaixo são **Classe C**, decided_by **Lucinei (Mantenedor)**, 2026-11-16:
  1. **D-V0-01 ADIADO** — stack **não** definida; LangGraph permanece **condicional** (canônicos 41–45, DEC-003); implementação **não iniciada**.
  2. **Repositório-alvo** da implementação futura = **este mesmo repositório** (`sdlc-agentico`).
  3. **Infra/CI = nenhuma por ora.** Quando houver, será de baixo risco (F0–F1); repo permanece **sem remote configurado**.
  4. **Stakeholders/capacidade = Mantenedor único (Lucinei).** Não há sponsor/operador externo, não há equipe.
  5. **Cadência = sob demanda; sem SLA formal** — **substitui** a `[PREMISSA-P1]` quinzenal do plano I1 (`docs/20` §6/Premissas). Nenhuma cadência quinzenal está vigente.
  6. **Tracking = nenhuma ferramenta externa; `docs/` é a trilha** de rastreabilidade (sem board/issue tracker; IDs e estados vivem nos canônicos/log).
- **Alternativas consideradas:**
  - (i-a) Definir stack agora (Python/LangGraph/etc.) — rejeitada: o Mantenedor adiou explicitamente; inventar stack violaria as regras do repo e o D-V0-01.
  - (ii-a) Repositório-alvo separado para implementação — rejeitada: o alvo é este repo.
  - (iii-a) CI mínima agora (lint/markdown) — rejeitada: nenhuma por ora; repo é docs-only; sem remote, CI não se aplica hoje.
  - (iv-a) Declarar sponsor/operador externo ou equipe mínima — rejeitada: Mantenedor único.
  - (v-a) Manter premissa quinzenal do I1 — rejeitada: substituída por "sob demanda, sem SLA formal".
  - (vi-a) Adotar GitHub Projects/Jira/similar — rejeitada: `docs/` é a trilha; nenhuma ferramenta externa.
- **Consequências:**
  - `[PREMISSA-P1]` quinzenal (`docs/20`) está **formalmente substituída** por DEC-006(v); `docs/20` não foi editado nesta sessão (restrição de escopo) — ver "Propagação pendente".
  - Sem SLA de decisão/aceite: riscos R4 (capacidade) e R6 (dependências) de `docs/20` permanecem abertos, com mitigação = decisão do Mantenedor único sob demanda; **não prometer prazo sem buffer** continua regra vigente.
  - Sem tracking externo: estados/IDs vivem em `docs/`; DoR/DoD dependem de disciplina documental; critério de `completed` e taxonomia de tracking seguem `[LACUNA]` (D-V0-05).
  - Cadência de revisão do RACI (`docs/40`) e checkpoints do semáforo ficam **sob demanda**.
  - **A publicação do baseline v0 NÃO é desbloqueada por esta decisão** — permanece bloqueada por D-V0-03/04/05/06 (ver DEC-008 e "Decisões pendentes").
- **Evidência:** ata `docs/46-ata-kickoff-d-v0-01-02-v0.md`; sessão de 2026-11-16 (esta sessão); `docs/00` §5 (D-V0-01/02 originais) e §8.2; decisão do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisões humanas de 2026-11-16, Classe C — 6 pontos).
