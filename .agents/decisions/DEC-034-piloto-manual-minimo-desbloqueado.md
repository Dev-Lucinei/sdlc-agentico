---
title: "DEC-034 — Piloto manual mínimo desbloqueado (Classe C)"
date: "2026-11-18"
project: "sdlc-agentico"
source: "Mantenedor Lucinei (sessão OpenCode 2026-11-18, pergunta interativa — resposta 'Desbloquear via Classe C')"
status: "vigente"
classe: "C"
decided_by: "Lucinei (Mantenedor)"
human_interaction_ref: "sessão OpenCode 2026-11-18 (pergunta interativa — desbloqueio do piloto manual mínimo; decisão explícita do Mantenedor)"
---

## DEC-034 — Piloto manual mínimo desbloqueado (Classe C)

- **Data:** 2026-11-18
- **Classe:** C
- **Decisão:** o Mantenedor (Lucinei) decidiu explicitamente, em sessão OpenCode 2026-11-18 (pergunta interativa), **"Desbloquear via Classe C"** o piloto manual mínimo — desfazendo, exclusivamente para esse escopo, o bloqueio registrado em DEC-032.

### a) Contexto

A crítica externa identificou (i) o **custo de governança vs. a capacidade ~4–8h/sem do mantenedor único** e (ii) os **gates locais insuficientes como evidência de operação real**; a recomendação foi um **piloto manual curto e rastreável com uma tarefa real pequena**. DEC-032 (2026-11-18) bloqueou "piloto" até nova decisão Classe C.

### b) Decisão (Classe C)

**FICA DESBLOQUEADO exclusivamente o piloto manual mínimo:** uma tarefa real pequena, rastreável, com registro manual (mecanismo atual: git + log de decisões + painel) de **TEMPO DE REVISÃO, RETRABALHO e ACEITE**; **SEM ferramenta nova, SEM processo novo, SEM cerimônia adicional** (consistente com DEC-029).

O piloto desta sessão = a própria resolução dos **gaps 2.1–2.4 da crítica** (demanda real do Mantenedor): executada via subagentes com evidência, gates (`make lint`/`make test`/`make audit` exit 0) e commits locais `92a17ec` (docs) e `17f8297` (teste de guarda de drift). O registro pós-execução (tempos/retrabalho/aceite) será feito no fechamento da sessão, sob decisão/aceite do Mantenedor.

### c) Aceite

O aceite do resultado do piloto é **ato exclusivo do Mantenedor/PO** (semântica de estados mantida: execução ≠ `completed` ≠ `approved`). **Nada é promovido a `approved` por esta decisão.**

### d) O que NÃO muda (mantém-se bloqueado até Classe C própria)

E4; G3; CR-009-C; CR-010-C; adoção de ferramenta externa de tracking; promoção do DRAFT `docs/adr/core/DRAFT-criterio-completed-e-dod-g2-g3.md`; KPIs (lacuna mantida, DEC-026/DEC-030); LAC-IDEMP-02..05; `docs/48-contrato-canonico-v1-0-0.md` intocado; `docs/decisions/DEC-001…033` e `arquivo-2026-11-16.md` NÃO são reescritos (append-only).

### e) Lacunas remanescentes

Métricas de revisão/retrabalho/aceite **NÃO estão instrumentadas** (proposital); instrumentar somente com evidência do piloto concluído, por nova decisão Classe C (ou B, conforme o escopo).

- **Decisão tomada em:** sessão OpenCode 2026-11-18 pelo Mantenedor (resposta interativa — "Desbloquear via Classe C").
