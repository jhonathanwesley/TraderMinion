@echo off
REM Abre o shell interativo do Django

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo Abrindo shell interativo do Django...
python manage.py shell

