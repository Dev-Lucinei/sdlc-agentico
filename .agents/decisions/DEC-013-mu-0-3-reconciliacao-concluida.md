---
title: "DEC-013 — Registro de reconciliação MU-0.3 concluída"
date: "2026-11-16"
project: "sdlc-agentico"
status: "registrado — concluído (MU-0.3)"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-013 — Registro de reconciliação MU-0.3 concluída (propagação documental + pautas DEC-009+) (Classe B — registro)

- **Contexto:** F-ÚNICO-0/MU-0.2+MU-0.3 (propagação documental e registro de pautas Classe C) executado em 2026-11-16 pelo `gerente-projeto`, consolidando a reconciliação documental do baseline v0 sem tocar em `docs/10/30/47/48` (já reconciliados) e sem criar `docs/evidence/` ou numerar ADRs.
- **Decisão (registro, Classe B):** registrar a conclusão de MU-0.3 com evidências verificáveis. Arquivos editados neste change set:
  1. `docs/20-governanca-pm-plano-baseline-v0.md` — bloco §0 (mapeamento F0–F2 → F-ÚNICO-0/1/2); `[PREMISSA-P1]` marcada substituída por DEC-006(v); cadência "sob demanda, sem SLA" registrada (§3); normativos externos por caminho+sha256 completo; `docs/evidence/` rejeitado (DEC-005); status honesto `partial/condicional`.
  2. `docs/40-operacao-raci-repo-v0.md` — front matter `vigente` (DEC-002) + linha de evidência; matriz RACI inalterada.
  3. `docs/README.md` — índice atualizado (entradas 46/47/48/DECISIONS; contagem `00–48` + DECISIONS + 46; data 2026-11-16); DIV-6 fechado.
  4. `docs/00-painel-gerencial-consolidado.md` — §8 (subagents tech-lead/gerente-produto reconciliação; lacunas_consolidadas atualizadas; proxima_acao; adendo §8.4).
  5. `docs/DECISIONS.md` — DEC-009…DEC-013 adicionados; tabela-resumo e "Propagação pendente" atualizados.
- **Não editados (já reconciliados):** `docs/10`, `docs/30`, `docs/47`, `docs/48`.
- **Não criados:** `docs/evidence/` (DEC-005); nenhum ADR numerado; nenhuma promoção a `approved`/`completed`.
- **Evidências (verificáveis):**
  - Normativos externos pinados (DEC-003), verificados via `sha256sum` em 2026-11-16:
    - `~/.opencode/references/contrato-resumo-subagentes.md` → `163e0aad7654d0a60930e90388afa9b9474ee727f119e94a62337d8321442a60`
    - `~/.opencode/references/autonomia-e-estados.md` → `776af494ee702cf4d3db8837f2b1c0c23450844f9b54e376a052d7adbc42c78a`
  - `git status` pré-commit: modificações em `docs/10`, `docs/20`, `docs/30`, `docs/40`, `docs/47`, `docs/48` + novos em `docs/00`, `docs/README.md`, `docs/DECISIONS.md`.
  - Nenhuma promoção a `approved`/`completed`: status permanece `condicional`/`partial` em todos os canônicos (exceto DEC-001…DEC-006 vigentes e `docs/40` vigente por DEC-002).
- **Alternativas consideradas:** (a) editar 10/30/47/48 — rejeitada (já reconciliados; fora do escopo); (b) criar `docs/evidence/` — rejeitada (DEC-005); (c) numerar ADRs — rejeitada (D-V0-04 pendente).
- **Consequências:** reconciliação MU-0.3 concluída e registrada; pautas D-V0-03/04/05/06 despachadas como DEC-009…DEC-012 (aguardando decisão do Mantenedor); baseline v0 permanece não publicado (DEC-008/CR-013-publicação bloqueada); DIV-6 fechado.
- **Status final:** **registrado — concluído (MU-0.3)** (Classe B — registro; nenhuma aprovação inferida).
