"""Testes e2e de reentrega at-least-once e dedupe por idempotency_key (DEC-033).

Semântica vigente (DEC-033, 2026-11-18, Classe C — supersede R7/ADR-003 para eventos
COM idempotency_key):
- Event Log é append-only para eventos SEM idempotency_key (keyless: append livre).
- Eventos COM idempotency_key: dedupe ATÔMICO na persistência (UNIQUE parcial
  `ux_events_idempotency_key ... WHERE idempotency_key IS NOT NULL` +
  INSERT ... ON CONFLICT DO NOTHING, em transação BEGIN IMMEDIATE).
- Reentrega da mesma key = no-op deduplicado: InsertResult(event_id=<id original>,
  deduplicated=True); sem exceção; chain hash preservado; registro original permanece.
- Exactly-once fim-a-fim continua NÃO adotado (ADR-003) — a fronteira de dedupe
  passa a ser garantida também na persistência para eventos com chave.

LACUNAS remanescentes (não corrigidas aqui — ver DEC-033 §e):
- LAC-IDEMP-02: tasks NÃO possuem coluna idempotency_key — fora de escopo.
- LAC-IDEMP-03: list_events(idempotency_key=None) NÃO filtra por NULL (omite a cláusula).
- LAC-IDEMP-04: via transition_task a idempotency_key deriva do event_id
  ('transition:{task_id}:{eid}'); reentrega só é correlacionável se o chamador fixar
  event_id. Exceções de persistência NÃO são mais engolidas silenciosamente
  (log WARNING + métrica event_log_persist_failures; best-effort mantido, DEC-033 §c).
"""

from __future__ import annotations

import threading
from pathlib import Path

from src.persistence import create_persistence_db, create_test_db
from src.state import new_state, transition_task


def _consumer_dedupe(events: list[dict]) -> list[dict]:
    """Dedupe no consumidor (defesa em profundidade): mantém a 1ª ocorrência por key."""
    seen: set[str] = set()
    unique: list[dict] = []
    for ev in events:
        key = ev["idempotency_key"]
        if key is not None and key in seen:
            continue
        if key is not None:
            seen.add(key)
        unique.append(ev)
    return unique


# --------------------------------------------------------------- (a) eventos
def test_reentrega_mesmo_evento_mesma_key_deduplica_atomicamente() -> None:
    db = create_test_db()
    try:
        e1 = db.insert_event("task.dispatched", {"task_id": "t-1"}, idempotency_key="key-a")
        e2 = db.insert_event("task.dispatched", {"task_id": "t-1"}, idempotency_key="key-a")
        # DEC-033: persistência deduplica — um único registro append-only.
        assert e1.deduplicated is False
        assert e2.deduplicated is True
        assert e2.event_id == e1.event_id
        rows = db.list_events(idempotency_key="key-a")
        assert len(rows) == 1
        assert db.get_event(e1.event_id) is not None
        assert db.verify_chain().ok is True
    finally:
        db.close()


# ---------------------------------------------------------------- (c) chaves distintas
def test_chaves_diferentes_ambos_persistem() -> None:
    db = create_test_db()
    try:
        db.insert_event("e", {"n": 1}, idempotency_key="key-1")
        db.insert_event("e", {"n": 2}, idempotency_key="key-2")
        assert len(db.list_events(idempotency_key="key-1")) == 1
        assert len(db.list_events(idempotency_key="key-2")) == 1
        assert db.verify_chain().ok is True
    finally:
        db.close()


# ---------------------------------------------------------------- (b) tasks
def test_tasks_nao_possuem_idempotency_key__lacuna_documentada() -> None:
    """LAC-IDEMP-02: schema de tasks não tem idempotency_key; reentrega de task
    não é correlacionável via API de persistência. Teste documenta a lacuna vigente."""
    db = create_test_db()
    try:
        cols = {row["name"] for row in db.connection.execute("PRAGMA table_info(tasks)")}
        assert "idempotency_key" not in cols
        tid1 = db.insert_task(title="reentrega", status="todo", input_data={"x": 1})
        tid2 = db.insert_task(title="reentrega", status="todo", input_data={"x": 1})
        assert tid1 != tid2  # sem dedupe: dois registros independentes
        assert len(db.list_tasks()) == 2
    finally:
        db.close()


