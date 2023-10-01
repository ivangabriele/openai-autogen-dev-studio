.PHONY: clean run test type

clean:
	find ./project -mindepth 1 -type f,d ! -name '.gitkeep' -exec rm -Rf {} +

run:
	poetry run python ./main.py

test:
	poetry run pytest

type:
	poetry run mypy ./main.py
