@echo off
REM Inicia a aplicação desktop

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo ======================================================================
echo TraderMinion - Aplicacao Desktop
echo ======================================================================
echo.

REM Verifica se Kivy está instalado
python -c "import kivy" >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Kivy nao encontrado!
    echo.
    echo As dependencias nao estao instaladas.
    echo Execute setup.bat primeiro para instalar todas as dependencias.
    echo.
    pause
    exit /b 1
)

echo Certifique-se de que o servidor Django esta rodando!
echo Execute start_server.bat em outro terminal se necessario.
echo.

python main_desktop.py

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao iniciar aplicacao desktop!
    echo Verifique se todas as dependencias estao instaladas.
    pause
)

