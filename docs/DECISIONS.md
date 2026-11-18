---
title: "DECISIONS — Log de Decisões do sdlc-agentico"
date: "2026-11-16"
project: "sdlc-agentico"
source: "gerente-projeto + Mantenedor Lucinei (decisões Classe C de 2026-11-16)"
status: "vigente"
---

# DECISIONS — Log de Decisões do `sdlc-agentico`

**Classe de autonomia desta elaboração:** B (registro documental reversível, executado pelo `gerente-projeto` sob coordenação). As decisões marcadas como **Classe C** foram tomadas pelo **Mantenedor humano Lucinei** em 2026-11-16 e são irreversíveis apenas por nova decisão humana explícita.

## Propósito e regra de ouro

Este arquivo é o **log canônico de decisões do repositório** (criado por DEC-001). Ele registra decisões de escopo, governança, arquitetura e processo que afetem a baseline documental ou a operação do repo — não substitui os artefatos canônicos, que permanecem nas suas trilhas (`00/10/20/30/40/41–45`).

**Regra de ouro (obrigatória):**

1. **Classe C exige `decided_by` humano explícito + evidência.** Nenhum agente (orquestrador, PO, PM, TL, subagentes) aprova Classe C por inferência, silêncio ou maioria.
2. **Execução ≠ `completed` ≠ `approved`.** `done/blocked/partial` (execução) ≠ `completed` (OPS) ≠ `approved` (valor, PO). Este log não promove nada a `approved` por conta própria.
3. **Sugestão externa ≠ canon.** Insumos externos (ex.: auditoria técnica externa de 2026-11-16) são insumo não canônico; só viram decisão quando o Mantenedor decide (Classe C) ou quando registradas como Classe B/registro sem efeito de aprovação.
4. **Ausência de decisão humana explícita ⇒ não aprovado.** Itens sem `decided_by` humano permanecem `[LACUNA]` ou "aguardando", nunca `approved`/`vigente` por omissão.

**Referências normativas e canônicas:**
- `docs/20-governanca-pm-plano-baseline-v0.md` §5 (change control; decisão registrada ⇒ baseline muda);
- `docs/00-painel-gerencial-consolidado.md` (adendos §8.1/§8.2 — fila de CRs e decisões Classe C a submeter);
- `docs/40-operacao-raci-repo-v0.md` (RACI do repo; linhas 6, 9, 10 e 12–14 exigem/vetem o Mantenedor; regra de desempate = parar e escalar);
- `~/.opencode/references/contrato-resumo-subagentes.md` e `~/.opencode/references/autonomia-e-estados.md` (normativos externos, por caminho+sha256 — ver DEC-003).

## Tabela-resumo

| ID | Data | Título | Classe | decided_by | Status |
|---|---|---|---|---|---|
| DEC-001 | 2026-11-16 | Criação deste log canônico de decisões (CR-012) | C | Lucinei (Mantenedor) | vigente |
| DEC-002 | 2026-11-16 | `docs/40-operacao-raci-repo-v0.md` validado como **vigente** (CR-001) | C | Lucinei (Mantenedor) | vigente |
| DEC-003 | 2026-11-16 | Inclusão condicional dos canônicos 41–45 na baseline v0 + normativos externos por caminho+sha256, sem cópia física (CR-002B + CR-005B) | C | Lucinei (Mantenedor) | vigente |
| DEC-004 | 2026-11-16 | LICENSE: **nenhuma por ora** — repo mantém todos os direitos reservados (CR-003) | C | Lucinei (Mantenedor) | vigente |
| DEC-005 | 2026-11-16 | Criação de `docs/evidence/` **REJEITADA** (CR-004) | C | Lucinei (Mantenedor) | vigente |
| DEC-006 | 2026-11-16 | Kickoff D-V0-01/02: D-V0-01 adiado; repo-alvo = este repo; CI nenhuma por ora; Mantenedor único; cadência sob demanda sem SLA; tracking = `docs/` como trilha | C (6 pontos) | Lucinei (Mantenedor) | vigente |
| DEC-007 | 2026-11-16 | Política de segredos permanece `[LACUNA]`; reavaliar após D-V0-01 (CR-011) | B (registro) | gerente-projeto (registro) | registrado — `[LACUNA]` aberta |
| DEC-008 | 2026-11-16 | Reconciliação do baseline v0 planejada (CR-013); roadmap único em elaboração (`docs/47`); publicação bloqueada por D-V0-03/04/05/06 | B (planejamento) | gerente-projeto (registro) | registrado — planejamento |
| DEC-009 | 2026-11-16 | Pauta D-V0-03 — Aceite do PO sobre visão, escopo MVP (M1–M3), semântica de estados e metas/KPIs iniciais | C (aprovado) | Mantenedor (Lucinei, 2026-11-16) — PO A/R | aprovado (Classe C) — materializado em docs/11-visao-mvp-v0.md |
| DEC-010 | 2026-11-16 | Pauta D-V0-04 — Aprovação da baseline técnica e ADRs iniciais (A–G) + convenção/numeração canônica de ADRs | C (aprovado) | Mantenedor (Lucinei, 2026-11-16) — TL propõe | aprovado (Classe C) — materializado em docs/adr/core/ADR-001…ADR-007 (status proposed) |
| DEC-011 | 2026-11-16 | Pauta D-V0-05 — Consolidação do contrato canônico v1.0.0 (resumo + envelope + estados + correlação + `schema_version`) | C (aprovado) | Mantenedor (Lucinei, 2026-11-16) — TL+PO+PM | aprovado (Classe C) — reconciliado em docs/41/45 (1.0.0) |
| DEC-012 | 2026-11-16 | Pauta D-V0-06 — Política unificada de gates/evidência e thresholds (lidos do projeto-alvo) | C (aprovado) | Mantenedor (Lucinei, 2026-11-16) — TL/PM/PO | aprovado (Classe C) — materializado em Makefile/pyproject.toml (parametrizados) |
| DEC-013 | 2026-11-16 | Registro de reconciliação MU-0.3 concluída (propagação documental + pautas DEC-009+); evidências: hashes, arquivos editados, git diff | B (registro) | gerente-projeto (registro) | registrado — concluído (MU-0.3) |
| DEC-014 | 2026-11-16 | Registro de grill-with-docs (pendências bloqueantes PM): orçamento formal = zero; cadência RACI = semanal (PM R / Mantenedor A); kickoff D-V0-01 antes da semana 1; propostas PR-01…PR-07 (D-V0-01 restante, D-V0-02 restante, roadmap, riscos R12, cronograma 1 semana, tracking) | B (registro) | gerente-projeto (registro) + Mantenedor (input grill) | aprovado (Classe C, 2026-11-16) — materializado em docs/21-cronograma-raci-riscos-v0.md |
| DEC-015 | 2026-11-16 | Consolidação PO da pauta D-V0-03 — proposta de visão/MVP M1–M3, semântica de estados (execução≠operação≠valor), KPIs mensuráveis em 1 semana (tracking=docs/), aceite de valor e backlog (E1–E4) — grill-with-docs 2×3 aplicado (lacunas peso 5: KPIs mensuráveis, semântica de estados, handoff PR→aceite, capacidade/rastreabilidade) | B (registro) | gerente-produto (proposta) | aprovado (Classe C, 2026-11-16) — materializado em docs/11-visao-mvp-v0.md |
| DEC-016 | 2026-11-16 | Consolidação TL das pautas D-V0-04 (ADRs A–G + convenção de numeração), D-V0-05 (contrato v1.0.0), D-V0-06 (gates), CR-008-C (unificação de gates documental), CR-009-C (LangGraph condicional + kickoff antes da semana 1), arquitetura e dívida técnica documental — grill-with-docs 2×3 aplicado (lacunas peso 5: numeração ADR local, thresholds parametrizados, convenção ADR, dívida documental, CR-008-C agora) | B (registro) | tech-lead (proposta) | aprovado (Classe C, 2026-11-16) — materializado em docs/adr/core/ADR-001…ADR-007 + Makefile/pyproject.toml |
| DEC-017 | 2026-11-16 | Mudança de identidade do repositório: documentação + gates/CI (Makefile/pyproject.toml parametrizados, fail-closed) — implementação de aplicação ainda não iniciada (F-ÚNICO-1 bloqueada por D-V0-01) | B (registro) | Mantenedor (Lucinei, 2026-11-16) | registrado — mudança de identidade documentada em AGENTS.md |
| DEC-018 | 2026-11-17 | Resolução de D-V0-01 (Opção B): stack mínima definida — Python 3.12 + pytest + ruff + mypy, sem CI externo; pyproject.toml real com thresholds absolutos (cobertura ≥50%, 0 erros críticos); F-ÚNICO-1 desbloqueada (infraestrutura real mínima) | C | Lucinei (Mantenedor) | vigente |
| DEC-019 | 2026-11-17 | D-V0-03 — Aceite do PO sobre visão/MVP/estados/KPIs: APROVADO E MATERIALIZADO (Classe C); referência DEC-009/DEC-015; artefatos docs/10, docs/11, docs/41 | C | Lucinei (Mantenedor) — PO A/R | vigente |
| DEC-020 | 2026-11-17 | D-V0-04 — Aprovação da baseline técnica e ADRs iniciais (ADR-001…ADR-008): promovidos de `proposed` para `accepted`; convenção ADR-<NNN>-<slug>.md confirmada | C | Lucinei (Mantenedor) — TL propõe | vigente |
| DEC-021 | 2026-11-17 | D-V0-05 — Adoção formal do contrato canônico v1.0.0 (docs/48 v1.0.0-PROPOSTA → v1.0.0; validador docs/schemas/contract-v1.0.0.schema.json; migração aditiva 0.1.0-draft → 1.0.0) | C | Lucinei (Mantenedor) — TL+PO+PM | vigente |
| DEC-022 | 2026-11-17 | D-V0-06 — Política unificada de gates/evidência/thresholds: cobertura ≥50%, 0 erros críticos (absolutos, hardcoded); artefatos pyproject.toml, Makefile, docs/42 | C | Lucinei (Mantenedor) — TL/PM/PO | vigente |
| DEC-023 | 2026-11-17 | DEC-007 — Política de segredos: injeção via variáveis de ambiente (os.environ), nunca hardcode; mascaramento em logs; proibição de segredos em SoT, logs, artefatos; referência src/secrets.py | C | Lucinei (Mantenedor) | vigente |
| DEC-024 | 2026-11-17 | Consolidação da baseline v0 e início da F-ÚNICO-2 (Evolução): 6/6 critérios de §8.3 PASS; painel consolidado (§1/§5/§8/§8.3) atualizado; README sincronizado; F-ÚNICO-1 concluída (implementação: SQLite, validador, segredos, máquina de estados, 65 testes, 74,84% cobertura); F-ÚNICO-2 iniciada | C | Lucinei (Mantenedor) | vigente |
| DEC-026 | 2026-11-17 | Aceite de valor do PO para incrementos MVP: AC Given/When/Then completos para E1–E3 + handoff PR→aceite PO documentado + KPIs (KPI-1…KPI-6) calibrados para F-ÚNICO-2; `approved` exclusivo do PO com evidência; transição `pending→approved` exige `human_interaction_ref`; aceite formal pendente de execução | C | Lucinei (Mantenedor) — PO A/R | Materializado (Classe C, 2026-11-17) |
| DEC-025 | 2026-11-17 | Reconciliação de docs/41 e docs/45 para contrato v1.0.0 (F-ÚNICO-2): migração aditiva 0.1.0-draft → 1.0.0; campos do contrato adicionados (schema_name, schema_version, envelope_id, idempotency_key, correlation_id); seção de mapeamento de estados (done/completed/approved, ADR-005); exit codes com ação automática (docs/42); gates G2/G3 com thresholds do pyproject.toml; LangGraph condicional atualizado para stack mínima (DEC-018) | B | tech-lead (registro) | concluído (Classe B, 2026-11-17) |

---

## DEC-001 — Criação deste log canônico de decisões (CR-012)

- **Contexto:** o repo acumulava decisões (auditoria externa de 2026-11-16, fila de CRs não registrada — `docs/00` §8.2; change control pendente — `docs/20` §5) sem um log único append-only. Registros espalhados em painel/adendos geravam risco de drift e de decisões "informais" sem `decided_by`.
- **Decisão:** criar `docs/DECISIONS.md` como **log canônico de decisões do repositório**, com front matter próprio, tabela-resumo, uma seção por decisão e seção de decisões pendentes. Numeração `DEC-NNN` sequencial; entradas nunca são reescritas — correções entram como nova entrada ou adendo explícito.
- **Alternativas consideradas:**
  - (a) Seção de decisões dentro de `docs/20-*` §5 — rejeitada: `20-*` é o plano de governança (proposta PM), não log operacional; incha o artefato e mistura proposta com decisão humana.
  - (b) Manter decisões só no painel (`docs/00`) e nos adendos — rejeitada: painel é agregação de status, não trilha de decisão; sem append único, com risco de contradição silenciosa.
  - (c) Criar `docs/governance/DECISIONS.md` — rejeitada: estrutura de diretórios (`docs/governance/`) é `[PREMISSA]` pendente de decisão Classe C; faixa `≥40` já em uso pelos canônicos operacionais.
- **Consequências:** fonte única de registro de decisões do repo; toda decisão Classe C deve ser registrada aqui no mesmo change set em que for tomada; índice (`docs/README.md`) e painel (`docs/00` §5/§8) devem referenciar este log (propagação pendente — ver "Propagação pendente" ao final).
- **Evidência:** sessão de 2026-11-16 (esta sessão); CR-012; `docs/20` §5 (change control); `docs/00` §8.2 (fila de CRs); `docs/40` linha 6 (adicionar canônico = **A** do Mantenedor) e regra de desempate.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C).

## DEC-002 — `docs/40-operacao-raci-repo-v0.md` validado como vigente (CR-001)

