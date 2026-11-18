---
title: "DEC-024 — Baseline v0 consolidada; F-ÚNICO-2 iniciada"
date: "2026-11-17"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-024 — Consolidação da baseline v0 e início da F-ÚNICO-2 (Classe C, 2026-11-17)

- **Contexto:** F-ÚNICO-1 (MVP Controlado) concluída tecnicamente (implementação: persistência SQLite, validador de contrato, segredos, máquina de estados, 65 testes, 74,84% cobertura). Todos os 6 critérios de §8.3 do painel atendidos (6/6 PASS). D-V0-01 resolvido (DEC-018); D-V0-03/04/05/06 aprovados e materializados (DEC-019…DEC-022); DEC-007 fechado (DEC-023); D-V0-02 parcial (capacidade/tracking).
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **CONSOLIDAR BASELINE v0 PUBLICADA e INICIAR F-ÚNICO-2 (Evolução).** Atualizar painel `docs/00` (§1 semáforo, §5, §8 machine-readable, §8.3 critérios 6/6 PASS), `docs/README.md` (DEC-001…DEC-024; observações de governança), `docs/20`, `docs/30`, `docs/45`, `docs/47`, `docs/48` (remoção de lacunas resolvidas; F-ÚNICO-1 concluída; F-ÚNICO-2 iniciada). `no_go_flags: []`. `proxima_acao_recomendada`: "Baseline v0 publicada; iniciar F-ÚNICO-2 (evolução)".
- **Referência:** DEC-018 (D-V0-01), DEC-019 (D-V0-03), DEC-020 (D-V0-04), DEC-021 (D-V0-05), DEC-022 (D-V0-06), DEC-023 (DEC-007).
- **Artefatos:** `docs/00-painel-gerencial-consolidado.md`, `docs/README.md`, `docs/20-*`, `docs/30-*`, `docs/45-*`, `docs/47-*`, `docs/48-*`, `docs/DECISIONS.md`.
- **Nota:** `approved` de valor permanece exclusivo do PO; F-ÚNICO-2 (Evolução) inicia como trilha documental/técnica com change control. D-V0-02 permanece parcial (capacidade/tracking) — não bloqueante para F-ÚNICO-2.
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).
