---
title: "DECISIONS — log de decisões Classe C (índice vigente)"
date: "2026-11-19"
project: "sdlc-agentico"
source: "gerente-projeto + Mantenedor Lucinei (bifurcação DEC-031, 2026-11-18)"
status: "vigente"
---

# DECISIONS — log de decisões Classe C (índice vigente)

**Classe de autonomia desta elaboração:** B (registro documental reversível). Decisões Classe C foram tomadas pelo Mantenedor humano; execução ≠ `completed` ≠ `approved`.

## Regra de ouro (DEC-001)

Classe C exige `decided_by` humano explícito + evidência; execução ≠ `completed` ≠ `approved`; ausência de decisão humana ⇒ não aprovado. Entradas nunca são reescritas — correções entram como nova entrada ou adendo explícito.

PROIBIDO: promover/registrar `approved`/`accepted` sem decisão humana Classe C explícita registrada neste log. Anti-pattern: inferir "aceite" de execução concluída (ex.: suíte verde ⇒ incremento `approved` sem DEC). Recuperação: reverter a promoção, registrar a correção como nova entrada ou adendo explícito (nunca reescrever entradas) e submeter a decisão ao humano antes do próximo passo.

Corpos em `.agents/decisions/DEC-NNN-<slug>.md`; arquivo congelado `.agents/decisions/arquivo-2026-11-16.md` (seções stale, 2026-11-16).

LEIA quando: propor promoção de estado/ADR novo/mudança de gate ou threshold. O quê extrair: filtrar status ≠ superseded; toda promoção exige decisão humana Classe C registrada antes do próximo passo. Demais leituras: sob demanda. (~4k tokens)

## Índice (DEC-001…DEC-037)

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
| DEC-032 | 2026-11-18 | Kickoff formal da Fase 2 (F-ÚNICO-2, Evolução) | C | vigente | — |
| DEC-033 | 2026-11-18 | Dedupe atômico por idempotency_key (LAC-IDEMP-01, Classe C) | C | vigente | — |
| DEC-034 | 2026-11-18 | Piloto manual mínimo desbloqueado (Classe C) | C | vigente (Classe C) — somente o piloto mínimo; E4/G3/CR-009-C/CR-010-C mantidos | — |
| DEC-035 | 2026-11-18 | Aceite do piloto manual mínimo + proposta de faixa de KPIs (Classe C) | C | vigente (Classe C) — aceite do piloto; KPIs NÂO aprovados (proposta pendente) | — |
| DEC-036 | 2026-11-19 | Ratificação: docs/00 como vigente + fail_under=80 (gate cobertura) | C | vigente (Classe C) | — |
| DEC-037 | 2026-11-19 | Reorganização do SoT de agente para .agents/ (padrão de mercado) | C | vigente (Classe C) | — |

## Ponteiros

- Corpos: `.agents/decisions/DEC-NNN-<slug>.md` (append-only; nunca reescrever).
- Arquivo congelado: `.agents/decisions/arquivo-2026-11-16.md`.
- Índice do repo: `docs/README.md`; DEC-031: `.agents/decisions/DEC-031-bifurcacao-log-decisoes.md`; DEC-032: `.agents/decisions/DEC-032-kickoff-fase2-evolucao.md`; DEC-033: `.agents/decisions/DEC-033-dedupe-atomico-idempotency-key.md`; DEC-034: `.agents/decisions/DEC-034-piloto-manual-minimo-desbloqueado.md`; DEC-035: `.agents/decisions/DEC-035-aceite-piloto-kpis-proposta.md`; DEC-036: `.agents/decisions/DEC-036-ratificacao-00-vigente-fail-under-80.md`; DEC-037: `.agents/decisions/DEC-037-reorganizacao-sot-agents.md`.
