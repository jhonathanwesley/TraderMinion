# TraderMinion - Setup Local

## 🚀 Como executar a aplicação localmente

### Pré-requisitos
- Python 3.9+
- Node.js 18+ e npm
- Make (opcional, mas recomendado)
  - **Windows**: Instale via [Chocolatey](https://chocolatey.org/) (`choco install make`) ou use Git Bash/WSL
  - **Linux/Mac**: Geralmente já vem instalado

## 🎯 Método 1: Usando Makefile (Recomendado)

O Makefile simplifica todo o processo de setup e execução:

### Setup Inicial

```bash
# Ver todos os comandos disponíveis
make help

# Setup completo (instala dependências e aplica migrações)
make setup
```

### Executar a Aplicação

```bash
# Terminal 1: Iniciar servidor backend Django
make server

# Terminal 2: Iniciar servidor frontend (opcional, se quiser rodar o frontend)
make dev-frontend
```

### Outros Comandos Úteis

```bash
# Instalar apenas dependências do backend
make install-backend

# Instalar apenas dependências do frontend
make install-frontend

# Aplicar migrações
make migrate

# Criar novas migrações
make makemigrations

# Criar superusuário
make createsuperuser

# Testar API
make test

# Limpar arquivos temporários
make clean

# Build de produção do frontend
make build-frontend
```

## 📝 Método 2: Instalação Manual

Se preferir não usar o Makefile, siga os passos abaixo:

### Passo 1: Instalar dependências do backend

```bash
pip install -r requirements.txt
```

### Passo 2: Instalar dependências do frontend

```bash
cd client
npm install
cd ..
```

### Passo 3: Criar/Aplicar migrações do banco de dados

```bash
python manage.py migrate
```

### Passo 4: Criar superusuário (opcional, para acessar admin)

```bash
python manage.py createsuperuser
# ou usar as credenciais padrão: admin / admin123
```

### Passo 5: Iniciar o servidor Django (em um terminal)

```bash
python manage.py runserver
```

O servidor estará disponível em: **http://127.0.0.1:8000**

### Passo 6: Iniciar o frontend (em outro terminal, opcional)

```bash
cd client
npm run dev
```

### Passo 7: Testar a API (em outro terminal)

```bash
python test_api.py
```

## 📋 Endpoints disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/trades/` | Listar todas as operações |
| POST | `/api/trades/` | Criar nova operação |
| PATCH | `/api/trades/{id}/` | Atualizar operação |
| DELETE | `/api/trades/{id}/` | Deletar operação |
| GET | `/api/dashboard/stats/` | Obter estatísticas do dashboard |
| GET | `/api/trades/stats/` | Obter estatísticas do dashboard (alternativo) |

## 🔗 URLs importantes

- **API REST**: http://127.0.0.1:8000/api/
- **Admin Django**: http://127.0.0.1:8000/admin/
- **Usuário Admin**: `admin` / `admin123`

## 📝 Exemplos de requisição

### Criar uma operação (POST)

```bash
curl -X POST http://127.0.0.1:8000/api/trades/ \
  -H "Content-Type: application/json" \
  -d '{
    "asset": "BTC/USD",
    "type": "BUY",
    "category": "CRYPTO",
    "quantity": "0.5",
    "entry_price": "45000.00",
    "exit_price": "46000.00",
    "status": "CLOSED",
    "notes": "Trade de compra"
  }'
```

### Listar operações (GET)

```bash
curl http://127.0.0.1:8000/api/trades/
```

### Obter estatísticas (GET)

```bash
curl http://127.0.0.1:8000/api/dashboard/stats/
```

### Atualizar operação (PATCH)

```bash
curl -X PATCH http://127.0.0.1:8000/api/trades/1/ \
  -H "Content-Type: application/json" \
  -d '{"notes": "Trade atualizado"}'
```

### Deletar operação (DELETE)

```bash
curl -X DELETE http://127.0.0.1:8000/api/trades/1/
```

## 🐞 Estrutura do banco de dados

### Modelo Trade

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | ID único |
| asset | String | Nome do ativo (ex: BTC/USD) |
| type | Choice | BUY ou SELL |
| category | Choice | CRYPTO, STOCKS, FOREX, DERIVATIVES |
| quantity | Decimal | Quantidade operada |
| entry_price | Decimal | Preço de entrada |
| exit_price | Decimal | Preço de saída (opcional) |
| stop_loss | Decimal | Preço de stop loss (opcional) |
| take_profit | Decimal | Preço de take profit (opcional) |
| status | Choice | OPEN, CLOSED, PENDING |
| opened_at | DateTime | Data/hora de abertura |
| closed_at | DateTime | Data/hora de fechamento (opcional) |
| notes | Text | Anotações sobre a operação |
| screenshot | Image | Screenshot da operação (opcional) |
| profit_loss | Decimal (calculado) | Lucro/Prejuízo |
| profit_loss_percentage | Decimal (calculado) | Lucro/Prejuízo em % |

## 🌐 Integração Frontend

O frontend (React/Vite) faz requisições para:
- `http://localhost:8000/api/trades/`
- `http://localhost:8000/api/dashboard/stats/`

CORS está configurado para aceitar requisições de:
- `http://localhost:3000`
- `http://localhost:5173`
- `http://127.0.0.1:3000`
- `http://127.0.0.1:5173`

## 📁 Estrutura do projeto

```
TraderMinion/
├── app/                    # Configurações Django
│   ├── settings.py         # Configurações do projeto
│   ├── urls.py             # Rotas principais
│   ├── wsgi.py
│   └── asgi.py
├── logger/                 # App principal
│   ├── models.py           # Modelo Trade
│   ├── views.py            # ViewSet da API
│   ├── serializers.py      # Serializers DRF
│   ├── admin.py            # Admin do Django
│   └── migrations/
├── client/                 # Frontend React/Vite
│   ├── src/
│   │   ├── components/     # Componentes React
│   │   ├── services/       # API client
│   │   ├── types/          # TypeScript types
│   │   └── contexts/       # React contexts
│   └── vite.config.js
├── media/                  # Uploads (screenshots)
├── db.sqlite3              # Banco de dados
├── manage.py               # Django CLI
├── test_api.py             # Script de testes
├── requirements.txt        # Dependências Python
└── README.md
```

## ⚙️ Configurações importantes

### CORS (Cross-Origin Resource Sharing)
Habilitado no `settings.py` para aceitar requisições do frontend local.

### Media files
Uploads de screenshots salvos em `media/screenshots/`

### Database
SQLite (`db.sqlite3`) para desenvolvimento local.

## 🧪 Testando

### Usando Makefile

```bash
make test
```

### Manualmente

```bash
python test_api.py
```

Este script:
1. ✓ Lista trades
2. ✓ Cria um novo trade
3. ✓ Obtém estatísticas
4. ✓ Cria outro trade com loss
5. ✓ Atualiza trade
6. ✓ Deleta trade

## 🧹 Limpeza

### Usando Makefile

```bash
# Limpar arquivos temporários e cache
make clean

# Remover banco de dados (CUIDADO: apaga todos os dados!)
make clean-db
```

### Manualmente

```bash
# Limpar cache Python
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# Limpar node_modules (se necessário)
rm -rf client/node_modules
```

## 🛠️ Comandos Makefile Completos

| Comando | Descrição |
|---------|-----------|
| `make help` | Mostra todos os comandos disponíveis |
| `make setup` | Setup completo (instala dependências + migrações) |
| `make install` | Instala todas as dependências (backend + frontend) |
| `make install-backend` | Instala apenas dependências Python |
| `make install-frontend` | Instala apenas dependências Node.js |
| `make migrate` | Aplica migrações do banco de dados |
| `make makemigrations` | Cria novas migrações |
| `make createsuperuser` | Cria um superusuário Django |
| `make server` | Inicia servidor Django (backend) |
| `make dev-backend` | Alias para `make server` |
| `make dev-frontend` | Inicia servidor de desenvolvimento do frontend |
| `make test` | Executa testes da API |
| `make test-api` | Alias para `make test` |
| `make clean` | Limpa arquivos temporários e cache |
| `make clean-db` | Remove o banco de dados SQLite (CUIDADO!) |
| `make build-frontend` | Build de produção do frontend |
| `make collectstatic` | Coleta arquivos estáticos (Django) |
| `make shell` | Abre o shell interativo do Django |
| `make check` | Verifica o código com linters |
| `make typecheck` | Verifica tipos TypeScript |

## 📞 Suporte

Para mais informações sobre Django REST Framework:
- Documentação: https://www.django-rest-framework.org/
- DRF ViewSets: https://www.django-rest-framework.org/api-guide/viewsets/

## 💡 Dicas

- **Windows**: Se não tiver `make` instalado, você pode usar Git Bash ou WSL para executar os comandos do Makefile
- **Primeira execução**: Sempre execute `make setup` na primeira vez para configurar tudo
- **Servidor Django**: Deve rodar em um terminal separado e permanecer aberto (não há modo detached no servidor de desenvolvimento)
- **Frontend**: O frontend é opcional se você quiser apenas testar a API diretamente
