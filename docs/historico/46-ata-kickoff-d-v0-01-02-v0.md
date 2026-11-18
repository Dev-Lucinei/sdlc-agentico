---
title: "Ata de Kickoff — D-V0-01 / D-V0-02 (Contexto e Governança do sdlc-agentico)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "gerente-projeto + Lucinei (Mantenedor)"
status: "vigente"
---
> **HISTÓRICO/SUPERSEDED** — documento de design/kickoff condicional, não executável como está; a implementação vigente é a Fase 1 em `src/` (65 testes, 75,00% cobertura; E1–E3 approved por DEC-030). Registrado como histórico; dúvidas → `docs/DECISIONS.md` e `git log`.

# Ata de Kickoff — D-V0-01 / D-V0-02 (2026-11-16)

**Classe de autonomia desta ata:** B (registro documental reversível, elaborado pelo `gerente-projeto`). As decisões listadas na seção 4 são **Classe C**, decided_by **Lucinei (Mantenedor)**, em 2026-11-16 — registradas canonicamente em `docs/DECISIONS.md`. Esta ata **não** aprova baseline, **não** promove status e **não** declara o baseline v0 pronto.

## 1) Participantes

| Participante | Papel | Natureza |
|---|---|---|
| **Lucinei (Mantenedor)** | Mantenedor humano do repo; decisor Classe C | Humano (única autoridade de aprovação) |
| `gerente-produto` (PO) | Papel de produto sob coordenação | Agente (subagente) |
| `gerente-projeto` (PM) | Papel de governança/coordenação; redator desta ata | Agente (subagente) |
| `tech-lead` (TL) | Papel técnico sob coordenação | Agente (subagente) |
| Orchestrator | Dispatcher + agregador (sem implementação de domínio) | Agente (sessão orquestradora) |

*Nota:* não há outros humanos, sponsor ou operador externo — capacidade = **Mantenedor único** (DEC-006(iv)). Data: 2026-11-16 (horário não registrado `[LACUNA]`). Evidência: **esta sessão (este chat) é a evidência**; esta ata documenta o resultado — não há gravação/ata externa.

## 2) Agenda

1. D-V0-01 — stack, repositório-alvo, infra/CI/gates e restrições (`docs/00` §5).
2. D-V0-02 — stakeholders, capacidade, prazo/orçamento, cadência e tracking (`docs/00` §5).
3. Fila de CRs pós-auditoria externa (`docs/00` §8.2): CR-001 (docs/40), CR-002B/CR-005B (inclusão 41–45 + normativos), CR-003 (LICENSE), CR-004 (`docs/evidence/`), CR-011 (segredos), CR-012 (log de decisões), CR-013 (reconciliação do baseline v0).
4. Desdobramentos: o que permanece `[LACUNA]`; ações e donos; próxima reunião.

## 3) Premissas e critérios aplicados

- Regra de ouro: Classe C exige `decided_by` humano explícito + evidência; execução ≠ `completed` ≠ `approved`; sugestão externa ≠ canon.
- Change control conforme `docs/20` §5; registro canônico de decisões em `docs/DECISIONS.md` (DEC-001).
- Sem promessa de prazo sem buffer (PERT ×1,3) — e sem cadência formal vigente (ver DEC-006(v)).

## 4) Decisões tomadas (2026-11-16, decided_by Lucinei — Classe C salvo indicação contrária)

Detalhes, alternativas e consequências em `docs/DECISIONS.md`. Resumo:

- **DEC-004 (CR-003) — LICENSE: nenhuma por ora (decisão explícita).** Repo mantém todos os direitos reservados. (Classe C)
- **DEC-005 (CR-004) — `docs/evidence/` REJEITADA.** Risco de segunda SoT; evidências permanecem embutidas/por link rastreável até D-V0-05/06. (Classe C)
- **DEC-006 (Kickoff D-V0-01/02) — 6 pontos, todos Classe C:**
  1. **D-V0-01 ADIADO** — stack não definida; LangGraph permanece condicional (canônicos 41–45); implementação não iniciada;
  2. **Repositório-alvo** da implementação futura = **este mesmo repo** (`sdlc-agentico`);
  3. **Infra/CI = nenhuma por ora** (quando houver: F0–F1/baixo risco; repo sem remote configurado);
  4. **Stakeholders/capacidade = Mantenedor único (Lucinei)**;
  5. **Cadência = sob demanda; sem SLA formal** — substitui a `[PREMISSA-P1]` quinzenal do plano I1 (`docs/20`);
  6. **Tracking = nenhuma ferramenta externa; `docs/` é a trilha.**
- **DEC-007 (CR-011) — Política de segredos permanece `[LACUNA]`**; reavaliar após D-V0-01. (Classe B — registro; nenhuma política em vigor)
- **DEC-008 (CR-013) — Reconciliação do baseline v0 planejada**; roadmap único em elaboração em `docs/historico/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` (criado em 2026-11-16 pelo TL como proposta condicional; não editado nesta sessão); **publicação do baseline permanece BLOQUEADA** por D-V0-03/04/05/06. (Classe B — planejamento)

