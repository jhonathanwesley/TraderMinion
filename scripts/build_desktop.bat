@echo off
REM Compila a aplicação desktop com PyInstaller

REM Muda para o diretório raiz do projeto
cd /d %~dp0\..

echo ======================================================================
echo TraderMinion - Build Desktop App
echo ======================================================================
echo.

REM Verifica se PyInstaller está instalado
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [INFO] PyInstaller nao encontrado. Instalando...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar PyInstaller!
        pause
        exit /b 1
    )
)

echo Compilando aplicacao desktop...
python build_desktop.py

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao compilar aplicacao!
    pause
    exit /b 1
)

echo.
echo [OK] Build concluido com sucesso!
echo Executavel criado em: dist\TraderMinion.exe
echo.
pause

