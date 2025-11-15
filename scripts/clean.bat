@echo off
REM Limpa arquivos temporários e cache

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo Limpando arquivos temporarios...

REM Remove __pycache__
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d" 2>nul

REM Remove arquivos .pyc
for /r . %%f in (*.pyc) do @if exist "%%f" del /q "%%f" 2>nul

REM Remove arquivos .pyo
for /r . %%f in (*.pyo) do @if exist "%%f" del /q "%%f" 2>nul

REM Remove diretórios .egg-info
for /d /r . %%d in (*.egg-info) do @if exist "%%d" rd /s /q "%%d" 2>nul

REM Remove diretórios build e dist do PyInstaller
if exist build rd /s /q build 2>nul
if exist dist rd /s /q dist 2>nul

echo [OK] Limpeza concluida!
pause

