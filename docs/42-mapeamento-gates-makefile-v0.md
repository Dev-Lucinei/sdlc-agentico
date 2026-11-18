---
title: "Mapeamento de Gates de Validação ↔ Makefile (v0, proposta)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead (subagente; classe B; t2 da demanda de design dos itens de execução agêntica)"
status: "condicional"
---
> **HISTÓRICO/SUPERSEDED** — documento de design/kickoff condicional, não executável como está; a implementação vigente é a Fase 1 em `src/` (65 testes, 75,00% cobertura; E1–E3 approved por DEC-030). Registrado como histórico; dúvidas → `docs/DECISIONS.md` e `git log`.

> **Change Control:** inclusão condicional na baseline v0 autorizada por CR-002 / DEC-003 (`docs/DECISIONS.md`) — o conteúdo permanece `condicional`; isto NÃO aprova o conteúdo nem inicia implementação.

**Classe de autonomia declarada:** B (proposta documental reversível; nenhuma ação Classe C executada; nenhum `approved` declarado).

> **Aviso obrigatório:** Proposta de design — **não é implementação aprovada**; stack LangGraph condicional (CR-009-C); D-V0-06 APROVADO E MATERIALIZADO (DEC-022, 2026-11-17) — thresholds absolutos cobertura ≥50%, 0 erros críticos; nenhum `approved` declarado.
>
> **Atualização 2026-11-16:** `Makefile` e `pyproject.toml` foram **materializados (parametrizados, fail-closed)** neste repositório (DEC-016 — materialização concluída). Thresholds numéricos são **materializados** (`fail_under=50` neste repo; D-V0-06 materializado (DEC-022)); thresholds parametrizados valem para projetos-alvo futuros (lidos do `pyproject.toml` do projeto-alvo — nunca hardcoded). Os alvos de design (`make lint-ads`, `make test-unit`, `make test-integration`) e suas assinaturas abaixo permanecem **proposta condicional** (alvos não implementados). `specs/` e CI de aplicação **não existem**.

## 🔧 Decisão / Diagnóstico
Propõe-se mapear os quatro gates de validação do ciclo de vida (**Design → Arquitetura → Coding → QA**) para três alvos de Makefile (`lint-ads`, `test-unit`, `test-integration`), com assinaturas de entrada/saída e uma **tabela determinística `exit_code → AgentState`** (campos `errors[]`, `integration_test_output`, `pr_ready`, `tasks[].status`) que permite o ciclo de reparo automático definido em t4/t5. **Trade-off assumido:** alvos mínimos e monosemânticos (poucos entrypoints, comportamento determinístico por exit code) em detrimento de granularidade de diagnóstico — erros são classificados por faixa de exit code e refinados por `error_class` no `AgentState`, não por parsing de logs. Dependência obrigatória de t1 (`docs/41-agentstate-esquema-v0.md`).

## 🗂️ Artefato

### 1) Gates do ciclo de vida × comandos do Makefile (proposta)

| Gate (ciclo de vida) | Nó/fase | Comando Makefile (proposta) | Assinatura de entrada | Assinatura de saída (esperada) |
|---|---|---|---|---|
| **Design** (ADS + Mermaid válidos) | `design` (t3) | `make lint-ads` | `ADS_PATH=<caminho do ADS>` (proposta: `specs/current_ads.md` — **inexistente; proposta**); `SCHEMA_REF` opcional | stdout/stderr: relatório de lint (regras ADS + presença de Mermaid); exit `0|1|5`; artefato de relatório `[PREMISSA: .artifacts/lint-ads.log]` |
| **Arquitetura** (consistência técnica do ADS/desenho; gate de bloqueio) | `architecture` (t3) | `make lint-ads ADS_KIND=architecture` (mesmo alvo, **escopo proposto**) — ver nota §5 | `ADS_PATH`, `ADS_KIND=architecture`, `GLOBAL_CONTEXT_REF` | stdout/stderr: relatório de consistência (contratos, estados, transições vs t1); exit `0|1|5`; inconsistência = `[LACUNA]` registrada + bloqueio (t3) |
| **Coding → QA unitária** (validação pós-TDD) | `tdd` → `qa/unit` (t4) | `make test-unit` | `TASK_ID=<ULID>`; `PROJECT`/`PKG` `[LACUNA]` | stdout/stderr: resultado de testes unitários + cobertura medida (limiar lido do `pyproject.toml`, **[LACUNA]**); exit `0|2|4` |
| **QA integração** (pré-PR) | `qa/integration` (t4/t5) | `make test-integration` | `TASK_ID=<ULID>`; `ENV=<ambiente de integração [LACUNA]>` | stdout/stderr: resultado de integração; exit `0|3|4`; alimenta `integration_test_output` |

