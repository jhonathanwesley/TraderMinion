# TraderMinion - Acompanhamento de Operações de Especulações Financeiras

Aplicação desktop para acompanhamento de operações financeiras com:
- **Backend**: Django REST Framework (API REST)
- **Desktop App**: Python + Kivy (aplicação desktop nativa)

## 🚀 Início Rápido

### Windows (Recomendado - Duplo Clique)

1. **Setup Completo**: Duplo clique em `setup.bat`
2. **Iniciar Tudo**: Duplo clique em `start_all.bat` (abre servidor e desktop automaticamente)
   - Ou inicie separadamente: `scripts\start_server.bat` e `scripts\start_desktop.bat`

### Linux/Mac (Makefile)

```bash
# Ver todos os comandos disponíveis
make help

# Setup completo (instala dependências e aplica migrações)
make setup

# Terminal 1: Iniciar servidor backend Django
make server

# Terminal 2: Iniciar aplicação desktop
make desktop

# Para compilar executável standalone:
make build-desktop
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
| `make install` | Instala todas as dependências (backend) |
| `make install-backend` | Instala dependências Python |
| `make migrate` | Aplica migrações do banco de dados |
| `make makemigrations` | Cria novas migrações |
| `make server` | Inicia servidor Django (backend) |
| `make desktop` | Inicia aplicação desktop Kivy |
| `make build-desktop` | Compila aplicação desktop com PyInstaller |
| `make test` | Executa testes da API |
| `make clean` | Limpa arquivos temporários e cache |

## 📚 Documentação

- [SETUP.md](SETUP.md) - Guia completo de instalação e configuração
- [API Documentation](#) - Documentação detalhada da API

## 🏗️ Tecnologias

- **Backend**: Django 5.2, Django REST Framework
- **Desktop App**: Python 3.9+, Kivy 2.2+
- **Banco de Dados**: SQLite (desenvolvimento)
- **Build**: PyInstaller (para executável desktop)
- **Outras**: Pillow (processamento de imagens), django-cors-headers, requests

## 📱 Aplicação Desktop

A aplicação desktop é a interface principal, desenvolvida com Kivy para uma experiência nativa. Ela se comunica com o backend Django via API REST.

### Características:
- ✅ Interface moderna e intuitiva
- ✅ Dashboard com estatísticas em tempo real
- ✅ Registro de operações com upload de screenshots
- ✅ Design moderno e responsivo
- ✅ Compilável em executável standalone com PyInstaller

### Executar no Windows:
1. Duplo clique em `start_server.bat` (Terminal 1)
2. Duplo clique em `start_desktop.bat` (Terminal 2)

### Executar no Linux/Mac:
```bash
# Certifique-se de que o backend está rodando
make server

# Em outro terminal
make desktop
```

### Compilar executável:
- **Windows**: Duplo clique em `scripts\build_desktop.bat`
- **Linux/Mac**: `make build-desktop` (na pasta scripts)
- O executável estará em `dist/TraderMinion.exe` (Windows) ou `dist/TraderMinion` (Linux/Mac)

## 📝 Notas

- O servidor Django deve rodar em um terminal separado e permanecer aberto
- A aplicação desktop se conecta ao backend em `http://localhost:8000/api`
- CORS está configurado para desenvolvimento local
- Screenshots são salvos em `media/screenshots/`
- O executável compilado ainda requer o backend Django rodando (não é totalmente standalone)
