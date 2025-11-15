# Scripts TraderMinion

Esta pasta contém todos os scripts de automação do projeto.

## Scripts Disponíveis

### Setup e Instalação
- `install.bat` - Instala dependências Python
- `migrate.bat` - Aplica migrações do banco de dados
- `makemigrations.bat` - Cria novas migrações
- `createsuperuser.bat` - Cria um superusuário Django
- `check_superuser.bat` - Verifica/cria superusuário padrão

### Executar Aplicação
- `start_server.bat` - Inicia servidor Django (backend)
- `start_desktop.bat` - Inicia aplicação desktop Kivy
- `run_all.ps1` - Inicia servidor e desktop juntos (PowerShell)

### Testes e Build
- `test_api.bat` - Executa testes da API
- `build_desktop.bat` - Compila aplicação desktop com PyInstaller

### Utilitários
- `clean.bat` - Limpa arquivos temporários e cache
- `shell.bat` - Abre shell interativo do Django
- `help.bat` - Mostra ajuda sobre os comandos

### Makefile
- `Makefile` - Scripts para Linux/Mac (equivalente aos .bat)

## Nota

Todos os scripts mudam automaticamente para o diretório raiz do projeto antes de executar, então podem ser chamados de qualquer lugar.

