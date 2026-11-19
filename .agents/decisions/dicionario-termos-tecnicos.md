---
title: Dicionário Técnico SDLC Agêntico v0 (Profundo)
date: 2026-11-18
project: sdlc-agentico
source: docs/
status: done
version: 1.0.0
tags: [governance, tech, llm, quality, slang, deep-scan]
---

# Dicionário Técnico SDLC Agêntico v0 (Profundo)

> **Fonte de Verdade:** Este glossário foi gerado via varredura integral (`deep-scan`) de todos os artefatos canônicos do repositório (`docs/`, `src/`, `tools/`).
> **Regra de Ouro:** Termos não listados aqui devem ser considerados fora do escopo padrão ou registrados como `[LACUNA]`.

---

## 📂 Categorias e Definições

### 1. Governança, Processos e Ciclo de Vida (SDLC)
*   **Baseline (v0):** Estado inicial ou referência técnica estabelecida como ponto de partida para o projeto. No SDLC Agêntico, refere-se à versão pública da documentação e implementação da Fase 1.
*   **Fase X (F-ÚNICO-X):** Designação para etapas do ciclo de vida do projeto. Ex: `F-ÚNICO-1` (Validação), `F-ÚNICO-2` (Evolução). Cada fase tem objetivos, entregas e critérios de aceite distintos.
*   **Incremento (E1–En):** Unidade atômica de valor ou funcionalidade entregue dentro de uma Fase. O aceito de valor é exclusivo do PO; execução ≠ aprovação.
*   **PO (Product Owner):** Responsável pelo aceite de valor dos incrementos. A aprovação do PO é o único evento que eleva um incremento a `accepted`.
*   **PM (Project Manager):** Responsável pela governança, plano e baseline do projeto.
*   **TL (Tech Lead):** Responsável pela arquitetura técnica e decisões técnicas (`docs/30-*`).
*   **Class C:** Nível de decisão formalizado que exige aprovação humana explícita para alterar o estado do projeto ou documentação canônica.
*   **DEC (Decision Record):** Abreviação para "Decision". Ex: `DEC-032`. Registra decisões formais, regras e mudanças de direção.
*   **ADR (Architecture Decision Record):** Registra decisões técnicas específicas (`docs/adr/core/`). Diferente de DEC, foca em "como" e "porquê" técnico, mas também é fonte de verdade.
*   **Kickoff:** Evento formal de início de uma nova fase ou grande iniciativa (ex: Kickoff da Fase 2).
*   **Acceptance of Value:** Processo pelo qual o PO valida que um incremento atende aos requisitos de negócio. É a única forma de `approved`.

### 2. Documentação, Estrutura e Rastreabilidade
*   **Append-only:** Padrão de escrita onde novos dados são adicionados ao final do arquivo sem sobrescrever o histórico anterior. Usado em `docs/decisions/` para garantir auditabilidade imutável.
*   **Front Matter:** Seção inicial de um arquivo Markdown (ex: `title`, `date`, `project`, `status`) usada para metadados estruturados e rastreabilidade automática.
*   **Canônico:** Documento que serve como referência oficial e permanente, não descartável. Alterações devem ser propagadas ao índice principal.
*   **Índice Vigente:** Tabela de artefatos (geralmente em `docs/README.md` ou `DECISIONS.md`) que mapeia o status e localização dos documentos canônicos.
*   **Conflito:** Situação onde há divergência entre documentos ou decisões. A regra do projeto é registrar como `[LACUNA]` e escalar, evitando resolução silenciosa.
*   **Lacuna (`[LACUNA]`):** Termo usado para documentar conflitos, lacunas de evidência ou divergências que não podem ser resolvidas localmente e exigem escalabilidade formal. É o "padrão" para quando documentos entram em conflito.
*   **Status Dinâmico:** Estado volátil do sistema (ex: `done`, `blocked`, `partial`) que é derivado automaticamente das decisões e testes, servindo como telemetria para o painel gerencial.
*   **Fonte Única de Verdade:** Princípio de que um arquivo específico contém a informação mais atual e confiável, evitando duplicação ou versões desatualizadas.

### 3. Qualidade de Software, Testes e Gates
*   **Cobertura ≥ Threshold:** Métrica obrigatória onde a cobertura de testes deve ser maior ou igual ao valor mínimo definido (ex: 50% em `pyproject.toml`).
*   **Exit Code:** Código numérico retornado por um comando (`make audit`, `pytest`) indicando sucesso (0) ou falha (não-zero).
*   **Threshold:** Limite mínimo ou máximo estabelecido para uma métrica de qualidade.
*   **Suíte de Testes:** Conjunto completo de testes que devem passar para considerar a fase como concluída.
*   **Gates Funcionais:** Pontos de controle obrigatórios na pipeline de desenvolvimento (via Makefile). Se não forem atendidos, o processo é bloqueado.
*   **Fail-closed:** Mecanismo de gate que impede o avanço do processo se uma verificação falhar, gerando um erro de saída (`exit code` não zero).
*   **Makefile / Targets:** Arquivo de automação usado para definir alvos (`lint`, `test`, `audit`). Os gates são implementados como targets no Makefile.
*   **No New Errors:** Princípio de que novas falhas não devem ser introduzidas sobre a baseline declarada.
*   **Audit:** Processo de verificação de conformidade (G0–G3) executado via `make audit`.

