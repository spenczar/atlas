virtualenv:
	python -m venv virtualenv

VENV = virtualenv/bin
$(VENV): virtualenv
$(VENV)/pip: $(VENV)

.git/hooks/pre-commit:
	ln -sf ../../dev/pre-commit.sh


# Development tools
.PHONY: dev-setup
dev-setup: .git/hooks/pre-commit $(VENV)/flake8 $(VENV)/black $(VENV)/mypy

$(VENV)/flake8 $(VENV)/black $(VENV)/mypy &: $(VENV)/pip
	$(VENV)/pip install -e '.[dev]'

.PHONY: lint format typecheck precommit
lint: $(VENV)/flake8
	$(VENV)/flake8 ./src

format: $(VENV)/black
	$(VENV)/black \
		--target-version py38 \
		./src/atlas

typecheck: $(VENV)/mypy
	$(VENV)/mypy ./src

precommit: format typecheck lint
