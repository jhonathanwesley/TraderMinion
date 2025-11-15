@echo off
REM Executa testes da API

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo ======================================================================
echo TraderMinion - Testes da API
echo ======================================================================
echo.
echo Certifique-se de que o servidor Django esta rodando!
echo Execute start_server.bat se necessario.
echo.

python test_api.py

if errorlevel 1 (
    echo.
    echo [ERRO] Alguns testes falharam!
    pause
    exit /b 1
)

echo.
echo [OK] Todos os testes passaram!
pause

