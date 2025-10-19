lint:
	uv run ruff check

install:
	uv sync

test-coverage:
	uv run pytest --cov=csv-project --cov-report xml

test:
	uv run pytest

check: test lint
