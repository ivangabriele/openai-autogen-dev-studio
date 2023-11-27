.PHONY: clean lint install run test type

clean:
	find ./project -maxdepth 1 -mindepth 1 -type f,d ! -name '.gitkeep' -exec rm -fr {} +

install:
	poetry install

lint:
	poetry run pylint $(shell find . -name '*.py')

ran:
	poetry run python ./niam.py

run:
	poetry run python ./main.py

test:
	poetry run pytest

type:
	poetry run mypy ./main.py