# ------------------------------------------------------------- (d) ponta a ponta
def test_fluxo_dispatch_persist_dedupe_ponta_a_ponta() -> None:
    """Caminho real existente: transition_task (máquina de estados pura) → persist=True
    → insert_event('state.transition').

    Semântica DEC-033: a idempotency_key deriva do event_id
    ('transition:{task_id}:{eid}'). Reexecutar com o mesmo event_id ⇒ mesma key ⇒
    INSERT ... ON CONFLICT DO NOTHING ⇒ no-op deduplicado (sem exceção, sem novo
    registro, chain íntegra) — dedupe atômico na persistência, não mais colapso
    silencioso de PK. Chaves distintas (event_id novo) ⇒ novo registro."""
    db = create_test_db()
    try:
        state = new_state(request_id="req-e2e", task_id="task-e2e", autonomy_class="A")
        state["tasks"].append({"task_id": "task-e2e", "status": "todo"})

        def dispatch_once() -> str:
            return transition_task(
                "task-e2e", "todo", "in_progress",
                "evt-e2e-fixed", "evidence-e2e",
                state=state, db=db, persist=True, event_id="evt-e2e-fixed",
            )

        dispatch_once()
        events_after_first = db.list_events(idempotency_key="transition:task-e2e:evt-e2e-fixed")
        assert len(events_after_first) == 1

        # Reentrega at-least-once (mesmo event_id): no-op deduplicado (DEC-033).
        dispatch_once()
        dispatch_once()

        events = db.list_events(idempotency_key="transition:task-e2e:evt-e2e-fixed")
        assert len(events) == 1  # DEC-033: dedupe atômico por idempotency_key
        assert db.verify_chain().ok is True
        assert db.verify_chain().eventos_verificados == 1
        assert len(_consumer_dedupe(events)) == 1

        # event_id distinto ⇒ nova key derivada ⇒ novo registro (sem colisão de key).
        transition_task(
            "task-e2e", "in_progress", "done",
            "evt-e2e-segundo", "evidence-e2e-2",
            state=state, db=db, persist=True, event_id="evt-e2e-segundo",
        )
        assert len(db.list_events()) == 2
        assert db.verify_chain().ok is True
    finally:
        db.close()


def test_reexecucao_do_grafo_nao_persiste_nada_por_conta_propria() -> None:
    """run_graph (simulação local) NÃO persiste eventos — o caminho de persistência
    real é transition_task(..., db=...). Documenta o limite do fluxo atual."""
    from src.graph import run_graph

    db = create_test_db()
    try:
        state = new_state(request_id="req-graph", task_id="task-graph", autonomy_class="A")
        state["tasks"].append({"task_id": "task-graph", "status": "todo"})
        run_graph(state, autonomy_class="A", exit_code=0, task_id="task-graph")
        assert db.list_events() == []  # nenhum evento persistido pelo grafo
        assert db.verify_chain().ok is True
    finally:
        db.close()


# ------------------------------------------------------- (e) key ausente/None
def test_idempotency_key_none_e_aceita_sem_dedupe__lacuna_documentada() -> None:
    """LAC-IDEMP-03: insert_event aceita idempotency_key=None (coluna nullable).
    Keyless permanece append-only SEM dedupe; e list_events(idempotency_key=None)
    NÃO filtra eventos-sem-chave (omite a cláusula WHERE). Comportamento vigente."""
    db = create_test_db()
    try:
        e1 = db.insert_event("e", {"n": 1})
        e2 = db.insert_event("e", {"n": 2}, idempotency_key=None)
        assert e1.event_id != e2.event_id
        assert e1.deduplicated is False and e2.deduplicated is False
        # Ambos persistem; list_events sem argumento retorna TODOS (não filtra NULL).
        all_events = db.list_events()
        assert len(all_events) == 2
        assert {ev["idempotency_key"] for ev in all_events} == {None}
        # Não há como consultar apenas eventos com chave nula via API pública.
    finally:
        db.close()


