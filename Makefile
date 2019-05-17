SHELL := /bin/bash

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  all               to update, generate and test this SDK"
	@echo "  test              to run service test"
	@echo "  unit              to run all sort of unit tests except runtime"
	@echo "  build             to build sdist and bdist_wheel"
	@echo "  clean             to clean build and dist files"
	@echo "  update            to update git submodules"
	@echo "  generate          to generate service code"

all: update generate unit

test:
	@echo "run service test"
	behave scenarios/features
	@echo "ok"

generate:
	@if [[ ! -f "$$(which snips)" ]]; then \
		echo "ERROR: Command \"snips\" not found."; \
	fi
	snips \
		-f ./specs/qingstor/2016-01-06/swagger/api_v2.0.json \
		-t="./template" \
		-o="./qingstor/sdk/service"
	rm ./qingstor/sdk/service/object.py
	yapf -i -r ./qingstor ./tests ./scenarios
	@echo "ok"

update:
	git submodule update --remote
	@echo "ok"

unit:
	@echo "run unit test"
	nosetests
	@echo "ok"

clean:
	@echo "clean build and dist files"
	rm -rf build/ dist/ qingstor_sdk.egg-info
	@echo "ok"

build: clean
	@echo "build sdist and bdist_wheel"
	python setup.py sdist bdist_wheel
	@echo "ok"
