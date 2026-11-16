---
title: "Contrato Canônico v1.0.0 — Proposta (AgentState + Envelope + Estados)"
date: "2026-11-16"
project: "sdlc-agentico"
source: "tech-lead (subagente; classe B; PROPOSTA condicional; D-V0-05 pendente; adoção exige Classe C)"
status: "condicional"
---

**Classe de autonomia declarada:** B (proposta documental reversível; nenhuma ação Classe C executada; nenhum `approved` declarado; nenhum contrato entra em vigor por este documento).

> **Aviso obrigatório:** este é o **Contrato Canônico v1.0.0-PROPOSTA**. Ele **não está aprovado**, **não vira baseline** e **não tem efeito normativo** até decisão explícita do Mantenedor sob **D-V0-05** (Classe C para adoção). Nenhum campo `approved` é escrevível por agente de execução — em nenhuma versão deste contrato. Divergência `0.1.0-draft` × v1.0.0 permanece registrada, não resolvida silenciosamente.

## 🔧 Decisão / Conclusão

Fica proposta a consolidação do **Contrato Canônico v1.0.0** — cobrindo (i) envelope de delegação, (ii) contrato de resumo de subagente, (iii) semântica de estados (execução ≠ operação ≠ valor), (iv) mapeamento execução→operação→valor com critério operacional proposto de `completed`, (v) exit codes unificados, (vi) regra de migração `0.1.0-draft` → `1.0.0` e (vii) versionamento semântico de contratos. **Problema que resolve:** os canônicos de design usam `schema_version 0.1.0-draft` (`docs/41`, `docs/45`) enquanto o D-V0-05 propõe v1.0.0 (`docs/00` §5; `docs/30` §Contratos); **sem contrato único não há** schema registry, **nem** compatibilidade aditiva verificável, **nem** idempotência checável na borda, **nem** aceite auditável. **Trade-off assumido:** explicitação e verbosidade contratual (mais campos, mais invariantes) em detrimento de compacidade — rastreabilidade e auditabilidade são requisitos centrais do baseline v0. **HONESTO:** status `condicional`; adoção exige **Classe C** (D-V0-05); **nada aqui vira baseline sem decisão**; nenhum campo `approved` escrevível por agente; divergência com 41–45 permanece até D-V0-05/06.

## 🗂️ Artefato

### (i) Envelope de delegação (proposta)

Campos mínimos obrigatórios do envelope `sdlc.task.delegation`:

| Campo | Tipo | Obrigatório | Semântica |
|---|---|---|---|
| `schema_name` | string | sim | `"sdlc.task.delegation"` (imutável por versão). |
| `schema_version` | string semver | sim | `"1.0.0"` nesta proposta. Imutável por versão publicada. |
| `envelope_id` | ULID | sim | Identificador único do envelope; nunca reutilizado. |
| `idempotency_key` | string (hash) | sim | `hash(task_id + agent_role + input_fingerprint + schema_version)` — dedupe de reentregas (R7). |
| `correlation_id` | ULID | sim | Correlação ponta a ponta (request→task→run→artifact→gate→decisão). |
| `tarefa` | objeto | sim | `{ objective, role, input_ref, expected_outputs, autonomy_class_expected }` — papel de destino, objetivo e **referência de entrada** (`input_ref`: caminho/URI do insumo). |
| `correlation` | objeto | sim | `{ request_id, task_id, parent_run_id }` (rastreio hierárquico). |
| `acceptance` | objeto | sim | `{ technical_dod[], evidence_required[] }` — critérios técnicos e evidências mínimas. |
| `timestamps` | objeto | sim | `{ created_at }` ISO-8601. |

Exemplo completo (bloco de exemplo, não executável):

