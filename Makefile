brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
build:
	rm dist/*
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl
lint:
	poetry run flake8 brain_games
