@echo off
REM Inicia o servidor Django

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo ======================================================================
echo TraderMinion - Servidor Django
echo ======================================================================
echo.

REM Verifica se Django está instalado
python -c "import django" >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Django nao encontrado!
    echo.
    echo As dependencias nao estao instaladas.
    echo Execute setup.bat primeiro para instalar todas as dependencias.
    echo.
    pause
    exit /b 1
)

echo Servidor iniciando em: http://127.0.0.1:8000
echo Admin disponivel em: http://127.0.0.1:8000/admin
echo API disponivel em: http://127.0.0.1:8000/api
echo.
echo Pressione CTRL+C para parar o servidor
echo.

python manage.py runserver 127.0.0.1:8000

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao iniciar servidor!
    pause
)

