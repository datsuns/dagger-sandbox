default:

init:
	dagger init --sdk python --name hello --source .

run:
	cd src && python main.py

install:
	python -m venv .venv
	source .venv/bin/activate
	pip install dagger-io

.PHONY: default init install
