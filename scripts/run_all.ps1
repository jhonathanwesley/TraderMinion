# TraderMinion - Script PowerShell para executar servidor e desktop juntos
# Este script inicia o servidor Django e a aplicação desktop em processos separados

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "TraderMinion - Iniciando Servidor e Desktop" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERRO] Python não encontrado! Por favor, instale Python 3.9 ou superior." -ForegroundColor Red
    Write-Host "Baixe em: https://www.python.org/downloads/" -ForegroundColor Yellow
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Muda para o diretório raiz do projeto
$rootDir = Split-Path -Parent $PSScriptRoot
Set-Location $rootDir

# Inicia servidor Django em background
Write-Host "[1/2] Iniciando servidor Django..." -ForegroundColor Yellow
$serverJob = Start-Job -ScriptBlock {
    $root = $using:rootDir
    Set-Location $root
    python manage.py runserver 127.0.0.1:8000
}

# Aguarda alguns segundos para o servidor iniciar
Start-Sleep -Seconds 3

# Verifica se o servidor está rodando
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api/" -TimeoutSec 2 -UseBasicParsing -ErrorAction Stop
    Write-Host "[OK] Servidor Django iniciado com sucesso!" -ForegroundColor Green
} catch {
    Write-Host "[AVISO] Servidor pode não estar pronto ainda. Continuando..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[2/2] Iniciando aplicação desktop..." -ForegroundColor Yellow
Write-Host ""

# Inicia aplicação desktop
try {
    Set-Location $rootDir
    python main_desktop.py
} catch {
    Write-Host "[ERRO] Falha ao iniciar aplicação desktop!" -ForegroundColor Red
}

# Quando a aplicação desktop fechar, para o servidor
Write-Host ""
Write-Host "Parando servidor Django..." -ForegroundColor Yellow
Stop-Job $serverJob
Remove-Job $serverJob

Write-Host "[OK] Servidor parado." -ForegroundColor Green
Read-Host "Pressione Enter para sair"

