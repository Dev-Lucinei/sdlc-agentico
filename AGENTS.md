# AGENTS.md — sdlc-agentico

Repo de **documentação canônica** do projeto SDLC Agêntico (baseline v0 **publicada**, DEC-024) **+ implementação da Fase 1 (Python 3.12) concluída**. Tratá-lo como fonte documental permanente do projeto: manter índice e artefatos consistentes, não tratar como descartável.

> **Última atualização:** 2026-11-18 — DEC-030 registrada e propagada (aceite de valor **E1–E3 APROVADO**, Classe C, por Lucinei (Mantenedor, PO) em sessão OpenCode 2026-11-18 via pergunta interativa — "Aprovar E1–E3 (Classe C)"; E4 fora do escopo e **não aprovado**); DEC-029 (reestruturação SoT; telemetria volátil = `docs/00` §0) vigente.

## O que este repo É (e o que não é)
- **Documentação canônica + implementação da Fase 1 concluída.** A Fase 1 (F-ÚNICO-1) foi implementada e está `done` (execução): stack Python 3.12 (DEC-018), `src/` com 9 módulos (~57 KB), suíte com **65 testes passando**, `make audit` com **exit 0** (lint ruff + typecheck mypy + pytest; cobertura 75,00% ≥ threshold de 50% lido de `pyproject.toml` — DEC-022). Commits da Fase 1: `e54c083` (validador JSON do contrato), `71fc6f6` (orquestração LangGraph local), `f6d74f6` (SQLite, validador, segredos, máquina de estados). Aceite de valor é ato exclusivo do PO — **execuções nunca são `approved` por inferência**; os incrementos E1–E3 foram **aprovados explicitamente pelo PO em DEC-030 (2026-11-18, Classe C)**; E4 e demais artefatos seguem **não aprovados**.
- **Gates funcionais via Makefile/pyproject.toml** (parametrizados, fail-closed): `make lint` (ruff), `make typecheck` (mypy), `make test` (pytest), `make audit` (G0–G3 + verificação de `pyproject.toml`, exit 6 fail-closed se ausente). Cobertura parametrizada (fail_under=50) — lida do projeto-alvo, não hardcodada em prosa.
- **Implementação de aplicação existe (Fase 1); F-ÚNICO-2 (Evolução) em andamento** (DEC-024). Não declarar nada como `approved`/`accepted` por inferência de execução.
- Não há CI externo (sem GitHub Actions etc.) por decisão explícita (DEC-018). LangGraph permanece **condicional** (CR-009-C dormente); a baseline técnica é a máquina de estados Python pura em `src/`.

## Fontes de verdade e layout
- Canônicos (manter sincronizados): `docs/00-painel-gerencial-consolidado.md` (painel só-humano; JSON machine-readable extraído para `docs/schemas/painel-status.json` em 2026-11-18; §0 "Status dinâmico" = fonte única de telemetria volátil, DEC-029), `docs/10-produto-visao-v0.md` (PO; fusão DEC-029 de `docs/10`+`docs/11`), `docs/20-governanca-pm-plano-baseline-v0.md` (PM), `docs/30-arquitetura-tech-lead-baseline-v0.md` (TL) e o índice/política `docs/README.md`.
- `docs/README.md` é a política canônica: ao adicionar/remover/renomear docs, **atualize o índice** (tabela de artefatos, status e seção de rastreabilidade) no mesmo commit.
- `docs/40-operacao-raci-repo-v0.md` — matriz RACI das operações deste repo (edição de canônicos, índice, Classe C, git); complementar ao RACI de produto do `20-*` §2. Status `vigente` (validação Classe C do Mantenedor em 2026-11-16, DEC-002; ver `docs/DECISIONS.md`).
- `docs/DECISIONS.md` — log canônico de decisões Classe C (DEC-001…DEC-030; DEC-030 = aceite de valor E1–E3, 2026-11-18, Classe C). Consultar ANTES de propor promoção de status/ADR/contrato.
- `src/` — implementação da Fase 1 (Python 3.12): `contract_validator`, `exit_codes`, `graph`, `human_review`, `persistence`, `quality_gates`, `secrets`, `state`, pacote `stubs/`. `tests/` — suíte pytest (65 testes). `tools/validate_contract.py` — validador JSON do Contrato Canônico v1.0.0 (implementação real; **não** é shim). `tools/contract_validator.py` — shim de reexport de `src.contract_validator` **mantido**: é o entrypoint CLI invocado via subprocess pelos testes (`tests/test_contract_validator.py`, `tests/test_t_requirements.py`); removê-lo quebra a suíte (verificado em 2026-11-18: 6 testes falham com `FileNotFoundError`). Demais shims da raiz e de `tools/` foram removidos em 2026-11-18 (sessão 2026-11-18).
- Os arquivos `baseline-v0-*.md` foram removidos em 2026-11-13 por serem duplicatas/parciais — **não recriá-los**. Duplicata ≠ fonte de verdade; divergência → registrar como `[LACUNA]`, nunca duplicar.
- Locais canônicos propostos (`docs/product/`, `docs/tech/`, `docs/governance/`, `docs/evidence/`, `docs/adr/core/ADR-<NNN>-<slug-kebab>.md`) — convenção ADR confirmada por DEC-020 (`docs/adr/core/ADR-<NNN>-<slug>.md`). ADRs ADR-001…ADR-008 **`accepted`** (DEC-020, 2026-11-17). `docs/evidence/` **rejeitado** (DEC-005) — não criar.

