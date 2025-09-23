import subprocess
import sys
from datetime import datetime
from pathlib import Path


def ensure_reports_dir():
    """Crear carpeta tests/reports si no existe"""
    reports_dir = Path("tests/reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir


def main():
    print("\n🎯 CONFIGURACIÓN DEL REPORTE DE TESTS")
    print("=" * 40)

    comment = input("💬 Comentario/contexto del test: ").strip() or "Sin comentario"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_file = ensure_reports_dir() / f"test_{timestamp}.html"

    print("\n🚀 Iniciando tests...")
    print(f"   📝 Comentario: {comment}")
    print(f"   💾 Reporte: {html_file}")
    print("=" * 50)

    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-p",
        "pytest_html",
        "-v",
        "tests/unit/",
        f"--html={html_file}",
        "--self-contained-html",
    ]

    print(f"🔧 Ejecutando: {' '.join(cmd)}")
    exit_code = subprocess.call(cmd)

    result = "✅ ÉXITO" if exit_code == 0 else "❌ FALLOS"
    print(f"\n{result}")
    print(f"   📊 Reporte: {html_file}")
    print(f"   📋 Código: {exit_code}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
