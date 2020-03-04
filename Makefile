flake:
	flake8 paftdunk
	flake8 tests

install:
	pip install -e ".[dev]"

develop: install
	python setup.py develop
	pre-commit install

test:
	pytest --cov=paftdunk

check: flake test clean

clean:
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf scikit_lego.egg-info
	rm -rf .ipynb_checkpoints
	rm -rf notebooks/.ipynb_checkpoints

build:
	docker build -t pythoncontainer .

serve:
	uvicorn paftdunk.web:app --reload

test-gitlab:
	gitlab-runner exec docker test