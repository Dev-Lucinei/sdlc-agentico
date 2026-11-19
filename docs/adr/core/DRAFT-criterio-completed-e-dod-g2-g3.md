---
title: "DRAFT — Critério operacional de `completed` e DoD de saída G2→G3 (Fase 2, F2.7-téc)"
date: "2026-11-18"
project: "sdlc-agentico"
source: "tech-lead/code-implementer (sessão atual), DEC-032 F2.7-téc"
status: "draft — não aprovado; promoção a accepted = Classe C"
---

> **Aviso obrigatório:** este é um **rascunho NÃO numerado** (prefixo `DRAFT-`, sem identidade ADR-NNN), autorizado pela fatia Classe B da Fase 2 (DEC-032, 2026-11-18, F2.7-téc) exclusivamente para **propor** (i) o critério operacional de `completed` e (ii) o DoD de saída G2→G3. **Nada aqui é vigente.** Promoção deste rascunho a ADR `accepted` (numerado) é **Classe C** futura, exclusiva do Mantenedor/PO, com registro em `docs/DECISIONS.md`. Nenhuma semântica `done/completed/approved` vigente é alterada por este documento; nenhum status de ADR accepted é modificado; nenhum `approved` é declarado. G3 "verde"/operacional **não** é declarável por este rascunho (DEC-032, seção (d)).

**Classe de autonomia declarada:** B (proposta documental reversível; nenhuma ação Classe C executada; nenhum `approved`/`completed` declarado como fato).

## a. Contexto

- **Lacuna do critério operacional de `completed`:** a semântica canônica `done ⇏ completed ⇏ approved` está fixada (ADR-005 `accepted`, DEC-020; Contrato Canônico v1.0.0 §(iii)/(iv), adotado por DEC-021, 2026-11-17), mas o **critério operacional exato** de `completed` no tracking alvo (`docs/` como trilha, DEC-006(vi); sem board/tool — DEC-027) permanece `[LACUNA]` aberto desde `docs/historico/41-agentstate-esquema-v0.md` §4.1 (e §"Premissas e Lacunas"), `docs/48-contrato-canonico-v1-0-0.md` §(iv)/§(vi) e DEC-024/DEC-030. O painel (`docs/00-painel-gerencial-consolidado.md` §1, linha "Execução de implementação") lista o critério operacional de `completed` como pendência real da Fase 2.
- **DoD de saída da fatia G2→G3 inexistente como gate verde:** os gates G2 (Endurecimento) e G3 (Escala/governança) estão descritos em `docs/30-arquitetura-tech-lead-baseline-v0.md` (§ Gates; F3) e o gate executável `make audit-g2` foi materializado (DEC-032 F2.1-téc), porém **não existe DoD binário e verificável** que defina as condições de saída da fatia técnica G2→G3 na Fase 2. Sem DoD, o fechamento G2→G3 fica indeterminado e sujeito a declaração por inferência — o que viola a regra de ouro do repo (execução ≠ `completed` ≠ `approved`).
- **DEC-032 (2026-11-18, Classe C)** autorizou, na fatia técnica Classe B, o item **F2.7-téc**: "ADR draft **NÃO numerado** sobre critério operacional de `completed` + DoD G2→G3 (promoção a `accepted` = Classe C futura)". Gates de saída propostos no DEC-032 §(c): G-F2-1 (processo), G-F2-2 (qualidade), G-F2-3 (valor — PO por incremento), G-F2-4 (fechamento — painel/JSON/README consistentes). Itens explicitamente fora de escopo (§(d)): E4/F2.3, **G3 verde/operacional e piloto multi-papel como marco**, LangGraph, CI externo, alteração de thresholds, promoção de KPIs/visão a `approved`, `docs/evidence/` (DEC-005).
- **Referências de taxonomia (vigentes, não alteradas por este rascunho):** `done/blocked/partial` = execução de subagente (nunca implica `completed` nem `approved`); `completed` = operacional/OPS do sistema; `approved` = valor, exclusivo do PO (Decision/Acceptance com `evidence` + `decided_by` + `decided_at`).

## b. Decisão PROPOSTA (não vigente) — Critério operacional de `completed`

> **STATUS: PROPOSTA.** Não é gate vigente, não é aceito, não altera o Contrato v1.0.0 nem ADRs accepted. Vigência somente após promoção Classe C futura (ou decisão equivalente registrada).

**Definição proposta.** `completed` é o **estado operacional/OPS do SISTEMA** — não é estado de execução de subagente e não é estado de valor. Uma tarefa/incremento transita para `completed` quando **todos** os itens abaixo se verificam:

