@echo off
REM Verifica se existe superusuário, se não existir, cria um padrão

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

python create_superuser.py 2>nul
if errorlevel 1 (
    echo [INFO] Execute createsuperuser.bat para criar um superusuario manualmente.
) else (
    echo [OK] Superusuario verificado/criado.
)

