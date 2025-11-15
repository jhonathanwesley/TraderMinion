#!/usr/bin/env python
"""
Simple wrapper to keep the server running
"""
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
PYTHON_EXE = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
MANAGE_PY = PROJECT_ROOT / "manage.py"

def run_server():
    """Run the Django development server"""
    cmd = [
        str(PYTHON_EXE),
        str(MANAGE_PY),
        "runserver",
        "127.0.0.1:8000",
        "--nothreading",
        "--noreload"
    ]
    
    try:
        print("=" * 70)
        print("TraderMinion - Servidor de Desenvolvimento")
        print("=" * 70)
        print("\n✓ Servidor iniciado em http://127.0.0.1:8000")
        print("✓ Admin em http://127.0.0.1:8000/admin (admin / admin123)")
        print("✓ API em http://127.0.0.1:8000/api/")
        print("\nPressione CTRL+C para parar\n")
        
        subprocess.run(cmd, cwd=str(PROJECT_ROOT), check=False)
    except KeyboardInterrupt:
        print("\n\n✓ Servidor parado")
        sys.exit(0)

if __name__ == "__main__":
    run_server()
