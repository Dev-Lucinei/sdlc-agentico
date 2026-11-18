---
title: "DEC-008 — Reconciliação do baseline v0 planejada (CR-013)"
date: "2026-11-16"
project: "sdlc-agentico"
status: "registrado — planejamento"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-008 — Reconciliação do baseline v0 planejada (CR-013); publicação bloqueada (Classe B — planejamento)

- **Contexto:** PO/PM/TL produziram entregáveis paralelos nunca reconciliados formalmente. Divergências conhecidas (`docs/00` §4): roadmap F0–F2/I1–I2 (PM) × F0–F5 (TL) × M1–M3/E1–E4 (PO); `schema_version 0.1.0-draft` (designs) × contrato v1.0.0 proposto (D-V0-05); cadência `[PREMISSA-P1]` quinzenal × "sob demanda" (DEC-006(v)); CR de inclusão de 41–45 (resolvido condicionalmente por DEC-003). CR-013 aberto; **roadmap único em elaboração em `docs/47`** (`docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md`, criado em 2026-11-16 por sessão `tech-lead` concorrente a esta — proposta documental condicional, status `condicional`; **não criado nem editado nesta sessão**, fora do escopo).
- **Decisão (planejamento, não aprovação):** a reconciliação do baseline v0 será executada via **roadmap único (`docs/47`, em elaboração)**, unificando trilhas PO/PM/TL, contrato canônico e taxonomia de estados. **A publicação do baseline canônico permanece BLOQUEADA por D-V0-03 (aceite do PO), D-V0-04 (baseline técnica + ADRs), D-V0-05 (contrato v1.0.0) e D-V0-06 (gates/thresholds).** Esta entrada não aprova, não publica e não promove nada.
- **Alternativas consideradas:**
  - (a) Publicar o baseline v0 agora como "vigente/canônico" — rejeitada: sem D-V0-03/04/05/06 e sem reconciliação, violaria as regras duras do repo (Classe C; execução ≠ `approved`).
  - (b) Manter indefinição sem plano — rejeitada: CR-013 existe; divergências exigem unificação, não silêncio.
  - (c) Reconciliação incremental, arquivo a arquivo, sem roadmap único — rejeitada: as divergências são transversais (roadmap × contrato × cadência); exigem visão única.
- **Consequências:** nenhum baseline é publicado por este registro; `docs/47` será o artefato de planejamento da reconciliação; ao concluir, a publicação exigirá decisões Classe C (D-V0-03/04/05/06) registradas neste log como DEC-009+ (ou adendo explícito); até lá, todos os canônicos permanecem `condicional`/`partial` conforme seus front matters (exceto DEC-001…DEC-006, que são decisões Classe C vigentes).
- **Evidência:** `docs/00` §4 (pontos a reconciliar), §5 (decisões pendentes), §7 (ordem recomendada), §8.1/§8.2 (adendos e fila de CRs); CR-013; DEC-003; DEC-006.
- **Status final:** **registrado — planejamento** (Classe B; publicação **bloqueada**; nenhuma aprovação inferida).
