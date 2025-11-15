@echo off
REM TraderMinion - Setup Completo para Windows
REM Execute este arquivo com duplo clique para configurar o projeto

echo ======================================================================
echo TraderMinion - Setup Completo
echo ======================================================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado! Por favor, instale Python 3.9 ou superior.
    echo Baixe em: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/3] Instalando dependencias Python...
call scripts\install.bat
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias!
    pause
    exit /b 1
)

echo.
echo [2/3] Aplicando migracoes do banco de dados...
call scripts\migrate.bat
if errorlevel 1 (
    echo [ERRO] Falha ao aplicar migracoes!
    pause
    exit /b 1
)

echo.
echo [3/3] Verificando superusuario...
call scripts\check_superuser.bat

echo.
echo ======================================================================
echo Setup concluido com sucesso!
echo ======================================================================
echo.
echo Para iniciar o servidor backend:
echo   - Duplo clique em: start_all.bat (inicia tudo)
echo   - Ou execute: scripts\start_server.bat
echo.
echo Para iniciar a aplicacao desktop:
echo   - Duplo clique em: start_all.bat (inicia tudo)
echo   - Ou execute: scripts\start_desktop.bat
echo.
echo Para testar a API:
echo   - Duplo clique em: scripts\test_api.bat
echo.
pause

