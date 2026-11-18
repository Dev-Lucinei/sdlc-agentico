---
title: "DEC-018 — D-V0-01 resolvido (Opção B): stack mínima Python 3.12"
date: "2026-11-17"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-018 — Resolução de D-V0-01 (Opção B): stack mínima definida (Classe C, 2026-11-17)

- **Contexto:** D-V0-01 permaneceu adiado desde DEC-006(i) (stack/infra/repo/CI/gates indefinidos), bloqueando F-ÚNICO-1 (R8) e mantendo o repo em modo documental. Em 2026-11-17 o Mantenedor decidiu (Classe C, Opção B) resolver D-V0-01 com stack mínima, desbloqueando F-ÚNICO-1 com infraestrutura real mínima e eliminando o bloqueio crítico R8/R12 para o MVP.
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):**
  1. **D-V0-01 RESOLVIDO** — stack mínima definida: **Python 3.12 + pytest + ruff + mypy**, **sem CI externo**.
  2. **pyproject.toml real** com thresholds **absolutos** (hardcoded, não parametrizados): **cobertura ≥ 50%** (fail_under = 50) e **0 erros críticos** (ruff/mypy sem erros bloqueantes).
  3. **F-ÚNICO-1 desbloqueada** — infraestrutura real mínima (repo-alvo = este repositório, DEC-006(ii)); Makefile/pyproject.toml existentes atualizados para os thresholds absolutos; gates G0–G1 executáveis localmente.
  4. LangGraph permanece **condicional** (CR-009-C dormente); máquina de estados Python pura (já implementada em `src/`) é a baseline de execução; LangGraph pode ser adotado ou substituído por decisão futura.
  5. Sem CI externo (DEC-006(iii) mantido: nenhuma infra de CI; gates rodam localmente via Makefile).
- **Alternativas consideradas:**
  - (a) Manter D-V0-01 adiado (status quo) — rejeitada: mantinha F-ÚNICO-1 bloqueada indefinidamente (R8/R12).
  - (b) Stack expandida (Python 3.11/Poetry/GitHub Actions, conforme auditoria externa Antigravity) — rejeitada: inventaria contexto não decidido; viola regra "não inventar stack"; exige infra não disponível.
  - (c) Thresholds parametrizados (fail_under=0) — rejeitada: a decisão Opção B fixa valores absolutos (≥50% cobertura, 0 erros críticos) para destravar o MVP; parametrização permanece para projetos-alvo futuros.
- **Consequências:**
  - D-V0-01 deixa de ser `[LACUNA]`/adiado; R8 (estagnação por stack adiada) → **mitigado**; R12 (MVP de 1 semana inviável sem kickoff) → **mitigado** (F-ÚNICO-1 desbloqueada).
  - F-ÚNICO-1 passa de "bloqueada" para "desbloqueada (condicionada a D-V0-03/04/05/06 para aceite/contrato)".
  - `pyproject.toml` real (thresholds absolutos) a ser materializado/atualizado pelo `code-implementer` no próximo change set; Makefile atualizado para os alvos com thresholds.
  - DEC-007 (política de segredos) permanece `[LACUNA]` aberta com gatilho reavaliado (stack agora definida — reavaliação permitida, mas decisão formal pendente).
  - Nenhuma promoção a `approved`/`completed` de artefatos de valor; `approved` permanece exclusivo do PO.
- **Evidência:** decisão do Mantenedor (Lucinei, Classe C, 2026-11-17, Opção B); `docs/00` §5 (D-V0-01); `docs/47` §6 (critérios de promoção); `docs/DECISIONS.md` DEC-006(i) (adiamento original) e DEC-014/DEC-016 (kickoff/reabertura); `pyproject.toml`/`Makefile` do repo (a ser atualizados).
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).