def test_keyless_appends_nao_sao_afetados_pelo_dedupe() -> None:
    """DEC-033 §c: eventos sem idempotency_key permanecem append-only livre —
    2 appends sem key → 2 eventos, mesmo com payload idêntico."""
    db = create_test_db()
    try:
        e1 = db.insert_event("e", {"n": 1})
        e2 = db.insert_event("e", {"n": 1})
        assert e1.event_id != e2.event_id
        assert e1.deduplicated is False and e2.deduplicated is False
        assert len(db.list_events()) == 2
        assert db.verify_chain().ok is True
    finally:
        db.close()


# --------------------------------------------- (f) concorrência leve de reentrega
def test_reentrega_concorrente_mesma_chave_duas_conexoes_deduplica(
    tmp_path: Path,
) -> None:
    """DEC-033: duas conexões (dois 'workers' at-least-once) inserindo a mesma
    idempotency_key persistem NO MÁXIMO 1 registro — o índice UNIQUE parcial +
    ON CONFLICT DO NOTHING barram a corrida de forma determinística."""
    db_path = tmp_path / "race.db"
    seed = create_persistence_db(db_path)
    seed.close()  # cria o schema

    barrier = threading.Barrier(2)
    errors: list[BaseException] = []

    def worker() -> None:
        try:
            local = create_persistence_db(db_path)
            try:
                barrier.wait(timeout=5.0)
                local.insert_event("task.dispatched", {"task_id": "t-race"},
                                   idempotency_key="key-race")
            finally:
                local.close()
        except BaseException as exc:  # noqa: BLE001 — repassado à thread principal
            errors.append(exc)

    t1, t2 = threading.Thread(target=worker), threading.Thread(target=worker)
    t1.start()
    t2.start()
    t1.join(timeout=10.0)
    t2.join(timeout=10.0)
    assert not errors, f"falha inesperada nas threads: {errors!r}"

    check = create_persistence_db(db_path)
    try:
        rows = check.list_events(idempotency_key="key-race")
        # DEC-033: dedupe atômico — exatamente 1 registro.
        assert len(rows) == 1
        result = check.verify_chain()
        assert result.ok is True
        assert result.eventos_verificados == 1
    finally:
        check.close()


def test_reentrega_concorrente_chaves_distintas_chain_integra(tmp_path: Path) -> None:
    """DEC-033: insert_event roda em transação BEGIN IMMEDIATE — dois writers
    concorrentes com chaves distintas não encadeiam sobre o mesmo predecessor;
    verify_chain() permanece íntegra."""
    db_path = tmp_path / "chain-race.db"
    seed = create_persistence_db(db_path)
    seed.close()

    barrier = threading.Barrier(2)
    errors: list[BaseException] = []

    def worker(n: int) -> None:
        try:
            local = create_persistence_db(db_path)
            try:
                barrier.wait(timeout=5.0)
                local.insert_event("e", {"worker": n}, idempotency_key=f"key-c-{n}")
            finally:
                local.close()
        except BaseException as exc:  # noqa: BLE001
            errors.append(exc)

    t1 = threading.Thread(target=worker, args=(1,))
    t2 = threading.Thread(target=worker, args=(2,))
    t1.start()
    t2.start()
    t1.join(timeout=10.0)
    t2.join(timeout=10.0)
    assert not errors, f"falha inesperada nas threads: {errors!r}"

    check = create_persistence_db(db_path)
    try:
        result = check.verify_chain()
        assert result.ok is True
        assert result.eventos_verificados == 2
    finally:
        check.close()
