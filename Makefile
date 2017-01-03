SHELL := /bin/bash

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  all               to update, generate and test this SDK"
	@echo "  test              to run service test"
	@echo "  unit              to run all sort of unit tests except runtime"
	@echo "  update            to update git submodules"
	@echo "  generate          to generate service code"

all: update generate unit

test:
	@echo "run service test"
	pip install -r scenarios/requirements.txt
	behave scenarios/features
	@echo "ok"

generate:
	@if [[ ! -f "$$(which snips)" ]]; then \
		echo "ERROR: Command \"snips\" not found."; \
	fi
	snips \
		--service=qingstor --service-api-version=latest \
		--spec="./specs" --template="./template" --output="./qingstor/sdk/service"
	rm ./qingstor/sdk/service/object.py
	yapf -i -r ./qingstor ./tests ./scenarios --style google
	@echo "ok"

update:
	git submodule update --remote
	@echo "ok"

unit:
	@echo "run unit test"
	nosetests
	@echo "ok"

tox:
	@echo "run unit test in multi python version"
	@echo "please do pyenv local before run this script"
	tox
	@echo "ok"
