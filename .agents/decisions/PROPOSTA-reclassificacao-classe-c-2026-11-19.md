---
title: "PROPOSTA — Reclassificação de DECs Classe C (2026-11-19)"
date: "2026-11-19"
project: "sdlc-agentico"
source: "executor operacional (tarefa #3 — proposta, não decisão)"
status: "proposta — decisão humana pendente"
---

# PROPOSTA — Reclassificação de DECs Classe C (2026-11-19)

> **Este arquivo é uma PROPOSTA. Não é decisão. Nada aqui foi aplicado.**
> Reclassificar Classe C exige decisão humana (Classe C). Nenhum status de DEC foi alterado.

## Premissa

27/37 DECs são Classe C; esse número indica saturação — a classe não diferencia mais
o que exige decisão humana irreversível. **Meta: ≤ 10 Classe C.**

As 27 DECs abaixo foram lidas nos corpos `.agents/decisions/DEC-NNN-*.md` em 2026-11-19
(HEAD ba45672) e categorizadas. Categorias:

- **A) Ratificação de decisão já tomada** → candidata a Classe B (ou A, se puramente registro)
- **B) Registro/planejamento/consolidação** → candidata a Classe B
- **C) Decisão real nova, irreversível** → permanece Classe C
- **D) Ambígua / requer discussão humana** → mantém C por default

## Tabela de categorização (27 DECs Classe C)

| ID | Título (resumido) | Categoria | Nova classe proposta | Justificativa (1 linha) |
|---|---|---|---|---|
| DEC-001 | Criação do log canônico de decisões (CR-012) | B | B | Consolida decisões pré-existentes (adendos/painel) em trilha única; sem irreversibilidade nova |
| DEC-002 | docs/40 RACI validado como vigente (CR-001) | A | B | Ratificação/validação de artefato existente; sem conteúdo novo |
| DEC-003 | Inclusão condicional canônicos 41–45 + sha256 | C | C (mantém) | Decisão real: inclusão condicional + política de referência externa; consequências duradoutras |
| DEC-004 | LICENSE: nenhuma por ora (CR-003) | D | C (default) | "Por ora" é reversível — não é irreversível strictu sensu; requer desempate humano |
| DEC-005 | docs/evidence/ REJEITADA (CR-004) | C | C (mantém) | Rejeição com consequência normativa (segunda SoT proibida); contorno exige nova decisão |
| DEC-006 | Kickoff D-V0-01/02 — 6 decisões Classe C | C | C (mantém) | 6 decisões fundacionais (stack adiado, repo-alvo, sem CI, mantenedor único, cadência, tracking) |
| DEC-009 | D-V0-03 — Aceite do PO visão/MVP (pauta) | B | B | Pauta/proposta aguardando decisão; registro de planejamento, não decisão tomada |
| DEC-010 | D-V0-04 — Baseline técnica e ADRs (pauta) | B | B | Pauta/proposta aguardando decisão; registro de planejamento, não decisão tomada |
| DEC-011 | D-V0-05 — Contrato canônico v1.0.0 (pauta) | B | B | Pauta/proposta aguardando decisão; registro de planejamento, não decisão tomada |
| DEC-012 | D-V0-06 — Gates/thresholds unificados (pauta) | B | B | Pauta/proposta aguardando decisão; registro de planejamento, não decisão tomada |
| DEC-018 | D-V0-01 resolvido (Opção B): stack mínima Python 3.12 | C | C (mantém) | Decisão real: stack, thresholds absolutos e desbloqueio de F-ÚNICO-1; mudar depois tem custo |
| DEC-019 | D-V0-03 — Aceite do PO aprovado e materializado | A | B | Ratificação/materialização da pauta DEC-009/DEC-015 pelo Mantenedor |
| DEC-020 | D-V0-04 — Baseline técnica e ADRs accepted | A | B | Ratificação: promove ADRs A–G a `accepted`; pauta DEC-010/DEC-016 já existia |
| DEC-021 | D-V0-05 — Contrato canônico v1.0.0 adotado | A | B | Ratificação: adoção da proposta DEC-011; migração aditiva já delineada |
| DEC-022 | D-V0-06 — Política unificada de gates/thresholds | A | B | Ratificação: adota política proposta em DEC-012; parâmetros já delineados |
| DEC-023 | Política de segredos: os.environ, nunca hardcode | C | C (mantém) | Política normativa nova e vinculante para todo código futuro (proibição + mascaramento) |
| DEC-024 | Baseline v0 consolidada; F-ÚNICO-2 iniciada | C | C (mantém) | Decisão real: publica baseline e inicia F-ÚNICO-2; muda o estado do projeto |
| DEC-026 | Aceite de valor PO — incrementos MVP (E1–E3) — materialização | B | B | Materializa AC/handoff/KPIs sem decidir valor; `approved` permaneceu pendente |
| DEC-029 | Reestruturação SoT + Escalonamento Progressivo de Governança | C | C (mantém) | Decisão estrutural: fusão de canônicos, telemetria centralizada, governança escalonada |
| DEC-030 | Aceite de valor E1–E3: APROVADO | C | C (mantém) | Decisão de valor irreversível-ish (aceite do PO); ato de maior peso do log |
| DEC-031 | Bifurcação do log de decisões (índice + corpos) | C | C (mantém) | Decisão estrutural sobre o próprio SoT de decisões; consequências de navegação permanentes |
| DEC-032 | Kickoff formal da Fase 2 (F-ÚNICO-2, Evolução) | C | C (mantém) | Decisão real: confirma P10, autoriza fatia Classe B, define gates de saída e exclusões |
| DEC-033 | Dedupe atômico por idempotency_key (LAC-IDEMP-01) | C | C (mantém) | Decisão técnica real que altera semântica (reentrega → no-op deduplicado); supersede ADR-003 parcial |
| DEC-034 | Piloto manual mínimo desbloqueado | D | C (default) | Desbloqueio reversível e limitado; pode ser visto como operacional — requer desempate humano |
| DEC-035 | Aceite do piloto manual mínimo + proposta de faixa de KPIs | A | B | "Sim, aceito o piloto" ratifica resultado do piloto; KPIs ficam como proposta não aprovada |
| DEC-036 | Ratificação docs/00 vigente + fail_under=80 | A | B | Ratificação explícita pelo título; atenção: altera gate de cobertura — revisar impacto antes de rebaixar |
| DEC-037 | Reorganização do SoT de agente para `.agents/` | C | C (mantém) | Decisão estrutural real: migração SoT para `.agents/` com stubs e paths reescritos |