- **Contexto:** `docs/40` criado em 2026-11-13 com status `condicional`, explicitamente pendente de validação do Mantenedor (suas "Próximas Ações" #1). A divergência índice↔painel (40 ausente do painel) foi corrigida no adendo §8.2 de `docs/00` (painel passou a referenciar `docs/40`).
- **Decisão:** validar `docs/40-operacao-raci-repo-v0.md` como **vigente** (Classe C, decided_by Lucinei, 2026-11-16). A matriz RACI das operações do repo passa a ser referência vigente para operação documental.
- **Alternativas consideradas:**
  - (a) Manter `condicional` — rejeitada: a validação do Mantenedor foi concedida nesta data.
  - (b) Migrar o conteúdo para `AGENTS.md` ("Fontes de verdade") e remover `docs/40` — rejeitada por ora: `AGENTS.md` fora do escopo de alteração desta sessão; permanece como opção futura (40 §Próximas Ações #2/#3).
  - (c) Remover o arquivo — rejeitada: artefato válido e referenciado.
- **Consequências:** `docs/40` vigente para operação do repo; linhas 9, 10 e 12–14 continuam exigindo humano (Classe C); nenhuma linha autoriza inferir `approved`. **Propagação pendente:** o front matter de `docs/40` ainda exibe `status: "condicional"`, e o índice/painel ainda o descrevem como condicional — a atualização desses três pontos exige change set designado (fora do escopo desta sessão). Ver "Propagação pendente".
- **Evidência:** `docs/40-operacao-raci-repo-v0.md` (conteúdo integral lido em 2026-11-16); `docs/README.md` (linha do índice); `docs/00` §8.2 (adendo que referencia `docs/40`); decisão do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C). Nota honesta: o canônico `docs/40` em si ainda não foi editado para refletir a vigência — ver "Propagação pendente".

## DEC-003 — Inclusão condicional dos canônicos 41–45 na baseline v0 + normativos externos por caminho+sha256 (CR-002B + CR-005B)

- **Contexto:** os canônicos de design t1–t5 (`docs/41`–`docs/45`, criados em 2026-11-16) receberam 5× `concordo_com_ressalvas` (PO e PM) e permanecem proposta documental condicional. O change request de inclusão na baseline v0 estava pendente desde o adendo §8.1 do painel. A auditoria externa chegou a propor **cópia física** de normativos externos para dentro do repo — proposta recusada (criaria drift / segunda SoT).
- **Decisão (dois pontos, ambos Classe C, decided_by Lucinei, 2026-11-16):**
  1. **Inclusão condicional** dos canônicos `41`–`45` na baseline v0. *Inclusão ≠ aprovação de conteúdo.* O conteúdo permanece proposta de design condicional (stack LangGraph não aprovada — ver DEC-006(i) e D-V0-01; gates/thresholds — D-V0-06). Promoção de conteúdo exige D-V0-04 (baseline técnica) e demais decisões Classe C.
  2. **Normativos externos referenciados por caminho+sha256 abreviado, sem cópia física** no repo. Registrados:
     - `~/.opencode/references/contrato-resumo-subagentes.md` — sha256 abreviado `163e0aad…` `[PREMISSA]`
     - `~/.opencode/references/autonomia-e-estados.md` — sha256 abreviado `776af494…` `[PREMISSA]`
     - *Nota:* os hashes completos **não** são fixados nesta data; devem ser recalculados pelo TL no próximo change set se o Mantenedor quiser pin exato. Verificação de 2026-11-16 (`sha256sum`): os prefixos acima conferem com os arquivos vivos no ambiente.
- **Alternativas consideradas:**
  - (a) Cópia física dos normativos no repo — rejeitada: drift garantido, segunda SoT, viola decisão do Mantenedor.
  - (b) Vendoring via submódulo/pacote — rejeitada: sem remote configurado; complexidade injustificada para 2 arquivos de referência.
  - (c) Excluir 41–45 da baseline v0 — rejeitada: são proposta condicional válida, revisada com ressalvas; exclusão perderia rastreabilidade.
  - (d) Aprovar o conteúdo/stack junto com a inclusão — rejeitada: exigiria D-V0-01 (adiado — DEC-006(i)) e D-V0-04; `inclusão ≠ aprovação`.
- **Consequências:** a baseline v0 passa a **incluir como propostas condicionais** os canônicos 00–45 (mais `DECISIONS.md` e a ata `docs/46`); nenhuma promoção de conteúdo é inferida; normativos permanecem vivos fora do repo, com risco de drift mitigado por referência+hash abreviado (pin exato pendente de decisão); qualquer mudança nos normativos externos invalida a referência até re-registro.
- **Evidência:** `docs/41`–`docs/45`; `docs/00` §8.1 (revisões PO/PM, 5× concordo_com_ressalvas) e §8.2 (recusa de cópia física); `docs/README.md` (índice 41–45); `sha256sum` local em 2026-11-16 (prefixos `163e0aad…` e `776af494…` conferem); decisão do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C) — para a *inclusão condicional* e a *política de referência por caminho+sha256*; o conteúdo de 41–45 permanece **condicional**.

## DEC-004 — LICENSE: nenhuma por ora (CR-003)

- **Contexto:** `LICENSE` ausente no repo (verificado em 2026-11-16; adendo §8.2 do painel). A auditoria externa tratou a ausência como falha objetiva; não é: é decisão explícita do Mantenedor.
- **Decisão:** **nenhuma LICENSE por ora**. O repositório mantém a proteção padrão de copyright — **todos os direitos reservados**. Qualquer licenciamento futuro exige nova decisão Classe C do Mantenedor.
- **Alternativas consideradas:**
  - (a) MIT / Apache-2.0 / GPL / outra licença permissiva ou copyleft — todas rejeitadas por ora (decisão explícita de não licenciar).
  - (b) Arquivo `LICENSE` com texto proprietário/"todos os direitos reservados" — rejeitada: redundante; o default legal já opera sem arquivo.
  - (c) Licenciar apenas docs vs. código futuro separadamente — rejeitada por ora: sem stack/repo-alvo de código (D-V0-01 adiado), não há o que licenciar em separado.
- **Consequências:** terceiros não têm permissão de uso, cópia ou distribuição; o repo permanece documental/privado na prática; nenhuma mudança de arquivo é necessária; se/quando houver release público ou contribuição externa, será necessária nova decisão Classe C (e provável D-V0-01 resolvida antes).
- **Evidência:** verificação de ausência de `LICENSE` em 2026-11-16 (registrada no adendo §8.2 de `docs/00`); decisão explícita do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C, decisão explícita).

## DEC-005 — Criação de `docs/evidence/` REJEITADA (CR-004)

- **Contexto:** a auditoria externa propôs `docs/evidence/` como repositório de evidências de execução/aceite. A proposta criaria uma **segunda source-of-truth** paralela ao painel/índice/canônicos, antes de existirem contrato canônico (D-V0-05) e política de gates/thresholds (D-V0-06). A convergência PO/PM/TL (adendo §8.2) foi de recusa.
- **Decisão:** **rejeitar a criação de `docs/evidence/`** (decisão Classe C, decided_by Lucinei, 2026-11-16). Evidências permanecem **embutidas nos artefatos canônicos** (seções de evidência) ou **referenciadas por link rastreável** a partir do item/decisão. Reavaliação somente junto de D-V0-05/D-V0-06 e por nova decisão humana.
- **Alternativas consideradas:**
  - (a) Criar `docs/evidence/` agora — rejeitada: segunda SoT; sem contrato/gates não há critério do que é evidência canônica.
  - (b) `docs/governance/evidence/` ou similar — rejeitada: mesma classe de problema; estrutura de diretórios indefinida (`[PREMISSA]` pendente de Classe C).
  - (c) Evidências embutidas/por link (escolhida) — consistente com DoD do `docs/20` §DoD ("sem evidência não há `done`") e com o painel.
- **Consequências:** nenhum diretório novo é criado; todo `done`/aceite deve carregar evidência embutida ou link rastreável no próprio artefato; auditorias futuras não podem exigir `docs/evidence/`; risco de evidências dispersas mitigado por rastreabilidade item↔decisão↔evidência (quando tracking existir — DEC-006(vi)).
- **Evidência:** `docs/00` §8.2 (vereditos convergentes PO/PM/TL; recusa registrada); `docs/20` §5 (DoD/change control); decisão do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisão humana de 2026-11-16, Classe C — rejeição).

## DEC-006 — Kickoff D-V0-01/02 (realizado em 2026-11-16): 6 decisões Classe C (decided_by Lucinei, 2026-11-16)

- **Contexto:** lacunas D-V0-01 (stack/repo/infra/CI/gates) e D-V0-02 (stakeholders/capacidade/prazo/cadência/tracking) abertas desde a agregação inicial (`docs/00` §5). Kickoff realizado em 2026-11-16 — ata: `docs/46-ata-kickoff-d-v0-01-02-v0.md`. Todas as 6 decisões abaixo são **Classe C**, decided_by **Lucinei (Mantenedor)**, 2026-11-16:
  1. **D-V0-01 ADIADO** — stack **não** definida; LangGraph permanece **condicional** (canônicos 41–45, DEC-003); implementação **não iniciada**.
  2. **Repositório-alvo** da implementação futura = **este mesmo repositório** (`sdlc-agentico`).
  3. **Infra/CI = nenhuma por ora.** Quando houver, será de baixo risco (F0–F1); repo permanece **sem remote configurado**.
  4. **Stakeholders/capacidade = Mantenedor único (Lucinei).** Não há sponsor/operador externo, não há equipe.
  5. **Cadência = sob demanda; sem SLA formal** — **substitui** a `[PREMISSA-P1]` quinzenal do plano I1 (`docs/20` §6/Premissas). Nenhuma cadência quinzenal está vigente.
  6. **Tracking = nenhuma ferramenta externa; `docs/` é a trilha** de rastreabilidade (sem board/issue tracker; IDs e estados vivem nos canônicos/log).
- **Alternativas consideradas:**
  - (i-a) Definir stack agora (Python/LangGraph/etc.) — rejeitada: o Mantenedor adiou explicitamente; inventar stack violaria as regras do repo e o D-V0-01.
  - (ii-a) Repositório-alvo separado para implementação — rejeitada: o alvo é este repo.
  - (iii-a) CI mínima agora (lint/markdown) — rejeitada: nenhuma por ora; repo é docs-only; sem remote, CI não se aplica hoje.
  - (iv-a) Declarar sponsor/operador externo ou equipe mínima — rejeitada: Mantenedor único.
  - (v-a) Manter premissa quinzenal do I1 — rejeitada: substituída por "sob demanda, sem SLA formal".
  - (vi-a) Adotar GitHub Projects/Jira/similar — rejeitada: `docs/` é a trilha; nenhuma ferramenta externa.
- **Consequências:**
  - `[PREMISSA-P1]` quinzenal (`docs/20`) está **formalmente substituída** por DEC-006(v); `docs/20` não foi editado nesta sessão (restrição de escopo) — ver "Propagação pendente".
  - Sem SLA de decisão/aceite: riscos R4 (capacidade) e R6 (dependências) de `docs/20` permanecem abertos, com mitigação = decisão do Mantenedor único sob demanda; **não prometer prazo sem buffer** continua regra vigente.
  - Sem tracking externo: estados/IDs vivem em `docs/`; DoR/DoD dependem de disciplina documental; critério de `completed` e taxonomia de tracking seguem `[LACUNA]` (D-V0-05).
  - Cadência de revisão do RACI (`docs/40`) e checkpoints do semáforo ficam **sob demanda**.
  - **A publicação do baseline v0 NÃO é desbloqueada por esta decisão** — permanece bloqueada por D-V0-03/04/05/06 (ver DEC-008 e "Decisões pendentes").
- **Evidência:** ata `docs/46-ata-kickoff-d-v0-01-02-v0.md`; sessão de 2026-11-16 (esta sessão); `docs/00` §5 (D-V0-01/02 originais) e §8.2; decisão do Mantenedor em 2026-11-16.
- **Status final:** **vigente** (decisões humanas de 2026-11-16, Classe C — 6 pontos).

## DEC-007 — Política de segredos permanece `[LACUNA]`; reavaliar após D-V0-01 (CR-011)

- **Contexto:** a fila de CRs pós-auditoria (`docs/00` §8.2) inclui política de segredos. Sem stack/infra/repo-alvo de código definidos (D-V0-01 adiado — DEC-006(i)), não há o que escanear, rotacionar ou isolar; fixar política agora seria inventar contexto.
- **Decisão (registro, não aprovação):** nenhuma política de segredos é adotada. Permanece **`[LACUNA]`**. **Gatilho de reavaliação: decisão futura de D-V0-01** (quando a stack for definida) ou decisão explícita do Mantenedor, o que ocorrer primeiro.
- **Alternativas consideradas:**
  - (a) Adotar já `.env.example` + secret scanning + rotação — rejeitada: sem stack/código; teatro de segurança sem alvo.
  - (b) Declarar "não há segredos neste repo" como política — rejeitada sem decisão Classe C; e a afirmação seria frágil (credenciais locais/futuro código).
  - (c) `[LACUNA]` com gatilho explícito (escolhida).
- **Consequências:** risco residual registrado (segredo commitado por engano permanece possível — mitigação atual: revisão humana em todo commit, linha 12 do `docs/40`); nenhum controle automatizado existe hoje; a decisão definitiva exige Classe C quando D-V0-01 ocorrer.
- **Evidência:** `docs/00` §8.2 (fila de CRs, CR-011); DEC-006(i); `docs/40` linha 12.
- **Status final:** **registrado — `[LACUNA]` aberta** (Classe B — registro; **não** é decisão de aprovação; nenhuma política em vigor).

## DEC-008 — Reconciliação do baseline v0 planejada (CR-013); publicação bloqueada (Classe B — planejamento)

- **Contexto:** PO/PM/TL produziram entregáveis paralelos nunca reconciliados formalmente. Divergências conhecidas (`docs/00` §4): roadmap F0–F2/I1–I2 (PM) × F0–F5 (TL) × M1–M3/E1–E4 (PO); `schema_version 0.1.0-draft` (designs) × contrato v1.0.0 proposto (D-V0-05); cadência `[PREMISSA-P1]` quinzenal × "sob demanda" (DEC-006(v)); CR de inclusão de 41–45 (resolvido condicionalmente por DEC-003). CR-013 aberto; **roadmap único em elaboração em `docs/47`** (`docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md`, criado em 2026-11-16 por sessão `tech-lead` concorrente a esta — proposta documental condicional, status `condicional`; **não criado nem editado nesta sessão**, fora do escopo).
- **Decisão (planejamento, não aprovação):** a reconciliação do baseline v0 será executada via **roadmap único (`docs/47`, em elaboração)**, unificando trilhas PO/PM/TL, contrato canônico e taxonomia de estados. **A publicação do baseline canônico permanece BLOQUEADA por D-V0-03 (aceite do PO), D-V0-04 (baseline técnica + ADRs), D-V0-05 (contrato v1.0.0) e D-V0-06 (gates/thresholds).** Esta entrada não aprova, não publica e não promove nada.
- **Alternativas consideradas:**
  - (a) Publicar o baseline v0 agora como "vigente/canônico" — rejeitada: sem D-V0-03/04/05/06 e sem reconciliação, violaria as regras duras do repo (Classe C; execução ≠ `approved`).
  - (b) Manter indefinição sem plano — rejeitada: CR-013 existe; divergências exigem unificação, não silêncio.
  - (c) Reconciliação incremental, arquivo a arquivo, sem roadmap único — rejeitada: as divergências são transversais (roadmap × contrato × cadência); exigem visão única.
