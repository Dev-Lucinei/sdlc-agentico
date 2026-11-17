# Quality gates do sdlc-agentico (parametrizados).
# Thresholds (cobertura, lint, tipos) vêm do projeto-alvo (pyproject.toml); nunca hardcoded aqui.
# Repo documental: não há código-fonte executável nem testes neste repositório.
# fail_under = 0 é placeholder; valor real deve ser lido do pyproject.toml do projeto-alvo (D-V0-06).

PYTHON ?= python3

.PHONY: lint typecheck test build audit

lint:
	ruff check .

typecheck:
	@if [ -z "$$(find . -type f -name '*.py' -not -path './.git/*' -not -path '*/__pycache__/*' -print -quit 2>/dev/null)" ]; then \
		echo "Nenhum arquivo .py — typecheck ignorado (repo documental)"; \
		exit 0; \
	else \
		mypy .; \
	fi

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
