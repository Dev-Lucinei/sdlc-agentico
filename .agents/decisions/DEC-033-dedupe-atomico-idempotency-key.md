---
title: "DEC-033 — Dedupe atômico por idempotency_key na persistência (LAC-IDEMP-01; Classe C)"
date: "2026-11-18"
project: "sdlc-agentico"
source: "Mantenedor Lucinei (sessão OpenCode 2026-11-18, pergunta interativa)"
status: "vigente"
classe: "C"
decided_by: "Lucinei (Mantenedor)"
human_interaction_ref: "sessão OpenCode 2026-11-18 (pergunta interativa — LAC-IDEMP-01..05 → Opção A: dedupe atômico via UNIQUE index em idempotency_key)"
---

## DEC-033 — Dedupe atômico por idempotency_key na persistência (LAC-IDEMP-01; Classe C)

- **Data:** 2026-11-18
- **Classe:** C
- **Decisão:** adoção de **dedupe atômico na camada de persistência** para eventos **com** `idempotency_key`. O Mantenedor (Lucinei, PO) decidiu explicitamente em sessão OpenCode 2026-11-18 (pergunta interativa): **LAC-IDEMP-01..05 → Opção A: dedupe atômico (UNIQUE index em `idempotency_key`)**.

### a) Contexto

Fatos técnicos verificados em 2026-11-18 (F2.2/F2.4-téc, DEC-032):

- **LAC-IDEMP-01:** não há dedupe atômico na persistência. `events` é append-only com chain hash, mas `idempotency_key` **não tem** UNIQUE constraint; `insert_event` faz **read-then-insert** (lê o último hash → INSERT) **sem transação/lock**. Consequências verificadas: (i) duas conexões inserindo a mesma chave persistem 2 registros (race determinística — não depende de timing, não existe constraint que a barre); (ii) sob interleaving, dois writers podem encadear sobre o mesmo predecessor, **quebrando `verify_chain()`**.
- **LAC-IDEMP-02:** `tasks` NÃO possui coluna `idempotency_key` — task reentregue não é correlacionável/deduplicável via API. **Fora do escopo desta decisão** (ver seção e).
- **LAC-IDEMP-03:** `list_events(idempotency_key=None)` NÃO filtra por NULL (omite a cláusula); não há como listar apenas eventos sem chave.
- **LAC-IDEMP-04:** via `transition_task`, a `idempotency_key` deriva do `event_id` (`transition:{task_id}:{eid}`); como o `event_id` é aleatório por padrão, a reentrega só é correlacionável se o chamador fixar `event_id`. Reentrega com mesmo `event_id` colapsa na PK `event_id` e a exceção é **ENGOLIDA** (`except Exception: pass` em `src/state.py`, linha ~208) — persistência best-effort silenciosa; falha de INSERT não é sinalizada ao chamador.
- **LAC-IDEMP-05:** dedupe por `idempotency_key` na persistência NÃO existe (por desenho R7/ADR-003); nenhum helper de dedupe existe em `src/` — o consumidor usa `list_events` manualmente.

**Vigente até esta decisão:** ADR-003 (`accepted`, DEC-020) e R7 do Contrato Canônico v1.0.0 (D-V0-05, DEC-021) fixam "reentrega gera novo registro + dedupe no consumidor". O teste `test_reentrega_gera_novo_registro` (`tests/test_persistence.py`) codifica essa semântica. A decisão do Mantenedor **altera essa semântica para eventos com `idempotency_key`** — ver seções b–d.

### b) Decisão (Classe C)

Adotar **dedupe ATÔMICO na persistência** para eventos **COM** `idempotency_key`:

1. **Índice UNIQUE parcial** em `events(idempotency_key)` com cláusula **`WHERE idempotency_key IS NOT NULL`** (eventos sem chave permanecem sem restrição de unicidade).
2. **`insert_event` passa a usar `INSERT ... ON CONFLICT DO NOTHING`** (ou equivalente transacional), de modo atômico.
3. **Contrato de retorno (definido aqui, normativo):** `insert_event(...)` retorna objeto ou tupla contendo **`event_id`** e **`deduplicated: bool`**. Quando `deduplicated=True`:
   - **NÃO** se insere novo registro;
   - **NÃO** se quebra a cadeia (chain hash preservado);
   - **NÃO** se levanta exceção para o chamador — reentrega é idempotente (no-op deduplicado).
   
   O formato concreto (dataclass vs tupla nomeada vs outro) fica **a critério do implementador** na tarefa de implementação seguinte; o contrato `event_id` + `deduplicated: bool` é obrigatório e não negociável.
4. **Chain hash íntegro sob concorrência:** o read-then-insert deixa de existir como janela de corrida — o insert passa a ser transacional/atômico com o índice UNIQUE como arbitro.

### c) Semântica