**Nota (§5):** dois usos do mesmo alvo (`lint-ads`) para Design e Arquitetura é decisão deliberada de minimizar superfície de automação inexistente; alternativamente, um alvo futuro `make lint-arch` poderia ser proposto — **não criado, não assumido** `[LACUNA]`.

### 2) Tabela obrigatória: `exit_code → AgentState` (ciclo de reparo)

Todo alvo retorna exit code inteiro. O dispatcher (t5) **deve** traduzir o código para o `AgentState` conforme a tabela antes de qualquer retry; nenhuma falha avança o grafo sem registro em `errors[]`.

| `exit_code` | Origem (gate) | `errors[].source_gate` | `errors[].error_class` | Efeito no `AgentState` (t1) | Reparo | **Ação automática do sistema** |
|---|---|---|---|---|---|---|
| `0` | qualquer | — | — | Portão verde; `tasks[].status` avança; `errors[].attempt` preservado para auditoria | — | prosseguir para próximo nó |
| `1` | `lint-ads` (design/arch) | `make lint-ads` | `logica` | `errors[] += {error_class:"logica", exit_code:1}`; `ads[].status=blocked` ou `tasks[].status=blocked` conforme nó | Retorno ao nó de origem (`design`/`architecture`); correção direcionada | retornar a Coding (falha de lint/format) |
| `2` | `test-unit` | `make test-unit` | `logica` (ou `flaky` se heurística de flake declarar) | `errors[] += {...}`; `tasks[].attempts += 1`; `integration_test_output` **inalterado** (ainda não executada) | **Retorno forçado ao nó `coding`** (t4); TDD revalida antes de nova unitária | retornar a Coding (falha de tipo) |
| `3` | `test-integration` | `make test-integration` | `logica` ou `ambiente` | `errors[] += {...}`; `integration_test_output="failure"`; `pr_ready=false`; `tasks[].attempts += 1` | **Retorno forçado ao nó `coding`** (t4) | retornar a Coding (falha unitária) |
| `4` | qualquer (ferramenta ausente/env quebrado) | gate que falhou | `ambiente` | `errors[] += {...}`; `tasks[].status=blocked`; escala | **Sem retry cego**; intervenção humana/infra | retornar a Coding (falha de integração) |
| `5` | `lint-ads` (contrato/schema) | `make lint-ads` | `logica` | `errors[] += {...}`; `ads[].status=blocked` | Retorno a `design`; ADS inválido nunca avança | bloquear (falha de segurança) |
| `6` | `pr_generation` (gate de cobertura; `pyproject.toml` materializado, threshold absoluto cobertura ≥50% — DEC-018/DEC-022) | `coverage` (t5) | `lacuna` | `errors[] += {... exit_code:6}`; `pr_ready=false`; `integration_test_output` inalterado; `pr_generation` **bloqueado (fail-closed)** | Retorno a `coding`/`tdd` para elevar cobertura; **nunca** avançar PR | bloquear PR generation (cobertura abaixo do threshold) |
| `10` | `lint-ads` (`ADS_KIND=architecture`, inconsistência técnica) | `make lint-ads` | `lacuna` | `errors[] += {...}`; inconsistência marcada `[LACUNA]`; **avanço para Coding bloqueado** (t3) | Retorno a `architecture`; exige resolução humana ou nova evidência | escalar (erro de ambiente) |
| `130` | qualquer (SIGINT/watchdog/1 crítico) | gate que falhou | `critico` | `errors[] += {...}`; `tasks[].status=blocked`; interrupção imediata | **Parada total + escala humana** (autonomia-e-estados: 1 crítico → stop) | interromper (SIGINT) |
| `>=64` | não mapeado | gate que falhou | `lacuna` | `errors[] += {...}` com `message="exit code não mapeado"` | Tratar como `[LACUNA]`; **nunca** inferir sucesso | escalar (erro fatal) |

Nota: `exit_code 6` é gerado pelo gate de cobertura do grafo (t5, `source_gate="coverage"`) quando a cobertura medida fica abaixo do threshold do `pyproject.toml` (materializado, parametrizado, fail-closed; D-V0-06 materializado (DEC-022)) — adicionado em 2026-11-16 após revisão do gerente-projeto (PM) para fechar a inconsistência t2×t5.

**Regra dos 3 strikes:** `tasks[].attempts >= 3` na mesma validação ⇒ `tasks[].status=blocked` + escalonamento humano, independentemente de `error_class` (exceto `critico`, que para na 1ª ocorrência). Consistente com `docs/30-arquitetura-tech-lead-baseline-v0.md` §Tratamento de falhas.

