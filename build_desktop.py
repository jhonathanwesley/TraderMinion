"""
Script para build da aplicação desktop com PyInstaller
"""
import subprocess
import sys
import os
from pathlib import Path

def build_app():
    """Compila a aplicação desktop"""
    print("=" * 70)
    print("TraderMinion - Build Desktop App")
    print("=" * 70)
    
    # Verifica se PyInstaller está instalado
    try:
        import PyInstaller
    except ImportError:
        print("❌ PyInstaller não está instalado!")
        print("Instale com: pip install pyinstaller")
        sys.exit(1)
    
    # Caminho do arquivo spec
    spec_file = Path(__file__).parent / "build.spec"
    
    if not spec_file.exists():
        print(f"❌ Arquivo {spec_file} não encontrado!")
        sys.exit(1)
    
    print(f"\n📦 Compilando aplicação...")
    print(f"   Arquivo spec: {spec_file}")
    
    # Executa PyInstaller
    try:
        cmd = [
            sys.executable,
            "-m", "PyInstaller",
            str(spec_file),
            "--clean",
            "--noconfirm"
        ]
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("\n✅ Build concluído com sucesso!")
        print(f"\n📁 Executável criado em: dist/TraderMinion.exe")
        print("\n💡 Nota: Certifique-se de que o servidor Django está rodando")
        print("   antes de executar a aplicação desktop.")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erro durante o build:")
        print(e.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_app()

