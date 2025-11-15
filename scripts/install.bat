@echo off
REM Instala dependências Python

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo Instalando dependencias do backend...
echo.

REM Atualiza pip
echo [1/3] Atualizando pip...
python -m pip install --upgrade pip --quiet
if errorlevel 1 (
    echo [ERRO] Falha ao atualizar pip!
    exit /b 1
)

REM Instala dependências
echo [2/3] Instalando dependencias do requirements.txt...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias!
    exit /b 1
)

REM Verifica instalação
echo [3/3] Verificando instalacao...
python -c "import django; import kivy; import requests" >nul 2>&1
if errorlevel 1 (
    echo [AVISO] Algumas dependencias podem nao estar instaladas corretamente.
    echo Tente executar novamente: python -m pip install -r requirements.txt
    exit /b 1
)

echo.
echo [OK] Dependencias instaladas com sucesso!
echo.
exit /b 0