### 3) Fluxo de reparo automático (sequência esperada)

```
coding → (patch) → tdd → make test-unit ──exit 0──► qa/integration → make test-integration ──exit 0──► integration_test_output=success ─► pr_ready=true (se gates verdes) → pr_generation (t5)
                      │                                     │
                   exit 2/1                            exit 3/1/4
                      ▼                                     ▼
              errors[] += ...; attempts += 1        errors[] += ...; integration_test_output=failure; pr_ready=false
                      └────────────► retorno forçado a CODING ◄────────────┘
```

### 4) Gates × evidências (DoD técnico incremental, proposta)
| Gate | Evidência mínima esperada | Baseline "no new errors" |
|---|---|---|
| Design | Relatório `lint-ads` exit 0 + ADS com Mermaid (`ads[].mermaid_present=true`) | Zero erros de schema ADS na emissão atual |
| Arquitetura | Relatório exit 0 + `[LACUNA]`s registradas (nenhuma silenciosa) | Zero inconsistência bloqueante aberta |
| Coding/QA unitária | Exit 0 + cobertura medida ≥ limiar do projeto-alvo `[LACUNA]` | Sem nova falha vs baseline declarada |
| QA integração | Exit 0 + `integration_test_output=success` | Idem |

### 5) O que NÃO existe (verificação explícita em 2026-11-16)
- `Makefile` na raiz do repo — **criado (parametrizado)**; thresholds reais: D-V0-06 materializado (DEC-022) (`fail_under=50`). (Alvos `lint-ads`/`test-unit`/`test-integration` do design permanecem proposta — não implementados.)
- `pyproject.toml` — **criado (parametrizado, fail-closed)**; neste repo `fail_under=50` (D-V0-06 materializado (DEC-022)); thresholds para projetos-alvo futuros são parametrizados, lidos do `pyproject.toml` do alvo.
- `specs/current_ads.md` — **não existe**; citado apenas como template proposto (t3).
- CI/ferramentas (lint/test/scan de aplicação) — **não existem**; G0–G3 de `docs/30` §Gates permanecem proposta.

## Evidências
- `docs/41-agentstate-esquema-v0.md` (t1; campos `errors[].source_gate/exit_code/error_class`, `integration_test_output`, `pr_ready`, `tasks[].attempts/status`) — criado nesta entrega e lido.
- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Qualidade e Gates (G0–G3; "no new errors"; thresholds lidos do `pyproject.toml`, nunca hardcoded).
- `docs/20-governanca-pm-plano-baseline-v0.md` §5 (DoD: sem evidência não há `done`).
- Verificação local em 2026-11-16: `Makefile` e `pyproject.toml` materializados (parametrizados, fail-closed); `specs/` ausente.

## Premissas e Lacunas
- **[LACUNA]** Alvos `lint-ads`/`test-unit`/`test-integration`, sua gramática de flags (`ADS_KIND`, `TASK_ID`, `ENV`) e semântica exata de relatórios: inexistentes; definição pendente de implementação (alvos não criados); D-V0-06 materializado (DEC-022).
- **[LACUNA]** Threshold numérico de cobertura/lint/tipos: será lido do `pyproject.toml` do projeto-alvo quando existir; **nenhum valor hardcoded**.
- **[LACUNA]** `error_class=flaky` exige política de detecção de flake (retry com backoff, máx 3x) ainda não definida; classe `ambiente` vs `logica` pode exigir triagem humana.
- **[LACUNA]** Destino de artefatos de relatório (`.artifacts/`, logs) e retenção: indefinido; `[PREMISSA]` referenciado como caminho lógico.
- **[PREMISSA]** Exit codes `10`/`>=64` são extensão proposta desta tabela; alvos reais podem adotar convenção distinta — mapear na implementação (D-V0-01/06).
- **[PREMISSA]** `make test-integration` pressupõe ambiente de integração isolado; sem `ENV` definido, proposta não executável.

## ✅ Próximas Ações
1. Incorporar esta tabela à política de gates/thresholds com D-V0-06 materializado (DEC-022) — Dono: TL (R), PM/PO (C) — Prazo: F0/F1 `[LACUNA]`.
2. Escrever o `Makefile` (ou pipeline equivalente) no **repositório-alvo** (não neste repo), com alvos e exit codes conforme §1–§2 — Dono: TL/DevEx — Prazo: após D-V0-01.
3. Definir no projeto-alvo o `pyproject.toml` com limiar de cobertura; documentar a leitura nele na fase de gates G2 — Dono: TL — Prazo: F3 `[LACUNA]`.
4. t3/t4/t5 consomem esta tabela como contrato de reparo — Dono: tech-lead — Prazo: esta entrega.