```json
{
  "schema_name": "sdlc.task.delegation",
  "schema_version": "1.0.0",
  "envelope_id": "01K8Z3Q7M2N4P6R8T0V1W2X3Y4",
  "idempotency_key": "sha256:9f2c1a7b4e5d60718293a4b5c6d7e8f90123456789abcdef0123456789abcdef",
  "correlation_id": "01K8Z3Q7M2N4P6R8T0V1W2X3A0",
  "tarefa": {
    "objective": "Revisar docs/47 e docs/48 (roadmap unificado + contrato v1.0.0-PROPOSTA) e emitir veredito condicional",
    "role": "tech-lead",
    "input_ref": "docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md",
    "expected_outputs": ["resumo_subagente", "machine_readable_json"],
    "autonomy_class_expected": "B"
  },
  "correlation": {
    "request_id": "01K8Z3Q7M2N4P6R8T0V1W2X3A0",
    "task_id": "01K8Z3Q7M2N4P6R8T0V1W2X3B1",
    "parent_run_id": null
  },
  "acceptance": {
    "technical_dod": ["artefato criado com front matter completo", "nenhuma promoção de estado"],
    "evidence_required": ["caminho do arquivo criado", "leitura dos canônicos citados"]
  },
  "timestamps": { "created_at": "2026-11-16T12:00:00-03:00" }
}
```

### (ii) Contrato de resumo de subagente (proposta)

Obrigatório em toda devolução. Campos obrigatórios (compatível com o normativo vigente e com `docs/30` §Contratos):

| Campo | Obrigatório | Regra |
|---|---|---|
| `objetivo` | sim | O que foi pedido. |
| `ação executada` | sim | O que foi feito (ou não). |
| `resultado/artefato` | sim | Artefato(s) produzido(s) ou `[LACUNA]` explícita. |
| `evidência` | sim | Referência verificável; ausência ⇒ `done` proibido. |
| `status` | sim | `done` \| `blocked` \| `partial` — **somente** estes. |
| `bloqueios/riscos` | se `blocked`/`partial` | Não vazio nesses estados. |
| `decisão pendente` | sim | Explícita quando houver aceite/decisão externa; `null`/"nenhuma" quando inexistente. |
| `próxima ação recomendada` | sim | Não vazia. |
| `classe_autonomia` | sim | `A` \| `B` \| `C`. |
| `lacunas` | sim | Lista explícita; `[LACUNA]` quando aplicável; nunca inferência silenciosa. |
| JSON machine-readable | sim | Bloco anexo contendo `decision_id`, `papel`, `classe_autonomia`, `decision_type`, `adr_ref`, `status`, `evidencia[]`, `lacunas[]`, `proximas_acoes[]`, `schema_version`. |

Regras R1–R7 (normativas, herdadas): `done` exige evidência (R3); `blocked`/`partial` exigem bloqueios + próxima ação (R4); `[LACUNA]` explícita (R6); reentrega = novo registro, dedupe no consumidor (R7); orquestrador re-delega 1× se o resumo for inválido.

Exemplo completo de resumo de subagente (bloco de exemplo, não executável):

