---
title: "DEC-023 — Política de segredos: os.environ, nunca hardcode"
date: "2026-11-17"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-023 — DEC-007: Política de segredos (Classe C, 2026-11-17)

- **Contexto:** DEC-007 permaneceu `[LACUNA]` aberta (registrado em 2026-11-16) com gatilho de reavaliação após D-V0-01. Com a stack definida (DEC-018, 2026-11-17 — Python 3.12 + pytest + ruff + mypy), a política de segredos pode ser formalizada. Referência de implementação: `src/secrets.py` (code-implementer).
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **APROVADO E MATERIALIZADO.** Política de segredos:
  1. **Injeção via variáveis de ambiente** (`os.environ`); nunca hardcode em código, configuração ou artefatos.
  2. **Mascaramento em logs** (ex.: `"sk-...****"`); segredos nunca aparecem em claro em logs, SoT, evidências ou artefatos.
  3. **Proibição de segredos** em SoT, logs, artefatos, commits e documentação.
  4. Implementação de referência: `src/secrets.py` (code-implementer).
- **Referência:** DEC-007 (registro 2026-11-16, `[LACUNA]` aberta); DEC-018 (stack definida, 2026-11-17).
- **Artefatos:** `src/secrets.py` (implementado pelo code-implementer).
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).