1. **Execução `done` com evidência verificável referenciada** — resumo(s) de subagente em `done` com `evidence_refs` não vazio, rastreável ao item (trilha `docs/`, DEC-006(vi)).
2. **Gates aplicáveis verdes** — `make audit-g2` com exit 0 (ruff + mypy `src` + pytest com cobertura ≥ `fail_under` lido do `pyproject.toml` + SAST `ruff --select S src/`), e `make audit` exit 0 quando aplicável ao item. Thresholds **sempre** lidos do `pyproject.toml` do projeto-alvo (`fail_under=50` vigente; DEC-018/DEC-022) — nunca hardcodados, nunca alterados por este rascunho.
3. **Integridade do event log verificada** — `verify_chain().ok == True` (`src/persistence.py`, `ChainVerificationResult.ok`), quando o item toca persistência/event log; para itens sem superfície de persistência, este item é `N/A` justificado explicitamente (não silenciosamente).
4. **Consistência documental** — `docs/README.md` (índice), artefatos numerados e `docs/schemas/painel-status.json` consistentes com a realidade do repositório; zero divergência conhecida índice ↔ numerados ↔ painel; lacunas remanescentes registradas explicitamente como `[LACUNA]`.
5. **Decisão Classe C humana registrada quando o item for Classe C** — decisão do Mantenedor/PO registrada em `docs/DECISIONS.md` (ou corpo correspondente em `docs/decisions/`) **antes** de qualquer marca de fechamento que implique aceite. **Sem decisão Classe C registrada, o item alcança no máximo `completed` — NUNCA `approved`.**

**Mapeamento (execução → operação → valor):**

```
subagente done  →  (gates + integridade + docs consistentes)  →  completed  →  (PO Decision/Acceptance)  →  approved
   (execução)              (itens 1–4 deste critério)            (OPS)            (item 5; só p/ valor)      (valor)
```

- `completed ≠ approved`; `approved` nunca ocorre por inferência de gates, testes, cobertura ou execução.
- `done ⇏ completed`: execução concluída não fecha o item no sistema operacional sem os itens 2–4.
- `completed ⇏ approved`: item concluído operacionalmente permanece `pending` para valor até decisão do PO.
- Nenhuma transição entre camadas é automática (Contrato v1.0.0 §(iii); ADR-005).

**Quem marca `completed`:**

- Itens 1–4: podem ser verificados por gate automatizado (`make audit-g2`, `verify_chain()`, checagem de consistência documental) **e/ou** pelo humano/mantenedor — a verificação é necessária, não suficiente para itens Classe C.
- Item 5: **sempre humano** (Mantenedor/PO), com registro. Agente de execução nunca escreve `approved` nem "aprova" Classe C.
- **Default vigente (até decisão em contrário):** a autoridade para marcar `completed` hoje é o **Mantenedor** (humano), apoiado em evidência automatizada para os itens 1–4. Nenhum agente/subagente marca `completed` por conta própria.

## c. Decisão PROPOSTA (não vigente) — DoD de saída G2→G3 (fatia técnica da Fase 2)

> **STATUS: PROPOSTA.** DoD binário e verificável, mapeado aos gates G-F2-* do DEC-032 §(c). **G3 "verde"/operacional NÃO é declarável por este rascunho** — promoção de semáforo/marco (G3 verde, piloto multi-papel como marco) é Classe C futura (DEC-032 §(d)).

DoD de saída da fatia técnica G2→G3 — cada item é binário (`pass`/`fail`) e verificável:

