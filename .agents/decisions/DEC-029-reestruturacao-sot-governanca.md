---
title: "DEC-029 — Reestruturação SoT + Escalonamento Progressivo de Governança"
date: "2026-11-18"
project: "sdlc-agentico"
status: "vigente (Classe C, 2026-11-18)"
source: "docs/DECISIONS.md (extração DEC-031)"
---

## DEC-029 — Reestruturação SoT + Escalonamento Progressivo de Governança (2026-11-18)

- **Contexto:** análise do áudio "Governança excessiva no desenvolvimento agêntico" (2026-11-18), trazida pelo Mantenedor. Diagnóstico: governança excessiva para um projeto de mantenedor único — duplicação de canônicos (`docs/10` × `docs/11`), telemetria volátil (capacidade/alocação) espalhada por múltiplos canônicos (`docs/20`, `docs/21`, `docs/47`), e change control formal aplicado com a mesma cerimônia a mudanças de qualquer peso. Referências: `docs/00` §0–§8, `docs/10-produto-visao-v0.md`, `docs/20` §0.1, `docs/21`, `docs/47`.
- **Decisão (Classe C, decided_by Lucinei, 2026-11-18):**
  1. **Fusão docs/10+docs/11 → `docs/10-produto-visao-v0.md`:** consolidação da trilha PO em canônico único. Visão, problema, personas e proposta de valor (fonte: docs/11) prevalecem em conflitos sobre MVP (docs/10); escopo MVP (MoSCoW+WSJF), backlog E1–E4 com AC Given/When/Then e DoR, semântica canônica de estados (execução≠operação≠valor), KPIs, mecanismo de feedback/aceite, Decision/Acceptance v0 (`pending`) e pacote de evidência de aceite de E1–E3 (§0.2, DEC-028) preservados. `docs/10-produto-po-visao-mvp-baseline-v0.md` e `docs/11-visao-mvp-v0.md` removidos (`git rm`) no mesmo change set. Referências cruzadas atualizadas nos canônicos vivos; entradas históricas do log (DEC-001…DEC-028) não reescritas — caminhos antigos nelas citados permanecem como registro histórico.
  2. **Telemetria volátil centralizada:** capacidade, alocação, cadência efetiva e afins passam a ter fonte única em `docs/00-painel-gerencial-consolidado.md` §0 "Status dinâmico". `docs/20`, `docs/21` e `docs/47` não carregam mais valores voláteis de capacidade — apontam para `docs/00` §0. [PREMISSA-P7] (40h/sem, DEC-014) marcada como **depreciada/histórica** em todos os canônicos; [PREMISSA-P10] (DEC-027) permanece a referência volátil vigente, **não confirmada com o Mantenedor**.
  3. **Governança escalonada:** para mantenedor único, change control formal **simplificado** — decisões Classe C continuam humanas, explícitas e registradas neste log; mudanças documentais Classe B fluem sem cerimônia adicional de aprovação; nenhuma Classe C é inferida de execução (`done/blocked/partial` ≠ `completed` ≠ `approved`). Escalonamento progressivo: ao crescerema equipe/colaboradores, o formalismo aumenta proporcionalmente.
  4. **Fachada human-friendly:** `docs/ONBOARDING.md` (criado pelo `gerente-produto`, 2026-11-18) registrado como documento de entrada **não canônico** no índice `docs/README.md`; não substitui canônicos nem promove status.
  5. **Não removidos:** `docs/30-arquitetura-tech-lead-baseline-v0.md` (arquitetura) e `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (contrato v1.0.0) — preservados por decisão explícita.
- **Alternativas consideradas:**
  - (a) Manter docs/10 e docs/11 como canônicos separados — **rejeitada**: duplicação/ambiguidade de SoT sem ganho; divergência de conteúdo entre eles.
  - (b) Remover `docs/30`/`docs/48` no mesmo movimento — **rejeitada**: decisão explícita do Mantenedor de preservá-los; fora do escopo desta reestruturação.
  - (c) Mover telemetria volátil para `docs/20` ou novo arquivo de status — **rejeitada**: `docs/00` é o painel de agregação já lido primeiro; nova fonte criaria segunda SoT.
  - (d) Reduzir governança Classe C — **rejeitada**: Classe C (aceite de valor, promoção de baseline, decisões irreversíveis) permanece humana e exclusiva; o escalonamento afeta apenas o custo cerimonial de mudanças Classe B/documentais.
- **Consequências:**
  - SoT documental reduzida: 14 canônicos numerados + `DECISIONS.md` + `README.md` + `ONBOARDING.md` (não canônico).
  - `docs/00` §0 passa a ser a única fonte de telemetria volátil; demais canônicos referenciam-na.
  - P7 depreciada; P10 mantida pendente de confirmação do Mantenedor.
  - Aceite de valor E1–E3 (DEC-028) permanece **`pending`**, exclusivo do PO — esta reestruturação não decide valor.
  - Nenhuma promoção a `approved`/`completed`; nenhum `docs/evidence/` criado (DEC-005); IDs DEC-001…DEC-028 inalterados (G2).
- **Evidência:** decisão do Mantenedor em 2026-11-18 (Classe C); análise do áudio "Governança excessiva no desenvolvimento agêntico" (2026-11-18); fusão materializada em `docs/10-produto-visao-v0.md` (mesmo change set); `docs/00` §0 e §8.7; `docs/README.md`; `docs/20` §0.1.1, `docs/21`, `docs/47` reconciliados neste change set.
- **Status final:** **vigente (Classe C, 2026-11-18)** — reestruturação documental/SoT e escalonamento de governança; aceite de valor E1–E3 segue `pending` do PO. [Nota posterior: o `pending` de aceite E1–E3 foi decidido e aprovado em **DEC-030** (2026-11-18, Classe C) — E1–E3 `approved`; E4 fora de escopo. Corpo desta entrada preservado como registro histórico.]
