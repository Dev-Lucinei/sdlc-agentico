---
title: "ARQUIVO — entradas não-vigentes do índice de decisões Classe C (2026-11-19)"
date: "2026-11-19"
project: "sdlc-agentico"
source: "executor operacional (tarefa #1 — intervenção 2026-11-19, HEAD ba45672)"
status: "arquivo"
note: "arquivado em 2026-11-19 (intervenção #1); para reabrir, mover de volta ao índice + nova DEC"
---

# ARQUIVO — entradas não-vigentes arquivadas em 2026-11-19

## Critério de arquivamento

Entradas cujo `status` **não é** `vigente` no índice (`.agents/DECISIONS.md`) em 2026-11-19.
A tabela abaixo é uma **foto** do status no momento do arquivamento — não altera, promove
ou rebaixa o status de nenhuma DEC. Os corpos append-only em
`.agents/decisions/DEC-NNN-<slug>.md` permanecem intocados e são a fonte completa.

Nenhuma entrada foi deletada; corpos permanecem em `.agents/decisions/`.
Este arquivo é um registro de navegação/histórico, não uma decisão.

## Entradas arquivadas (15)

| ID | Data | Título | Status no momento do arquivamento | Motivo do arquivamento (curto) |
|---|---|---|---|---|
| DEC-007 | 2026-11-16 | Política de segredos permanece [LACUNA] (CR-011) | registrado — `[LACUNA]` aberta | superseded por DEC-023 (2026-11-17) |
| DEC-008 | 2026-11-16 | Reconciliação do baseline v0 planejada (CR-013) | registrado — planejamento | superseded por DEC-024 (baseline consolidada) |
| DEC-009 | 2026-11-16 | D-V0-03 — Aceite do PO visão/MVP/estados/KPIs (pauta) | aprovado (Classe C) | superseded por DEC-019 (materializado) |
| DEC-010 | 2026-11-16 | D-V0-04 — Baseline técnica e ADRs A–G (pauta) | aprovado (Classe C) | superseded por DEC-020 (ADRs accepted) |
| DEC-011 | 2026-11-16 | D-V0-05 — Contrato canônico v1.0.0 (pauta) | aprovado (Classe C) | superseded por DEC-021 (contrato adotado) |
| DEC-012 | 2026-11-16 | D-V0-06 — Gates/evidência/thresholds unificados (pauta) | aprovado (Classe C) | superseded por DEC-022 (política unificada) |
| DEC-013 | 2026-11-16 | Reconciliação MU-0.3 concluída | registrado — concluído (MU-0.3) | registro de execução concluída; sem vigência operacional |
| DEC-014 | 2026-11-16 | Grill-with-docs — pendências bloqueantes PM | aprovado (Classe C) | superseded por DEC-027 (parcial; DEC-029 deprecia P7) |
| DEC-015 | 2026-11-16 | Consolidação PO da pauta D-V0-03 (proposta) | aprovado (Classe C) | superseded por DEC-019…DEC-022 |
| DEC-016 | 2026-11-16 | Consolidação TL das pautas D-V0-04/05/06 (proposta) | aprovado (Classe C) | superseded por DEC-019…DEC-022 |
| DEC-017 | 2026-11-16 | Mudança de identidade: documentação + gates/CI | registrado | registro de mudança já incorporada; sem vigência operacional |
| DEC-025 | 2026-11-17 | Reconciliação de docs/41 e docs/45 para contrato v1.0.0 | concluído (Classe B) | execução concluída; sem vigência operacional |
| DEC-026 | 2026-11-17 | Aceite de valor PO — incrementos MVP (E1–E3) | Materializado (Classe C) | superseded por DEC-030 (aceite explícito E1–E3) |
| DEC-027 | 2026-11-17 | D-V0-02 — Capacidade ~4-8h/sem; tracking docs/ | registrado (Classe B) | registrado; sem vigência operacional no índice |
| DEC-028 | 2026-11-17 | Pacote de evidência de aceite E1–E3 preparado | aprovado via DEC-030 (era ~~Pending~~) | superseded por DEC-030 |

## Notas

- Motivo "superseded por DEC-NNN" reflete a coluna `superseded_by` do índice no momento
  do arquivamento (2026-11-19, HEAD ba45672); não é decisão nova.
- Para reabrir qualquer entrada: mover a linha de volta ao índice **e** registrar nova
  decisão Classe C (conforme nota do front matter).
- Contagem de corpos preservados: 37/37 (`ls .agents/decisions/DEC-*.md`).
