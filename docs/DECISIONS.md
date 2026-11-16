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

## Decisões pendentes (Classe C, aguardando)

| ID | Decisão pendente | Tipo | Dono(s) recomendado(s) | Observação |
|---|---|---|---|---|
| D-V0-03 | **Aceite do PO** sobre visão, escopo MVP (M1–M3), semântica de estados e metas/KPIs iniciais | Valor (Classe C no efeito de aceite) | PO (A/R); PM/TL (C) | Não inferir `approved`; pacote mínimo de evidência + Given/When/Then |
| D-V0-04 | Aprovar **baseline técnica e ADRs iniciais (A–G)** e convenção/numeração canônica de ADRs | Arquitetura/governança técnica (Classe C) | TL propõe; humano aprova (Mantenedor) | `adr_ref` indefinido até decisão; sem número atribuído |
| D-V0-05 | Consolidar **contrato canônico v1.0.0** (resumo + envelope + estados + correlação + `schema_version`) e taxonomia operacional (`completed`/tracking) | Contrato (adoção pode exigir aprovação) | TL + PO + PM | Base para idempotência/rastreabilidade/gates |
| D-V0-06 | Definir **política unificada de gates/evidência e thresholds** (ex.: cobertura) lidos do projeto-alvo quando aplicável | Qualidade | TL, PM, PO | Evitar hardcode; "no new errors" sobre baseline declarada |
| CR-008-C | **Unificação de gates** (gates incrementais G0–G3 × mapeamento design t2/t5 × `exit_code → AgentState`) | Qualidade/arquitetura (Classe C) | TL propõe; Mantenedor (A) | Depende de D-V0-06; `Makefile` inexistente neste repo |
| CR-009-C | Stack/LangGraph — **dormente**: só se um kickoff futuro decidir stack | Stack/arquitetura (Classe C) — condicional a D-V0-01 futura | TL propõe; Mantenedor (A) | Hoje sem efeito: D-V0-01 adiado (DEC-006(i)); não executar |
| CR-010-C | Ferramenta de tracking externa — **dormente**: só se um kickoff futuro decidir tracking | Governança/tracking (Classe C) — condicional a D-V0-02 futura | PM propõe; Mantenedor (A) | Hoje sem efeito: DEC-006(vi) — `docs/` é a trilha |
| CR-013-publicação | **Publicação do baseline canônico v0** (após reconciliação via `docs/47`) | Baseline/publicação (Classe C) | Mantenedor (A); PO/PM/TL (C/R) | Bloqueada por D-V0-03/04/05/06 + DEC-008 |
| CR-006 | **Numeração/convenção ADR** canônica (`docs/adr/core/ADR-<NNN>-…`?) | Convenção/numeração (Classe C) | TL propõe; Mantenedor (A) | Parte de D-V0-04; ADRs A–G propostos e sem número |
| CR-007-C | **Adoção do contrato v1.0.0** (in-repo/SoT; `schema_version`; estados) | Contrato/adoção (Classe C) | TL + PO + PM; Mantenedor (A) | Depende de D-V0-05 |

*Nota:* CR-011 (segredos) **não** está nesta tabela porque está registrado como `[LACUNA]` aberta com gatilho definido — ver DEC-007.

## Propagação pendente (fora do escopo desta sessão — registrar para o próximo change set)

Itens abaixo **não foram executados** nesta sessão (restrição explícita: não tocar em `docs/00/10/20/30/40/41–45`, `AGENTS.md`, `README.md`):

1. `docs/40` front matter: `status: "condicional"` → `vigente` (DEC-002) + linha do índice no `docs/README.md` + painel `docs/00` §5/§8 (menção a DEC-002).
2. `docs/README.md`: adicionar entradas para `docs/DECISIONS.md` e `docs/46-ata-kickoff-d-v0-01-02-v0.md`; atualizar contagem de canônicos.
3. `docs/00` §5/§8: refletir DEC-001…DEC-008 (D-V0-01/02 resolvidas conforme DEC-006; fila de CRs parcialmente decidida); §8.3 (adendo) sugerido.
4. `docs/20`: `[PREMISSA-P1]` quinzenal substituída por "sob demanda, sem SLA" (DEC-006(v)); referência cruzada a DEC-006.
5. Recalcular sha256 **completos** dos normativos externos (ou decisão de pin exato) — Dono: TL (DEC-003).
6. `docs/47` (roadmap único de reconciliação) — criado em 2026-11-16 pelo TL (proposta condicional, status `condicional`); revisão/reconciliação conduzida em sessão própria (DEC-008); fora do escopo desta sessão e não editado por ela.

## Rodapé

Nada aqui é `approved` exceto os itens expressamente marcados como decisão humana de 2026-11-16 (DEC-001…DEC-006); a ausência de decisão humana explícita ⇒ não aprovado.