```json
{
  "schema_name": "sdlc.subagent.summary",
  "schema_version": "1.0.0",
  "summary_id": "01K8Z3Q7M2N4P6R8T0V1W2X3C2",
  "envelope_id": "01K8Z3Q7M2N4P6R8T0V1W2X3Y4",
  "correlation_id": "01K8Z3Q7M2N4P6R8T0V1W2X3A0",
  "objetivo": "Criar docs/47 (roadmap) e docs/48 (contrato v1.0.0-PROPOSTA)",
  "acao_executada": "Leitura integral dos canônicos 00–45 e README; criação dos 2 documentos; nenhuma edição de outros arquivos",
  "resultado_artefato": ["docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md", "docs/48-contrato-canonico-v1-0-0-proposta-v0.md"],
  "evidencia": ["ls docs/ (2026-11-16): sem docs/46-*.md", "canônicos citados lidos integralmente"],
  "status": "done",
  "bloqueios_riscos": [],
  "decisao_pendente": "D-V0-05 (adoção do contrato v1.0.0; Classe C); validação do roadmap pelo Mantenedor",
  "proxima_acao_recomendada": "Mantenedor decide D-V0-05/D-V0-03/D-V0-04/D-V0-06; não iniciar F-ÚNICO-1",
  "classe_autonomia": "B",
  "lacunas": ["D-V0-01 adiada (DEC-006(i))", "D-V0-03/04/05/06 pendentes", "critério operacional de completed no tracking alvo"],
  "machine_readable": {
    "decision_id": "01K8Z3Q7M2N4P6R8T0V1W2X3D3",
    "papel": "tech-lead",
    "classe_autonomia": "B",
    "decision_type": "arquitetura",
    "adr_ref": "none",
    "status": "condicional",
    "evidencia": ["docs/00 §5", "docs/41-45", "docs/42 linha exit_code 6"],
    "premissas_validadas": ["done != completed != approved", "approved somente via humano"],
    "lacunas": ["D-V0-01 adiada (DEC-006(i))", "D-V0-05/D-V0-06 pendentes", "completed operacional indefinido no tracking alvo"],
    "proximas_acoes": [{"acao": "Submeter contrato à decisão D-V0-05", "dono": "TL (proposta) / Mantenedor (decisão)"}],
    "schema_version": "1.0"
  }
}
```

> Nota de compatibilidade: `machine_readable.schema_version` permanece `"1.0"` (formato do normativo de resumo vigente); `schema_version` do **contrato** é `"1.0.0"` (semver). A unificação dos dois em um único campo semver é decisão de D-V0-05, não desta proposta.

### (iii) Semântica de estados — execução ≠ operação ≠ valor

Três camadas, donos distintos, **nenhuma transição automática entre camadas**:

| Camada | Estados | Dono | Regra central |
|---|---|---|---|
| **Execução** (subagente) | `recebendo → analisando → decidindo → emitindo → (aguardando_aprovacao \| bloqueado \| concluido)`; no resumo: **`done` \| `blocked` \| `partial`** | agente/orquestrador | `done` exige evidência. Nunca implica `completed` nem `approved`. |
| **Operação** (OPS/board) | **`completed`** | OPS/sistema | Conclui o item no sistema operacional. Exige rastreio a resumo(s)/evidência(s). **NÃO implica `approved`.** |
| **Valor** (negócio) | **`pending` \| `approved` \| `rejected`** | **PO** | `approved` terminal; exige `evidence`, `decided_by=PO`, `decided_at`. Agente **nunca** escreve `approved`. |

```
EXECUÇÃO (agente/subagente)        OPERAÇÃO (OPS)                VALOR (PO)
─────────────────────────────      ──────────────────           ──────────────────────────
recebendo → analisando
   → decidindo → emitindo
      ├── done ──────────────────┐
      ├── blocked ──► (escala humana)
      └── partial ───► (lacunas)
                       │
                       ▼
              completed (OPS, se aplicável)
                       │  (habilita avaliação; NÃO decide valor)
                       ▼
                     pending ──────► approved   (terminal; PO + evidence + decided_at)
                       ▲              │
                       │              ▼
                       └── rejected ──┘   (rejected → pending SOMENTE com nova evidência)

Regras: done ⇏ completed ⇏ approved. Nenhuma seta é automática.
Classe C: NUNCA transita para approved sem aprovação humana explícita registrada.
Rejeitado → pending somente com nova evidência (docs/10 §3.3).
```

### (iv) Mapeamento execução → operação → valor + critério operacional proposto de `completed`

