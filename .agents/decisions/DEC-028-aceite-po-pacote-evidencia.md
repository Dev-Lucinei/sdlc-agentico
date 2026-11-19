---
title: "DEC-028 — Aceite de valor PO — pacote de evidência E1–E3"
date: "2026-11-17"
project: "sdlc-agentico"
status: "~~Pending — aguardando aceite explícito do PO~~ → **approved via DEC-030 (2026-11-18)** (E1–E3; E4 fora de escopo)"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-028 — Aceite de valor PO — pacote de evidência preparado (Classe B registro; aceite = Classe C; 2026-11-17)

- **Contexto:** DEC-026 (2026-11-17, Classe C) materializou a trilha documental do aceite de valor (AC Given/When/Then E1–E3 + handoff PR→aceite PO + KPIs calibrados), mas nenhum incremento MVP foi submetido formalmente para decisão. F-ÚNICO-2 exige a preparação do **pacote de evidência** de aceite dos incrementos E1–E3 (implementação da F-ÚNICO-1: contrato v1.0.0 + validador; máquina de estados; persistência SQLite). Nota de numeração: a numeração solicitada para esta entrada era "DEC-026"; `DEC-026` já estava ocupado (materialização da trilha, acima) e `DEC-027` foi ocupado por `gerente-projeto` no mesmo dia (D-V0-02 — capacidade/tracking). Esta entrada assume o número livre seguinte, **DEC-028**, sem reescrever DEC-026 nem DEC-027 (regra: entradas nunca são reescritas).
- **Decisão (Classe B — registro; a decisão de aceite permanece Classe C, exclusiva do PO):** declarar os incrementos **E1–E3 prontos para aceite de valor**, com pacote de evidência verificável anexado em `docs/10-produto-po-visao-mvp-baseline-v0.md` §0.2 e referenciado em `docs/11-visao-mvp-v0.md` §"Incrementos MVP implementados (E1–E3)":
  1. **E1** — Contrato canônico v1.0.0 + validador JSON Schema (`src/contract_validator.py`, `src/exit_codes.py`, `docs/schemas/contract-v1.0.0.schema.json`); testes `tests/test_contract_validator.py`, `tests/test_validate_contract.py`; commits `e54c083`, `c6b2567`, `f6d74f6`.
  2. **E2** — Máquina de estados (done ⇏ completed ⇏ approved) + transições validadas (`src/state.py`); testes `tests/test_state_transitions.py`; commit `f6d74f6`; ADR-005 `accepted` (DEC-020).
  3. **E3** — Persistência SQLite (SoT + Event Log append-only) (`src/persistence.py`); testes `tests/test_persistence.py`; commit `f6d74f6`; DEC-024.
- **Evidência verificável (medida em 2026-11-17, sessão de preparação do pacote):**
  - `python -m pytest --cov=src` → **65 passed**; cobertura total **75,00%** (threshold ≥ 50% — `pyproject.toml`, DEC-018/DEC-022).
  - `make audit` → **verde** (ruff `check .` + mypy `src` + pytest; `make build` placeholder documental; exit fail-closed preservado).
  - Drift registrado: DEC-024 e o painel `docs/00` citam "74,84% cobertura" (medição anterior); a medição atual é **75,00%** — painel atualizado nesta mesma trilha.
- **Decision/Acceptance v0 (embutido em `docs/10` §0.2):** `decision_id` `01M7P3NFTDNKR760KBBBHE8PSV`; `decision_type` `aceite`; `criterio` `Given/When/Then`; `status` **`pending`**; `decided_by` = PO (exclusivo) — decisão explícita pendente; `human_interaction_ref` **obrigatório** e a preencher no ato da decisão; `decided_at`/`rationale` nulos até decisão.
- **Nota (regra de valor):** execução ≠ valor. `done` (E1–E3) ≠ `completed` ≠ `approved`. Este registro **não** declara `approved` de nenhum incremento; `approved` é exclusivo do PO com `evidence` + `decided_by=PO` + `decided_at` (+ `human_interaction_ref` quando a decisão for tomada por interação humana). `rejected → pending` somente com nova evidência.
- **Consequências:** pacote submetido à fila de aceite do PO; nenhuma promoção de status de incremento; critério operacional de `completed` no tracking alvo (`docs/`) e identificadores correlacionáveis/storage de trilha (E4) permanecem `[LACUNA]`.
- **Referência:** DEC-026 (trilha de aceite materializada), DEC-027 (D-V0-02 — registro concorrente do mesmo dia), DEC-019 (D-V0-03), DEC-021 (contrato), DEC-022 (gates), DEC-024 (baseline v0), DEC-018 (stack/thresholds), docs/10 §0.2, docs/11, docs/00.
- **Status final:** **Pending — aguardando aceite explícito do PO** (decisão Classe C; `decided_by`=PO; este registro é Classe B e não decide valor).
