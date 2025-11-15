@echo off
REM Mostra ajuda sobre os comandos disponíveis

echo ======================================================================
echo TraderMinion - Comandos Disponiveis
echo ======================================================================
echo.
echo SETUP E INSTALACAO:
echo   setup.bat              - Setup completo (instala dependencias + migracoes)
echo   scripts\install.bat    - Instala dependencias Python
echo   scripts\migrate.bat    - Aplica migracoes do banco de dados
echo   scripts\makemigrations.bat - Cria novas migracoes
echo   scripts\createsuperuser.bat - Cria um superusuario Django
echo.
echo EXECUTAR APLICACAO:
echo   start_all.bat          - Inicia servidor E desktop (recomendado)
echo   scripts\start_server.bat - Inicia servidor Django (backend)
echo   scripts\start_desktop.bat - Inicia aplicacao desktop Kivy
echo.
echo TESTES E BUILD:
echo   scripts\test_api.bat   - Executa testes da API
echo   scripts\build_desktop.bat - Compila aplicacao desktop com PyInstaller
echo.
echo UTILITARIOS:
echo   scripts\clean.bat      - Limpa arquivos temporarios e cache
echo   scripts\shell.bat      - Abre shell interativo do Django
echo   scripts\help.bat       - Mostra esta ajuda
echo.
echo ======================================================================
echo.
echo DICA: Para setup completo, execute setup.bat com duplo clique!
echo.
pause