- **Consequências:** nenhum baseline é publicado por este registro; `docs/47` será o artefato de planejamento da reconciliação; ao concluir, a publicação exigirá decisões Classe C (D-V0-03/04/05/06) registradas neste log como DEC-009+ (ou adendo explícito); até lá, todos os canônicos permanecem `condicional`/`partial` conforme seus front matters (exceto DEC-001…DEC-006, que são decisões Classe C vigentes).
- **Evidência:** `docs/00` §4 (pontos a reconciliar), §5 (decisões pendentes), §7 (ordem recomendada), §8.1/§8.2 (adendos e fila de CRs); CR-013; DEC-003; DEC-006.
- **Status final:** **registrado — planejamento** (Classe B; publicação **bloqueada**; nenhuma aprovação inferida).

---

## DEC-009 — Pauta D-V0-03: Aceite do PO sobre visão, escopo MVP (M1–M3), semântica de estados e metas/KPIs iniciais (Classe C — pauta; proposta do trio 2026-11-16)

- **Contexto:** D-V0-03 (painel `docs/00` §5) exige aceite do PO sobre visão, escopo MVP (M1–M3), semântica de estados e metas/KPIs iniciais. É decisão de **valor (Classe C no efeito de aceite)** — exclusiva do PO; nenhum agente pode inferir `approved`. Registrada como pauta despachável no MU-0.2 (F-ÚNICO-0) para o Mantenedor.
- **Decisão (pauta, não execução):** submeter o pacote de visão/MVP/estados/KPIs (`docs/10-produto-po-visao-mvp-baseline-v0.md` + revisão PO dos designs t1–t5) à decisão do Mantenedor/PO. **Status: aguardando decisão do Mantenedor.** Nenhum `approved` é declarado por este registro.
- **Decisão Recomendada (proposta do trio, 2026-11-16):** **Sim** — aceitar a proposta do PO (visão/MVP/estados/KPIs) condicionada ao modo documental (sem código) e à resolução das lacunas (handoff PR→aceite PO, AC Given/When/Then, KPIs instrumentáveis). Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).
- **Evidência:** `docs/10-*` §1–§4; `docs/00` §5 (D-V0-03); `docs/47` (F-ÚNICO-1 depende de D-V0-03); revisão PO `ses_e1b33e791ffeK0gwIR9QY7Y7z5` (5× `concordo_com_ressalvas`); proposta PO (gerente-produto, 2026-11-16): DEC-009 Sim + DEC-011 Sim + D-V0-01 manter adiada + F-ÚNICO-1 modo documental; critérios mínimos de aceite (Given/When/Then) e KPIs iniciais (conformidade de resumo ≥95%, clareza de evidência 100%, distinção de estados 0 ocorrências, lead time [LACUNA], taxa de retrabalho decrescente, visibilidade de lacunas 100%).
- **Ressalvas dos gestores:** PO — no-go para aceite/implementação até D-V0-03; PM — consenso condicional, divergência residual de ritmo; TL — consenso condicional de substância.
- **Status final:** **[RESOLVIDO-PROPOSTA]** (Classe C — pauta; proposta emitida pelos 3 gestores; nenhuma aprovação inferida; aguardando decisão do Mantenedor).

## DEC-010 — Pauta D-V0-04: Aprovação da baseline técnica e ADRs iniciais (A–G) + convenção/numeração canônica de ADRs (Classe C — pauta; proposta do trio 2026-11-16)

- **Contexto:** D-V0-04 (painel `docs/00` §5) exige aprovação da baseline técnica e dos ADRs iniciais (A–G) e da convenção/numeração canônica de ADRs. `adr_ref="none"` hoje; nenhum ADR numerado. Decisão de **arquitetura/governança técnica (Classe C)**.
- **Decisão (pauta, não execução):** submeter a baseline técnica proposta (`docs/30-arquitetura-tech-lead-baseline-v0.md` — ADRs A–G propostos, sem número) e a convenção `docs/adr/core/ADR-<NNN>-<slug>.md` (proposta) à decisão do Mantenedor. **Status: aguardando decisão do Mantenedor.** Nenhum ADR é numerado/promovido por este registro.
- **Decisão Recomendada (proposta do trio, 2026-11-16):** **Sim** — aprovar a baseline técnica documental + ADRs A–G propostos + convenção sem números (adr_ref="none"), com estrutura técnica neutra e human_review único escritor técnico de `approved`. Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).
- **Evidência:** `docs/30-*` (ADRs A–G, `adr_ref="none"`); `docs/00` §5 (D-V0-04); CR-006 no log; `docs/47` (F-ÚNICO-1 depende de D-V0-04); proposta PM (gerente-projeto, 2026-11-16): DEC-010 Sim (baseline técnica documental + ADRs A–G proposed + convenção sem números) + impacto cronograma/riscos F-ÚNICO-1 + mediação de trade-off; proposta TL (tech-lead, 2026-11-16): DEC-012 Sim + estrutura técnica de ADRs neutra (convenção sem números, adr_ref="none", human_review único escritor técnico de approved, aceite de valor do PO).
- **Ressalvas dos gestores:** PM — R8 reavaliado (M×A Alto, mitigação ativa), R10/R11 mitigados; TL — consenso condicional de substância; PO — aceite de valor reservado ao PO.
- **Status final:** **[RESOLVIDO-PROPOSTA]** (Classe C — pauta; proposta emitida pelos 3 gestores; nenhuma aprovação inferida; aguardando decisão do Mantenedor).

## DEC-011 — Pauta D-V0-05: Consolidação do contrato canônico v1.0.0 (resumo + envelope + estados + correlação + `schema_version`) (Classe C — pauta; proposta do trio 2026-11-16)

