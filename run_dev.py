#!/usr/bin/env python
"""
Script para iniciar a aplicação TraderMinion em desenvolvimento local
Inicia o servidor Django e o cliente React/Vite
"""
import subprocess
import time
import sys
import os
from pathlib import Path

# Define os caminhos
PROJECT_ROOT = Path(__file__).parent
PYTHON_EXE = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
MANAGE_PY = PROJECT_ROOT / "manage.py"

def start_django_server():
    """Inicia o servidor Django"""
    print("=" * 70)
    print("Iniciando Servidor Django...")
    print("=" * 70)
    
    cmd = [str(PYTHON_EXE), str(MANAGE_PY), "runserver", "127.0.0.1:8000"]
    
    try:
        process = subprocess.Popen(
            cmd,
            cwd=str(PROJECT_ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        print(f"✓ Servidor Django iniciado (PID: {process.pid})")
        print("  URL: http://127.0.0.1:8000/api")
        print("  Admin: http://127.0.0.1:8000/admin")
        return process
    except Exception as e:
        print(f"✗ Erro ao iniciar servidor Django: {e}")
        return None

def print_instructions():
    """Imprime instruções de uso"""
    print("\n" + "=" * 70)
    print("TraderMinion - Aplicação de Acompanhamento de Operações Financeiras")
    print("=" * 70)
    print("\n📋 Endpoints da API disponíveis:")
    print("  GET    /api/trades/           - Listar todas as operações")
    print("  POST   /api/trades/           - Criar nova operação")
    print("  PATCH  /api/trades/{id}/      - Atualizar operação")
    print("  DELETE /api/trades/{id}/      - Deletar operação")
    print("  GET    /api/trades/stats/     - Obter estatísticas do dashboard")
    print("\n🔗 URLs importantes:")
    print("  API Backend:   http://127.0.0.1:8000/api/")
    print("  Admin Django:  http://127.0.0.1:8000/admin/")
    print("  Usuário Admin: admin / admin123")
    print("\n📝 Para testar a API, execute:")
    print("  python test_api.py")
    print("\n⚙️  Configurações:")
    print("  - Banco de dados: SQLite (db.sqlite3)")
    print("  - Media uploads: media/")
    print("  - CORS configurado para: http://localhost:3000, http://localhost:5173")
    print("=" * 70)

if __name__ == "__main__":
    try:
        print_instructions()
        
        # Inicia o servidor Django
        django_process = start_django_server()
        
        if django_process:
            time.sleep(2)  # Aguarda o servidor iniciar
            print("\n✓ Sistema pronto!")
            print("  Pressione CTRL+C para parar o servidor\n")
            
            # Mantém o servidor rodando
            try:
                django_process.wait()
            except KeyboardInterrupt:
                print("\n\nParando servidor Django...")
                django_process.terminate()
                django_process.wait()
                print("✓ Servidor parado")
                sys.exit(0)
    except KeyboardInterrupt:
        print("\n\nAplicação interrompida pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"✗ Erro: {e}")
        sys.exit(1)
