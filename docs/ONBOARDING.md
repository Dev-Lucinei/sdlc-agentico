---
title: "Onboarding — sdlc-agentico"
date: "2026-11-18"
project: "sdlc-agentico"
source: "gerente-produto"
status: "condicional"
---

# Bem-vindo ao sdlc-agentico

Este é o seu ponto de partida. Aqui você entende, em linguagem direta, **o que estamos construindo, por que estamos construindo e como você — humano — participa do processo**. Sem jargão de processo, sem cerimônia.

> **Tom honesto:** Fase 1 concluída; E1–E3 aprovadas (DEC-030); F-ÚNICO-2 em andamento. Parte do que você vai ler descreve a visão e o desenho em curso — não tudo está implementado ainda. Onde algo ainda não existe, dizemos isso claramente.

## 1. O que estamos construindo (e por quê)

Estamos construindo um **SDLC agêntico**: agentes de IA executam o trabalho pesado (projetar, codar, testar, abrir PR) e um humano — você — decide o que tem valor. O problema central é a ambiguidade de "está pronto" em sistemas multiagente: execução ≠ conclusão ≠ aceite de valor, e a confusão gera retrabalho e falsa sensação de conclusão. A proposta: um contrato único, estados separados, aceite humano explícito e lacunas declaradas — ver `docs/10-produto-visao-v0.md`.

## 2. O fluxo humano: como você interage com o sistema

Pense no sistema como uma **equipe bem-orquestrada**, não como um robô monolítico:

- **O orquestrador é um dispatcher + agregador.** Ele não executa o trabalho e não tem opinião de domínio. Ele recebe a demanda, divide em tarefas, despacha para os especialistas certos e junta os resultados no final. Pense nele como um bom gerente de projeto: coordena, não codar.
- **Subagentes especializados executam.** Cada um tem um papel (design, arquitetura, codificação, testes, QA) e responde sempre no mesmo formato, com evidência.
- **Você aprova apenas decisões de valor final.** O sistema não pede sua opinião para cada passo — só quando algo precisa de julgamento humano de verdade: aceitar ou rejeitar o resultado (tipicamente no PR / no marco de entrega).
- **Tarefas de baixo risco são aprovadas automaticamente.** Lint, testes e verificações mecânicas passam por portões automáticos. Se o portão é verde, o fluxo segue; se é vermelho, o trabalho volta para correção sem te incomodar.

Em resumo:

```
Você (demanda + critério de valor)
        ↓
Orquestrador (despacha e agrega — não executa)
        ↓
Subagentes especializados (executam, com evidência)
        ↓
Portões automáticos (lint, testes, checks mecânicos)
        ↓
Você (aprova ou rejeita o resultado final — só aqui)
```

## 3. O motor por dentro

O ciclo é desenhado como grafo (`design → architecture → coding → tdd → qa → human_review → pr_generation`); o desenho vive em `docs/historico/45-grafo-langgraph-classe-c-v0.md` (superseded).
A implementação vigente é a máquina de estados Python pura em `src/graph.py` (DEC-018); LangGraph está dormente (CR-009-C).
Nenhuma transição para "aprovado" acontece sem um humano na revisão (ver seção 7).

## 4. Quem faz o quê: humano vs. máquina

| Responsabilidade | Humano (PO / Mantenedor) | Sistema (orquestrador + agentes) |
|---|---|---|
| Definir o que tem valor e os critérios de aceite | ✅ Dono | Apoia (propõe, estrutura) |
| Decompor demanda em tarefas e despachar | ❌ | ✅ Dono |
| Executar design, código, testes, QA | ❌ | ✅ Dono |
| Rodar lint/testes e aplicar portões mecânicos | ❌ | ✅ Automático |
| Corrigir falhas de validação (até o limite de tentativas) | ❌ | ✅ Automático |
| Escalar quando o reparo esgota ou há erro crítico | Recebe e decide | ✅ Detecta e escala |
| Aprovar entrega de valor (aceite final) | ✅ Exclusivo | ❌ Jamais |
| Promover mudança de alto risco / irreversível | ✅ Exclusivo | ❌ Bloqueado por desenho |
| Tarefas de baixo risco (lint, testes, checks) | ❌ Não precisa | ✅ Aprovação automática |
| Marcar "lacuna" quando falta informação | ✅ Pode questionar | ✅ Obrigado a declarar, nunca a inventar |

Regra prática: **se a decisão muda o que o produto é ou vale, é sua. Se é mecânica e reversível, é do sistema.**

## 5. Como começar

### Pré-requisitos

- Linux, Python 3.12+
- `make`, `git`
- Sem serviços externos obrigatórios para rodar a base local

### Setup local