- **Contexto:** D-V0-05 (painel `docs/00` §5) exige consolidação do contrato canônico v1.0.0 (resumo + envelope + estados + correlação + `schema_version`) e da taxonomia operacional (`completed`/tracking). Proposta em `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (status `condicional`); adoção exige Classe C (CR-007-C).
- **Decisão (pauta, não execução):** submeter o Contrato Canônico v1.0.0-PROPOSTA (`docs/48`) à decisão do Mantenedor (+PO+PM). **Status: aguardando decisão do Mantenedor.** Nada aqui tem efeito normativo até lá; `0.1.0-draft` permanece vigente nos designs.
- **Decisão Recomendada (proposta do trio, 2026-11-16):** **Sim** — adotar o contrato v1.0.0 (resumo + envelope + estados + correlação + `schema_version`), com migração aditiva de `0.1.0-draft` e `completed`≠`approved`. Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).
- **Evidência:** `docs/48-*`; `docs/47` §(vi) (migração aditiva); `docs/00` §5 (D-V0-05); `docs/30-*` §Contratos; CR-007-C no log; proposta PO (gerente-produto, 2026-11-16): DEC-011 Sim (adoção contrato v1.0.0) + AC Given/When/Then + KPIs iniciais; proposta TL (tech-lead, 2026-11-16): DEC-012 Sim (política unificada de gates/evidência/thresholds) + contrato canônico v1.0.0.
- **Ressalvas dos gestores:** PO — KPIs iniciais e AC Given/When/Then; TL — "no new errors" sobre baseline declarada, G0–G3, exit_code 6 fail-closed; PM — consenso condicional, divergência residual de ritmo.
- **Status final:** **[RESOLVIDO-PROPOSTA]** (Classe C — pauta; proposta emitida pelos 3 gestores; nenhuma aprovação inferida; aguardando decisão do Mantenedor).

## DEC-012 — Pauta D-V0-06: Política unificada de gates/evidência e thresholds (lidos do projeto-alvo) (Classe C — pauta; proposta do trio 2026-11-16)

- **Contexto:** D-V0-06 (painel `docs/00` §5) exige política unificada de gates/evidência e thresholds (ex.: cobertura) lidos do projeto-alvo quando aplicável. Proposta em `docs/30-*` (gates G0–G3) e `docs/42-*` (mapeamento gates↔Makefile, exit_code 6 fail-closed). Evitar hardcode; "no new errors" sobre baseline declarada. Decisão de **qualidade (Classe C)**.
- **Decisão (pauta, não execução):** submeter a política de gates unificada (G0–G3 × exit_code → AgentState, thresholds lidos do alvo) à decisão do Mantenedor (+TL/PM/PO). **Status: aguardando decisão do Mantenedor.** Nenhum gate é adotado nem threshold fixado por este registro.
- **Decisão Recomendada (proposta do trio, 2026-11-16):** **Sim** — adotar a política unificada de gates/evidência/thresholds parametrizada ("no new errors" sobre baseline declarada, G0–G3, exit_code 6 fail-closed, thresholds lidos do projeto-alvo). Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).
- **Evidência:** `docs/30-*` §Qualidade e Gates; `docs/42-*` §2 (exit_code 6); `docs/48-*` §(v); `docs/00` §5 (D-V0-06); CR-008-C no log; proposta TL (tech-lead, 2026-11-16): DEC-012 Sim (política unificada de gates/evidência/thresholds parametrizada, "no new errors" sobre baseline declarada, G0–G3, exit_code 6 fail-closed) + estrutura técnica de ADRs neutra; proposta PM (gerente-projeto, 2026-11-16): trilha TL (schemas offline), trilha PO (AC/KPIs/handoff), trilha PM (R8/R10/R11), gatilho de implementação.
- **Ressalvas dos gestores:** TL — consenso condicional de substância com PO/PM; PM — R8 reavaliado (M×A Alto, mitigação ativa), R10/R11 mitigados; PO — critérios mínimos de aceite (Given/When/Then) e KPIs iniciais.
- **Status final:** **[RESOLVIDO-PROPOSTA]** (Classe C — pauta; proposta emitida pelos 3 gestores; nenhuma aprovação inferida; aguardando decisão do Mantenedor).

## DEC-013 — Registro de reconciliação MU-0.3 concluída (propagação documental + pautas DEC-009+) (Classe B — registro)

- **Contexto:** F-ÚNICO-0/MU-0.2+MU-0.3 (propagação documental e registro de pautas Classe C) executado em 2026-11-16 pelo `gerente-projeto`, consolidando a reconciliação documental do baseline v0 sem tocar em `docs/10/30/47/48` (já reconciliados) e sem criar `docs/evidence/` ou numerar ADRs.
- **Decisão (registro, Classe B):** registrar a conclusão de MU-0.3 com evidências verificáveis. Arquivos editados neste change set:
  1. `docs/20-governanca-pm-plano-baseline-v0.md` — bloco §0 (mapeamento F0–F2 → F-ÚNICO-0/1/2); `[PREMISSA-P1]` marcada substituída por DEC-006(v); cadência "sob demanda, sem SLA" registrada (§3); normativos externos por caminho+sha256 completo; `docs/evidence/` rejeitado (DEC-005); status honesto `partial/condicional`.
  2. `docs/40-operacao-raci-repo-v0.md` — front matter `vigente` (DEC-002) + linha de evidência; matriz RACI inalterada.
  3. `docs/README.md` — índice atualizado (entradas 46/47/48/DECISIONS; contagem `00–48` + DECISIONS + 46; data 2026-11-16); DIV-6 fechado.
  4. `docs/00-painel-gerencial-consolidado.md` — §8 (subagents tech-lead/gerente-produto reconciliação; lacunas_consolidadas atualizadas; proxima_acao; adendo §8.4).
  5. `docs/DECISIONS.md` — DEC-009…DEC-013 adicionados; tabela-resumo e "Propagação pendente" atualizados.
- **Não editados (já reconciliados):** `docs/10`, `docs/30`, `docs/47`, `docs/48`.
- **Não criados:** `docs/evidence/` (DEC-005); nenhum ADR numerado; nenhuma promoção a `approved`/`completed`.
- **Evidências (verificáveis):**
  - Normativos externos pinados (DEC-003), verificados via `sha256sum` em 2026-11-16:
    - `~/.opencode/references/contrato-resumo-subagentes.md` → `163e0aad7654d0a60930e90388afa9b9474ee727f119e94a62337d8321442a60`
    - `~/.opencode/references/autonomia-e-estados.md` → `776af494ee702cf4d3db8837f2b1c0c23450844f9b54e376a052d7adbc42c78a`
  - `git status` pré-commit: modificações em `docs/10`, `docs/20`, `docs/30`, `docs/40`, `docs/47`, `docs/48` + novos em `docs/00`, `docs/README.md`, `docs/DECISIONS.md`.
  - Nenhuma promoção a `approved`/`completed`: status permanece `condicional`/`partial` em todos os canônicos (exceto DEC-001…DEC-006 vigentes e `docs/40` vigente por DEC-002).
- **Alternativas consideradas:** (a) editar 10/30/47/48 — rejeitada (já reconciliados; fora do escopo); (b) criar `docs/evidence/` — rejeitada (DEC-005); (c) numerar ADRs — rejeitada (D-V0-04 pendente).
- **Consequências:** reconciliação MU-0.3 concluída e registrada; pautas D-V0-03/04/05/06 despachadas como DEC-009…DEC-012 (aguardando decisão do Mantenedor); baseline v0 permanece não publicado (DEC-008/CR-013-publicação bloqueada); DIV-6 fechado.
- **Status final:** **registrado — concluído (MU-0.3)** (Classe B — registro; nenhuma aprovação inferida).

---
## DEC-014 — Registro de grill-with-docs (pendências bloqueantes PM) e propostas de resolução (Classe B — registro)

- **Contexto:** sessão `sdlc-agentico-pm-pendencias-bloqueantes` (gerente-projeto, 2026-11-16) consolidou as pendências bloqueantes da especialidade PM: D-V0-01 (restante: infra/CI/gates), D-V0-02 (restante: orçamento formal e cadência de revisão RACI), roadmap F-ÚNICO, riscos, cronograma de 1 semana e tracking em `docs/`. Aplicou grill-with-docs em 2 rodadas × 3 perguntas para lacunas de peso 5 (orçamento formal, cadência de revisão RACI, timing do kickoff D-V0-01). **Nenhuma decisão Classe C final foi tomada; nenhuma promoção a `approved`/`completed`; nenhum ADR numerado; nenhum diretório criado.** Materialização de artefatos (cronograma, RACI, riscos) **não** executada — aguarda aprovação explícita do Mantenedor via subagente de escrita (Class B apenas neste registro).
- **Respostas do grill (Mantenedor, 2026-11-16):**
  1. **Orçamento formal:** sem orçamento monetário; MVP sustentado exclusivamente pelo esforço do Mantenedor (40h/semana). → `[PREMISSA-P7]` (operacional): capacidade = 40h/semana do Mantenedor único; nenhum custo externo; não prometer prazo sem buffer.
  2. **Cadência de revisão RACI/checkpoints:** semanal (1x/semana), fixa. → substitui a cadência "sob demanda" (DEC-006(v)) **apenas** para a revisão RACI/checkpoints semanais; demais decisões permanecem sob demanda sem SLA (DEC-006(v) vigente para aceite/decisão).
  3. **Dono da revisão RACI:** PM delegado (R) com aprovação do Mantenedor (A) — consistente com `docs/40` RACI (PM A/R em governança; Mantenedor A em impactos relevantes).
  4. **Timing do kickoff D-V0-01:** **antes da semana 1** (bloqueia MVP até decisão). → F-ÚNICO-1 permanece bloqueada até kickoff concluído; semana 1 não inicia MVP sem kickoff resolvido.
  5. **D-V0-01 para o MVP de 1 semana:** reabrir kickoff de stack/CI antes do MVP (decisão do Mantenedor no grill) — **não** é resolução de D-V0-01 (continua adiado até kickoff); apenas autoriza a reabertura. Requer decisão Classe C formal (D-V0-01) + registro em `docs/DECISIONS.md` como DEC-015+ quando ocorrer.
- **Propostas de resolução (Class B, reversíveis; não aprovadas):**
  - **PR-01 (D-V0-01 restante — infra/CI/gates):** manter D-V0-01 adiado (DEC-006(i)) como baseline; reabrir kickoff antes da semana 1 (conforme grill #4/#5) com escopo mínimo: stack (condicional LangGraph), repo-alvo (este repo — DEC-006(ii)), CI (nenhuma por ora — DEC-006(iii)) e gates (G0–G3 propostos, thresholds lidos do alvo — D-V0-06). Sem kickoff resolvido, F-ÚNICO-1 permanece bloqueada (R8). **Não criar Makefile/pyproject.toml sem decisão Classe C.**
  - **PR-02 (D-V0-02 restante — orçamento formal):** orçamento monetário = zero (grill #1); capacidade = 40h/semana do Mantenedor único; PERT+30% aplicável sobre capacidade confirmada (40h/sem ≈ 8h/dia, 5 dias). Estimativas declaráveis apenas como `[PREMISSA]` com buffer 30%: `E = ((O+4M+P)/6) × 1.3`. **Não prometer prazo sem buffer** (regra vigente).
  - **PR-03 (D-V0-02 restante — cadência de revisão RACI):** revisão RACI/checkpoints **semanal** (grill #2), PM delegado (R) com aprovação do Mantenedor (A) (grill #3). Atualizar `docs/20` §3 e `docs/40` no próximo change set autorizado (propagação pendente). Demais rituais (revisão de backlog/DoR, review de valor/aceite, change control) permanecem sob demanda sem SLA (DEC-006(v)) até nova decisão.
  - **PR-04 (roadmap F-ÚNICO):** manter `docs/47` (proposta condicional) como mapa vigente; F-ÚNICO-0 executável (documental, baixo risco); F-ÚNICO-1 bloqueada até kickoff D-V0-01 + D-V0-03/04/05/06; F-ÚNICO-2 depende de F-ÚNICO-1. Sem PERT declarável para F-ÚNICO-1/2 (depende de D-V0-01/02).
  - **PR-05 (riscos):** manter R1–R11 (`docs/20`) vigentes; reavaliar R8 (D-V0-01 adiado) após kickoff; R4/R10 (capacidade/bus factor) mitigados parcialmente pela confirmação de 40h/sem + cadência semanal; R9 (drift DECISIONS×change control) e R11 (drift 47/48×10/20/30) permanecem abertos até reconciliação. Novo risco registrado: **R12** — "MVP de 1 semana inviável sem kickoff D-V0-01 resolvido (bloqueio ativo)" | A×A (Crítico) | mitigação: kickoff antes da semana 1; modo documental F-ÚNICO-1 | Mantenedor/PM.
  - **PR-06 (cronograma de 1 semana):** condicional ao kickoff D-V0-01 (antes da semana 1). Proposta de 5 dias úteis (40h) com buffer 30% (PERT), modo documental (sem código) até kickoff resolvido:
    | Dia | Atividade | Dono (R) | Aprovador (A) | Est. PERT E (×1.3) |
    |---|---|---|---|---|
    | pré-S1 (D-2…D-1) | Kickoff D-V0-01 (stack/CI/gates) — gate bloqueante | Mantenedor (A/R) | Mantenedor | — (decisão humana) |
    | D1 | Revisão RACI semanal + atualização `docs/40`/`docs/20` §3 | PM (R) | Mantenedor (A) | 0.5d→0.65d |
    | D2 | Consolidação contrato v1.0.0 (proposta) + semântica de estados (PO/PM/TL) | TL (R) | Mantenedor+PO+PM | 1d→1.3d |
    | D3 | Cronograma PERT+30% + DoR/DoD + change control registro | PM (R) | Mantenedor (A) | 1d→1.3d |
    | D4 | Reconciliação `docs/10/20/30` + painel + README + DECISIONS | PM (R) + TL/PO (C) | Mantenedor (A) | 1.5d→1.95d |
    | D5 | Review de valor (PO) + semáforo + checkpoint + riscos | PO (R) + PM (C) | Mantenedor (A) | 0.5d→0.65d |
    - **Total estimado:** ~5.85d equivalente sobre 5d úteis (117% da capacidade) — **sobrecarga**; re-planejar ou reduzir escopo. Marcar `[PREMISSA]` e `[LACUNA]` de capacidade real por dia.
    - **Bloqueio:** se kickoff D-V0-01 não concluído antes da semana 1, toda a semana 1 permanece em F-ÚNICO-0 documental (sem MVP) — R12 ativo.
  - **PR-07 (tracking em `docs/`):** manter `docs/` como trilha (DEC-006(vi)); estados/IDs nos canônicos e no log; critério operacional de `completed` segue `[LACUNA]` (D-V0-05). Cadência de revisão RACI agora semanal (PR-03). Sem board/issue tracker externo.
- **Riscos e premissas:**
  - `[RISCO] R12` (novo) | A×A (Crítico) | MVP de 1 semana inviável sem kickoff D-V0-01 resolvido | mitigação: kickoff antes da semana 1; modo documental F-ÚNICO-1 | Mantenedor/PM
  - `[RISCO] R4/R10` (capacidade/bus factor) | A×M (Alto) | Mantenedor único 40h/sem; cadência semanal pode sobrecarregar | mitigação: reduzir escopo; delegar PM (R) com aprovação (A); re-planejar se total > 100% capacidade | PM/Mantenedor
  - `[RISCO] R9/R11` (drift documental) | M×A (Alto) | DECISIONS×change control; 47/48×10/20/30 | mitigação: propagação pendente registrada; revisão semanal | PM
  - `[PREMISSA-P7]` (nova, operacional) Orcamento monetario = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada; sem custo externo. Teste: capacidade 40h/sem (S08).
  - `[PREMISSA-P8]` (nova, operacional) Cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A). Teste: checkpoint semanal realizado.
  - `[LACUNA]` Capacidade real por dia (não confirmada); total estimado 117% da capacidade (sobrecarga) — re-planejar.
  - `[LACUNA]` Critério operacional de `completed` no tracking alvo (`docs/`) — D-V0-05.
  - `[LACUNA]` Stack/CI/gates (D-V0-01) — kickoff antes da semana 1; não resolvido.
  - `[LACUNA]` Thresholds de gates (D-V0-06) — lidos do projeto-alvo (inexistente).
- **Alternativas consideradas:**
  - (a) Manter D-V0-01 adiado sem kickoff (status quo) — rejeitada pelo Mantenedor no grill (#4/#5); manteria F-ÚNICO-1 bloqueada indefinidamente.
  - (b) Orcamento monetario > 0 — rejeitada pelo Mantenedor no grill (#1); MVP sem custo externo.
  - (c) Cadência "sob demanda" (DEC-006(v)) para RACI — rejeitada pelo Mantenedor no grill (#2); fixar semanal.
  - (d) Materializar cronograma/RACI/riscos como arquivos novos agora — rejeitada: exige aprovação explícita do Mantenedor via subagente de escrita (regra vigente); apenas registro Class B aqui.
  - (e) Marcar DEC-014 como decisão Classe C — rejeitada: este registro é Class B (proposta/reversível); formalização Classe C ocorre quando o Mantenedor confirmar via DEC-015+.
- **Evidência:** grill-with-docs (2 rodadas × 3 perguntas) realizado em 2026-11-16 (respostas do Mantenedor registradas acima); `docs/00` §5/§8; `docs/20` (R1–R11, P1–P6, §3, §6); `docs/40` (RACI, status vigente DEC-002); `docs/47` (F-ÚNICO-0/1/2, bloqueios); `docs/48` (contrato v1.0.0-PROPOSTA); `docs/DECISIONS.md` (DEC-001…DEC-013); AGENTS.md (regras duras); `~/.opencode/references/contrato-resumo-subagentes.md` e `autonomia-e-estados.md` (normativos).
- **Status final:** **registrado — proposta (Class B)** (grill-with-docs concluído; nenhuma aprovação inferida; nenhuma promoção a `approved`/`completed`; materialização de artefatos aguarda aprovação explícita do Mantenedor; propagação para `docs/20` §3, `docs/40`, `docs/00` §8 e `docs/README.md` pendente no próximo change set autorizado).

## DEC-015 — Consolidação PO da pauta D-V0-03 (proposta; Classe B — registro)

- **Contexto:** D-V0-03 (painel `docs/00` §5) exige aceite do PO sobre visão, escopo MVP (M1–M3), semântica de estados e metas/KPIs iniciais. É decisão de **valor (Classe C no efeito de aceite)** — exclusiva do PO; nenhum agente pode inferir `approved`. Este registro consolida a proposta do PO (docs/10 §1–§4 + revisão PO dos designs t1–t5) com as premissas operacionais vigentes (capacidade 40h/semana — DEC-014 [PREMISSA-P7]; prazo 1 semana MVP — DEC-014 PR-06; mantenedor único; tracking = docs/ — DEC-006(vi); cadência sob demanda sem SLA para aceite — DEC-006(v); revisão RACI semanal — DEC-014). **Nenhuma decisão Classe C final é tomada; nenhum `approved`/`completed` é declarado; nenhum ADR numerado; nenhum diretório criado; backlog/visão NÃO materializados (aguarda aprovação explícita do Mantenedor).**

- **Proposta consolidada (Classe B — reversível):**

  1. **Visão** (docs/10 §1): SDLC agêntico previsível, auditável e orientado a valor; execução técnica rastreável ponta a ponta; nenhum resultado tratado como valor entregue sem aceite explícito do PO. (Sem alteração de substância.)
  2. **MVP (MoSCoW + WSJF)** (docs/10 §2): Must = M1 (contrato canônico de resumo + validação), M2 (semântica canônica de estados), M3 (fluxo de aceite de valor PO). Should = S1 (rastreabilidade ponta a ponta), S2 (dashboard). Could = C1 (métricas automatizadas), C2 (catálogo de templates). Won't (MVP) = W1 (automação avançada cross-agente). WSJF: M2=13,0 (maior), M1=7,8, M3=6,8. MoSCoW Must = exatamente 3 itens (sem exceção), conforme docs/10.
  3. **Backlog (épicos/histórias)** (docs/10 §2): E1 (Must, M1) H1.1–H1.3; E2 (Must, M2) H2.1–H2.2; E3 (Must, M3) H3.1–H3.3; E4 (Should, S1) H4.1. **Modo documental (F-ÚNICO-0) em 1 semana:** E1+E2+E3 cabem como refinamento documental; E4 (H4.1) adiado para F-ÚNICO-2 (depende de IDs correlacionáveis — [LACUNA]).
  4. **Semântica de estados** (docs/10 §3, docs/48 §iii/iv): três camadas — execução (`done/blocked/partial`), operação (`completed`), valor (`pending/approved/rejected`). `done` ⇏ `completed` ⇏ `approved`; `approved` terminal, exclusivo do PO, exige `evidence`+`decided_by`+`decided_at`; agente nunca escreve `approved`. Critério operacional proposto de `completed` = "item executado (resumo `done` com evidência) + gates aplicáveis da fase atendidos + registro de conclusão no sistema operacional de tracking, com rastreio explícito" — semântica aceita como conceitual; ferramenta exata permanece [LACUNA] (tracking = docs/, sem board/tool — DEC-006(vi)/D-V0-05).
  5. **KPIs mensuráveis em 1 semana (tracking=docs/, sem infra externa)** (docs/10 §4, calibrados para 40h/sem):
     - KPI-1 Conformidade de resumo ≥95% — mensurável por auditoria manual de resumos em 1 semana (gate binário).
     - KPI-2 Clareza de evidência 100% (gate) — mensurável por auditoria.
     - KPI-3 Distinção de estados preservada = 0 ocorrências de `done/completed` tratado como `approved` sem decisão do PO — mensurável por revisão.
     - KPI-4 Lead time até decisão do PO — parcialmente mensurável (requer registro de datas; [LACUNA] baseline); meta inicial [LACUNA] (sem SLA — DEC-006(v)); calibrar após 2 iterações.
     - KPI-5 Taxa de retrabalho pós-decisão — NÃO mensurável em 1 semana (tendência); adiado para F-ÚNICO-2.
     - KPI-6 Visibilidade de lacunas 100% em casos aplicáveis — mensurável por auditoria.
     - Metas de 1 semana (gates binários): KPI-1, KPI-2, KPI-3, KPI-6. KPI-4 e KPI-5 permanecem [LACUNA] com tracking manual.
  6. **Aceite de valor (Decision/Acceptance v0)** (docs/10 §3.3, docs/48): `pending|approved|rejected`; `approved` terminal, exige `evidence`+`decided_by=PO`+`decided_at`; `rejected` exige `rationale`; `rejected→pending` somente com nova evidência. Handoff PR→aceite PO inexistente (lacuna da revisão PO) — registrado como [LACUNA] a materializar em F-ÚNICO-1 (não bloqueia a proposta).
  7. **Mecanismo de feedback/aceite (MVP)** (docs/10 §4): pronto para aceite (done+evidência+critérios) → orquestrador marca "valor pendente de aceite do PO" → PO valida Given/When/Then + evidências → decisão registrada → se rejected, rationale acionável + condição de nova submissão → revisão periódica de rejeições/lacunas/conformidade.

- **Grill-with-docs aplicado (2 rodadas × 3 perguntas, lacunas de peso 5):**
  - Rodada 1:
    - Q1 (KPIs mensuráveis): Quais dos 6 KPIs são mensuráveis em 1 semana com tracking=docs/? → Resposta: KPI-1/2/3/6 mensuráveis por auditoria manual; KPI-4 parcial; KPI-5 não mensurável em 1 semana. Ação: metas de 1 semana = KPI-1/2/3/6 como gates binários; KPI-4/5 = [LACUNA] com tracking manual, calibrar em F-ÚNICO-2.
    - Q2 (semântica de estados): O critério operacional proposto de `completed` deve ser aceito como canônico ou permanecer [LACUNA]? → Resposta: aceitar a semântica conceitual; ferramenta exata permanece [LACUNA] (tracking=docs/, sem board/tool; D-V0-05). Não promover baseline sem D-V0-05.
    - Q3 (handoff PR→aceite): O pacote mínimo de evidência é suficiente ou falta o handoff? → Resposta: lacuna confirmada (revisão PO ses_e1b33e791ffeK0gwIR9QY7Y7z5: handoff PR→aceite PO inexistente; AC Given/When/Then ausentes nos designs; KPIs não instrumentáveis). Ação: adicionar à DoR de H3.1/H3.2 o campo "handoff: PR/entrega → pacote de evidência → fila de aceite do PO" como [LACUNA] a materializar em F-ÚNICO-1. Não bloqueia a proposta de valor.
  - Rodada 2:
    - Q4 (capacidade/backlog): Com 40h/sem e 1 semana (modo documental, sem código), quais histórias cabem? → Resposta: E1+E2+E3 cabem como refinamento documental (≈3d/24h com buffer 30% sobre 40h); E4 (H4.1) adiado para F-ÚNICO-2. Estimativa PERT: 40h = 5d×8h; buffer 30% ⇒ ~30h úteis.
    - Q5 (rastreabilidade): E4/H4.1 pode entrar no MVP de 1 semana sem IDs correlacionáveis? → Resposta: Não. Manter E4 como Should (S1); [LACUNA] "identificadores correlacionáveis e storage de trilha" registrada. E4 entra em F-ÚNICO-2.
    - Q6 (cadência de aceite): Lead time viável com mantenedor único + revisão semanal? → Resposta: lead time KPI-4 permanece [LACUNA] (sem SLA de decisão — DEC-006(v) para aceite; revisão semanal cobre RACI/checkpoints, não aceite). Proposta: medir em dias entre "pronto para aceite" e decisão; meta inicial [LACUNA] a calibrar após 2 iterações. Risco R7 mitigado por pacote mínimo de evidência + cadência sob demanda.

- **Lacunas persistentes (registradas, não resolvidas silenciosamente):**
  - [LACUNA] D-V0-01 adiado (DEC-006(i)): stack/CI/repo-alvo indefinidos ⇒ F-ÚNICO-1 bloqueada; implementação não iniciada; MVP de 1 semana = modo documental (F-ÚNICO-0).
  - [LACUNA] D-V0-03 pendente (Classe C): este registro é proposta, não aceite; `approved` exclusivo do PO com evidência.
  - [LACUNA] D-V0-04 pendente (Classe C): baseline técnica/ADRs A–G sem número; `adr_ref="none"`.
  - [LACUNA] D-V0-05 pendente (Classe C): contrato v1.0.0 não adotado; `0.1.0-draft` vigente nos designs.
  - [LACUNA] D-V0-06 pendente (Classe C): política de gates/thresholds; "no new errors" sem baseline.
  - [LACUNA] Handoff PR→aceite PO inexistente (revisão PO); AC Given/When/Then ausentes nos designs t1–t5.
  - [LACUNA] KPIs não instrumentáveis (revisão PO); métricas baseline inexistentes.
  - [LACUNA] Identificadores correlacionáveis e storage de trilha/evidências/decisões (E4 adiado).
  - [LACUNA] Critério operacional exato de `completed` no tracking alvo (docs/ como trilha, sem board/tool).
  - [LACUNA] Capacidade real por dia (total estimado 117% da capacidade — sobrecarga; re-planejar).
  - [LACUNA] DEC-007 (política de segredos) permanece [LACUNA] aberta.

- **Conflitos registrados (não resolvidos silenciosamente):**
  - DIV-1 (roadmap PM F0–F2 × TL F0–F5 × PO M1–M3) — mapa em docs/47 §1; em andamento.
  - DIV-2 (`schema_version 0.1.0-draft` × v1.0.0) — proposta em docs/48; em andamento.
  - Divergência revisão PO: KPIs não instrumentáveis / AC ausentes nos designs — registrada como [LACUNA], não resolvida.

- **Premissas operacionais (vigentes, com teste correspondente):**
  - P1: MVP M1–M3 entregue em 1 semana com 40h/sem — teste: escopo documental (F-ÚNICO-0) cabe em 5d×8h com buffer 30% (~30h úteis); F-ÚNICO-1 bloqueada por D-V0-01 (R8) — não prometer código.
  - P2: KPIs mensuráveis sem infra externa (docs/) — teste: KPI-1/2/3/6 auditáveis manualmente em 1 semana; KPI-4/5 [LACUNA].
  - [PREMISSA-P7] (DEC-014): orçamento monetário = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada.
  - [PREMISSA-P8] (DEC-014): cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A).

- **Riscos de produto (vigentes):** R1 (ambiguidade contratual), R2 (rastreabilidade), R4 (capacidade), R7 (gargalo de aceite PO), R8 (D-V0-01 adiado ⇒ F-ÚNICO-1 bloqueada), R10 (bus factor 1), R11 (drift documental), R12 (MVP de 1 semana inviável sem kickoff D-V0-01 — Crítico).

- **Alternativas consideradas:**
  - (a) Declarar D-V0-03 aprovado agora — rejeitada: viola regra dura (aceite de valor é Classe C, exclusivo do PO, com evidência; nenhum agente infere `approved`).
  - (b) Materializar backlog/visão em arquivos novos (docs/product/*) — rejeitada: exige aprovação explícita do Mantenedor via subagente de escrita; não concedida.
  - (c) Promover ADR/baseline — rejeitada: D-V0-04 pendente (Classe C).
  - (d) Resolver lacunas de peso 5 silenciosamente — rejeitada: regra R2/R8; registradas como [LACUNA].
  - (e) Criar diretórios/ADRs numerados — rejeitada: sem decisão Classe C (AGENTS.md regra dura).

- **Consequências:** proposta consolidada e registrada (Classe B, reversível); nenhuma promoção a `approved`/`completed`; D-V0-03 permanece pendente (Classe C) aguardando decisão do Mantenedor; backlog/visão permanecem não materializados; publicação do baseline bloqueada (DEC-008/CR-013-publicação); baseline v0 permanece `condicional`/não pronta.

- **Decisão Recomendada (proposta do PO, 2026-11-16):** **Sim** — aceitar a proposta consolidada (visão/MVP M1–M3, semântica de estados, KPIs mensuráveis em 1 semana como gates binários KPI-1/2/3/6, aceite de valor, backlog E1–E4 com E4 adiado) condicionada ao modo documental (sem código) até D-V0-01 resolvido, com resolução das lacunas registradas (handoff PR→aceite, AC Given/When/Then, KPIs instrumentáveis, IDs correlacionáveis). Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).

- **Ressalvas:** PO — no-go para aceite/implementação até D-V0-03/04/05/06; PM — consenso condicional, divergência residual de ritmo; TL — consenso condicional de substância. Aceite de valor permanece exclusivo do PO.

- **Evidência:** `docs/10-*` §1–§4; `docs/00` §5/§8 (D-V0-03; revisão PO ses_e1b33e791ffeK0gwIR9QY7Y7z5); `docs/20-*` (R1–R11, P1–P6, PR-01…PR-07); `docs/30-*` (ADRs A–G, gates G0–G3); `docs/47-*` (F-ÚNICO-0/1/2, bloqueios, DIV-1/2); `docs/48-*` (semântica de estados, critério de `completed`, exit codes); `docs/DECISIONS.md` (DEC-001…DEC-014); `docs/README.md`; AGENTS.md (regras duras); `~/.opencode/references/contrato-resumo-subagentes.md` (sha256 `163e0aad…`); `~/.opencode/references/autonomia-e-estados.md` (sha256 `776af494…`); grill-with-docs 2×3 (respostas registradas acima).

- **Status final:** **registrado — proposta (Classe B)** (consolidação PO de D-V0-03; nenhuma aprovação inferida; nenhuma promoção a `approved`/`completed`; materialização de backlog/visão aguarda aprovação explícita do Mantenedor via subagente de escrita; propagação para `docs/10`/`docs/00`/`docs/README.md` pendente no próximo change set autorizado).

## DEC-016 — Consolidação TL das pautas D-V0-04/05/06, CR-008-C, CR-009-C, arquitetura e dívida técnica (proposta; Classe B — registro)

- **Contexto:** pendências bloqueantes da especialidade TL: D-V0-04 (aprovação da baseline técnica e ADRs iniciais A–G + convenção/numeração canônica de ADRs), D-V0-05 (consolidação do contrato canônico v1.0.0), D-V0-06 (política unificada de gates/evidência/thresholds), CR-008-C (unificação de gates), CR-009-C (LangGraph — dormente, condicional a D-V0-01), arquitetura (dispatcher+agregador, SoT/event-log, idempotência, contratos versionados, estados/autonomia A/B/C, qualidade incremental, observabilidade/segurança) e dívida técnica. Aplicou-se grill-with-docs em 2 rodadas × 3 perguntas para lacunas de peso 5 (numeração ADR, thresholds, convenção ADR, dívida documental, CR-008-C). **Nenhuma decisão Classe C final foi tomada; nenhuma promoção a `approved`/`completed`; nenhum ADR numerado; nenhum diretório/Makefile/pyproject.toml criado.** Materialização de artefatos (ADRs numerados, contrato adotado, Makefile, pyproject.toml) **não** executada — aguarda aprovação explícita do Mantenedor via subagente de escrita (Classe B apenas neste registro).

- **Respostas do grill (Mantenedor, 2026-11-16):**
  - Rodada 1:
    1. **Numeração ADR:** reiniciar local (ADR-001…) — namespace isolado ao repo `sdlc-agentico`; citação por caminho (ADR-009) evita ambiguidade prática. NÃO continuar da árvore compartilhada (019+).
    2. **Thresholds:** `[LACUNA]` + parametrização (fail-closed, exit_code 6) até o projeto-alvo existir; thresholds lidos do `pyproject.toml` do projeto-alvo quando existir; "no new errors" sobre baseline declarada. NÃO adotar default conservador hardcoded.
    3. **Kickoff D-V0-01:** reabrir antes da semana 1 (conforme DEC-014) com escopo mínimo (stack condicional LangGraph, repo-alvo este repo, CI nenhuma, gates G0–G3 propostos). LangGraph permanece condicional até decisão formal de D-V0-01; F-ÚNICO-1 bloqueada até kickoff + D-V0-03/04/05/06.
  - Rodada 2:
    4. **Convenção ADR:** confirmada conforme `docs/30` — status `proposed|accepted|superseded|rejected`, data, contexto, decisão, alternativas, trade-offs, consequências, evidências; slug kebab-case.
    5. **Dívida técnica:** registrada como dívida documental (drift, lacunas, riscos R1–R12) em `docs/DECISIONS.md`; sem backlog separado (tracking = `docs/`). Criar `docs/tech/debt.md` exigiria decisão Classe C (estrutura de diretórios pendente).
    6. **CR-008-C:** unificação feita agora (documental) — G0–G3 × exit_code → AgentState × contrato v1.0.0 registrada como proposta (Classe B); materialização (Makefile) somente após D-V0-06 decidida + projeto-alvo existente.

- **Proposta consolidada (Classe B, reversível):**

  1. **ADRs A–G (D-V0-04):** manter como proposta (`status: proposed`), **sem número atribuído**, até D-V0-04 decidida. Convenção canônica (proposta): `docs/adr/core/ADR-<NNN>-<slug-kebab>.md`, **numeração local reiniciando em ADR-001** (namespace isolado ao repo; citação por caminho conforme ADR-009 do ecossistema); status `proposed|accepted|superseded|rejected`; campos: data, contexto, decisão, alternativas consideradas, trade-offs, consequências, evidências. **Sem criar diretório `docs/adr/` nem ADRs numerados sem decisão Classe C** (AGENTS.md regra dura; DEC-008 bloqueia publicação). Atribuição de `adr_ref` permanece `none` até D-V0-04.
  2. **Contrato canônico v1.0.0 (D-V0-05):** manter `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` como proposta até D-V0-05 decidida. Migração aditiva `0.1.0-draft → 1.0.0` (sem remoção/re-tipagem de campos; minor aditivo; major exige migração explícita). `completed` ≠ `approved`; `approved` terminal e exclusivo do PO (com `evidence` + `decided_by` + `decided_at`); agente nunca escreve `approved`. Sem efeito normativo até adoção (Classe C). `machine_readable.schema_version` ("1.0") × `schema_version` de contrato ("1.0.0") permanece decisão de D-V0-05.
  3. **Gates (D-V0-06 + CR-008-C):** política unificada registrada como proposta (Classe B, agora): G0 (schema/contrato, lint/format de artefatos normativos, checagem de links/paths), G1 (testes do núcleo + smoke dispatcher→agregação + correlação/lineage), G2 (cobertura mínima lida do `pyproject.toml` do projeto-alvo + análise estática/tipos + SAST básico + SLOs), G3 (performance/carga se aplicável + revisão de ADRs + auditoria periódica) × `exit_code → AgentState` (docs/42 §2, incluindo linha 6 fail-closed) × contrato v1.0.0 (docs/48 §v). Thresholds: `[LACUNA]` + parametrização (fail-closed, exit_code 6) até o projeto-alvo existir; "no new errors" sobre baseline declarada; thresholds numéricos lidos do `pyproject.toml` do projeto-alvo quando existir (nunca hardcoded). **Materialização (Makefile/pyproject.toml) somente após D-V0-06 decidida + projeto-alvo existente**; não criar sem decisão Classe C (DEC-006(i) mantém D-V0-01 adiado).
  4. **LangGraph / CR-009-C:** reabrir kickoff D-V0-01 antes da semana 1 (conforme DEC-014 PR-01) com escopo mínimo (stack condicional LangGraph, repo-alvo este repo — DEC-006(ii), CI nenhuma — DEC-006(iii), gates G0–G3 propostos, thresholds lidos do alvo — D-V0-06). LangGraph permanece **condicional** até decisão formal de D-V0-01 (Classe C); F-ÚNICO-1 bloqueada até kickoff + D-V0-03/04/05/06. CR-009-C permanece dormente hoje (sem efeito até D-V0-01 decidida).
  5. **Arquitetura (ADRs A–G):** manter como proposta até D-V0-04: ADR-A (orquestrador dispatcher+agregador, sem domínio), ADR-B (SoT central + event log append-only), ADR-C (idempotência + ingestão at-least-once com dedupe), ADR-D (contratos versionados, envelope + resumo + JSON, validação na borda), ADR-E (modelo de estados e autonomia, execução vs aceite, A/B/C), ADR-F (qualidade incremental por gates e evidência, "no new errors"), ADR-G (observabilidade e segurança mínima by design). Status `proposed`; sem número; sem promoção.
  6. **Dívida técnica (documental):** registrada em `docs/DECISIONS.md` (esta entrada + R1–R12, DIV-1…DIV-6). Itens vigentes: DIV-1 (roadmap PM F0–F2 × TL F0–F5 × PO M1–M3) — em andamento; DIV-2 (`schema_version 0.1.0-draft` × v1.0.0) — em andamento; DIV-3 (ata 46 existente) — fechado; DIV-4 (exit_code 6) — fechado; DIV-5 (inclusão condicional 41–45) — fechado (inclusão condicional vigente); DIV-6 (índice README) — fechado. Riscos vigentes R1–R12 (R8 D-V0-01 adiado, R10 bus factor 1, R11 drift documental, R12 MVP de 1 semana inviável sem kickoff). Sem código neste repo ⇒ sem dívida de código; dívida é documental (drift, lacunas, inconsistências). Sem backlog separado (tracking = `docs/`).

- **Lacunas persistentes (registradas, não resolvidas silenciosamente):**
  - [LACUNA] D-V0-01 adiado (DEC-006(i)): stack/CI/repo-alvo indefinidos ⇒ F-ÚNICO-1 bloqueada; implementação não iniciada; kickoff reaberto antes da semana 1 (DEC-014/DEC-016) mas decisão formal (Classe C) pendente.
  - [LACUNA] D-V0-03 pendente (Classe C): aceite do PO sobre visão/MVP/estados/KPIs; este registro é proposta, não aceite; `approved` exclusivo do PO com evidência.
  - [LACUNA] D-V0-04 pendente (Classe C): baseline técnica/ADRs A–G sem número; `adr_ref="none"`; convenção de numeração (local ADR-001…) proposta mas não adotada.
  - [LACUNA] D-V0-05 pendente (Classe C): contrato v1.0.0 não adotado; `0.1.0-draft` vigente nos designs.
  - [LACUNA] D-V0-06 pendente (Classe C): política de gates/thresholds; "no new errors" sem baseline; thresholds numéricos inexistentes (sem `pyproject.toml`).
  - [LACUNA] CR-008-C: unificação registrada como proposta (Classe B); materialização (Makefile) após D-V0-06 + projeto-alvo.
  - [LACUNA] CR-009-C: LangGraph dormente; sem efeito até D-V0-01 decidida.
  - [LACUNA] CR-013-publicação: baseline v0 não publicado; bloqueada por D-V0-03/04/05/06 + DEC-008.
  - [LACUNA] Critério operacional exato de `completed` no tracking alvo (`docs/` como trilha, sem board/tool) — D-V0-05.
  - [LACUNA] Identificadores correlacionáveis e storage de trilha/evidências/decisões (E4 adiado para F-ÚNICO-2).
  - [LACUNA] Capacidade real por dia (total estimado 117% da capacidade — sobrecarga; re-planejar).
  - [LACUNA] DEC-007 (política de segredos) permanece aberta (gatilho: D-V0-01 resolvido).
  - [LACUNA] Handoff PR→aceite PO inexistente; AC Given/When/Then ausentes nos designs t1–t5 (revisão PO).
  - [LACUNA] KPIs não instrumentáveis (revisão PO); métricas baseline inexistentes.

- **Conflitos registrados (não resolvidos silenciosamente):**
  - DIV-1 (roadmap PM F0–F2 × TL F0–F5 × PO M1–M3) — mapa em `docs/47` §1; em andamento.
  - DIV-2 (`schema_version 0.1.0-draft` × v1.0.0) — proposta em `docs/48`; em andamento.
  - Divergência revisão PO: KPIs não instrumentáveis / AC ausentes nos designs — registrada como [LACUNA], não resolvida.

- **Premissas operacionais (vigentes, com teste correspondente):**
  - P1: MVP M1–M3 entregue em 1 semana com 40h/sem — teste: escopo documental (F-ÚNICO-0) cabe em 5d×8h com buffer 30% (~30h úteis); F-ÚNICO-1 bloqueada por D-V0-01 (R8) — não prometer código.
  - P2: KPIs mensuráveis sem infra externa (docs/) — teste: KPI-1/2/3/6 auditáveis manualmente em 1 semana; KPI-4/5 [LACUNA].
  - [PREMISSA-P7] (DEC-014): orçamento monetário = zero; capacidade = 40h/sem do Mantenedor único; PERT+30% sobre capacidade confirmada.
  - [PREMISSA-P8] (DEC-014): cadência de revisão RACI/checkpoints = semanal (1x/semana), PM delegado (R), Mantenedor (A).
  - P3 (DEC-016): numeração de ADRs reinicia local em ADR-001 (namespace isolado ao repo; citação por caminho). Teste: nenhum id nu citado sem caminho (ADR-009).
  - P4 (DEC-016): thresholds parametrizados (fail-closed exit_code 6) até projeto-alvo existir. Teste: nenhum número de cobertura/lint/types hardcoded em justificativa.
  - P5 (DEC-016): kickoff D-V0-01 reaberto antes da semana 1 (escopo mínimo). Teste: F-ÚNICO-1 permanece bloqueada até decisão formal.

- **Riscos vigentes (topo):** R1 (ambiguidade contratual), R2 (rastreabilidade), R3 (gates), R4 (capacidade), R6 (dependências), R7 (gargalo de aceite PO), R8 (D-V0-01 adiado ⇒ F-ÚNICO-1 bloqueada), R9 (drift DECISIONS×change control), R10 (bus factor 1), R11 (drift documental), R12 (MVP de 1 semana inviável sem kickoff D-V0-01 — Crítico). Mitigações ativas conforme DEC-014/DEC-016.

- **Alternativas consideradas:**
  - (a) Numerar ADRs continuando da árvore compartilhada (019+) — rejeitada pelo Mantenedor (grill #1): namespace isolado ao repo é suficiente; citação por caminho evita ambiguidade.
  - (b) Adotar default conservador de cobertura (ex.: ≥ 80%) hardcoded — rejeitada pelo Mantenedor (grill #2): violaria regra "thresholds lidos do projeto-alvo"; parametrização + fail-closed é a política.
  - (c) Manter D-V0-01 adiado indefinidamente — rejeitada pelo Mantenedor (grill #3): kickoff antes da semana 1 (DEC-014) autorizado; LangGraph permanece condicional.
  - (d) Criar backlog separado de dívida técnica (`docs/tech/debt.md`) — rejeitada pelo Mantenedor (grill #5): tracking = `docs/`; DECISIONS.md é o log canônico; criar diretório exige decisão Classe C (estrutura pendente).
  - (e) Aguardar D-V0-06 para registrar CR-008-C — rejeitada pelo Mantenedor (grill #6): unificação documental (Classe B) pode ser registrada agora; materialização (Makefile) após D-V0-06 + projeto-alvo.
  - (f) Declarar D-V0-04/05/06 aprovados agora — rejeitada: viola regra dura (Classe C, aprovação humana explícita; execução ≠ `approved`).
  - (g) Materializar ADRs numerados/contrato/Makefile/pyproject.toml agora — rejeitada: exige aprovação explícita do Mantenedor via subagente de escrita; não concedida.
  - (h) Resolver lacunas de peso 5 silenciosamente — rejeitada: regra R2/R8; registradas como [LACUNA].

- **Consequências:** proposta consolidada e registrada (Classe B, reversível); nenhuma promoção a `approved`/`completed`; D-V0-04/05/06 permanecem pendentes (Classe C) aguardando decisão do Mantenedor; ADRs A–G permanecem sem número (`adr_ref="none"`); contrato v1.0.0 permanece proposta (sem efeito normativo); gates permanecem propostos (sem Makefile/pyproject.toml); LangGraph permanece condicional; dívida técnica documental registrada (sem backlog separado); publicação do baseline bloqueada (DEC-008/CR-013-publicação); baseline v0 permanece `condicional`/não pronta (2 PASS parciais, 4 FAIL — painel §8.3). Propagação para `docs/30`, `docs/47`, `docs/48`, `docs/00` §8 e `docs/README.md` pendente no próximo change set autorizado.

- **Decisão Recomendada (proposta do TL, 2026-11-16):** **Sim** — aceitar a proposta consolidada TL (ADRs A–G como proposta com convenção de numeração local ADR-001…; contrato v1.0.0 como proposta com migração aditiva; política de gates unificada documentalmente com thresholds parametrizados; LangGraph condicional com kickoff antes da semana 1; arquitetura dispatcher+agregador/SoT/idempotência/contratos/estados/qualidade/observabilidade como proposta; dívida técnica documental registrada em DECISIONS.md) condicionada ao modo documental (sem código) até D-V0-01 resolvido, com resolução das lacunas registradas. Classificação: **[RESOLVIDO-PROPOSTA]** (não aprovado; aguarda decisão humana Classe C).

- **Ressalvas:** TL — consenso condicional de substância com PO/PM; PO — aceite de valor reservado ao PO; PM — consenso condicional, divergência residual de ritmo; Mantenedor — decisão Classe C pendente para D-V0-04/05/06/CR-008-C/CR-009-C/CR-013-publicação; aceite de valor permanece exclusivo do PO.

- **Evidência:** `docs/30-arquitetura-tech-lead-baseline-v0.md` (ADRs A–G, gates G0–G3, contratos, riscos/lacunas); `docs/47-roadmap-unico-fundacao-mvp-evolucao-v0.md` (F-ÚNICO-0/1/2, bloqueios, DIV-1…DIV-6); `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (contrato v1.0.0, semântica de estados, exit codes); `docs/42-mapeamento-gates-makefile-v0.md` §2 (exit_code 6 fail-closed); `docs/00-painel-gerencial-consolidado.md` §5/§8 (D-V0-04/05/06, lacunas, bloqueios); `docs/DECISIONS.md` (DEC-001…DEC-015); `docs/10-produto-po-visao-mvp-baseline-v0.md` (semântica de estados, KPIs); `docs/20-governanca-pm-plano-baseline-v0.md` (R1–R12, P1–P8, PR-01…PR-07); `docs/README.md` (índice canônicos); AGENTS.md (regras duras, precedência); `~/.opencode/references/contrato-resumo-subagentes.md` (sha256 `163e0aad…`); `~/.opencode/references/autonomia-e-estados.md` (sha256 `776af494…`); `~/.agents/adr/core/INDEX.md` (convenção de numeração, ADR-016/017/018 existentes, citação por caminho — ADR-009); grill-with-docs 2×3 (respostas registradas acima).

