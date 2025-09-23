import sys
import os
import pytest

# Añadir el path del proyecto
sys.path.insert(0, os.path.dirname(__file__))

def run_specific_test():
    """Ejecuta un test específico manualmente"""
    
    # Configurar environment
    os.environ['PYTHONPATH'] = os.path.dirname(__file__)
    
    # Ejecutar pytest manualmente
    pytest.main([
        "tests/test_bug_repository.py::test_bug_repository_create",
        "-v", 
        "-s",
        "--tb=short"
    ])

if __name__ == "__main__":
    print("=== EJECUTANDO DEBUG MANUAL ===")
    run_specific_test()