```bash
git clone <repo> && cd sdlc-agentico
python3 -m venv .venv && source .venv/bin/activate
# Python 3.12 + `make lint typecheck test audit`
# (ruff/mypy/pytest; fail_under lido de pyproject.toml)
```

### Primeira execução

```bash
make lint        # ruff — análise estática
make typecheck   # mypy — checagem de tipos
make test        # pytest — suíte de testes
make audit       # portões G0–G3 + verificação fail-closed
```

Se `make audit` passar, seu ambiente está saudável. Se algo falhar, o erro é o ponto de partida — não tente contornar o portão; corrija a causa.

### Sua primeira interação real

1. Leia este documento e o mapa da seção 6.
2. Abra uma demanda pequena e bem delimitada (uma tarefa, critério claro de "pronto").
3. Observe o fluxo: despacho → execução → portões → resultado agregado.
4. Quando o resultado chegar para você, decida com base na evidência anexada — não na confiança no agente.

## 6. Onde encontrar o quê

Mapa dos documentos principais, em linguagem natural:

| Documento | O que você encontra lá |
|---|---|
| `docs/00-painel-gerencial-consolidado.md` | O painel de situação do projeto: semáforo, decisões pendentes, riscos e próximos passos. Leia primeiro se quer saber "como as coisas estão". |
| `docs/10-produto-visao-v0.md` | A visão de produto e o recorte de MVP: o problema, o valor, personas, proposta de valor, backlog com critérios de aceite verificáveis e o que entra (e o que fica de fora) na primeira versão. |
| `docs/20-governanca-pm-plano-baseline-v0.md` | O plano de governança: fases, marcos, riscos e cadência. Útil para "quando" e "em que ordem". |
| `docs/30-arquitetura-tech-lead-baseline-v0.md` | A arquitetura proposta: componentes, fluxos, decisões técnicas e portões de qualidade. |
| `docs/historico/41-agentstate-esquema-v0.md` | O "estado" que viaja pelo grafo: quais informações existem, quem escreve e o que significa cada campo. |
| `docs/historico/44-loop-feedback-coding-tdd-qa-v0.md` | O ciclo de codificação: uma tarefa por vez, teste antes da validação, retorno forçado em falha. |
| `docs/historico/45-grafo-langgraph-classe-c-v0.md` | O desenho do grafo de estados com o portão de revisão humana para decisões de alto risco. |
| `docs/48-contrato-canonico-v1-0-0-proposta-v0.md` | O contrato entre quem delega e quem executa: o formato do resumo, dos estados e dos códigos de saída. |
| `docs/DECISIONS.md` | O log de decisões relevantes do projeto, com contexto e justificativa. |
| `docs/README.md` | O índice completo e a política de manutenção desta pasta. |
| `AGENTS.md` | As regras de operação para agentes (e para você, ao operar este repo). |

## 7. Perguntas frequentes

### Como sei se uma decisão é minha ou do sistema?

Pergunte: **"isso muda o que o produto é, vale ou promete?"**
- Sim → é sua (aceite de valor, escopo, prioridade, risco irreversível).
- Não, é mecânico e reversível (lint, testes, formatação, verificação) → é do sistema, automático.
- Na dúvida → trate como sua. O sistema foi desenhado para **parar e perguntar**, nunca para decidir por conta própria o que é seu.

### O que acontece se um agente errar?

Depende do erro, e o sistema é explícito sobre isso:

- **Falha de validação** (teste vermelho, lint quebrado): o trabalho volta automaticamente para correção, com o erro registrado. Sem drama, sem você.
- **Três falhas na mesma validação**: o sistema para, marca a tarefa como bloqueada e escala para você com a evidência do que tentou.
- **Erro crítico** (violação de restrição, falha grave): parada imediata e escalonamento humano. Nunca há "tentativa heróica" silenciosa.
- **Saída ambígua ou sem evidência**: o resultado não é aceito como pronto; o agente é re-despachado uma vez com a lacuna apontada. Persistindo, você decide.

### Posso confiar em autopromoção para classes A/B?

Não — `approved` é exclusivo do PO (DEC-030; `src/human_review.py` + `src/contract_validator.py`).

### Preciso ler tudo antes de contribuir?

Não. Leia este documento e o painel de situação (`docs/00-painel-gerencial-consolidado.md`). O resto você consulta sob demanda, conforme a seção 6.

### O que significa "condicional" nos documentos?

Que o conteúdo é uma proposta registrada e rastreável, mas ainda não passou por aceite de valor. É o estado honesto de um projeto em construção — diferente de "aprovado", que exige decisão humana explícita.

## 8. Princípios que valem para todos (humanos e máquinas)

1. Ver `AGENTS.md` §Regras duras (semântica de estados; evidência antes de done).

---

*Dúvidas ou lacunas neste onboarding? Abra uma demanda apontando a seção — este documento deve evoluir junto com o projeto.*