- **Status final:** **registrado — proposta (Classe B)** (consolidação TL de D-V0-04/05/06, CR-008-C, CR-009-C, arquitetura e dívida técnica; nenhuma aprovação inferida; nenhuma promoção a `approved`/`completed`; nenhum ADR numerado; nenhum diretório/Makefile/pyproject.toml criado; materialização aguarda aprovação explícita do Mantenedor via subagente de escrita; propagação para `docs/30`/`docs/47`/`docs/48`/`docs/00`/`docs/README.md` pendente no próximo change set autorizado). [ATUALIZADO 2026-11-16: materialização Classe C concluída — ADR-001…ADR-007 (status proposed) em docs/adr/core/; Makefile e pyproject.toml na raiz (parametrizados, fail-closed). Nenhuma promoção a approved/completed.]

---

## Decisões pendentes (Classe C, aguardando)

| ID | Decisão pendente | Tipo | Dono(s) recomendado(s) | Observação |
|---|---|---|---|---|
| D-V0-03 | **Aceite do PO** sobre visão, escopo MVP (M1–M3), semântica de estados e metas/KPIs iniciais | Valor (Classe C no efeito de aceite) | PO (A/R); PM/TL (C) | Não inferir `approved`; pacote mínimo de evidência + Given/When/Then |
| D-V0-04 | Aprovar **baseline técnica e ADRs iniciais (A–G)** e convenção/numeração canônica de ADRs | Arquitetura/governança técnica (Classe C) | TL propõe; humano aprova (Mantenedor) | `adr_ref` indefinido até decisão; sem número atribuído |
| D-V0-05 | Consolidar **contrato canônico v1.0.0** (resumo + envelope + estados + correlação + `schema_version`) e taxonomia operacional (`completed`/tracking) | Contrato (adoção pode exigir aprovação) | TL + PO + PM | Base para idempotência/rastreabilidade/gates |
| D-V0-06 | Definir **política unificada de gates/evidência e thresholds** (ex.: cobertura) lidos do projeto-alvo quando aplicável | Qualidade | TL, PM, PO | Evitar hardcode; "no new errors" sobre baseline declarada |
| CR-008-C | **Unificação de gates** (gates incrementais G0–G3 × mapeamento design t2/t5 × `exit_code → AgentState`) | Qualidade/arquitetura (Classe C) | TL propõe; Mantenedor (A) | Depende de D-V0-06; `Makefile` inexistente neste repo |
| CR-009-C | Stack/LangGraph — **dormente**: só se um kickoff futuro decidir stack | Stack/arquitetura (Classe C) — condicional a D-V0-01 futura | TL propõe; Mantenedor (A) | D-V0-01 resolvido (DEC-018); LangGraph permanece condicional (CR-009-C dormente até decisão de adoção); máquina de estados Python pura (src/) é a baseline |
| CR-010-C | Ferramenta de tracking externa — **dormente**: só se um kickoff futuro decidir tracking | Governança/tracking (Classe C) — condicional a D-V0-02 futura | PM propõe; Mantenedor (A) | Hoje sem efeito: DEC-006(vi) — `docs/` é a trilha |
| CR-013-publicação | **Publicação do baseline canônico v0** (após reconciliação via `docs/47`) | Baseline/publicação (Classe C) | Mantenedor (A); PO/PM/TL (C/R) | Bloqueada por D-V0-03/04/05/06 + DEC-008 |
| CR-006 | **Numeração/convenção ADR** canônica (`docs/adr/core/ADR-<NNN>-…`?) | Convenção/numeração (Classe C) | TL propõe; Mantenedor (A) | Parte de D-V0-04; ADRs A–G propostos e sem número |
| CR-007-C | **Adoção do contrato v1.0.0** (in-repo/SoT; `schema_version`; estados) | Contrato/adoção (Classe C) | TL + PO + PM; Mantenedor (A) | Depende de D-V0-05 |

