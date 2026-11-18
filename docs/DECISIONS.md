---
title: "DECISIONS — log de decisões Classe C (índice vigente)"
date: "2026-11-18"
project: "sdlc-agentico"
source: "gerente-projeto + Mantenedor Lucinei (bifurcação DEC-031, 2026-11-18)"
status: "vigente"
---

# DECISIONS — log de decisões Classe C (índice vigente)

**Classe de autonomia desta elaboração:** B (registro documental reversível). Decisões Classe C foram tomadas pelo Mantenedor humano; execução ≠ `completed` ≠ `approved`.

## Regra de ouro (DEC-001)

Classe C exige `decided_by` humano explícito + evidência; execução ≠ `completed` ≠ `approved`; ausência de decisão humana ⇒ não aprovado. Entradas nunca são reescritas — correções entram como nova entrada ou adendo explícito.

Corpos em `docs/decisions/DEC-NNN-<slug>.md`; arquivo congelado `docs/decisions/arquivo-2026-11-16.md` (seções stale, 2026-11-16).

**Leitura obrigatória = índice + vigentes (~4k tokens); demais sob demanda.**

## Índice (DEC-001…DEC-031)

| ID | Data | Título | Classe | Status | superseded_by |
|---|---|---|---|---|---|
| DEC-001 | 2026-11-16 | Criação deste log canônico de decisões (CR-012) | C | vigente | — |
| DEC-002 | 2026-11-16 | docs/40 RACI validado como vigente (CR-001) | C | vigente | — |
| DEC-003 | 2026-11-16 | Inclusão condicional canônicos 41–45 + normativos por sha256 | C | vigente | — |
| DEC-004 | 2026-11-16 | LICENSE: nenhuma por ora | C | vigente | — |
| DEC-005 | 2026-11-16 | docs/evidence/ REJEITADA (CR-004) | C | vigente | — |
| DEC-006 | 2026-11-16 | Kickoff D-V0-01/02 — 6 decisões Classe C | C | vigente | DEC-018 (parcial; DEC-006(vi) vigente) |
| DEC-007 | 2026-11-16 | Política de segredos permanece [LACUNA] (CR-011) | B | registrado — `[LACUNA]` aberta | DEC-023 |
| DEC-008 | 2026-11-16 | Reconciliação do baseline v0 planejada (CR-013) | B | registrado — planejamento | DEC-024 |
| DEC-009 | 2026-11-16 | D-V0-03 — Aceite do PO visão/MVP/estados/KPIs (pauta) | C | aprovado (Classe C) | DEC-019 |
| DEC-010 | 2026-11-16 | D-V0-04 — Baseline técnica e ADRs A–G (pauta) | C | aprovado (Classe C) | DEC-020 |
| DEC-011 | 2026-11-16 | D-V0-05 — Contrato canônico v1.0.0 (pauta) | C | aprovado (Classe C) | DEC-021 |
| DEC-012 | 2026-11-16 | D-V0-06 — Gates/evidência/thresholds unificados (pauta) | C | aprovado (Classe C) | DEC-022 |
| DEC-013 | 2026-11-16 | Reconciliação MU-0.3 concluída | B | registrado — concluído (MU-0.3) | — |
| DEC-014 | 2026-11-16 | Grill-with-docs — pendências bloqueantes PM | B | aprovado (Classe C) | DEC-027 (parcial; DEC-029 deprecia P7) |
| DEC-015 | 2026-11-16 | Consolidação PO da pauta D-V0-03 (proposta) | B | aprovado (Classe C) | DEC-019…DEC-022 |
| DEC-016 | 2026-11-16 | Consolidação TL das pautas D-V0-04/05/06 (proposta) | B | aprovado (Classe C) | DEC-019…DEC-022 |
| DEC-017 | 2026-11-16 | Mudança de identidade: documentação + gates/CI | B | registrado | — |
| DEC-018 | 2026-11-17 | D-V0-01 resolvido (Opção B): stack mínima Python 3.12 | C | vigente | — |
| DEC-019 | 2026-11-17 | D-V0-03 — Aceite do PO aprovado e materializado | C | vigente | — |
| DEC-020 | 2026-11-17 | D-V0-04 — Baseline técnica e ADRs accepted | C | vigente | — |
| DEC-021 | 2026-11-17 | D-V0-05 — Contrato canônico v1.0.0 adotado | C | vigente | — |
| DEC-022 | 2026-11-17 | D-V0-06 — Política unificada de gates/thresholds | C | vigente | — |
| DEC-023 | 2026-11-17 | Política de segredos: os.environ, nunca hardcode | C | vigente | — |
| DEC-024 | 2026-11-17 | Baseline v0 consolidada; F-ÚNICO-2 iniciada | C | vigente | — |
| DEC-025 | 2026-11-17 | Reconciliação de docs/41 e docs/45 para contrato v1.0.0 | B | concluído (Classe B) | — |
| DEC-026 | 2026-11-17 | Aceite de valor PO — incrementos MVP (E1–E3) | C | Materializado (Classe C) | DEC-030 |
| DEC-027 | 2026-11-17 | D-V0-02 — Capacidade ~4-8h/sem; tracking docs/ | B | registrado (Classe B) | — |
| DEC-028 | 2026-11-17 | Pacote de evidência de aceite E1–E3 preparado | B | aprovado via DEC-030 (era ~~Pending~~) | DEC-030 |
| DEC-029 | 2026-11-18 | Reestruturação SoT + Escalonamento Progressivo de Governança | C | vigente (Classe C) | — |
| DEC-030 | 2026-11-18 | Aceite de valor E1–E3: APROVADO (Classe C) | C | vigente (Classe C) — E1–E3; E4 fora de escopo | — |
| DEC-031 | 2026-11-18 | Bifurcação do log de decisões (índice + corpos) | C | vigente (Classe C) | — |

## Ponteiros

- Corpos: `docs/decisions/DEC-NNN-<slug>.md` (append-only; nunca reescrever).
- Arquivo congelado: `docs/decisions/arquivo-2026-11-16.md`.
- Índice do repo: `docs/README.md`; DEC-031: `docs/decisions/DEC-031-bifurcacao-log-decisoes.md`.