| De (camada) | Para (camada) | Condição/guarda | Efeito |
|---|---|---|---|
| `done` (execução) | `completed` (OPS) | Item executado + **evidência** + gates aplicáveis atendidos + registro de conclusão no sistema operacional | Unidade concluída no board; **valor permanece pendente** |
| `done` (execução) | `pending` (valor) | Evidência + critérios Given/When/Then anexados; orquestrador marca "valor pendente de aceite do PO" | Aguardando decisão do PO |
| `completed` (OPS) | `pending` (valor) | Rastreio item↔resumo↔evidência disponível | Habilita avaliação; não decide |
| `pending` (valor) | `approved` (valor) | **PO** decide com `evidence` + `decided_by` + `decided_at` | Terminal; valor entregue/aceito |
| `pending` (valor) | `rejected` (valor) | PO decide com `rationale` + `decided_by` + `decided_at` | Bloqueia aceite até nova evidência |
| `rejected` (valor) | `pending` (valor) | **Nova** evidência submetida | Reavaliação |

**Critério operacional proposto de `completed` (OPS):** *"completed = item executado (resumo `done` com evidência) + gates aplicáveis da fase atendidos + registro de conclusão no sistema operacional de tracking, com rastreio explícito ao(s) resumo(s)/evidência(s)."* **NÃO implica `approved`.** `[LACUNA]` O critério **exato** no sistema de tracking alvo (hoje: `docs/` como trilha de tracking — DEC-006(vi); sem board/tool — DEC-006/D-V0-02) depende do contexto operacional; esta proposta fixa a semântica, não a ferramenta. Divergência com `docs/10` §3.2 (`[LACUNA]` original) e `docs/20` §5 (estados `todo→ready→in_progress→done→accepted/rejected`) é registrada no mapa de divergências de `docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` (DIV-1/DIV-4) e aguarda D-V0-05.

Invariantes canônicos: `done` ⇏ `completed` ⇏ `approved`; evidência obrigatória para `done` e `approved`; lacunas sempre explícitas; estados terminais de execução não retrocedem (retrabalho = nova execução/run); `approved` só com humano identificável + evidência. Nota: **tracking = `docs/` é a trilha** (DEC-006(vi), sem board/issue tracker); critério exato segue `[LACUNA]` — esta proposta fixa a semântica, não a ferramenta.

### (v) Exit codes unificados (referência: `docs/42` §2, com a linha 6)

| `exit_code` | Origem (gate) | `error_class` | Efeito (resumo) |
|---|---|---|---|
| `0` | qualquer | — | Portão verde; `tasks[].status` avança. |
| `1` | `lint-ads` (design/arch) | `logica` | `ads[]`/`tasks[]` → `blocked`; retorno ao nó de origem. |
| `2` | `test-unit` | `logica` (ou `flaky`) | Retorno forçado a `coding`; `attempts += 1`. |
| `3` | `test-integration` | `logica`/`ambiente` | `integration_test_output="failure"`; `pr_ready=false`; retorno a `coding`. |
| `4` | qualquer (ferramenta/ambiente quebrado) | `ambiente` | `tasks[].blocked`; escala; **sem retry cego**. |
| `5` | `lint-ads` (contrato/schema) | `logica` | ADS inválido nunca avança; retorno a `design`. |
| `6` | `pr_generation` (gate de cobertura; `pyproject.toml` inexistente no alvo) | `lacuna` | `pr_ready=false`; **fail-closed**; retorno a `coding`/`tdd` ou decisão D-V0-06; **nunca** avançar PR. |
| `10` | `lint-ads` (`ADS_KIND=architecture`, inconsistência técnica) | `lacuna` | Avanço para Coding **bloqueado**; retorno a `architecture`. |
| `130` | qualquer (SIGINT/watchdog/1 crítico) | `critico` | Parada total + escala humana. |
| `>=64` | não mapeado | `lacuna` | Tratar como `[LACUNA]`; **nunca** inferir sucesso. |

Fonte canônica: `docs/42-mapeamento-gates-makefile-v0.md` §2 — incluindo a **linha `exit_code 6`** (gate de cobertura em `pr_generation`, fail-closed, adicionada em 2026-11-16 após revisão do PM para fechar a inconsistência t2×t5). Regra dos 3 strikes: `attempts >= 3` na mesma validação ⇒ `blocked` + escala humana (exceto `critico`: parada na 1ª).

