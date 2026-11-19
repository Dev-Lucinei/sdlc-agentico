---
title: "Operação do Repositório — Matriz RACI (v0)"
date: "2026-11-13"
project: "sdlc-agentico"
source: "gerente-produto (Product Owner Sênior; tarefa delegada por sessão orquestradora; classe B)"
status: "vigente"
---
> **Status `vigente` desde 2026-11-16** — validação Classe C do Mantenedor (Lucinei), registrada em `docs/DECISIONS.md` (DEC-002). A matriz permanece em vigor como proposta operacional do repo; promoção de qualquer estado para `approved` continua exigindo decisão humana.

**Classe de autonomia declarada:** B (artefato documental reversível; nenhuma ação Classe C executada — nenhum status promovido a `approved`, nenhuma baseline/ADR aceita, nenhuma ação git). Validado pelo Mantenedor em 2026-11-16 (DEC-002); vigente. Promoções posteriores continuam Classe C.

**Evidência de vigência (DEC-002, 2026-11-16):** `docs/DECISIONS.md` (entrada DEC-002) — validação Classe C do Mantenedor Lucinei; front matter `status: "vigente"`; matriz RACI inalterada (já vigente); nenhuma linha autoriza inferir `approved`. Promoção de qualquer estado a `approved` permanece Classe C (Mantenedor humano).

## 📋 Decisão / Conclusão
Proposta de **matriz RACI das operações do repositório documental** (quem faz o quê na manutenção dos canônicos, do índice, do `AGENTS.md` e do git local), complementar — e **não duplicada** — ao RACI do baseline v0 (`20-governanca-pm-plano-baseline-v0.md` §2), que cobre o produto/projeto, não a operação deste repo. Critério: clareza de responsabilidade única (um **A** por linha), alinhamento às regras duras do repo (Classe C = humano; execução ≠ aceite) e mínimo necessário (enxuta e verificável). Local escolhido: **arquivo canônico novo `docs/40-operacao-raci-repo-v0.md`** em vez de seção no `AGENTS.md`, porque (i) o `AGENTS.md` é política raiz do repo e estava potencialmente em edição por outro agente na data desta criação, (ii) um canônico numerado entra no índice e no ciclo de reconciliação v0 já estabelecido, e (iii) mantém o `AGENTS.md` enxuto. **Trade-off:** cria um canônico a mais para manter sincronizado; mitigado com entrada no índice no mesmo change set.

## 🗂️ Artefato

**Legenda:** R = Responsável (executa) · A = Aprovador/Accountable (responde pelo resultado; **um por linha**) · C = Consultado · I = Informado.
**Papéis:** **Mant** = Mantenedor humano (owner do repo) · **Orch** = Orchestrator · **PO** = gerente-produto · **PM** = gerente-projeto · **TL** = tech-lead · **Sub** = subagentes especialistas/implementadores.
**Regra de desempate:** conflito entre canônicos ou dúvida sobre promoção de estado/Classe C → **parar e escalar ao Mantenedor humano**; nunca resolver silenciosamente.

