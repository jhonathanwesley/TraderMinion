@echo off
REM Cria novas migrações

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo Criando novas migracoes...
python manage.py makemigrations

if errorlevel 1 (
    echo [ERRO] Falha ao criar migracoes!
    pause
    exit /b 1
)

echo [OK] Migracoes criadas com sucesso!
pause

