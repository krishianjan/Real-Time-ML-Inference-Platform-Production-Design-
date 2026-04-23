.PHONY: help build up down test clean

help:
	@echo "Available commands:"
	@echo "  make build      Build Docker images"
	@echo "  make up         Start local stack (docker-compose)"
	@echo "  make down       Stop local stack"
	@echo "  make test       Run unit tests"
	@echo "  make clean      Remove containers and volumes"

build:
	docker build -f docker/ingestion.Dockerfile -t ingestion-service:latest .
	docker build -f docker/inference.Dockerfile -t inference-service:latest .

up:
	docker-compose up -d

down:
	docker-compose down

test:
	pytest tests/ -v

clean:
	docker-compose down -v
	find . -type d -name __pycache__ -exec rm -rf {} +