*Nota:* CR-011 (segredos) **não** está nesta tabela porque está registrado como `[LACUNA]` aberta com gatilho definido — ver DEC-007.

*Nota (DEC-016, 2026-11-16): a unificação de gates (CR-008-C) foi registrada como proposta documental (Classe B) em DEC-016 item 3 — G0–G3 × exit_code → AgentState × contrato v1.0.0, com thresholds parametrizados (fail-closed, exit_code 6) até o projeto-alvo existir. Materialização (Makefile/pyproject.toml) somente após D-V0-06 decidida + projeto-alvo existente. Dívida técnica documental registrada em DEC-016 item 6 (sem backlog separado). Convenção de numeração de ADRs (D-V0-04) proposta como `docs/adr/core/ADR-<NNN>-<slug-kebab>.md` com numeração local reiniciando em ADR-001 (decisão do Mantenedor no grill-with-docs, rodada 1). Nenhuma promoção a `approved`/`completed`; nenhum ADR numerado; nenhum diretório criado. [ATUALIZADO 2026-11-16: materialização concluída — ADR-001…ADR-007 (proposed) + Makefile/pyproject.toml (parametrizados).]

## Propagação pendente (atualizado em 2026-11-16 — MU-0.3)

Status após a reconciliação MU-0.3 (executada em 2026-11-16, registrada em DEC-013):