### 4. Desenvolvimento, Ferramentas e Código
*   **Entry Point:** Ponto de entrada principal para execução (ex: CLI invocado via subprocess nos testes).
*   **Stack Tecnológico:** Conjunto de tecnologias usadas na implementação (no SDLC Agêntico: Python 3.12, pytest, ruff, mypy).
*   **Shim:** Pequeno código ou arquivo que atua como interface intermediária (ex: `tools/contract_validator.py`). Mantido por compatibilidade, mas adiciona camadas de abstração.
*   **Drift (Deriva):** Desvio da implementação ou documentação em relação à baseline declarada. O projeto opera sob a regra "no new errors" sobre a baseline; drift não autorizado é tratado como falha de qualidade.
*   **Git / Branches:** `master` é a branch única atual. Pushes na `master` exigem autorização explícita do Mantenedor. Branches são usadas apenas para novas funcionalidades ou refatoração massiva.
*   **Conventional Commits:** Convenção de mensagens de commit em PT-BR com escopo (`docs(baseline): ...`).

### 5. Inteligência Artificial e LLMs (Configuração e Uso)
*   **Autocomplete Model:** Modelo especializado para geração de sugestões de código, otimizado para velocidade e baixa latência (`maxTokens` baixo).
*   **Context Length:** Limite máximo de tokens que o modelo pode processar em uma única solicitação.
*   **Local vs. Remoto:** Diferença entre modelos rodando no próprio hardware (`localhost`) versus chamados via API externa (com custo e risco de quota).
*   **Ollama:** Serviço local para execução de modelos de linguagem grandes (LLMs) diretamente na máquina.
*   **Provider:** Fonte ou serviço que fornece o modelo de linguagem (ex: `ollama`, `gemini`).
*   **Temperature:** Parâmetro de controle de aleatoriedade na geração de texto. Valor baixo favorece precisão/código; valor alto favorece criatividade.
*   **Context Providers:** Tipos de contexto fornecidos ao LLM (`code`, `docs`, `diff`, `terminal`, `problems`, `folder`, `codebase`).

### 6. Segurança e Privacidade
*   **Audit Trail:** Registro completo de ações e decisões, garantindo que qualquer alteração possa ser rastreada e verificada.
*   **Hardcode:** Prática não recomendada de inserir chaves de API ou senhas diretamente em arquivos de configuração visíveis (como `config.yaml` público). Recomenda-se uso de Secret Manager ou `.env`.
*   **Secret Manager:** Serviço seguro para armazenamento e gerenciamento de segredos (ex: Google Secret Manager).
*   **SAST (Static Application Security Testing):** Verificação estática de segurança executada via `ruff --select S`.

### 7. Siglas e Abreviações Específicas do Projeto
*   **DEC-NNN:** Identificador único para uma Decisão Classe C. Ex: `DEC-032`.
*   **ADR-NNN-<slug>:** Identificador único para um Architecture Decision Record. Ex: `ADR-001`.
*   **G0-G3:** Níveis de Gates de segurança/qualidade validados em `make audit`.
*   **F-ÚNICO-X:** Designação para uma Fase única do SDLC.
*   **E1–En:** Identificadores para Incrementos de valor dentro de uma Fase.
*   **Mantenedor:** Role responsável por validar mudanças no repositório, merges na `master` e gestão de branches.

### 8. Jargão e Gírias do Ecossistema SDLC Agêntico
*   **[LACUNA]:** Termo usado para indicar uma divergência, lacuna de evidência ou conflito que não pode ser resolvido localmente e deve ser escalado formalmente. É o "padrão" para quando documentos entram em conflito.
*   **Approved/Accepted:** Status de valor concedido pelo PO. Nunca inferido por execução; requer aprovação explícita.
*   **Done/Blocked/Partial:** Estados de execução (não operacionais). Diferente de `Approved`.
*   **Tech Debt:** Dever técnico acumulado, mas no SDLC Agêntico é mitigado estritamente pelos Gates e Baselines.

---

*Última atualização: 2026-11-18 | Fonte: Varredura Completa do Repositório SDLC Agêntico (Deep Scan)*