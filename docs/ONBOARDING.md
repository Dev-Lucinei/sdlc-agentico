---
title: "Onboarding — sdlc-agentico"
date: "2026-11-18"
project: "sdlc-agentico"
source: "gerente-produto"
status: "condicional"
---

# Bem-vindo ao sdlc-agentico

Este é o seu ponto de partida. Aqui você entende, em linguagem direta, **o que estamos construindo, por que estamos construindo e como você — humano — participa do processo**. Sem jargão de processo, sem cerimônia.

> **Tom honesto:** este projeto está em estágio inicial. Parte do que você vai ler descreve a visão e o desenho em curso — não tudo está implementado ainda. Onde algo ainda não existe, dizemos isso claramente.

## 1. O que estamos construindo (e por quê)

Estamos construindo um **SDLC agêntico**: um ciclo de desenvolvimento de software em que agentes de IA executam o trabalho pesado (projetar, codar, testar, abrir PR) e um humano — você — decide o que realmente tem valor.

O problema que resolvemos é simples de enunciar e difícil de resolver: **em sistemas multiagente, "está pronto" costuma ser ambíguo.** Um agente termina uma tarefa e diz "done" — mas isso não significa que o produto está entregue, nem que o valor foi aceito. Essa confusão gera retrabalho, falsa sensação de conclusão e pouca confiança de quem paga a conta.

Nossa proposta:

1. **Um contrato único** entre quem delega e quem executa — toda entrega vem com um resumo padronizado e evidência verificável.
2. **Estados separados de verdade** — execução técnica, conclusão operacional e aceite de valor são coisas diferentes, com donos diferentes.
3. **Aceite humano explícito** — nenhum resultado vira "valor entregue" sem um humano dizer que vira.
4. **Visibilidade honesta** — lacunas são marcadas como lacunas, nunca inventadas.

O resultado que buscamos: menos ambiguidade, mais auditabilidade e decisões de valor mais rápidas e objetivas.

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

## 3. O motor por dentro: o grafo em 7 nós

Por baixo dos panos, o ciclo de execução é desenhado como um **grafo de estados** (proposto sobre LangGraph, ainda sujeito a ajuste). A visão conceitual, sem afogar em detalhes:

1. **Desenho** — um agente transforma a demanda em especificação (ADS + diagrama). É o "o quê" e o "como conceitual".
2. **Arquitetura** — um agente valida a especificação contra as restrições do sistema. Inconsistência aqui **trava o fluxo**: ninguém chega a codar em cima de uma spec quebrada.
3. **Codificação com ciclo de testes** — o trabalho de verdade: uma tarefa por vez, testes escritos **antes** da validação, e retorno forçado à codificação sempre que um teste falhar. Três falhas na mesma validação = parada e escalonamento humano.
4. **Portão de PR** — só abre PR se os testes de integração passaram e a cobertura está acima do mínimo configurado no projeto.
5. **Revisão humana** — o único ponto em que um humano decide. Sem a sua aprovação (com evidência de que você interagiu), nada é "aceito".
6. **Bloqueado** — estado terminal de reparo esgotado ou erro crítico: o sistema para, registra a evidência e escala para você. Nunca finge que deu certo.
7. **Fim** — ciclo encerrado, com trilha completa do que aconteceu.

A regra de ouro do grafo: **nenhuma transição para "aprovado" acontece sem um humano no nó de revisão.** O resto é automação com portões.

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
pip install -e ".[dev]"   # se aplicável ao seu ambiente
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
| `docs/41-agentstate-esquema-v0.md` | O "estado" que viaja pelo grafo: quais informações existem, quem escreve e o que significa cada campo. |
| `docs/44-loop-feedback-coding-tdd-qa-v0.md` | O ciclo de codificação: uma tarefa por vez, teste antes da validação, retorno forçado em falha. |
| `docs/45-grafo-langgraph-classe-c-v0.md` | O desenho do grafo de estados com o portão de revisão humana para decisões de alto risco. |
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

**Sim, com o limite certo.** Classes A e B cobrem trabalho de baixo risco e reversível — por isso o sistema pode avançar sem você a cada passo, desde que os portões automáticos estejam verdes e a evidência esteja anexada.

O que você **não** deve delegar por autopromoção:

- Aceite de valor (isso é sempre seu, sem exceção).
- Mudanças irreversíveis, destrutivas ou de alto impacto (apagar dados, mudar contratos públicos, promover baseline).
- Qualquer coisa em que a evidência seja fraca ou ausente — "o agente disse que está pronto" nunca é evidência.

Na prática: confie na automação para **executar**; reserve seu julgamento para **aceitar**. Se um resultado de classe A/B chegar até você com evidência verificável e portões verdes, revise rápido e decida — o sistema já fez o trabalho de verificação mecânica; falta apenas o seu "sim" ou "não" de valor.

### Preciso ler tudo antes de contribuir?

Não. Leia este documento e o painel de situação (`docs/00-painel-gerencial-consolidado.md`). O resto você consulta sob demanda, conforme a seção 6.

### O que significa "condicional" nos documentos?

Que o conteúdo é uma proposta registrada e rastreável, mas ainda não passou por aceite de valor. É o estado honesto de um projeto em construção — diferente de "aprovado", que exige decisão humana explícita.

## 8. Princípios que valem para todos (humanos e máquinas)

1. **Sem evidência, não há "pronto".** Status de execução sem artefato verificável é só uma afirmação.
2. **Lacuna se declara, não se inventa.** "Não sei" dito explicitamente vale mais que uma resposta confiante e errada.
3. **Execução ≠ operação ≠ valor.** Terminar, ser concluído e ser aceito são três coisas diferentes, com donos diferentes.
4. **Fail-closed.** Na dúvida, o sistema para e pergunta — nunca assume.
5. **Humano no comando do valor.** A máquina acelera; você decide o que vale.

---

*Dúvidas ou lacunas neste onboarding? Abra uma demanda apontando a seção — este documento deve evoluir junto com o projeto.*