## Regras duras (não violar)
- **Nunca** marcar artefato como `approved`/`accepted` nem promover ADR/baseline por inferência. Decisões Classe C exigem aprovação humana explícita; aceite de valor é do PO. Execução ≠ aceite.
- Semântica de estados é distinta e não intercambiável: execução `done/blocked/partial` ≠ operacional `completed` ≠ valor `approved` (PO). Nunca inferir aprovação a partir de status de execução.
- Gates de qualidade exigem baseline e evidência; regra vigente é "no new errors" sobre baseline declarada; thresholds (ex.: cobertura) lidos do `pyproject.toml` do projeto-alvo — não hardcodar em prosa.
- Ferramenta de tracking/backlog: `docs/` é a trilha vigente (DEC-006(vi)); adoção de ferramenta externa (GitHub Issues/Projects) para escala pendente de decisão Classe C (CR-010-C, DEC-027) — não assumir board/issue tracker existente.
- Sem evidência, não há `done`: todo status de execução documentado deve referenciar artefato/evidência.
- Conflito entre documentos deste repo: não há fonte executável para desempate — registre o conflito como `[LACUNA]` e escale, não "resolva" silenciosamente.

## Convenções
- Idioma: **PT-BR** em todos os docs. Manter front matter `title/date/project/source/status` nos artefatos numerados; atualizar `status` honestamente (`condicional`/`partial`/`done` conforme realidade, nunca `approved` sem aceite).
- Nomenclatura: `docs/<NN>-<trilha>-<slug>.md` para artefatos numerados; numeração 00/10/20/30 = agregação/PO/PM/TL.
- Git: raiz do git = raiz do repo (não criar `.git` aninhado em `docs/`); branch única `master` hoje, **sem remote configurado**. **Branch apenas para novas funcionalidades ou refatoração massiva** — mudanças triviais (docs, correções pontuais) vão direto na `master`, sem branch nem PR. Commits: Conventional Commits em PT-BR com escopo (`docs(baseline): …` é o padrão observado).
- Mensagens de commit e docs podem citar sessões/subagentes (`ses_...`) — preservar rastreabilidade.

## Verificação
- Gates **funcionais** (Python 3.12, DEC-018): `make lint` (ruff — `ruff check .`), `make typecheck` (mypy — escopo `src`), `make test` (pytest — 65 testes; coleta tolerante a repo sem testes), `make build` (placeholder documental), `make audit` (G0–G3 + verificação de `pyproject.toml`, fail-closed exit 6 se ausente). Suíte atual: **65 testes verdes; cobertura 75,00% ≥ fail_under=50** (`pyproject.toml`; DEC-022). "Verificar" também = checar consistência cruzada: `docs/README.md` (índice/status) ↔ artefatos numerados ↔ JSON machine-readable (`docs/schemas/painel-status.json`, extraído do §8 do painel em 2026-11-18). Após qualquer edição, confira os três.
- Antes de editar um canônico, leia `docs/README.md` e o artefato afetado integralmente; depois, propague a mudança de status/estado para o índice e o painel se aplicável.

## Perguntas abertas / lacunas conhecidas
- D-V0-01 **RESOLVIDO** (DEC-018, 2026-11-17): repo-alvo = este repo; stack Python 3.12 + pytest + ruff + mypy; **sem CI por ora**.
- D-V0-02 **RESOLVIDO para a escala atual** (DEC-027, 2026-11-17, Classe B): Mantenedor único; capacidade ~4–8h/sem ([PREMISSA-P10], telemetria volátil — fonte única `docs/00` §0, DEC-029); tracking = `docs/` (DEC-006(vi)); ferramenta externa para escala pendente de decisão Classe C (CR-010-C).
- D-V0-03/04/05/06 **APROVADOS E MATERIALIZADOS** (DEC-019/DEC-020/DEC-021/DEC-022, 2026-11-17): aceite PO sobre visão/MVP/KPIs; baseline técnica + ADRs ADR-001…ADR-008 `accepted`; contrato canônico v1.0.0 adotado; política unificada de gates/thresholds.
- DEC-007 **FECHADO** (DEC-023, 2026-11-17): política de segredos (os.environ, nunca hardcode).
- Baseline v0 **PUBLICADA** (DEC-024, 2026-11-17); F-ÚNICO-1 (MVP Controlado) **concluída**; F-ÚNICO-2 (Evolução) **em andamento**.
- DEC-029 (2026-11-18): reestruturação SoT + escalonamento progressivo de governança — fusão `docs/10`+`docs/11` → `docs/10-produto-visao-v0.md`; telemetria volátil centralizada em `docs/00` §0; [PREMISSA-P7] depreciada/histórica.
- DEC-030 **VIGENTE** (2026-11-18, Classe C): aceite de valor **E1–E3 APROVADO** por Lucinei (Mantenedor, PO) em sessão OpenCode 2026-11-18 via pergunta interativa ("Aprovar E1–E3 (Classe C)"); registrado em `docs/DECISIONS.md` (`decision_id` `01M7P3NFTDNKR760KBBBHE8PSV`). Aplica-se **somente a E1–E3**; **E4 e demais artefatos seguem não aprovados**; KPIs não instrumentáveis (lacuna mantida); visão/MVP-como-um-todo não promovidos. `approved` permanece exclusivo do PO com evidência; nenhuma outra declaração de `approved` é válida neste arquivo.
- Em caso de dúvida sobre promoção de estado ou aprovação Classe C: **pare e pergunte ao humano**; não prosseguir por inferência.
