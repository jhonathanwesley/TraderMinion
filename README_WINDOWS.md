# TraderMinion - Guia Rápido para Windows

## 🚀 Setup Rápido (Duplo Clique)

### 1. Setup Completo
**Duplo clique em:** `setup.bat`

Este script irá:
- ✅ Instalar todas as dependências Python
- ✅ Aplicar migrações do banco de dados
- ✅ Criar superusuário padrão (admin/admin123)

### 2. Iniciar Aplicação

**Opção 1 - Iniciar Tudo de Uma Vez (Recomendado):**
- Duplo clique em: `start_all.bat`
- Isso abrirá o servidor e o desktop em janelas separadas automaticamente

**Opção 2 - Iniciar Separadamente:**
- **Terminal 1 - Servidor Backend:**
  - Duplo clique em: `scripts\start_server.bat`
  - Aguarde a mensagem "Starting development server"
- **Terminal 2 - Aplicação Desktop:**
  - Duplo clique em: `scripts\start_desktop.bat`
  - A aplicação desktop será aberta

## 📋 Scripts Disponíveis

### Scripts Principais (Raiz do Projeto)
| Script | Descrição |
|--------|-----------|
| `setup.bat` | **Setup completo** - Instala tudo e configura o projeto |
| `start_all.bat` | **Inicia tudo** - Abre servidor e desktop em janelas separadas |

### Setup e Instalação (pasta `scripts/`)
| Script | Descrição |
|--------|-----------|
| `scripts\install.bat` | Instala apenas as dependências Python |
| `scripts\migrate.bat` | Aplica migrações do banco de dados |
| `scripts\makemigrations.bat` | Cria novas migrações |
| `scripts\createsuperuser.bat` | Cria um superusuário Django |

### Executar Aplicação (pasta `scripts/`)
| Script | Descrição |
|--------|-----------|
| `scripts\start_server.bat` | Inicia servidor Django (backend) |
| `scripts\start_desktop.bat` | Inicia aplicação desktop Kivy |
| `scripts\run_all.ps1` | Inicia servidor e desktop juntos (PowerShell) |

### Testes e Build (pasta `scripts/`)
| Script | Descrição |
|--------|-----------|
| `scripts\test_api.bat` | Executa testes da API |
| `scripts\build_desktop.bat` | Compila aplicação desktop com PyInstaller |

### Utilitários (pasta `scripts/`)
| Script | Descrição |
|--------|-----------|
| `scripts\clean.bat` | Limpa arquivos temporários e cache |
| `scripts\shell.bat` | Abre shell interativo do Django |
| `scripts\help.bat` | Mostra ajuda sobre os comandos |

## 🔧 Requisitos

- **Python 3.9+** - [Download](https://www.python.org/downloads/)
- **pip** - Geralmente vem com Python

## 📝 Notas Importantes

1. **Primeira Execução**: Sempre execute `setup.bat` primeiro
2. **Servidor Django**: Deve estar rodando antes de iniciar o desktop
3. **Superusuário Padrão**: 
   - Usuário: `admin`
   - Senha: `admin123`
4. **URLs**:
   - API: http://127.0.0.1:8000/api/
   - Admin: http://127.0.0.1:8000/admin/

## 🐛 Solução de Problemas

### Python não encontrado
- Instale Python 3.9+ do site oficial
- Marque a opção "Add Python to PATH" durante a instalação
- Reinicie o terminal após instalar

### Erro "ModuleNotFoundError: No module named 'kivy'"
- Execute `setup.bat` novamente para instalar todas as dependências
- Ou execute manualmente: `python -m pip install -r requirements.txt`
- Verifique se está usando o mesmo Python: `python --version`

### Erro ao instalar dependências
- Execute: `python -m pip install --upgrade pip`
- Tente novamente: `install.bat` ou `setup.bat`
- Se usar virtualenv, certifique-se de que está ativado

### Porta 8000 já em uso
- Feche outros servidores Django
- Ou altere a porta em `start_server.bat`: `python manage.py runserver 127.0.0.1:8001`

### Aplicação desktop não conecta
- Verifique se o servidor está rodando (execute `start_server.bat`)
- Verifique se a URL está correta: http://127.0.0.1:8000/api/
- Verifique se não há firewall bloqueando a conexão

## 💡 Dicas

- Use `help.bat` para ver todos os comandos disponíveis
- Use `run_all.ps1` (PowerShell) para iniciar tudo de uma vez
- O executável compilado estará em `dist\TraderMinion.exe`

