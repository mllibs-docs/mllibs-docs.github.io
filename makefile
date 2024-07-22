.PHONY: serve
serve:
	poetry run python tools/docs.py serve

.PHONY: build
build:
	poetry run python tools/docs.py build-all

.PHONY:
static:
	poetry run python tools/docs.py static-server

.PHONY: icon
icon:
	poetry run python tools/favicon.py