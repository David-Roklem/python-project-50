install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

build: check
	poetry build

check: selfcheck test lint

selfcheck:
	poetry check

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

gendiff:
	poetry run gendiff

reinstall-package:
	pip install --user --force-reinstall dist/*.whl

.PHONY: install test lint selfcheck check build