### (vi) Regra de migração `0.1.0-draft` → `1.0.0`

1. **Aditiva e compatível:** `1.0.0` preserva todos os campos de `0.1.0-draft` com mesma semântica (`global_context`, `ads`, `tasks`, `errors`, `approvals[]`, `integration_test_output`, `pr_ready`). Nenhum campo é removido ou re-tipado.
2. **Sem campos obrigatórios novos sem major bump:** qualquer campo novo obrigatório (ou mudança de semântica de campo existente) exige **major** (`2.0.0`) + plano de migração. Minor (`1.1.0`) = aditivo opcional; patch (`1.0.1`) = editorial/correção semântica sem quebra.
3. **Forward-compat na borda:** consumidores validam `schema_version` declarada; campos desconhecidos são ignorados (não rejeitados) em minor/patch; rejeição só em major distinta.
4. **Validação na borda:** envelope/resumo/AgentState validados contra schema no dispatch e na ingestão; inválido ⇒ delegação rejeitada + 1 re-delegação automática (orquestrador).
5. **Idempotência preservada:** `idempotency_key` inclui `schema_version`; reentrega sob `1.0.0` não colide com dedupe de `0.1.0-draft`; histórico mantido (reentrega = novo registro, dedupe no consumidor — R7).
6. **Registry:** versões publicadas imutáveis; depreciação registrada; `0.1.0-draft` marcado `deprecated` **somente após** adoção de `1.0.0` (decisão D-V0-05), nunca antes.
7. **AgentState:** `sdlc.agentstate` migra com os mesmos passos; `docs/41` permanece como referência de design até D-V0-05/06; este contrato não edita o canônico 41.

### (vii) Versionamento semântico de contratos (`schema_version`)

- Formato: **semver** `MAJOR.MINOR.PATCH` aplicado a contratos/schemas (`sdlc.task.delegation`, `sdlc.subagent.summary`, `sdlc.agentstate`).
- **MAJOR:** remoção/renomeação de campo obrigatório, mudança de tipo ou de semântica, nova obrigação sem default ⇒ quebra; exige migração explícita e decisão (Classe C para adoção).
- **MINOR:** adição de campo **opcional** ou novo schema companheiro; retrocompatível.
- **PATCH:** correção editorial/descrição/exemplos; sem mudança semântica.
- `schema_version` é **imutável por versão publicada**; validação sempre contra a versão declarada no envelope/resumo.
- **Compatibilidade aditiva é a política default** (compatível com `docs/30` §Contratos e ADR-D proposto).
- Registry de contratos (D-V0-05) é **[LACUNA]**: ferramenta indefinida; este repo documental não hospeda registry executável.

### Relação com `AgentState` (`docs/41`)

Este contrato não redefine o `AgentState`: referencia-o como schema companheiro `sdlc.agentstate`, atualmente `0.1.0-draft`. A migração §(vi) aplica-se a ele sem edição do canônico 41. Invariante mantida: **nenhum campo `approved` escrevível por agente**; `approvals[].status=approved` somente via nó humano (ver `docs/45`) com `human_interaction_ref` + `evidence_refs` não vazio.

## Evidências

