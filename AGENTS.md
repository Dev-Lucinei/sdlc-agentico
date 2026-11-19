# AGENTS.md — sdlc-agentico

Repo de **documentação canônica** do projeto SDLC Agêntico (baseline v0 **publicada**, DEC-024) **+ implementação da Fase 1 (Python 3.12) concluída**. Tratá-lo como fonte documental permanente do projeto: manter índice e artefatos consistentes, não tratar como descartável.

> **Última atualização:** 2026-11-18 — Fases A–D de simplificação executadas; log de decisões bifurcado (DEC-031); painel derivado atualizado; kickoff formal da Fase 2 registrado (DEC-032).

## O que este repo É (e o que não é)
- **Documentação canônica + implementação da Fase 1 concluída.** A Fase 1 (F-ÚNICO-1) está `done` (execução): stack Python 3.12 (DEC-018), suíte com **100 testes passando**, cobertura **79,02%** ≥ threshold de 50% lido de `pyproject.toml` (DEC-022), `make audit` com **exit 0**. Histórico de commits: `git log`. Aceite de valor é ato exclusivo do PO — **execuções nunca são `approved` por inferência**; os incrementos E1–E3 foram **aprovados explicitamente pelo PO em DEC-030 (2026-11-18, Classe C)**; E4 e demais artefatos seguem **não aprovados**.
- **Gates funcionais via Makefile/pyproject.toml** (parametrizados, fail-closed): `make lint` (ruff), `make typecheck` (mypy), `make test` (pytest), `make audit` (G0–G3 + verificação de `pyproject.toml`, exit 6 fail-closed se ausente). Cobertura parametrizada (fail_under=50) — lida do projeto-alvo, não hardcodada em prosa.
- **Implementação de aplicação existe (Fase 1); F-ÚNICO-2 (Evolução) em andamento** (DEC-024). Não declarar nada como `approved`/`accepted` por inferência de execução.
- Não há CI externo (sem GitHub Actions etc.) por decisão explícita (DEC-018). LangGraph permanece **condicional** (CR-009-C dormente); a baseline técnica é a máquina de estados Python pura em `src/`.

## Fontes de verdade e layout
- Canônicos (manter sincronizados): `docs/00-painel-gerencial-consolidado.md` (painel só-humano; JSON machine-readable extraído para `docs/schemas/painel-status.json` em 2026-11-18; §0 "Status dinâmico" = fonte única de telemetria volátil, DEC-029), `docs/10-produto-visao-v0.md` (PO; fusão DEC-029 de `docs/10`+`docs/11`), `docs/20-governanca-pm-plano-baseline-v0.md` (PM), `docs/30-arquitetura-tech-lead-baseline-v0.md` (TL) e o índice/política `docs/README.md`.
- `docs/README.md` é a política canônica: ao adicionar/remover/renomear docs, **atualize o índice** (tabela de artefatos, status e seção de rastreabilidade) no mesmo commit.
- `docs/40-operacao-raci-repo-v0.md` — matriz RACI das operações deste repo (edição de canônicos, índice, Classe C, git); complementar ao RACI de produto do `20-*` §2. Status `vigente` (validação Classe C do Mantenedor em 2026-11-16, DEC-002; ver `docs/DECISIONS.md`).
- `docs/DECISIONS.md` — **índice vigente** do log de decisões Classe C (~771 palavras; leitura obrigatória): regra de ouro condensada + tabela-índice DEC-001…DEC-034 + ponteiros. Corpos append-only em `docs/decisions/DEC-NNN-<slug>.md`; arquivo congelado `docs/decisions/arquivo-2026-11-16.md` (DEC-031). Consultar ANTES de propor promoção de status/ADR/contrato.
- `src/` — implementação da Fase 1 (Python 3.12): `contract_validator`, `exit_codes`, `graph`, `human_review`, `persistence`, `quality_gates`, `secrets`, `state`, pacote `stubs/`. `tests/` — suíte pytest (100 testes). `tools/validate_contract.py` — validador JSON do Contrato Canônico v1.0.0 (implementação real; **não** é shim). `tools/contract_validator.py` — shim de reexport de `src.contract_validator` **mantido**: é o entrypoint CLI invocado via subprocess pelos testes (`tests/test_contract_validator.py`, `tests/test_t_requirements.py`); removê-lo quebra a suíte (verificado em 2026-11-18: 6 testes falham com `FileNotFoundError`). Demais shims da raiz e de `tools/` foram removidos em 2026-11-18 (sessão 2026-11-18).
- `docs/historico/` — propostas/kickoff v0 superseded (`21`, `41`, `43`–`47`); não canônicos; conteúdo preservado, `git log` preserva o histórico.
- `docs/decisions/` — 34 corpos append-only `DEC-NNN-<slug>.md` (DEC-001…DEC-034) + `arquivo-2026-11-16.md` congelado (quarentena de seções stale, DEC-031). Nunca reescrever.
- `docs/48-contrato-canonico-v1-0-0.md` — Contrato Canônico v1.0.0 (DEC-021); status `condicional`; renomeado em 2026-11-18 (sufixo `-proposta-` removido).
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
- Git: raiz do git = raiz do repo (não criar `.git` aninhado em `docs/`); branch única `master` hoje; remote origin = https://github.com/Dev-Lucinei/sdlc-agentico.git (detectado 2026-11-18); pushes SOMENTE com autorização explícita do Mantenedor. **Branch apenas para novas funcionalidades ou refatoração massiva** — mudanças triviais (docs, correções pontuais) vão direto na `master`, sem branch nem PR. Commits: Conventional Commits em PT-BR com escopo (`docs(baseline): …` é o padrão observado).
- Mensagens de commit e docs podem citar sessões/subagentes (`ses_...`) — preservar rastreabilidade.

## Verificação
- Gates **funcionais** (Python 3.12, DEC-018): `make lint` (ruff — `ruff check .`), `make typecheck` (mypy — escopo `src`), `make test` (pytest — 100 testes; coleta tolerante a repo sem testes), `make build` (placeholder documental), `make audit` (G0–G3 + verificação de `pyproject.toml`, fail-closed exit 6 se ausente), `make audit-g2` (G2 executável, DEC-032 F2.1-téc: ruff + mypy + pytest com cobertura ≥ `fail_under` lido do `pyproject.toml` + SAST `ruff --select S src/`; fail-closed). Suíte atual: **100 testes verdes; cobertura 79,02% ≥ fail_under=50** (`pyproject.toml`; DEC-022). "Verificar" também = checar consistência cruzada: `docs/README.md` (índice/status) ↔ artefatos numerados ↔ JSON machine-readable (`docs/schemas/painel-status.json`, derivado de `docs/DECISIONS.md` + `docs/decisions/` (ver `derivation_note` no JSON; regenerar a cada DEC)). Após qualquer edição, confira os três.
- Antes de editar um canônico, leia `docs/README.md` e o artefato afetado integralmente; depois, propague a mudança de status/estado para o índice e o painel se aplicável.

## Perguntas abertas / lacunas conhecidas
- Decisões vigentes → `docs/DECISIONS.md` (índice); corpos em `docs/decisions/` (append-only; arquivo congelado `arquivo-2026-11-16.md`).
- DEC-030 (2026-11-18, Classe C): aceite de valor **E1–E3** (`accepted`, único aceite de valor vigente); **E4 e demais artefatos NÃO aprovados**; KPIs não instrumentáveis (lacuna mantida).
- Em caso de dúvida sobre promoção de estado ou aprovação Classe C: **pare e pergunte ao humano**; não prosseguir por inferência.