1. `docs/40` front matter `status: "condicional"` → `vigente` (DEC-002) + linha de evidência + índice/painel — **EXECUTADO** em MU-0.3 (DEC-013 item 2). Matriz RACI inalterada.
2. `docs/README.md`: entradas para `docs/DECISIONS.md` e `docs/46` + contagem de canônicos — **EXECUTADO** em MU-0.3 (DEC-013 item 3); DIV-6 fechado.
3. `docs/00` §5/§8: refletir DEC-001…DEC-013 (D-V0-01/02 resolvidas conforme DEC-006; fila de CRs parcialmente decidida) + adendo §8.4 — **EXECUTADO PARCIALMENTE** em MU-0.3 (DEC-013 item 4); D-V0-03/04/05/06 permanecem abertas (DEC-009…DEC-012).
4. `docs/20`: `[PREMISSA-P1]` quinzenal substituída por "sob demanda, sem SLA" (DEC-006(v)) + bloco §0 + cadência + normativos — **EXECUTADO** em MU-0.3 (DEC-013 item 1).
5. Recalcular sha256 **completos** dos normativos externos (DEC-003) — **EXECUTADO** em MU-0.3 (pin exato verificado via `sha256sum`: `163e0aad…` / `776af494…`); sem divergência. (Dono: TL — concluído.)
6. `docs/47` (roadmap único de reconciliação) — criado em 2026-11-16 pelo TL (proposta condicional, status `condicional`); revisão/reconciliação conduzida em sessão própria (DEC-008); **NÃO editado** nesta sessão (restrito). Permanece pendente de validação do Mantenedor e de D-V0-05/06.
7. D-V0-01 resolvido (DEC-018, 2026-11-17): propagar status "RESOLVIDO" para `docs/00` §5/§8, `docs/20` (R8 mitigado), `docs/30` (lacuna removida, thresholds reais), `docs/45` (stack mínima definida), `docs/47` (F-ÚNICO-1 desbloqueada, §6 atualizado) e `docs/README.md` — **EM EXECUÇÃO neste change set (tech-lead, 2026-11-17)**.

## Adendo — Propostas do trio (2026-11-16) — classificação binária

Propostas de decisão emitidas pelos 3 gestores (PO/PM/TL) na sessão atual, reconciliadas pelo `gerente-projeto` em modo documental (sem código; sem promoção a `approved`/`completed`; sem criação de `docs/evidence/`; sem numeração de ADRs). Critério de classificação: **[RESOLVIDO-PROPOSTA]** quando há consenso condicional de substância entre os gestores e pauta despachável; **[BLOQUEIO-CRITICO]** quando a pauta permanece bloqueada por lacuna/decisão humana não resolvida.

| Pauta | Decisão Recomendada | Classificação | Evidência/ressalva |
|---|---|---|---|
| DEC-009 (D-V0-03 — aceite PO visão/MVP/estados/KPIs) | Sim | [RESOLVIDO-PROPOSTA] | PO: DEC-009 Sim + DEC-011 Sim + D-V0-01 manter adiada + F-ÚNICO-1 modo documental; critérios mínimos de aceite (Given/When/Then) e KPIs iniciais. PM/TL: consenso condicional. |
| DEC-010 (D-V0-04 — baseline técnica + ADRs A–G + convenção sem números) | Sim | [RESOLVIDO-PROPOSTA] | PM: DEC-010 Sim (baseline técnica documental + ADRs A–G proposed + convenção sem números); R8 reavaliado (M×A Alto, mitigação ativa), R10/R11 mitigados. TL: estrutura técnica de ADRs neutra (adr_ref="none", human_review único escritor técnico de approved). |
| DEC-011 (D-V0-05 — contrato canônico v1.0.0) | Sim | [RESOLVIDO-PROPOSTA] | PO: DEC-011 Sim (adoção contrato v1.0.0) + AC Given/When/Then + KPIs. TL: contrato v1.0.0 + "no new errors"/G0–G3. PM: consenso condicional, divergência residual de ritmo. |
| DEC-012 (D-V0-06 — política unificada de gates/evidência/thresholds) | Sim | [RESOLVIDO-PROPOSTA] | TL: DEC-012 Sim (política parametrizada, "no new errors" sobre baseline declarada, G0–G3, exit_code 6 fail-closed). PM: trilha TL (schemas offline), trilha PO (AC/KPIs/handoff), trilha PM (R8/R10/R11), gatilho de implementação. |
| D-V0-01 implementação (stack/repo/infra/CI) | Sim (Opção B, 2026-11-17) | [RESOLVIDO] | DEC-018: stack mínima Python 3.12 + pytest + ruff + mypy (sem CI externo); pyproject.toml real (cobertura ≥50%, 0 erros críticos); F-ÚNICO-1 desbloqueada. LangGraph permanece condicional (CR-009-C). |
| Publicação do baseline canônico v0 (CR-013-publicação) | — | [BLOQUEIO-CRITICO] | Bloqueada por D-V0-03/04/05/06 + DEC-008; reconciliação via `docs/47` pendente. |

**Riscos e premissas (propostas do trio):**
- [RISCO] R8 (estagnação por stack adiada) | M×A (Alto) | mitigação ativa (trilha TL schemas offline, trilha PO AC/KPIs/handoff, trilha PM R8/R10/R11, gatilho de implementação) | PM/TL
- [RISCO] R10/R11 (drift documental; bus factor 1) | M×M | mitigados (reconciliação MU-0.3; registro em DECISIONS) | PM
- [PREMISSA] Modo documental F-ÚNICO-1: sem código até gatilho de implementação (D-V0-01 resolvido) | — | manter adiado; não prometer prazo sem buffer | PM
- [PREMISSA] Buffer PERT+30% mantido; cadência sob demanda sem SLA (DEC-006(v)) | — | não prometer prazo sem buffer | PM

**Próximas ações:**
1. Despachar DEC-009…DEC-012 para o Mantenedor (Classe C) — Dono: gerente-projeto — Prazo: sob demanda.
2. Manter F-ÚNICO-1 em modo documental (sem código) até resolução de D-V0-01 — Dono: tech-lead/gerente-produto — Prazo: sob demanda.
3. Registrar gatilho de implementação quando D-V0-01 for decidido — Dono: gerente-projeto — Prazo: sob demanda.

## DEC-017 — Mudança de identidade do repositório: documentação + gates/CI (registro; Classe B)

- **Contexto:** o repo era "somente documentação" (sem código-fonte, manifests, build, testes, lint, CI). Em 2026-11-16 o Mantenedor aprovou (Classe C) a materialização de gates/CI parametrizados (Makefile + pyproject.toml) e ADRs numerados, alterando a identidade do repo para "documentação + gates/CI parametrizados (fail-closed)". A implementação de aplicação (F-ÚNICO-1) permanece bloqueada por D-V0-01 (adiado).
- **Decisão:** registrar a mudança de identidade; qualificar AGENTS.md ("Somente documentação" → "documentação + gates/CI parametrizados (sem código de aplicação)"). Makefile/pyproject.toml criados com thresholds parametrizados (fail_under=0 placeholder) e fail-closed (exit_code 6) para ausência de pyproject.toml.
- **Status:** registrado (Classe B — registro; efeito Classe C executado via DEC-009…DEC-012/DEC-014…DEC-016).
- **Consequências:** repo agora tem verificação documental (lint/typecheck/test/build/audit) parametrizada; thresholds reais pendentes de D-V0-06; implementação de aplicação não iniciada (F-ÚNICO-1 bloqueada).
- **Evidência:** Makefile, pyproject.toml, AGENTS.md (qualificado), docs/README.md, docs/00 (adendo §8.6).
- **Lacunas persistentes:** D-V0-01 adiado; thresholds reais [LACUNA]; completed operacional indefinido; IDs/storage; capacidade real; DEC-007.

---

## DEC-018 — Resolução de D-V0-01 (Opção B): stack mínima definida (Classe C, 2026-11-17)

- **Contexto:** D-V0-01 permaneceu adiado desde DEC-006(i) (stack/infra/repo/CI/gates indefinidos), bloqueando F-ÚNICO-1 (R8) e mantendo o repo em modo documental. Em 2026-11-17 o Mantenedor decidiu (Classe C, Opção B) resolver D-V0-01 com stack mínima, desbloqueando F-ÚNICO-1 com infraestrutura real mínima e eliminando o bloqueio crítico R8/R12 para o MVP.
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):**
  1. **D-V0-01 RESOLVIDO** — stack mínima definida: **Python 3.12 + pytest + ruff + mypy**, **sem CI externo**.
  2. **pyproject.toml real** com thresholds **absolutos** (hardcoded, não parametrizados): **cobertura ≥ 50%** (fail_under = 50) e **0 erros críticos** (ruff/mypy sem erros bloqueantes).
  3. **F-ÚNICO-1 desbloqueada** — infraestrutura real mínima (repo-alvo = este repositório, DEC-006(ii)); Makefile/pyproject.toml existentes atualizados para os thresholds absolutos; gates G0–G1 executáveis localmente.
  4. LangGraph permanece **condicional** (CR-009-C dormente); máquina de estados Python pura (já implementada em `src/`) é a baseline de execução; LangGraph pode ser adotado ou substituído por decisão futura.
  5. Sem CI externo (DEC-006(iii) mantido: nenhuma infra de CI; gates rodam localmente via Makefile).
- **Alternativas consideradas:**
  - (a) Manter D-V0-01 adiado (status quo) — rejeitada: mantinha F-ÚNICO-1 bloqueada indefinidamente (R8/R12).
  - (b) Stack expandida (Python 3.11/Poetry/GitHub Actions, conforme auditoria externa Antigravity) — rejeitada: inventaria contexto não decidido; viola regra "não inventar stack"; exige infra não disponível.
  - (c) Thresholds parametrizados (fail_under=0) — rejeitada: a decisão Opção B fixa valores absolutos (≥50% cobertura, 0 erros críticos) para destravar o MVP; parametrização permanece para projetos-alvo futuros.
- **Consequências:**
  - D-V0-01 deixa de ser `[LACUNA]`/adiado; R8 (estagnação por stack adiada) → **mitigado**; R12 (MVP de 1 semana inviável sem kickoff) → **mitigado** (F-ÚNICO-1 desbloqueada).
  - F-ÚNICO-1 passa de "bloqueada" para "desbloqueada (condicionada a D-V0-03/04/05/06 para aceite/contrato)".
  - `pyproject.toml` real (thresholds absolutos) a ser materializado/atualizado pelo `code-implementer` no próximo change set; Makefile atualizado para os alvos com thresholds.
  - DEC-007 (política de segredos) permanece `[LACUNA]` aberta com gatilho reavaliado (stack agora definida — reavaliação permitida, mas decisão formal pendente).
  - Nenhuma promoção a `approved`/`completed` de artefatos de valor; `approved` permanece exclusivo do PO.
- **Evidência:** decisão do Mantenedor (Lucinei, Classe C, 2026-11-17, Opção B); `docs/00` §5 (D-V0-01); `docs/47` §6 (critérios de promoção); `docs/DECISIONS.md` DEC-006(i) (adiamento original) e DEC-014/DEC-016 (kickoff/reabertura); `pyproject.toml`/`Makefile` do repo (a ser atualizados).
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).

## DEC-019 — D-V0-03: Aceite do PO sobre visão, MVP, estados e KPIs (Classe C, 2026-11-17)

- **Contexto:** D-V0-03 (painel `docs/00` §5) exige aceite do PO sobre visão, escopo MVP (M1–M3), semântica de estados e metas/KPIs iniciais. Registrada como pauta DEC-009/DEC-015 ([RESOLVIDO-PROPOSTA], 2026-11-16). Em 2026-11-17 o Mantenedor formaliza (Classe C) a aprovação e materialização.
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **APROVADO E MATERIALIZADO.** Visão/MVP/estados/KPIs materializados em `docs/10-produto-po-visao-mvp-baseline-v0.md` e `docs/11-visao-mvp-v0.md`; semântica canônica de estados em `docs/41-agentstate-esquema-v0.md`. `approved` de valor permanece pendente de aceite explícito do PO (execução ≠ valor).
- **Referência:** DEC-009, DEC-015 (pautas registradas em 2026-11-16).
- **Artefatos:** `docs/10`, `docs/11`, `docs/41`.
- **Nota:** KPIs instrumentáveis pendentes de implementação; KPI-4 (lead time) e KPI-5 (taxa de retrabalho) permanecem `[LACUNA]` com tracking manual.
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).

## DEC-020 — D-V0-04: Aprovação da baseline técnica e ADRs iniciais (Classe C, 2026-11-17)

- **Contexto:** D-V0-04 (painel `docs/00` §5) exige aprovação da baseline técnica e dos ADRs iniciais (A–G) e da convenção/numeração canônica de ADRs. Registrada como pauta DEC-010/DEC-016 ([RESOLVIDO-PROPOSTA], 2026-11-16). ADRs A–G (renumerados ADR-001…ADR-008) criados com status `proposed`.
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **APROVADO E MATERIALIZADO.** Promover ADR-001…ADR-008 de `proposed` para `accepted` (status no front matter e no corpo). Convenção `docs/adr/core/ADR-<NNN>-<slug-kebab>.md` confirmada (sem número reatribuído). ADR-008 (paradigma "Autonomia com Previsibilidade" + fail-closed) incluído.
- **Referência:** DEC-010, DEC-016 (pautas registradas em 2026-11-16).
- **Artefatos:** `docs/30-arquitetura-tech-lead-baseline-v0.md`, `docs/adr/core/ADR-001…ADR-008`.
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).