- **Append-only PRESERVADO** para eventos **sem** `idempotency_key` (keyless permanecem append-only sem dedupe, como hoje).
- **Com key:** reentrega é **idempotente** — no-op deduplicado, sem exceção para o chamador; o registro original permanece; o chain hash não é afetado.
- **Exceções de INSERT NÃO podem mais ser engolidas silenciosamente:** `transition_task` deve **propagar ou logar** (F2.3-téc já loga via observabilidade JSON/`correlation_id`); a escolha entre propagar e logar-envolver fica **a critério do implementador**, considerando o melhor design — mas o silêncio (`except Exception: pass` sem sinalização) é proibido pela semântica desta decisão.
- **Exactly-once fim-a-fim continua NÃO adotado** (ADR-003, seção Alternativas) — o que muda é a fronteira de dedupe: sai da responsabilidade exclusiva do consumidor e passa a ser garantida também na persistência para eventos com chave.

### d) Ajustes normativos derivados (autorizados por esta decisão)

1. **`test_reentrega_gera_novo_registro`** (`tests/test_persistence.py`) **será AJUSTADO** para a nova semântica: reentrega com a mesma chave → **deduplicado** (`deduplicated=True`, sem novo registro). Ajuste de teste é ato de implementação (próxima delegação), autorizado aqui.
2. **Adenda a ADR-003** (`docs/adr/core/ADR-003-idempotencia-dedupe.md`): nova seção `## Adendo 2026-11-18 — DEC-033 (dedupe atômico)` **APPENDED ao final** (corpo `accepted` intacto); item "reentrega gera novo registro" para eventos com `idempotency_key` fica **SUPERSEDED** por DEC-033; o restante (append-only keyless, chain hash, dedupe no consumidor para fluxos sem key) permanece vigente.
3. **`docs/48-contrato-canonico-v1-0-0.md` mencionado como afetado — NÃO alterado nesta tarefa.** Registro apenas: R7 e as seções sobre reentrega (`§(i)` `idempotency_key`; `§(vi)` "Idempotência preservada/histórico mantido (reentrega = novo registro, dedupe no consumidor — R7)") ficam **funcionalmente superseded para eventos com key** até revisão humana futura do contrato (**D-V0-05/DEC-021 segue vigente** até essa revisão). Qualquer revisão do contrato = decisão Classe C futura.

### e) EXPLICITAMENTE NÃO autorizado por este DEC

- **`schema tasks.idempotency_key` (LAC-IDEMP-02)** — permanece lacuna pendente de **nova decisão Classe C**; não implementar.
- Alteração de **thresholds** (`fail_under=50`, DEC-018/DEC-022).
- Alteração de **R7 do contrato** (`docs/48`) nesta tarefa — ver (d)(3); R7 só muda por revisão humana futura do contrato.
- **Promoção de ADR novo:** a adenda a ADR-003 **não é** um ADR `accepted` novo; é adenda a ADR-003 `accepted` (DEC-020). Nenhum ADR é promovido por este DEC.
- **Limpeza de aliases de `persistence.py`** — fora de escopo.
- **LAC-IDEMP-03, LAC-IDEMP-04, LAC-IDEMP-05:** não são resolvidos por este DEC em sua totalidade. LAC-IDEMP-01 e o aspecto de persistência de LAC-IDEMP-05 (dedupe atômico) são cobertos pela seção (b); LAC-IDEMP-03 (`list_events` sem filtro NULL) e LAC-IDEMP-04 (derivação de key a partir de `event_id` + exceção engolida) permanecem como estão, **exceto** pelo contrato de propagação/log de exceções da seção (c), que é autorizado e obrigatório quando a implementação tocar `transition_task`. Decisão específica sobre LAC-IDEMP-03/04, se necessária, exige nova decisão ou a tarefa de implementação respeitando (b) e (c).

### f) Consequências

- **Readers tolerantes à ausência de novo registro em reentrega:** consumidores não podem mais assumir 1 registro por chamada de `insert_event` com a mesma chave; devem inspecionar `deduplicated` quando relevante.
- **Testes ajustados:** `test_reentrega_gera_novo_registro` e testes e2e de reentrega concorrente (`tests/test_idempotency_e2e.py`) serão ajustados na tarefa de implementação para a nova semântica (reentrega same-key → deduplicado); LAC-IDEMP-02 permanece documentado como lacuna.
- **Cobertura preservada:** ≥ `fail_under` lido do `pyproject.toml` (50; DEC-018/DEC-022); gates `make lint` / `make typecheck` / `make test` / `make audit` / `make audit-g2` com **exit 0** exigidos na tarefa de implementação.
- **Painel/README/JSON propagados** neste change set (sem promoção de status; execuções permanecem `done`).
- **Riscos:** divergência temporária entre contrato v1.0.0 (R7, vigente até revisão humana) e comportamento implementado; mitigada pelo registro explícito em (d)(3) e pela adenda a ADR-003. Reentrega com chave derivada de `event_id` aleatório (LAC-IDEMP-04) continua não correlacionável sem chamador fixar `event_id` — lacuna conhecida, não resolvida aqui.

- **Decisão tomada em:** sessão OpenCode 2026-11-18 pelo Mantenedor (resposta interativa — Opção A: Dedupe atômico / UNIQUE index em `idempotency_key`).
- **Autorização:** implementação na próxima delegação (não incluída nesta tarefa; `src/` NÃO tocado aqui).
