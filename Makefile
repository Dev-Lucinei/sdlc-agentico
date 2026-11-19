# Quality gates do sdlc-agentico (D-V0-01 resolvido: Python 3.12 + pytest + ruff + mypy).
# Thresholds absolutos: cobertura >= 50%, 0 erros criticos (pyproject.toml).
# Sem CI/CD externo.

PYTHON ?= python3

.PHONY: lint typecheck test build audit audit-g2

lint:
	ruff check .

typecheck:
	mypy src

test:
	@rc=0; $(PYTHON) -m pytest --collect-only -q >/dev/null 2>&1; rc=$$?; \
	if [ $$rc -eq 5 ]; then \
		echo "Nenhum teste coletado — test ignorado (repo documental)"; \
		exit 0; \
	elif [ $$rc -ne 0 ]; then \
		echo "Erro na coleta de testes (exit $$rc)"; \
		exit $$rc; \
	else \
		$(PYTHON) -m pytest; \
	fi

build:
	@echo "build: placeholder documental — repositório documental; nenhuma build executável."
	@echo "G0-G3 aplicam-se ao projeto-alvo quando definido (D-V0-01/D-V0-06)."

audit: ## Roda G0-G3 + verifica pyproject.toml (fail-closed: exit_code 6 se ausente)
	@if [ ! -f pyproject.toml ]; then \
		echo "audit: pyproject.toml ausente — fail-closed (exit_code 6)"; \
		exit 6; \
	fi
	$(MAKE) lint
	$(MAKE) typecheck
	$(MAKE) test
	$(MAKE) build
	@echo "audit: G0-G3 concluídos (thresholds lidos do pyproject.toml do projeto-alvo)."

# G2 executável (DEC-032, F2.1-téc — fatia Classe B). Fail-closed. Thresholds NUNCA hardcoded:
# fail_under é lido de pyproject.toml via tomllib. Não altera o alvo `audit` nem seus exit codes.
audit-g2: ## G2 (DEC-032 F2.1-téc): ruff + mypy + pytest c/ cobertura >= fail_under do pyproject.toml + SAST básico (S) — fail-closed
	@if [ ! -f pyproject.toml ]; then \
		echo "audit-g2: pyproject.toml ausente — fail-closed (exit_code 6)"; \
		exit 6; \
	fi
	@FAIL_UNDER=$$($(PYTHON) -c 'import tomllib; print(tomllib.load(open("pyproject.toml","rb"))["tool"]["coverage"]["report"]["fail_under"])') || { \
		echo "audit-g2: não foi possível ler tool.coverage.report.fail_under de pyproject.toml — fail-closed (exit_code 6)"; \
		exit 6; \
	}; \
	echo "audit-g2: fail_under=$$FAIL_UNDER (lido de pyproject.toml)"; \
	echo "audit-g2: [1/4] ruff check ."; \
	ruff check . || exit $$?; \
	echo "audit-g2: [2/4] mypy src"; \
	mypy src || exit $$?; \
	echo "audit-g2: [3/4] pytest c/ cobertura >= $$FAIL_UNDER"; \
	$(PYTHON) -m pytest --cov=src --cov-report=term-missing --cov-fail-under=$$FAIL_UNDER || exit $$?; \
	echo "audit-g2: [4/4] SAST básico (ruff --select S src/)"; \
	ruff check --select S src/ || exit $$?; \
	echo "audit-g2: G2 concluído (lint+typecheck+testes verdes; cobertura >= $$FAIL_UNDER; SAST S limpo/documentado)."
