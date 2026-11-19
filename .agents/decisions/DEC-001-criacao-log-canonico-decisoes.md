---
title: "DEC-001 — Criação deste log canônico de decisões (CR-012)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "vigente"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-001 — Criação deste log canônico de decisões (CR-012)

- **Contexto:** o repo acumulava decisões (auditoria externa de 2026-11-16, fila de CRs não registrada — `docs/00` §8.2; change control pendente — `docs/20` §5) sem um log único append-only. Registros espalhados em painel/adendos geravam risco de drift e de decisões "informais" sem `decided_by`.
- **Decisão:** criar `docs/DECISIONS.md` como **log canônico de decisões do repositório**, com front matter próprio, tabela-resumo, uma seção por decisão e seção de decisões pendentes. Numeração `DEC-NNN` sequencial; entradas nunca são reescritas — correções entram como nova entrada ou adendo explícito.
- **Alternativas consideradas:**
  - (a) Seção de decisões dentro de `docs/20-*` §5 — rejeitada: `20-*` é o plano de governança (proposta PM), não log operacional; incha o artefato e mistura proposta com decisão humana.
  - (b) Manter decisões só no painel (`docs/00`) e nos adendos — rejeitada: painel é agregação de status, não trilha de decisão; sem append único, com risco de contradição silenciosa.
  - (c) Criar `docs/governance/DECISIONS.md` — rejeitada: estrutura de diretórios (`docs/governance/`) é `[PREMISSA]` pendente de decisão Classe C; faixa `≥40` já em uso pelos canônicos operacionais.
- **Consequências:** fonte única de registro de decisões do repo; toda decisão Classe C deve ser registrada aqui no mesmo change set em que for tomada; índice (`docs/README.md`) e painel (`docs/00` §5/§8) devem referenciar este log (propagação pendente — ver "Propagação pendente" ao final).
- **Evidência:** sessão de 2026-11-16 (esta sessão); CR-012; `docs/20` §5 (change control); `docs/00` §8.2 (fila de CRs); `docs/40` linha 6 (adicionar canônico = **A** do Mantenedor) e regra de desempate.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C).
