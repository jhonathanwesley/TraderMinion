.PHONY: help install install-backend install-frontend migrate createsuperuser server test clean setup dev-backend dev-frontend

# Variáveis
PYTHON := python
PIP := pip
NPM := npm
MANAGE := python manage.py
VENV := .venv
PYTHON_VENV := $(VENV)/Scripts/python.exe
PIP_VENV := $(VENV)/Scripts/pip.exe

# Cores para output (funciona no Git Bash e WSL)
CYAN := \033[0;36m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Mostra esta mensagem de ajuda
	@echo "$(CYAN)TraderMinion - Makefile Commands$(NC)"
	@echo ""
	@echo "$(GREEN)Comandos disponíveis:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(YELLOW)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""

install: install-backend install-frontend ## Instala todas as dependências (backend + frontend)

install-backend: ## Instala dependências Python do backend
	@echo "$(CYAN)Instalando dependências do backend...$(NC)"
	@if [ -d "$(VENV)" ]; then \
		$(PIP_VENV) install -r requirements.txt; \
	else \
		$(PIP) install -r requirements.txt; \
	fi
	@echo "$(GREEN)✓ Dependências do backend instaladas!$(NC)"

install-frontend: ## Instala dependências Node.js do frontend
	@echo "$(CYAN)Instalando dependências do frontend...$(NC)"
	@cd client && $(NPM) install
	@echo "$(GREEN)✓ Dependências do frontend instaladas!$(NC)"

migrate: ## Aplica migrações do banco de dados
	@echo "$(CYAN)Aplicando migrações...$(NC)"
	@if [ -d "$(VENV)" ]; then \
		$(PYTHON_VENV) manage.py migrate; \
	else \
		$(PYTHON) manage.py migrate; \
	fi
	@echo "$(GREEN)✓ Migrações aplicadas!$(NC)"

makemigrations: ## Cria novas migrações
	@echo "$(CYAN)Criando migrações...$(NC)"
	@if [ -d "$(VENV)" ]; then \
		$(PYTHON_VENV) manage.py makemigrations; \
	else \
		$(PYTHON) manage.py makemigrations; \
	fi
	@echo "$(GREEN)✓ Migrações criadas!$(NC)"

createsuperuser: ## Cria um superusuário Django
	@echo "$(CYAN)Criando superusuário...$(NC)"
	@if [ -d "$(VENV)" ]; then \
		$(PYTHON_VENV) manage.py createsuperuser; \
	else \
		$(PYTHON) manage.py createsuperuser; \
	fi

server: ## Inicia o servidor Django (backend)
	@echo "$(CYAN)Iniciando servidor Django...$(NC)"
	@echo "$(YELLOW)Servidor rodando em: http://127.0.0.1:8000$(NC)"
	@echo "$(YELLOW)API disponível em: http://127.0.0.1:8000/api$(NC)"
	@echo "$(YELLOW)Admin disponível em: http://127.0.0.1:8000/admin$(NC)"
	@echo "$(YELLOW)Pressione CTRL+C para parar$(NC)"
	@if [ -d "$(VENV)" ]; then \
		$(PYTHON_VENV) manage.py runserver 127.0.0.1:8000; \
	else \
		$(PYTHON) manage.py runserver 127.0.0.1:8000; \
	fi

dev-backend: server ## Alias para server (inicia backend)

dev-frontend: ## Inicia o servidor de desenvolvimento do frontend (Vite)
	@echo "$(CYAN)Iniciando servidor de desenvolvimento do frontend...$(NC)"
	@cd client && $(NPM) run dev

test: ## Executa testes da API
	@echo "$(CYAN)Executando testes da API...$(NC)"
	@if [ -d "$(VENV)" ]; then \
		$(PYTHON_VENV) test_api.py; \
	else \
		$(PYTHON) test_api.py; \
	fi

test-api: test ## Alias para test

clean: ## Limpa arquivos temporários e cache
	@echo "$(CYAN)Limpando arquivos temporários...$(NC)"
	@find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	@rm -rf client/node_modules 2>/dev/null || true
	@rm -rf client/dist 2>/dev/null || true
	@echo "$(GREEN)✓ Limpeza concluída!$(NC)"

clean-db: ## Remove o banco de dados SQLite (CUIDADO: apaga todos os dados!)
	@echo "$(RED)ATENÇÃO: Isso irá apagar todos os dados do banco!$(NC)"
	@echo "$(YELLOW)Para remover o banco, delete manualmente o arquivo db.sqlite3$(NC)"
	@echo "$(YELLOW)ou execute: rm -f db.sqlite3$(NC)"

setup: install migrate ## Setup completo: instala dependências e aplica migrações
	@echo "$(GREEN)✓ Setup completo!$(NC)"
	@echo "$(YELLOW)Execute 'make server' para iniciar o backend.$(NC)"
	@echo "$(YELLOW)Execute 'make dev-frontend' para iniciar o frontend.$(NC)"

build-frontend: ## Build de produção do frontend
	@echo "$(CYAN)Construindo frontend para produção...$(NC)"
	@cd client && $(NPM) run build
	@echo "$(GREEN)✓ Build do frontend concluído!$(NC)"

collectstatic: ## Coleta arquivos estáticos (Django)
	@echo "$(CYAN)Coletando arquivos estáticos...$(NC)"
	@if [ -d "$(VENV)" ]; then \
		$(PYTHON_VENV) manage.py collectstatic --noinput; \
	else \
		$(PYTHON) manage.py collectstatic --noinput; \
	fi
	@echo "$(GREEN)✓ Arquivos estáticos coletados!$(NC)"

shell: ## Abre o shell interativo do Django
	@if [ -d "$(VENV)" ]; then \
		$(PYTHON_VENV) manage.py shell; \
	else \
		$(PYTHON) manage.py shell; \
	fi

check: ## Verifica o código com linters
	@echo "$(CYAN)Verificando código...$(NC)"
	@cd client && $(NPM) run lint || true
	@echo "$(GREEN)✓ Verificação concluída!$(NC)"

typecheck: ## Verifica tipos TypeScript
	@echo "$(CYAN)Verificando tipos TypeScript...$(NC)"
	@cd client && $(NPM) run typecheck
	@echo "$(GREEN)✓ Verificação de tipos concluída!$(NC)"

# Comando padrão
.DEFAULT_GOAL := help

