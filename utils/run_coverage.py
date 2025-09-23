import subprocess
import sys
from datetime import datetime
from pathlib import Path


def ensure_reports_dir():
    """Crear carpeta tests/coverage_reports si no existe"""
    reports_dir = Path("tests/coverage_reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir


def main():
    print("\n🎯 CONFIGURACIÓN DEL REPORTE DE COVERAGE")
    print("=" * 50)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    reports_dir = ensure_reports_dir()
    htmlcov_dir = reports_dir / f"htmlcov_{timestamp}"

    print("\n🚀 Iniciando análisis de coverage...")
    print(f"   📁 Reporte HTML: {htmlcov_dir}")
    print("=" * 50)

    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "--cov=core",
        "--cov=data",
        "--cov-report=term-missing",
        f"--cov-report=html:{htmlcov_dir}",
        "tests/",
    ]

    print(f"🔧 Ejecutando: {' '.join(cmd)}")
    exit_code = subprocess.call(cmd)

    result = "✅ ÉXITO" if exit_code == 0 else "❌ FALLOS"
    print(f"\n{result}")
    print(f"   📊 Reporte HTML: {htmlcov_dir}")
    print(f"   📋 Código: {exit_code}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