| # | Item do DoD | Gate DEC-032 | Evidência esperada |
|---|---|---|---|
| 1 | `make audit-g2` com **exit 0** (ruff + mypy `src` + pytest cobertura ≥ `fail_under` lido do `pyproject.toml` + SAST `ruff --select S src/`) | G-F2-2 | Saída do target com `fail_under` impresso pelo próprio Makefile |
| 2 | `make audit` com **exit 0** (G0–G3 + verificação de `pyproject.toml`; fail-closed exit 6 se ausente) | G-F2-2 | Saída do target `audit` |
| 3 | `verify_chain()` **testado**, incluindo **teste negativo de corrupção** (event log adulterado ⇒ `ok == False` / `strict=True` levanta `PersistenceIntegrityError`) | G-F2-2 | Testes em `tests/` cobrindo caminho feliz e corrupção |
| 4 | **Reentrega at-least-once com dedupe comprovado** (idempotência/dedupe e2e; ADR-003) | G-F2-1 / G-F2-2 | Teste e2e demonstrando dedupe por `idempotency_key` |
| 5 | **Logs JSON com `correlation_id` em 100% dos envelopes de teste** (observabilidade mínima, sem backend externo; ADR-007; `src/observability.py`) | G-F2-2 | Asserção de presença de `correlation_id` nos envelopes/eventos de teste |
| 6 | **mypy incremental endurecido** (overrides por módulo; limpeza de aliases de `quality_gates.py`) **sem alterar `fail_under`** nem thresholds (F2.5-téc) | G-F2-2 | Config mypy com overrides por módulo; `git diff` sem alteração de `fail_under` |
| 7 | **Auditoria G3 registrada com evidência** — ADRs revistas (001–008 + este draft quando promovido), trilha `docs/` percorrida, `verify_chain()` executado e referenciado | G-F2-4 | Registro da auditoria (em `docs/`, trilha vigente) com referências verificáveis |
| 8 | **Painel/README/JSON consistentes** — `docs/00-painel-gerencial-consolidado.md` §0/§1, `docs/README.md` e `docs/schemas/painel-status.json` sem divergência entre si nem com os artefatos numerados | G-F2-4 | Checagem cruzada documentada |
| 9 | **Zero divergência conhecida índice ↔ numerados ↔ painel** (ou divergências registradas explicitamente como `[LACUNA]` com dono) | G-F2-4 | Lista vazia ou lacunas explicitadas com dono |
| 10 | **Toda dívida técnica registrada com dono** (quem, o quê, prazo/marco ou `[LACUNA]`) | G-F2-1 / G-F2-4 | Registro de dívida com dono explícito |
| 11 | **G-F2-1 (processo):** F2.1 + F2.2 remanescente `done` com evidência; **G-F2-3 (valor):** Decision/Acceptance do PO por incremento — **nunca por inferência** | G-F2-1 / G-F2-3 | Resumos de subagente `done` + decisões PO registradas |

Regras deste DoD:

- **Binariedade:** cada item é `pass` ou `fail`; "quase" = `fail`. Item não aplicável exige justificativa explícita registrada (não omissão silenciosa).
- **Sem promoção de marco:** satisfazer este DoD **não** declara G3 verde/operacional, não promove semáforo, não promove KPIs/visão/MVP, não cria `docs/evidence/` (DEC-005), não fecha E4 (DEC-030).
- **Gate humano preservado:** G-F2-3 (valor) é sempre decisão do PO/Mantenedor; nenhum agente o satisfaz por execução.
- **Thresholds inalterados:** `fail_under=50` (DEC-018/DEC-022) permanece; alteração é Classe C fora de escopo (DEC-032 §(d)).

## d. Consequências

**O que muda — se (e somente se) este rascunho for promovido a ADR `accepted` (Classe C futura):**

- O critério operacional de `completed` deixa de ser `[LACUNA]` e passa a ser referência canônica para fechamento de itens no tracking `docs/` (DEC-006(vi)).
- O DoD G2→G3 passa a ser checklist vinculante para a fatia técnica da Fase 2 (F2.x-téc), com verificação binária e evidência.
- Auditorias G3 passam a ter escopo definido (ADRs, trilha `docs/`, `verify_chain()`).
- Rastreabilidade `done → completed → pending → approved` ganha guarda operacional explícita nos itens 2–4.

**O que NÃO muda (independente de promoção):**

- **`approved` continua exclusivo do PO** (Decision/Acceptance, `evidence` + `decided_by` + `decided_at`); agente nunca escreve `approved`.
- **E4/F2.3 continua fora de escopo** e não aprovado (DEC-030, DEC-032 §(d)).
- **Thresholds inalterados** (`fail_under=50`; DEC-018/DEC-022); alteração = Classe C.
- **Taxonomia vigente preservada** (ADR-005/ADR-006 `accepted`; Contrato v1.0.0 §(iii)/(iv)): `done ⇏ completed ⇏ approved`.
- **Sem CI externo, sem LangGraph, sem tracking externo** (DEC-018, DEC-027, DEC-032 §(d)).
- **Promoção de semáforo/G3 verde = Classe C**, nunca por este rascunho nem por execução de gates.
- **Itens Classe C exigem decisão humana registrada** independentemente de gates verdes.

## e. Lacunas e questões abertas