| # | Atividade / decisão | Mant | Orch | PO | PM | TL | Sub |
|---|---|---|---|---|---|---|---|
| 1 | Editar conteúdo de `docs/10-*` (trilha Produto) | C | C | **A/R** | I | C | R (insumos) |
| 2 | Editar conteúdo de `docs/20-*` (trilha Governança) | C | C | C | **A/R** | C | R (insumos) |
| 3 | Editar conteúdo de `docs/30-*` (trilha Arquitetura) | C | C | C | C | **A/R** | R (insumos) |
| 4 | Editar/atualizar `docs/00-*` (agregação/painel) | C | **A/R** | C | C | C | I |
| 5 | Atualizar `docs/README.md` (índice/status/rastreabilidade) no mesmo change set da mudança no canônico | C | **A** | R* | R* | R* | R* |
| 6 | Adicionar / remover / renomear artefato canônico em `docs/` | **A** | C | C | C | C | R (execução) |
| 7 | Recriar/restaurar `baseline-v0-*.md` (proibido) | **A** (veta) | I | I | I | I | I (não recriar; reportar) |
| 8 | Atualizar status de **execução** honestamente (`done/blocked/partial`) com evidência | I | **A** | R | R | R | R |
| 9 | Aceite de valor / promoção a `approved` (Classe C) | **A** (humano) | I | **R** (recomenda/aceita valor) | C | C | I |
| 10 | Promover baseline/ADR/numeração v0 a canônico/aceito (Classe C) | **A** (humano) | C | C | C | R (proposta) | R (insumos) |
| 11 | Alterar `AGENTS.md` (regras/convenções do repo) | **A/R** ou A (R delegado a subagente designado) | C | I | I | I | R (se designado) |
| 12 | Commit na `master` (mudança trivial, política vigente) | **A/R** (ou R explícito delegado pelo Mant) | C | I | I | I | R (somente se autorizado) |
| 13 | Criar branch (nova funcionalidade ou refatoração massiva) | **A/R** | C | I | I | C | R (execução) |
| 14 | Push/remote/publicação | **A/R** | I | I | I | I | I |
| 15 | Registrar `[LACUNA]` / conflito entre canônicos (quem detecta registra) | I | **A** (triagem/escalonamento) | R | R | R | R |
| 16 | Resolver conflito entre canônicos (desempate) | **A** (humano) | R (mediação) | C | C | C | I |
| 17 | Verificação de consistência cruzada (`README` ↔ canônicos ↔ JSON `docs/schemas/painel-status.json`, derivado de `docs/DECISIONS.md` + `docs/decisions/` (regenerar a cada DEC)) | I | **A** | C | C | C | R (executa a checagem) |
| 18 | Definir/alterar política de gates, thresholds, CI (inexistente hoje) | **A** | C | C | C | R (proposta) | C |

\* Quem altera um canônico é **R** na atualização do índice no mesmo change set; o **A** é do Orchestrator (coordenação) e o **C/veto** final é do Mantenedor.

**Notas de semântica (obrigatórias)**
- `done` (execução) ≠ `completed` (OPS) ≠ `approved` (valor/PO). Nenhuma linha desta matriz autoriza inferir `approved` a partir de status de execução.
- Classe C (linhas 9, 10, 11 quando altera regra dura, 12–14 com efeito externo) exige **aprovação humana explícita**; subagente nunca autoaprova.
- Ausência de remote configurado torna a linha 14 hoje **no-op operacional**; mantida para explicitar ownership quando o remote existir `[LACUNA]`.

## ⚠️ Premissas e Lacunas
- `[LACUNA]` Identidade/disponibilidade formal do Mantenedor (papéis, contato, cadência de revisão) não documentada no repo; assumido "dono humano do repo" conforme AGENTS.md e ausência de remote.
- `[RESOLVIDO — DEC-027 (2026-11-17); vigente DEC-006(vi)]` Tracking/backlog: trilha vigente = `docs/` (Classe C); recomendação de adoção GitHub Issues (+ Projects) para escala registrada — adoção exige decisão Classe C do Mantenedor (CR-010-C; remote inexistente hoje, DEC-006(iii)); esta matriz não assume board/issue tracker.
- `[LACUNA]` Política de proteção de branch/permissões de commit para agentes (além da política "trivial → master") não formalizada; linha 12 assume delegação explícita por tarefa.
- `[LACUNA]` Cadência de revisão desta matriz não definida; sugerido revisar junto ao checkpoint F0 do plano PM.
- `[PREMISSA]` Numeração `40` livre (00/10/20/30 = agregação/PO/PM/TL) e não colide com artefatos futuros se a faixa ≥ 40 for respeitada.
- `[PREMISSA]` Sessões/identidades de agentes (Orchestrator, subagentes) são efêmeras; a matriz referencia papéis, não sessões.

## ✅ Próximas Ações
1. Mantenedor (humano) revisar e validar esta matriz; se aprovada, promover status `condicional` → vigente (decisão Classe C) — Dono: Mantenedor — Prazo: próximo checkpoint.
2. Se a decisão for por seção no `AGENTS.md` em vez de canônico próprio, migrar este conteúdo e remover este arquivo (evitar duplicata) — Dono: Mantenedor/Orchestrator — Prazo: junto da revisão do `AGENTS.md`.
3. Incluir referência a este canônico na seção "Fontes de verdade" do `AGENTS.md` após validação (edição do `AGENTS.md` fora do escopo desta tarefa) — Dono: Mantenedor/subagente designado — Prazo: junto da revisão.
4. Reconciliar com decisões D-V0-01…D-V0-06 quando o baseline v0 for formalmente reconciliado — Dono: PM/Orchestrator — Prazo: F0.
