---
title: "ADR-008 — Paradigma 'Autonomia com Previsibilidade' e princípio fail-closed"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead"
status: "accepted"
---

## Contexto

O SDLC agêntico nasce em um cenário de tensão estrutural: a **autonomia desenfreada** de agentes e subagentes maximiza velocidade local, mas destrói rastreabilidade, auditabilidade e previsibilidade do sistema como um todo; a **orquestração rígida** garante controle, mas pode sufocar a execução e inviabilizar a experimentação. A baseline técnica (`docs/30-arquitetura-tech-lead-baseline-v0.md`) e os canônicos de design (`docs/41`–`docs/45`) convergem para um paradigma híbrido: **autonomia com previsibilidade** — agentes executam com liberdade dentro de contratos rígidos, e o sistema só avança quando há evidência verificável.

Paralelamente, o projeto adota **fail-closed** como princípio de design: na presença de dúvida, lacuna, evidência ausente ou threshold não atingido, o sistema **para** (bloqueia o avanço) em vez de inferir ou assumir um valor. Este princípio é a contrapartida operacional do paradigma: a autonomia é permitida, mas nunca à custa de previsibilidade.

Este ADR formaliza ambos como decisão arquitetural (APROVADO E MATERIALIZADO — Classe C, 2026-11-17; DEC-020).

## Decisão

### 1. Paradigma: "Autonomia com Previsibilidade"

Adotar o paradigma **Autonomia com Previsibilidade** como princípio arquitetural do SDLC agêntico, materializado em quatro pilares:

1. **Dispatcher + Agregador (sem domínio):** o orquestrador coordena e agrega; toda execução de domínio é delegada a subagentes via contratos versionados (ADR-001). Autonomia de execução fica nos subagentes; previsibilidade, na coordenação.
2. **Contratos rígidos na borda:** envelope de delegação + Resumo do Subagente padronizado + JSON machine-readable + `schema_version` (ADR-004, `docs/48`). Nenhuma delegação nem agregação ocorre fora do contrato; campos obrigatórios validados.
3. **Semântica de estados explícita e não intercambiável:** `done/blocked/partial` = execução do subagente (com evidência); `completed` = operacional (OPS); `approved` = valor aceito pelo PO (com evidência e decisão explícita). Proibida a inferência de `approved` a partir de `done` (ADR-005, `docs/48`).
4. **Rastreabilidade ponta a ponta:** demanda/delegação → execução → evidência/artefato → decisão/aceite, persistida no SoT/event log (ADR-002). Toda decisão Classe C registrada em `docs/DECISIONS.md`.

### 2. Princípio fail-closed (seção dedicada)

**Definição:** o sistema **para** (bloqueia avanço / retorna `no_go` / emite `blocked`) na presença de qualquer dúvida, lacuna, evidência ausente, threshold não atingido ou decisão humana pendente. Nunca infere, assume ou promove automaticamente.

**Aplicação concreta:**
- **Gates de qualidade:** thresholds (cobertura, lint, tipos) lidos do `pyproject.toml` do projeto-alvo; ausência do arquivo ou do threshold → fail-closed (exit code 6, gate bloqueia) — nunca default permissivo (`docs/42`, ADR-006).
- **Promoção de status:** nenhuma transição para `approved`/`completed` sem evidência verificável + decisão explícita do dono (PO para valor; humano/arquitetura para Classe C). Execução ≠ aceite.
- **Aceite de valor:** `human_review` é o único escritor de `approved`, com evidência de interação humana (`docs/45`). Architecture Agent tem poder de veto, nunca de aprovação de valor.
- **Baseline v0:** implementação (F-ÚNICO-1) bloqueada enquanto D-V0-01 estiver adiado; publicação do baseline bloqueada até DEC-008/CR-013. "No new errors" exige baseline declarada.

**Trade-offs:**
- **Segurança vs. velocidade:** fail-closed reduz velocidade de entrega (bloqueios frequentes em contexto de lacunas), mas elimina promoções indevidas e regressões silenciosas. Em um sistema agêntico com múltiplos agentes autônomos, o custo de um avanço indevido (drift, decisão irreversível) supera o custo de um bloqueio.
- **Burocracia como segurança:** a exigência de evidência, decisão explícita e registro em `docs/DECISIONS.md` é deliberadamente burocrática — a burocracia é o recurso de segurança, não um atrito a ser eliminado.

**Alternativas rejeitadas:**
1. **Fail-open (avançar na dúvida, corrigir depois)** — rejeitada: em sistemas agênticos com decisões irreversíveis (aceite de valor, promoção de baseline), o custo de reverter supera o custo de bloquear; fail-open permite drift silencioso e promoção indevida de `approved`.
2. **Inferência automática de aprovação** (ex.: `done` ⇒ `approved` quando AC passam) — rejeitada: viola a separação execução/valor e a regra "Execução concluída ≠ Valor entregue/aceito"; remove o humano da decisão de valor.
3. **Thresholds default permissivos** (ex.: cobertura 0% quando `pyproject.toml` ausente) — rejeitada: mascara ausência de baseline; fail-closed exige baseline explícita.

## Status

`accepted` (APROVADO E MATERIALIZADO — Classe C, 2026-11-17; DEC-020).

## Consequências

- **Positivas:** rastreabilidade e auditabilidade end-to-end; previsibilidade do comportamento do sistema agêntico; bloqueio de promoções indevidas; compatibilidade com "no new errors" sobre baseline declarada; alinhamento com DoR/DoD e gates incrementais (ADR-006).
- **Negativas/custos:** overhead de coordenação e validação; latência adicional em fluxos com lacunas; exigência de evidência para cada avanço; risco de estagnação se lacunas não forem fechadas (R8, mitigação: modo documental F-ÚNICO-1).
- **Condicionais:** stack/infra/CI e thresholds numéricos reais permanecem `[LACUNA]` (D-V0-01/D-V0-06); promovido a `accepted` por decisão Classe C do Mantenedor (DEC-020, 2026-11-17).

## Alternativas consideradas

1. **Autonomia plena sem contratos (agentes livres)** — rejeitada: destrói rastreabilidade e permite drift silencioso; incompatível com aceite de valor pelo PO.
2. **Orquestração rígida centralizada (sem autonomia de subagentes)** — rejeitada: sufoca execução e inviabiliza especialização; contradiz o modelo de subagentes especializados.
3. **Fail-open com reconciliação posterior** — rejeitada: ver "Alternativas rejeitadas" do princípio fail-closed acima.

## Evidências

- `docs/00-painel-gerencial-consolidado.md` §1 (semáforo; critérios de 🟢), §3 (convergências; semântica de estados), §6 (riscos; promoção indevida Classe C).
- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Arquitetura proposta; §Qualidade e Gates.
- `docs/41-agentstate-esquema-v0.md` (semântica `done`≠`completed`≠`approved`; transições).
- `docs/42-mapeamento-gates-makefile-v0.md` (exit codes determinísticos; fail-closed exit 6).
- `docs/45-grafo-langgraph-classe-c-v0.md` (`human_review` único escritor de `approved`; `gate_pr_generation` fail-closed).
- `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (contrato v1.0.0; semântica de estados).
- `docs/DECISIONS.md` (DEC-010, DEC-016; D-V0-04 materializado).
- ADR-001 (dispatcher+agregador), ADR-004 (contratos versionados), ADR-005 (modelo de estados), ADR-006 (gates incrementais).
- `~/.opencode/references/autonomia-e-estados.md` (classes de autonomia A/B/C; estados).
- DEC-020 (D-V0-04) — APROVADO E MATERIALIZADO (Classe C, 2026-11-17).