- `docs/00-painel-gerencial-consolidado.md` §4 (ponto a reconciliar: contrato/envelope — "definir contrato canônico v1.0.0 único"), §5 (D-V0-05), §8.1 (`schema_version 0.1.0-draft` × v1.0.0 registrado como divergência; exit_code 6 corrigido no 42) — lido 2026-11-16.
- `docs/30-arquitetura-tech-lead-baseline-v0.md` §Contratos/Estados (envelope proposto; mapeamento de estados; idempotência; compatibilidade aditiva; ADR-D) — lido 2026-11-16.
- `docs/41-agentstate-esquema-v0.md` (campos do estado; invariantes §4; `0.1.0-draft`) e `docs/45-grafo-langgraph-classe-c-v0.md` (`human_review` único escritor de `approved`) — lidos 2026-11-16.
- `docs/42-mapeamento-gates-makefile-v0.md` §2 — tabela `exit_code → AgentState` **incluindo a linha `exit_code 6`** (cobertura em `pr_generation`, fail-closed; adicionada 2026-11-16) — lido 2026-11-16.
- `docs/10-produto-po-visao-mvp-baseline-v0.md` §3 (semântica canônica de estados; invariantes §3.4) e `docs/20-governanca-pm-plano-baseline-v0.md` §5 (estados `todo→ready→…→done→accepted/rejected`; DoD processual) — lidos 2026-11-16.
- Normativos vivos referenciados por caminho+sha256 (DEC-003; nunca copiados): `~/.opencode/references/contrato-resumo-subagentes.md` — sha256 completo `163e0aad7654d0a60930e90388afa9b9474ee727f119e94a62337d8321442a60` (prefixo `163e0aad…` confere com DEC-003; sem divergência) e `~/.opencode/references/autonomia-e-estados.md` — sha256 completo `776af494ee702cf4d3db8837f2b1c0c23450844f9b54e376a052d7adbc42c78a` (prefixo `776af494…` confere com DEC-003; sem divergência). Pin exato executado nesta reconciliação (Classe B, reversível), conforme DEC-003 (que registrava apenas prefixos como `[PREMISSA]`).
- `docs/DECISIONS.md` (log canônico; DEC-001…DEC-008) e `docs/46-ata-kickoff-d-v0-01-02-v0.md` (ata do kickoff D-V0-01/02) — **criados por sessão paralela em 2026-11-16** e lidos nesta sessão após a criação inicial deste documento; DEC-003 (inclusão condicional 41–45), DEC-005 (`docs/evidence/` rejeitado), DEC-006 (6 decisões Classe C), DEC-008 (reconciliação via `docs/47`; publicação bloqueada por D-V0-03/04/05/06) são referência direta para as decisões pendentes citadas aqui.

## ⚠️ Premissas e Lacunas

- **[LACUNA] D-V0-05 pendente (CR-007-C no log):** adoção do contrato v1.0.0 é decisão **Classe C** do Mantenedor (TL+PO+PM propõem). Nada neste documento tem efeito normativo até lá; `0.1.0-draft` continua sendo a versão dos canônicos de design. DEC-008: publicação do baseline bloqueada até D-V0-03/04/05/06.
- **[LACUNA] D-V0-01 adiada (DEC-006(i)):** sem stack/CI/repo-alvo, não há registry executável, validador nem borda de validação — a proposta §(vi)/(vii) é documental.
- **[LACUNA] D-V0-06 pendente (CR-008-C no log):** política única de gates/thresholds (incluindo leitura de `pyproject.toml`; unificação G0–G3 × exit_code → AgentState) indefinida; exit code 6 permanece fail-closed sem threshold.
- **[LACUNA] Critério exato de `completed` no sistema de tracking alvo:** tracking = `docs/` (DEC-006(vi); sem board/tool); a semântica está fixada, a ferramenta não.
- **[LACUNA] Unificação `machine_readable.schema_version` ("1.0") × `schema_version` de contrato ("1.0.0"):** decisão de D-V0-05.
- **[LACUNA] Convenção/numeração de ADRs (D-V0-04 / CR-006 no log):** `adr_ref="none"`; nenhum ADR numerado por este documento.
- **[LACUNA] Sincronia inicial:** na 1ª redação deste documento, `docs/46` e `docs/DECISIONS.md` constavam como inexistentes; foram criados por sessão paralela em 2026-11-16 e este documento foi corrigido para citá-los. Se o log indicar divergência com este contrato, **o log prevalece** e a divergência deve ser registrada no mapa (`docs/47` DIV-*).
- **[PREMISSA]** Compatibilidade aditiva (minor) como default; quebra só em major com decisão.
- **[PREMISSA]** `approved` permanece exclusivo de humano em qualquer versão deste contrato.
- **[PREMISSA]** `docs/evidence/` rejeitado pelo Mantenedor ⇒ evidências são referências (caminho/URI/hash) nos canônicos, nunca store paralelo.
- **Consistência (2026-11-16):** hashes completos dos normativos externos pinados em `docs/30` e `docs/48` (seção Evidências) são idênticos; prefixos conferem com DEC-003 (`163e0aad…`, `776af494…`); **nenhuma divergência detectada**. Divergência futura nos arquivos vivos invalida a referência até re-registro (DEC-003). Mapa de divergências DIV-1…DIV-6 em `docs/47` atualizado em 2026-11-16 (ver abaixo).

