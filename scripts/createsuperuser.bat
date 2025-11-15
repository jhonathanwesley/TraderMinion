@echo off
REM Cria um superusuário Django

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo Criando superusuario...
python manage.py createsuperuser

if errorlevel 1 (
    echo [ERRO] Falha ao criar superusuario!
    pause
    exit /b 1
)

echo [OK] Superusuario criado com sucesso!
pause

