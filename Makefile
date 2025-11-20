.PHONY: help install test lint clean deploy-local

help:
	@echo "Available commands:"
	@echo "  make install       - Install dependencies"
	@echo "  make test          - Run tests"
	@echo "  make lint          - Run linting"
	@echo "  make clean         - Clean build artifacts"
	@echo "  make deploy-local  - Deploy function locally"

install:
	cd azure-function/Summarize-alert && pip install -r requirements.txt

install-dev:
	cd azure-function/Summarize-alert && pip install -r requirements-dev.txt

test:
	cd azure-function/Summarize-alert && python -m unittest test_function.py -v

test-coverage:
	cd azure-function && pytest --cov=Summarize-alert --cov-report=html

lint:
	cd azure-function/Summarize-alert && \
		python -m pylint __init__.py || true && \
		python -m flake8 __init__.py || true

format:
	cd azure-function/Summarize-alert && python -m black __init__.py test_function.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".coverage" -delete

deploy-local:
	cd azure-function && func start