## ✅ Próximas Ações

1. **Submeter este contrato à decisão D-V0-05 (Classe C; CR-007-C no log)** — Dono: TL (proposta) / Mantenedor + PO + PM (decisão) — Prazo: sob demanda.
2. **Se adotado:** publicar schemas `sdlc.task.delegation@1.0.0`, `sdlc.subagent.summary@1.0.0`, `sdlc.agentstate@1.0.0` no registry decidido e marcar `0.1.0-draft` como `deprecated`; registrar DEC-009+ em `docs/DECISIONS.md` — Dono: TL — Prazo: F-ÚNICO-0/MU-0.2 (após decisão e DEC-008 publicado).
3. **Reconciliar `docs/41`/`docs/45` para `1.0.0`** (edição autorizada dos canônicos de design) — Dono: TL — Prazo: F-ÚNICO-0, após D-V0-05.
4. **Fixar critério operacional de `completed` no tracking alvo** (quando existir) — Dono: PM + TL — Prazo: D-V0-02 resolvida.
5. **Atualizar `docs/README.md`** com 47/48 no próximo change set autorizado (não tocado nesta entrega) — Dono: Orchestrator/Mantenedor — Prazo: próximo change set.

## Resumo do Subagente

- objetivo: Criar `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` — proposta do Contrato Canônico v1.0.0 (envelope + resumo + estados + migração + semver), condicional, sem efeito normativo.
- ação executada: Leitura integral dos canônicos 00/10/20/30/40/41/42/45 e README; **verificação concorrente**: `docs/46-ata-kickoff-d-v0-01-02-v0.md` e `docs/DECISIONS.md` (DEC-001…DEC-008) criados por sessão paralela em 2026-11-16 — documento corrigido para citá-los (o log prevalece em divergência); redação das seções (i)–(vii); dois blocos de exemplo completos (envelope e resumo); diagrama ascii de transições; critério operacional proposto de `completed`; exit codes unificados com a linha 6 do `docs/42`; regra de migração aditiva; avisos de que adoção = Classe C (D-V0-05/CR-007-C) e nenhum campo `approved` escrevível por agente.
- resultado/artefato: `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (este documento), status `condicional`, classe B, `adr_ref="none"`.
- evidência: Canônicos lidos em 2026-11-16; `docs/DECISIONS.md` e `docs/46` lidos após criação concorrente no mesmo dia; linha `exit_code 6` verificada em `docs/42` §2.
- status: done
- bloqueios/riscos: Adoção bloqueada por D-V0-05/CR-007-C (e D-V0-01/DEC-006(i) para tooling); publicação do baseline bloqueada por DEC-008; sem efeito normativo até decisão; risco de interpretação como baseline mitigado por avisos explícitos e pela prevalência do log em divergência.
- decisão pendente: D-V0-05 (adoção do contrato v1.0.0; Classe C); D-V0-06 (política de gates); aceite PO (D-V0-03) para efeito de valor.
- próxima ação recomendada: Mantenedor decide D-V0-05; somente após adoção, reconciliar 41–45 para 1.0.0.