## DEC-021 — D-V0-05: Adoção formal do contrato canônico v1.0.0 (Classe C, 2026-11-17)

- **Contexto:** D-V0-05 (painel `docs/00` §5) exige consolidação do contrato canônico v1.0.0 (resumo + envelope + estados + correlação + `schema_version`) e taxonomia operacional (`completed`/tracking). Proposta em `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (status `condicional`); validador `docs/schemas/contract-v1.0.0.schema.json` (Fase 0). Registrada como pauta DEC-011 ([RESOLVIDO-PROPOSTA], 2026-11-16).
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **APROVADO E MATERIALIZADO.** Adotar o contrato `docs/48` como v1.0.0 (de `v1.0.0-PROPOSTA`), com migração aditiva de `0.1.0-draft → 1.0.0` (sem remoção/re-tipagem). Validador `docs/schemas/contract-v1.0.0.schema.json` permanece referência. `completed ≠ approved` preservado; `approved` exclusivo do PO.
- **Referência:** DEC-011 (pauta registrada em 2026-11-16).
- **Artefato:** `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` (adotado como v1.0.0).
- **Nota:** a adoção formal não promove artefatos de valor a `approved`; `approved` permanece exclusivo do PO com evidência.
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).

## DEC-022 — D-V0-06: Política unificada de gates/evidência/thresholds (Classe C, 2026-11-17)

- **Contexto:** D-V0-06 (painel `docs/00` §5) exige política unificada de gates/evidência e thresholds (ex.: cobertura) lidos do projeto-alvo quando aplicável. Proposta em `docs/30` (gates G0–G3) e `docs/42` (mapeamento gates↔Makefile, exit_code 6 fail-closed). Registrada como pauta DEC-012 ([RESOLVIDO-PROPOSTA], 2026-11-16). DEC-018 (2026-11-17) fixou thresholds absolutos (cobertura ≥50%, 0 erros críticos) para o MVP.
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **APROVADO E MATERIALIZADO.** Adotar a política unificada de gates/evidência/thresholds: "no new errors" sobre baseline declarada; G0–G3; exit_code 6 fail-closed; thresholds absolutos para o MVP (cobertura ≥50%, 0 erros críticos — hardcoded em `pyproject.toml`/`Makefile`); thresholds parametrizados (lidos do projeto-alvo) para projetos-alvo futuros. Artefatos: `pyproject.toml`, `Makefile`, `docs/42`.
- **Referência:** DEC-012 (pauta registrada em 2026-11-16); DEC-018 (thresholds absolutos, 2026-11-17).
- **Artefatos:** `pyproject.toml`, `Makefile`, `docs/42-mapeamento-gates-makefile-v0.md`.
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).

## DEC-023 — DEC-007: Política de segredos (Classe C, 2026-11-17)

- **Contexto:** DEC-007 permaneceu `[LACUNA]` aberta (registrado em 2026-11-16) com gatilho de reavaliação após D-V0-01. Com a stack definida (DEC-018, 2026-11-17 — Python 3.12 + pytest + ruff + mypy), a política de segredos pode ser formalizada. Referência de implementação: `src/secrets.py` (code-implementer).
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **APROVADO E MATERIALIZADO.** Política de segredos:
  1. **Injeção via variáveis de ambiente** (`os.environ`); nunca hardcode em código, configuração ou artefatos.
  2. **Mascaramento em logs** (ex.: `"sk-...****"`); segredos nunca aparecem em claro em logs, SoT, evidências ou artefatos.
  3. **Proibição de segredos** em SoT, logs, artefatos, commits e documentação.
  4. Implementação de referência: `src/secrets.py` (code-implementer).
- **Referência:** DEC-007 (registro 2026-11-16, `[LACUNA]` aberta); DEC-018 (stack definida, 2026-11-17).
- **Artefatos:** `src/secrets.py` (implementado pelo code-implementer).
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).

## DEC-024 — Consolidação da baseline v0 e início da F-ÚNICO-2 (Classe C, 2026-11-17)

- **Contexto:** F-ÚNICO-1 (MVP Controlado) concluída tecnicamente (implementação: persistência SQLite, validador de contrato, segredos, máquina de estados, 65 testes, 74,84% cobertura). Todos os 6 critérios de §8.3 do painel atendidos (6/6 PASS). D-V0-01 resolvido (DEC-018); D-V0-03/04/05/06 aprovados e materializados (DEC-019…DEC-022); DEC-007 fechado (DEC-023); D-V0-02 parcial (capacidade/tracking).
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **CONSOLIDAR BASELINE v0 PUBLICADA e INICIAR F-ÚNICO-2 (Evolução).** Atualizar painel `docs/00` (§1 semáforo, §5, §8 machine-readable, §8.3 critérios 6/6 PASS), `docs/README.md` (DEC-001…DEC-024; observações de governança), `docs/20`, `docs/30`, `docs/45`, `docs/47`, `docs/48` (remoção de lacunas resolvidas; F-ÚNICO-1 concluída; F-ÚNICO-2 iniciada). `no_go_flags: []`. `proxima_acao_recomendada`: "Baseline v0 publicada; iniciar F-ÚNICO-2 (evolução)".
- **Referência:** DEC-018 (D-V0-01), DEC-019 (D-V0-03), DEC-020 (D-V0-04), DEC-021 (D-V0-05), DEC-022 (D-V0-06), DEC-023 (DEC-007).
- **Artefatos:** `docs/00-painel-gerencial-consolidado.md`, `docs/README.md`, `docs/20-*`, `docs/30-*`, `docs/45-*`, `docs/47-*`, `docs/48-*`, `docs/DECISIONS.md`.
- **Nota:** `approved` de valor permanece exclusivo do PO; F-ÚNICO-2 (Evolução) inicia como trilha documental/técnica com change control. D-V0-02 permanece parcial (capacidade/tracking) — não bloqueante para F-ÚNICO-2.
- **Status final:** **vigente** (decisão humana Classe C, 2026-11-17).

## DEC-025 — Reconciliação de docs/41 e docs/45 para contrato v1.0.0 (Classe B, 2026-11-17)

- **Contexto:** F-ÚNICO-2 (Evolução) iniciada (DEC-024). Os canônicos de design `docs/41` e `docs/45` permaneciam em `0.1.0-draft` (DIV-2) e precisavam ser reconciliados para o contrato v1.0.0 adotado (DEC-021), com campos do envelope canônico, mapeamento de estados (ADR-005), exit codes com ação automática (docs/42) e gates G2/G3 com thresholds do `pyproject.toml`. Ação de classe B (reversível, documental), sem promoção a `approved`/`completed` de artefatos de valor.
- **Decisão (Classe B, tech-lead, 2026-11-17):** **RECONCILIADO.** Alterações aplicadas:
  1. `docs/41-agentstate-esquema-v0.md`: migração aditiva `0.1.0-draft → 1.0.0` confirmada; campos do contrato adicionados ao bloco JSON_STRICT (`schema_name`, `schema_version`, `envelope_id`, `idempotency_key`, `correlation_id`); seção §4.1 "Mapeamento de estados (execução → operação → valor) — ADR-005" adicionada (camadas, transições com guardas, invariantes; critério operacional de `completed` permanece `[LACUNA]`). Campos existentes preservados (`global_context`, `ads`, `tasks`, `errors`, `approvals`, `integration_test_output`, `pr_ready`).
  2. `docs/45-grafo-langgraph-classe-c-v0.md`: migração aditiva confirmada; seção §2.1 "Exit codes → ação automática" (fonte docs/42 §2) adicionada; seção §2.2 "Gates G2/G3 com thresholds do pyproject.toml" adicionada (G0–G3, thresholds absolutos cobertura ≥50%, 0 erros críticos, fail-closed exit_code 6); nota LangGraph (CR-009-C) mantida condicional com stack mínima definida (DEC-018) e máquina de estados Python pura (src/) como baseline.
  3. `docs/00-painel-gerencial-consolidado.md`: §1 semáforo atualizado para F-ÚNICO-2; §8 `aggregation_status` → "F-ÚNICO-2 em andamento"; `proxima_acao_recomendada` → "Reconciliar docs/41/45, obter aceite PO, resolver D-V0-02"; `last_reviewed` 2026-11-17.
  4. `docs/README.md`: data da última atualização 2026-11-17 (verificado; consistência mantida).
- **Referência:** DEC-021 (D-V0-05, contrato v1.0.0 adotado), DEC-020 (ADR-005 accepted), DEC-022 (D-V0-06, gates/thresholds), DEC-018 (D-V0-01, stack mínima), DEC-024 (baseline v0 publicada, F-ÚNICO-2 iniciada).
- **Artefatos:** `docs/41-agentstate-esquema-v0.md`, `docs/45-grafo-langgraph-classe-c-v0.md`, `docs/00-painel-gerencial-consolidado.md`, `docs/README.md`, `docs/DECISIONS.md`.
- **Nota:** migração aditiva — sem remoção/re-tipagem de campos; consumidores de `0.1.0-draft` permanecem compatíveis por leitura tolerante. `machine_readable.schema_version` do painel (`"1.0"`) permanece distinto do `schema_version` de contrato (`"1.0.0"`) (decisão de D-V0-05). Nenhum campo `approved` escrevível por agente; `approved` permanece exclusivo do PO.
- **Status final:** **concluído** (Classe B, 2026-11-17 — registro documental reversível; nenhuma promoção a `approved`/`completed` de artefatos de valor).

## DEC-026 — Aceite de valor do PO para incrementos MVP (Classe C, 2026-11-17)

- **Contexto:** F-ÚNICO-2 (Evolução) exige formalização do aceite de valor do PO para os incrementos MVP (E1–E3), com critérios de aceite (AC Given/When/Then) completos e handoff PR→aceite PO documentado. A revisão PO dos designs t1–t5 (`ses_e1b33e791ffeK0gwIR9QY7Y7z5`) apontou como lacunas: handoff PR→aceite PO inexistente, AC Given/When/Then ausentes nos designs e KPIs não instrumentáveis. DEC-024 consolidou a baseline v0 e iniciou F-ÚNICO-2; D-V0-03 aprovado e materializado (DEC-019) mantém `approved` de valor pendente de aceite explícito do PO (execução ≠ valor).
- **Decisão (Classe C, decided_by Lucinei, 2026-11-17):** **MATERIALIZAR o aceite de valor do PO para incrementos MVP** como trilha documental e de governança, sem declarar `approved` de nenhum incremento:
  1. **AC Given/When/Then completos para E1–E3** registrados em `docs/11-visao-mvp-v0.md` §"Aceite de Valor (PO)" (fonte canônica do aceite de valor) e referenciados em `docs/10-produto-po-visao-mvp-baseline-v0.md` §4/§0.1.
  2. **Handoff PR→aceite PO** documentado (PR criado → evidência anexada → PO revisa → decisão `approved`/`rejected` → feedback estruturado), com SLA sob demanda sem SLA formal (DEC-006(v)).
  3. **KPIs (KPI-1 a KPI-6) calibrados para F-ÚNICO-2** em `docs/10` e `docs/11` (KPI-4/KPI-5 passam de `[LACUNA]` para metas propostas a calibrar).
  4. **`approved` é exclusivo do PO com evidência** — nenhum agente (orquestrador, PO-as-proposta, PM, TL, subagentes) pode inferir ou declarar `approved`; a transição `pending → approved` exige `evidence` verificável e `human_interaction_ref` quando a decisão for tomada por interação humana (Classe C). `rejected → pending` somente com nova evidência.
  5. **Decision/Acceptance v0** preservado: `pending | approved | rejected`; `approved` terminal (exige `evidence` + `decided_by=PO` + `decided_at`); `rejected` exige `rationale` + `decided_by=PO` + `decided_at`.
- **Nota:** `approved` de valor permanece pendente de aceite formal de execução — a materialização documental (AC + handoff + KPIs) não equivale a `approved` de nenhum incremento. A transição `pending → approved` exige evidência verificável e `human_interaction_ref` (Classe C).
- **Evidência:** AC Given/When/Then definidos (docs/11 §"Aceite de Valor (PO)" — E1 H1.1–H1.3, E2 H2.1–H2.2, E3 H3.1–H3.3); handoff PR→aceite PO documentado (docs/11 §C); KPIs calibrados (docs/10 §4, docs/11 §KPIs); revisão PO dos designs t1–t5 (`ses_e1b33e791ffeK0gwIR9QY7Y7z5`); DEC-019 (D-V0-03 materializado); DEC-024 (baseline v0 publicada, F-ÚNICO-2 iniciada).
- **Lacuna:** aceite formal pendente de execução (pending → approved) — nenhum incremento MVP (E1–E3) foi declarado `approved`; a transição exige evidência verificável e `human_interaction_ref` (Classe C), a ser registrada em `docs/DECISIONS.md` como DEC-* quando ocorrer. Identificadores correlacionáveis/storage de trilha (E4) e critério operacional de `completed` no tracking alvo permanecem `[LACUNA]`.
- **Referência:** DEC-019 (D-V0-03), DEC-024 (baseline v0/F-ÚNICO-2), DEC-006 (iv)-(vi) (mantenedor único, cadência sob demanda, tracking = docs/), docs/10, docs/11, docs/48 (semântica de estados).
- **Status final:** **Materializado (Classe C, 2026-11-17)** — trilha documental/governança do aceite de valor do PO; nenhum incremento declarado `approved`; `approved` permanece exclusivo do PO com evidência.

## Rodapé

Aprovados (decisão humana explícita, Classe C): DEC-001…DEC-006, DEC-009…DEC-012, DEC-014…DEC-016, DEC-018…DEC-024, DEC-026 (materialização executada em 2026-11-17). DEC-007 fechado por DEC-023 (política de segredos materializada); DEC-008, DEC-013, DEC-017, DEC-025 registrados (Classe B). DEC-026 MATERIALIZADO (aceite de valor do PO para incrementos MVP — AC Given/When/Then + handoff PR→aceite + KPIs calibrados; `approved` permanece exclusivo do PO com evidência). D-V0-01 RESOLVIDO (DEC-018); D-V0-03/04/05/06 APROVADOS E MATERIALIZADOS (DEC-019…DEC-022); DEC-007 FECHADO (DEC-023); baseline v0 PUBLICADA (DEC-024); D-V0-02 parcial. A ausência de decisão humana explícita em qualquer item ⇒ não aprovado.