*Registro complementar do mesmo ciclo (2026-11-16):* **DEC-001** (CR-012 — criação de `docs/DECISIONS.md`), **DEC-002** (CR-001 — `docs/40` validado como vigente) e **DEC-003** (CR-002B + CR-005B — inclusão condicional dos canônicos 41–45 na baseline v0, *inclusão ≠ aprovação de conteúdo*; normativos externos `~/.opencode/references/contrato-resumo-subagentes.md` (`163e0aad…`) e `autonomia-e-estados.md` (`776af494…`) referenciados por caminho+sha256 abreviado, **sem** cópia física `[PREMISSA]`). Ver `docs/DECISIONS.md`.

**O que NÃO foi decidido / NÃO está aprovado:** baseline v0; ADRs A–G; contrato v1.0.0; gates/thresholds; aceite do PO (D-V0-03); stack (D-V0-01, adiado); publicação de qualquer baseline. Nenhum `approved` foi declarado.

## 5) O que permanece como `[LACUNA]`

| # | Lacuna | Origem / gatilho de resolução |
|---|---|---|
| L1 | **Política de segredos** (CR-011) | Reavaliar após decisão de D-V0-01 (stack) ou decisão explícita do Mantenedor |
| L2 | **Roadmap de publicação / baseline canônico** (CR-013) | Depende de `docs/historico/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` (roadmap único, em elaboração) + D-V0-03/04/05/06 |
| L3 | **Contrato canônico v1.0.0** (resumo + envelope + estados + correlação + `schema_version`) + taxonomia operacional (`completed`/tracking) — D-V0-05 | TL + PO + PM propõem; adoção pode exigir Classe C (CR-007-C) |
| L4 | **Numeração/convenção ADR** canônica (ADRs A–G propostos, sem número) — CR-006 / D-V0-04 | TL propõe; Mantenedor aprova; `adr_ref` indefinido até lá |
| L5 | **Stack** (inclui LangGraph) — D-V0-01 | **Adiado** por DEC-006(i); nenhuma inferência permitida |
| L6 | **Capacidade/prazo/orçamento e SLA de decisão/aceite** | Mantenedor único, sob demanda, sem SLA (DEC-006(iv)/(v)); estimativas só com buffer quando houver escopo |
| L7 | **Ferramenta de tracking** | `docs/` é a trilha (DEC-006(vi)); ferramenta externa só por decisão futura (CR-010-C, dormente) |
| L8 | **Gates/thresholds unificados** (G0–G3 × t2/t5 × `exit_code`) — CR-008-C / D-V0-06 | TL propõe; depende de D-V0-06; `Makefile`/`pyproject.toml` inexistentes neste repo |

## 6) Ações e donos

| # | Ação | Dono | Prazo / gatilho |
|---|---|---|---|
| A1 | Elaborar roadmap único de reconciliação do baseline v0 (`docs/historico/47-roadmap-unico-fundacao-mvp-evolucao-v0.md`) | PM/TL sob coordenação do Orchestrator | Em elaboração; sem prazo (cadência sob demanda) |
| A2 | Propagar vigência de `docs/40` (front matter → `vigente`) + atualizar índice (`docs/README.md`) e painel (`docs/00` §5/§8, adendo §8.3) para incluir `docs/DECISIONS.md` e esta ata | Orchestrator / subagente designado | Próximo change set (não executado nesta sessão — restrição de escopo) |
| A3 | Recalcular sha256 **completos** dos normativos externos (ou decidir pin exato) | TL | Próximo change set, se o Mantenedor quiser pin exato (DEC-003) |
| A4 | Reavaliar CR-011 (política de segredos) | TL/PM | Após decisão de D-V0-01 (ou decisão explícita do Mantenedor) |
| A5 | Submeter pacote de reconciliação (roadmap, contrato v1.0.0, ADRs, gates) às decisões D-V0-03/04/05/06 | PM (consolidação); PO (aceite de valor); TL (baseline técnica); Mantenedor (Classe C) | Após A1; sem data — sob demanda |
| A6 | Manter `docs/DECISIONS.md` como log de toda decisão subsequente (DEC-009+) | Todos os papéis (via change control, `docs/20` §5) | Contínuo |

## 7) Próxima reunião

**Sob demanda (decisão do Mantenedor).** Não há cadência quinzenal vigente nem SLA formal (DEC-006(v)); reuniões/ checkpoints ocorrem quando o Mantenedor convocar ou quando um gatilho `[LACUNA]`→decisão for atingido (ex.: A1 concluído; D-V0-01 reaberto).

## 8) Declarações finais

- O **baseline v0 NÃO está pronto** e **não** está publicado; permanece `condicional`/não consolidado (`docs/00` §1). Publicação bloqueada por D-V0-03/04/05/06 (DEC-008).
- **Execução ≠ `completed` ≠ `approved`.** Nenhuma decisão desta ata declara valor aceito pelo PO.
- Evidência desta ata: a própria sessão de 2026-11-16 (este chat); não há ata/gravação externa. A ata documenta o resultado; não substitui evidência de execução de itens futuros.
- Rastreabilidade: decisões em `docs/DECISIONS.md` (DEC-001…DEC-008); índice/painel pendentes de propagação (A2); `docs/historico/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` pendente (A1).