1. **Critério exato de "gates aplicáveis verdes" para itens documentais puros** (ex.: edição de índice/painel sem código): `make audit-g2` cobre código, não docs; falta definir se itens documentais exigem apenas consistência (item 4 do critério) ou também algum gate documental automatizado (inexistente hoje). `[LACUNA]`
2. **Periodicidade da auditoria G3** (item 7 do DoD): este rascunho não fixa cadência (por release? por marco? sob demanda?). DEC-032 não autoriza declarar G3 verde; a periodicidade depende de decisão Classe C futura. `[LACUNA]`
3. **Relação com D-V0-05 / DEC-021:** `completed` é semântica operacional fixada pelo Contrato v1.0.0 §(iii)/(iv), mas **não é cláusula normativa do contrato** no sentido de gate executável — a ferramenta/tracking continua `docs/` (DEC-006(vi)). Este rascunho não altera o Contrato v1.0.0; eventual incorporação formal seria mudança de contrato (Classe C). `[LACUNA]`
4. **Autoridade para marcar `completed` hoje:** default = **Mantenedor** (humano), com apoio de evidência automatizada para itens 1–4; itens Classe C exigem decisão registrada independentemente. Formalizar essa autoridade (quem além do Mantenedor, se alguém) é decisão futura. `[LACUNA]`
5. **Interação com DEC-032 §(c) G-F2-4:** a consistência painel/README/JSON é gate de fechamento da Fase 2; este rascunho propõe o item, mas a atualização efetiva do painel/JSON é propagação do fecho (fora do escopo desta criação).
6. **Estratégia de promoção deste rascunho:** numeração (ADR-009?), escopo (único ADR vs. dois ADRs separados — critério `completed` e DoD G2→G3) e momento da Classe C são decisões futuras do Mantenedor. Não pré-comprometidas aqui. `[LACUNA]`
7. **Critério para "N/A justificado" do item 3 (integridade):** falta regra objetiva de quais itens dispensam `verify_chain()` (hoje: julgamento do Mantenedor caso a caso). `[LACUNA]`

## f. Alternativas consideradas e rejeitadas

1. **`completed` = sinônimo de `done`** — **rejeitada.** Colapsa execução e operação, viola ADR-005 (`accepted`), Contrato v1.0.0 §(iii)/(iv) e DEC-021 (D-V0-05), e reabre a divergência DIV-1/DIV-4 registrada em `docs/historico/47-roadmap-unico-fundacao-mvp-evolucao-v0.md`. Produziria falso "completed" por inferência de execução.
2. **`completed` por inferência de gates, sem humano, inclusive para itens Classe C** — **rejeitada.** Gates verdes são evidência de qualidade técnica, não de decisão; para itens Classe C, a decisão humana registrada é condição necessária (DEC-032 §(c) G-F2-3; regra de ouro do repo; ADR-005). Automação pode verificar itens 1–4; o item 5 é sempre humano.
3. **Não definir nada (manter a lacuna)** — **rejeitada.** Mantém o critério operacional de `completed` como `[LACUNA]` indefinidamente e o DoD G2→G3 como gate inexistente, perpetuando risco de declaração por inferência no fechamento da Fase 2 — exatamente o que DEC-032 F2.7-téc mandou endereçar (ainda que como draft não vigente).
4. **Declarar G3 verde/operacional neste documento** — **rejeitada.** Explicitamente fora de escopo (DEC-032 §(d)); promoção de marco/semáforo é Classe C. Este rascunho apenas propõe o DoD; não executa nem atesta seu cumprimento.
5. **Numerar este documento como ADR-009** — **rejeitada.** DEC-032 F2.7-téc autoriza draft **NÃO numerado**; numeração e promoção a `accepted` são Classe C futura.

## Fontes consultadas (2026-11-18)

- `docs/historico/41-agentstate-esquema-v0.md` §4.1, §"Premissas e Lacunas" (lacuna de `completed`; mapeamento de estados)
- `docs/48-contrato-canonico-v1-0-0.md` §(iii), §(iv), §(vi) (semântica; critério proposto no contrato; `[LACUNA]` do tracking; invariantes)
- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Gates G0–G3 (G2: threshold absoluto ≥50%, 0 erros críticos; G3: ADRs revistas, auditoria periódica de trilhas)
- `docs/00-painel-gerencial-consolidado.md` §1 ("Execução de implementação" — critério de `completed` como pendência da Fase 2)
- `docs/DECISIONS.md` + `docs/decisions/DEC-032-kickoff-fase2-evolucao.md` (DEC-032 F2.7-téc; gates G-F2-1…4; escopo (d)); DEC-021/DEC-022 (contrato/thresholds); DEC-024 (baseline); DEC-030 (E1–E3 approved; E4 fora)
- `docs/adr/core/ADR-005-modelo-estados-autonomia.md` (taxonomia; `accepted`) e `docs/adr/core/ADR-006-qualidade-incremental-gates.md` (gates incrementais; `accepted`)
- `src/persistence.py` (`verify_chain()` → `ChainVerificationResult.ok`); `src/observability.py` (logs JSON + `correlation_id`); `Makefile` (`audit`, `audit-g2`); `pyproject.toml` (`fail_under = 50`)
- `docs/README.md` §ADRs (índice atualizado para listar este draft como não aprovado)

## Evidências

- Arquivo criado: `docs/adr/core/DRAFT-criterio-completed-e-dod-g2-g3.md` (este documento), 2026-11-18.
- Nenhuma alteração em `src/`, `tests/`, `docs/decisions/*`, `docs/DECISIONS.md`, painel ou ADRs accepted.
- Nenhum commit executado. Nenhuma promoção de status. Nenhum `approved` declarado.
