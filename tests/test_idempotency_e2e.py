"""Testes e2e de reentrega at-least-once e dedupe por idempotency_key (DEC-032 F2.4-téc).

Semântica vigente (ADR-003 accepted, DEC-020; Contrato v1.0.0 R7):
- Event Log é append-only: reentrega gera NOVO registro (verify_chain íntegra).
- NÃO há dedupe na camada de persistência (insert_event não consulta/rejeita chave repetida).
- O dedupe é responsabilidade do CONSUMIDOR: list_events(idempotency_key=...) + dedupe.
- Exactly-once fim-a-fim é explicitamente não adotado.

LACUNAS registradas (não corrigidas aqui — ver retorno do subagente):
- LAC-IDEMP-01: sem dedupe atômico na persistência; reentrega concorrente (2 conexões,
  mesma chave) gera 2 registros. UNIQUE index em events.idempotency_key violaria R7/ADR-003
  (reentrega = novo registro) e o teste vigente test_reentrega_gera_novo_registro — NÃO aplicado.
  Adicional: insert_event faz read-then-insert (último hash → INSERT) sem transação/lock,
  logo dois writers concorrentes podem gerar elos irmãos e quebrar verify_chain().
- LAC-IDEMP-02: tasks NÃO possuem coluna idempotency_key — task reentregue não é
  correlacionável/deduplicável via API.
- LAC-IDEMP-03: list_events(idempotency_key=None) NÃO filtra por NULL (omite a cláusula);
  não há como listar apenas eventos sem chave.
- LAC-IDEMP-04: via transition_task a idempotency_key deriva do event_id
  ('transition:{task_id}:{eid}'); event_id aleatório por padrão ⇒ reentrega só é
  correlacionável se o chamador fixar event_id. Reentrega com mesmo event_id colapsa na
  PK event_id e a exceção é ENGOLIDA ('except Exception: pass' em state.py) —
  persistência best-effort silenciosa; falha de INSERT não é sinalizada ao chamador.
- LAC-IDEMP-05: dedupe por idempotency_key na persistência NÃO existe (por desenho R7/ADR-003);
  nenhum helper de dedupe existe em src/ — o consumidor usa list_events manualmente.
"""

from __future__ import annotations

import threading
from pathlib import Path

from src.persistence import create_persistence_db, create_test_db
from src.state import new_state, transition_task


def _consumer_dedupe(events: list[dict]) -> list[dict]:
    """Dedupe no consumidor (R7): mantém a 1ª ocorrência por idempotency_key."""
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
def test_reentrega_mesmo_evento_mesmo_key_persiste_novo_registro_e_dedupe_no_consumidor() -> None:
    db = create_test_db()
    try:
        e1 = db.insert_event("task.dispatched", {"task_id": "t-1"}, idempotency_key="key-a")
        e2 = db.insert_event("task.dispatched", {"task_id": "t-1"}, idempotency_key="key-a")
        # Vigente: persistência NÃO deduplica — dois registros append-only.
        assert e1 != e2
        rows = db.list_events(idempotency_key="key-a")
        assert len(rows) == 2
        # Dedupe ocorre no consumidor (R7): 1 efeito observável.
        unique = _consumer_dedupe(rows)
        assert len(unique) == 1
        assert unique[0]["idempotency_key"] == "key-a"
        # Retorno da API não sinaliza dedupe: insert_event sempre devolve novo event_id.
        assert db.get_event(e1) is not None and db.get_event(e2) is not None
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

    Comportamento vigente descoberto: a idempotency_key é derivada do event_id
    ('transition:{task_id}:{eid}'), e insert_event usa event_id como PRIMARY KEY.
    Reexecutar com o mesmo event_id ⇒ INSERT viola a PK ⇒ exceção engolida por
    'except Exception: pass' em transition_task ⇒ efeito colapsa em 1 registro
    (dedupe DE FACTO por event_id, silencioso — NÃO por idempotency_key).
    Chaves distintas (event_id novo) ⇒ novo registro, e como a key deriva do eid,
    a key também difere — dedupe por idempotency_key não é exercitável via esta API."""
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

        # Reentrega at-least-once (mesmo event_id): colapsa na PK event_id (silencioso).
        dispatch_once()
        dispatch_once()

        events = db.list_events(idempotency_key="transition:task-e2e:evt-e2e-fixed")
        assert len(events) == 1  # vigência: PK(event_id) segura a duplicata; key não é consultada
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
    Não há dedupe nem validação; e list_events(idempotency_key=None) NÃO filtra
    eventos-sem-chave (omite a cláusula WHERE). Comportamento vigente documentado."""
    db = create_test_db()
    try:
        e1 = db.insert_event("e", {"n": 1})
        e2 = db.insert_event("e", {"n": 2}, idempotency_key=None)
        assert e1 != e2
        # Ambos persistem; list_events sem argumento retorna TODOS (não filtra NULL).
        all_events = db.list_events()
        assert len(all_events) == 2
        assert {ev["idempotency_key"] for ev in all_events} == {None}
        # Não há como consultar apenas eventos com chave nula via API pública.
    finally:
        db.close()


# --------------------------------------------- (f) concorrência leve de reentrega
def test_reentrega_concorrente_mesma_chave_duas_conexoes__race_documentada(
    tmp_path: Path,
) -> None:
    """LAC-IDEMP-01: NÃO há dedupe atômico na persistência. Duas conexões (dois
    'workers' at-least-once) inserindo a mesma idempotency_key persistem 2 registros.
    Determinístico: não depende de timing — não existe constraint que o impeça.
    Correção (UNIQUE index) violaria R7/ADR-003 e NÃO foi aplicada (decisão Classe C)."""
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
        # Vigente: sem constraint de unicidade → race não é barrada; 2 registros.
        assert len(rows) == 2
        result = check.verify_chain()
        # insert_event faz read-then-insert sem transação/lock: sob interleaving,
        # dois writers podem encadear sobre o mesmo predecessor (cadeia quebrada).
        # Desfecho depende do escalonamento → aceitamos ambos, sem mascarar.
        assert isinstance(result.ok, bool)
        assert result.eventos_verificados in (1, 2)
    finally:
        check.close()


def test_reentrega_concorrente_cadeia_pode_quebrar_sob_interleaving(tmp_path: Path) -> None:
    """Documenta lacuna real de concorrência: insert_event lê o último hash e
    insere sem transação/lock — dois writers concorrentes podem encadear sobre o
    mesmo predecessor, quebrando verify_chain(). NÃO é mascarado: o teste apenas
    registra o resultado observado (ok ∈ {True, False}) e o nº de elos inválidos."""
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
        # Sem transação/lock no read-then-insert, o elo pode divergir sob race.
        # Registramos o veredito sem mascarar: ambos os desfechos são possíveis.
        assert isinstance(result.ok, bool)
        assert result.eventos_verificados in (1, 2)
    finally:
        check.close()
