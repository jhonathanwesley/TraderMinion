@echo off
REM TraderMinion - Inicia Servidor e Desktop
REM Este script inicia o servidor Django e a aplicação desktop em janelas separadas

echo ======================================================================
echo TraderMinion - Iniciando Servidor e Desktop
echo ======================================================================
echo.
echo Iniciando servidor Django em uma nova janela...
echo.

REM Inicia o servidor Django em uma nova janela
start "TraderMinion - Servidor Django" cmd /k "cd /d %~dp0 && scripts\start_server.bat"

REM Aguarda alguns segundos para o servidor iniciar
echo Aguardando servidor iniciar...
timeout /t 5 /nobreak >nul

echo Iniciando aplicacao desktop em uma nova janela...
echo.

REM Inicia a aplicação desktop em uma nova janela
start "TraderMinion - Desktop App" cmd /k "cd /d %~dp0 && scripts\start_desktop.bat"

echo.
echo ======================================================================
echo Servidor e Desktop iniciados!
echo ======================================================================
echo.
echo Duas janelas foram abertas:
echo   1. Servidor Django (backend)
echo   2. Aplicacao Desktop (frontend)
echo.
echo Para parar, feche as janelas ou pressione CTRL+C em cada uma.
echo.
pause

