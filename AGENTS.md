# AGENTS.md — sdlc-agentico

Repo de **documentação canônica** do projeto SDLC Agêntico (baseline v0). Tratá-lo como fonte documental permanente do projeto: manter índice e artefatos consistentes, não tratar como descartável.

## O que este repo É (e o que não é)
- **Documentação + gates/CI parametrizados (sem código de aplicação).** Gates/CI (Makefile/pyproject.toml) parametrizados (fail-closed) para verificação documental; implementação de aplicação ainda não iniciada (F-ÚNICO-1 bloqueada por D-V0-01). Não há código-fonte de aplicação, manifests de app, lockfiles, build de aplicação, testes de aplicação nem ferramentas de verificação de aplicação. Não procure nem tente rodar `npm test`/`pytest`/`make` como se houvesse aplicação — os alvos de `make` existentes são parametrizados/documentais (ver seção Verificação).
- **Implementação não iniciada.** Todo o conteúdo é baseline **v0 "condicional"**, pendente de reconciliação formal e de aprovações Classe C (ver `docs/00-painel-gerencial-consolidado.md` §5, decisões D-V0-01…D-V0-06).
- Nenhuma stack/repositório-alvo/CI foi escolhido `[LACUNA]` — não invente; registre como lacuna.

## Fontes de verdade e layout
- Canônicos (manter sincronizados): `docs/00-painel-gerencial-consolidado.md` (painel + JSON machine-readable), `docs/10-produto-visao-v0.md` (PO, fusão DEC-029 de `docs/10`+`docs/11`), `docs/20-governanca-pm-plano-baseline-v0.md` (PM), `docs/30-arquitetura-tech-lead-baseline-v0.md` (TL) e o índice/política `docs/README.md`.
- `docs/README.md` é a política canônica: ao adicionar/remover/renomear docs, **atualize o índice** (tabela de artefatos, status e seção de rastreabilidade) no mesmo commit.
- `docs/40-operacao-raci-repo-v0.md` — matriz RACI das operações deste repo (edição de canônicos, índice, Classe C, git); complementar ao RACI de produto do `20-*` §2. Status `vigente` (validação Classe C do Mantenedor em 2026-11-16, DEC-002; ver `docs/DECISIONS.md`).
- `docs/DECISIONS.md` — log canônico de decisões Classe C (DEC-001…008): kickoff 2026-11-16, D-V0-01 adiada, LICENSE nenhuma por ora, evidence/ rejeitado, normativos por caminho+sha256. Consultar ANTES de propor promoção de status/ADR/contrato.
- Os arquivos `baseline-v0-*.md` foram removidos em 2026-11-13 por serem duplicatas/parciais — **não recriá-los**. Duplicata ≠ fonte de verdade; divergência → registrar como `[LACUNA]`, nunca duplicar.
- Locais canônicos propostos (`docs/product/`, `docs/tech/`, `docs/governance/`, `docs/evidence/`, `docs/adr/core/ADR-<NNN>-<slug-kebab>.md`) são `[PREMISSA]` pendente de reconciliação — **não criar** diretórios/ADRs/numeração sem decisão explícita. ADRs iniciais A–G estão propostos e **sem número** (`adr_ref="none"`).

## Regras duras (não violar)
- **Nunca** marcar artefato como `approved`/`accepted` nem promover ADR/baseline. Decisões Classe C exigem aprovação humana explícita; aceite de valor é do PO. Execução ≠ aceite.
- Semântica de estados é distinta e não intercambiável: execução `done/blocked/partial` ≠ operacional `completed` ≠ valor `approved` (PO). Nunca inferir aprovação a partir de status de execução.
- Gates de qualidade exigem baseline e evidência; regra vigente é "no new errors" sobre baseline declarada — thresholds (ex.: cobertura) só podem ser lidos do projeto-alvo quando ele existir; não hardcodar.
- Ferramenta de tracking/backlog é `[LACUNA]` (indefinida); não assuma board/issue tracker existente.
- Sem evidência, não há `done`: todo status de execução documentado deve referenciar artefato/evidência.
- Conflito entre documentos deste repo: não há fonte executável para desempate — registre o conflito como `[LACUNA]` e escale, não "resolva" silenciosamente.

## Convenções
- Idioma: **PT-BR** em todos os docs. Manter front matter `title/date/project/source/status` nos artefatos numerados; atualizar `status` honestamente (`condicional`/`partial`/`done` conforme realidade, nunca `approved` sem aceite).
- Nomenclatura: `docs/<NN>-<trilha>-<slug>.md` para artefatos numerados; numeração 00/10/20/30 = agregação/PO/PM/TL.
- Git: raiz do git = raiz do repo (não criar `.git` aninhado em `docs/`); branch única `master` hoje, **sem remote configurado**; um único commit até agora. **Branch apenas para novas funcionalidades ou refatoração massiva** — mudanças triviais (docs, correções pontuais) vão direto na `master`, sem branch nem PR. Commits: Conventional Commits em PT-BR com escopo (`docs(baseline): …` é o padrão observado).
- Mensagens de commit e docs podem citar sessões/subagentes (`ses_...`) — preservar rastreabilidade.

## Verificação
- Gates documentais disponíveis: make lint (ruff), make typecheck (mypy, tolerante), make test (pytest, tolerante), make build (placeholder), make audit (G0–G3 + fail-closed exit 6 se pyproject.toml ausente). Thresholds (cobertura) parametrizados (fail_under=0 placeholder) — valores reais pendentes de D-V0-06/projeto-alvo. "Verificar" também = checar consistência cruzada: `docs/README.md` (índice/status) ↔ artefatos numerados ↔ JSON machine-readable no painel (`docs/00-painel-gerencial-consolidado.md` §8). Após qualquer edição, confira os três.
- Antes de editar um canônico, leia `docs/README.md` e o artefato afetado integralmente; depois, propague a mudança de status/estado para o índice e o painel se aplicável.

## Perguntas abertas / lacunas conhecidas
- Stack, repo-alvo, infra/CI/gates: `[LACUNA]` (D-V0-01). Capacidade/prazo/orçamento/cadência/tracking: `[LACUNA]` (D-V0-02). Aceite do PO sobre visão/MVP/KPIs: pendente (D-V0-03). Aprovação da baseline técnica/ADRs A–G e convenção de numeração: pendente (D-V0-04). Contrato canônico v1.0.0 (resumo+envelope+estados): pendente (D-V0-05). Política unificada de gates/thresholds: pendente (D-V0-06).
- Em caso de dúvida sobre promoção de estado ou aprovação Classe C: **pare e pergunte ao humano**; não prosseguir por inferência.