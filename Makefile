.PHONY: test build run-local

test:
	pytest tests

build:
	docker build -t ml-model:local .

run-local:
	docker-compose -f docker-compose.dev.yml up --build
