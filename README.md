# TraderMinion - Acompanhamento de Operações de Especulações Financeiras

Aplicação web full-stack para acompanhamento de operações financeiras, desenvolvida com Django REST Framework (backend) e React + TypeScript + Vite (frontend).

## 🚀 Início Rápido

### Usando Makefile (Recomendado)

```bash
# Ver todos os comandos disponíveis
make help

# Setup completo (instala dependências e aplica migrações)
make setup

# Iniciar servidor backend Django
make server

# Em outro terminal: Iniciar frontend
make dev-frontend

# Testar API
make test
```

### Instalação Manual

Veja o arquivo [SETUP.md](SETUP.md) para instruções detalhadas de instalação manual.

## 📋 Endpoints da API

A aplicação está pronta para consumir o backend Django nos seguintes endpoints:

- `GET /api/dashboard/stats/` - Estatísticas do dashboard
- `GET /api/trades/` - Listar operações
- `POST /api/trades/` - Criar operação (com suporte a multipart/form-data para screenshots)
- `PATCH /api/trades/{id}/` - Atualizar operação
- `DELETE /api/trades/{id}/` - Deletar operação

## 🛠️ Comandos Makefile Disponíveis

| Comando | Descrição |
|---------|-----------|
| `make help` | Mostra todos os comandos disponíveis |
| `make setup` | Setup completo (instala dependências + migrações) |
| `make install` | Instala todas as dependências (backend + frontend) |
| `make install-backend` | Instala apenas dependências Python |
| `make install-frontend` | Instala apenas dependências Node.js |
| `make migrate` | Aplica migrações do banco de dados |
| `make makemigrations` | Cria novas migrações |
| `make server` | Inicia servidor Django (backend) |
| `make dev-frontend` | Inicia servidor de desenvolvimento do frontend |
| `make test` | Executa testes da API |
| `make clean` | Limpa arquivos temporários e cache |
| `make build-frontend` | Build de produção do frontend |

## 📚 Documentação

- [SETUP.md](SETUP.md) - Guia completo de instalação e configuração
- [API Documentation](#) - Documentação detalhada da API

## 🏗️ Tecnologias

- **Backend**: Django 5.2, Django REST Framework
- **Frontend**: React 18, TypeScript, Vite, TailwindCSS
- **Banco de Dados**: SQLite (desenvolvimento)
- **Outras**: Pillow (processamento de imagens), django-cors-headers

## 📝 Notas

- O servidor Django deve rodar em um terminal separado e permanecer aberto
- CORS está configurado para desenvolvimento local
- Screenshots são salvos em `media/screenshots/`
