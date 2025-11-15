@echo off
REM Aplica migrações do banco de dados

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo Aplicando migracoes...
python manage.py migrate

if errorlevel 1 (
    echo [ERRO] Falha ao aplicar migracoes!
    exit /b 1
)

echo [OK] Migracoes aplicadas com sucesso!
exit /b 0