## Contagem por categoria

| Categoria | Quantidade | DECs |
|---|---|---|
| A — Ratificação de decisão já tomada | 7 | DEC-002, DEC-019, DEC-020, DEC-021, DEC-022, DEC-035, DEC-036 |
| B — Registro/planejamento/consolidação | 6 | DEC-001, DEC-009, DEC-010, DEC-011, DEC-012, DEC-026 |
| C — Decisão real nova, irreversível | 12 | DEC-003, DEC-005, DEC-006, DEC-018, DEC-023, DEC-024, DEC-029, DEC-030, DEC-031, DEC-032, DEC-033, DEC-037 |
| D — Ambígua / discussão humana | 2 | DEC-004, DEC-034 |
| **Total** | **27** | |

## Se a proposta for aceita

- Reclassificadas para **Classe B**: 7 (A) + 6 (B) = **13 DECs**
- Permanecem **Classe C**: 12 (C) + 2 (D, por default) = **14 DECs**
- **Redução: 27 → 14** Classe C

**A meta ≤ 10 NÃO é atingida por esta proposta.** Atingir ≤ 10 exigiria o mantenedor
reconsiderar também itens hoje em C — candidatos naturais (a juízo humano, não desta
agente): DEC-023 (política segredos, provavelmente Classe B operacional) e DEC-024
(consolidação + início F-ÚNICO-2, talvez B), ou promover os 2 itens D após discussão.
Nenhuma dessas extrapolações está proposta aqui — apenas sinalizadas para o humano.

## Notas e ressalvas

- Reclassificação **não** altera conteúdo, histórico nem status de vigência — apenas a
  *classe de autonomia* atribuída ao ato decisório, para fins de cerimônia/governança.
- DEC-036 altera gate de cobertura (fail_under 50→80): rebaixar a classe B reduz
  cerimônia, não o efeito normativo do gate; o humano deve confirmar se aceita isso.
- DEC-037 (esta reorganização) foi tratada como C estrutural; se o mantenedor considerar
  "padrão de mercado" puramente operacional, pode reavaliar — não proposto aqui.
- Pauta DECs (009–012) permanecem B independente da reclassificação das decisões que
  as ratificaram (019–022).
- **Nada foi aplicado.** Esta proposta aguarda decisão humana (Classe C).
