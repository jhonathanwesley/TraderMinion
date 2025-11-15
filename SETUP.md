# TraderMinion - Setup Local

## 🚀 Como executar a aplicação localmente

### Pré-requisitos
- Python 3.9+
- Virtualenv ativado

### Passo 1: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 2: Criar/Aplicar migrações do banco de dados

```bash
python manage.py migrate
```

### Passo 3: Criar superusuário (opcional, para acessar admin)

```bash
python manage.py createsuperuser
# ou usar as credenciais padrão: admin / admin123
```

### Passo 4: Iniciar o servidor Django (em um terminal)

```bash
python manage.py runserver
```

O servidor estará disponível em: **http://127.0.0.1:8000**

### Passo 5: Em outro terminal, testar a API

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
| GET | `/api/trades/stats/` | Obter estatísticas do dashboard |

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
curl http://127.0.0.1:8000/api/trades/stats/
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
- `http://localhost:8000/api/trades/stats/`

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

Execute o script de teste para validar todos os endpoints:

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

## 📞 Suporte

Para mais informações sobre Django REST Framework:
- Documentação: https://www.django-rest-framework.org/
- DRF ViewSets: https://www.django-rest-framework.org/api-guide/viewsets/
