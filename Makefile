.PHONY: clean lint run test type

clean:
	find ./project -mindepth 1 -type f,d ! -name '.gitkeep' -exec rm -Rf {} +

lint:
	poetry run pylint ./main.py

run:
	poetry run python ./main.py

test:
	poetry run pytest

type:
	poetry run mypy ./main.py
