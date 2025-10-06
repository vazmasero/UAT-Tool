"""Configuración centralizada de logging."""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logging(verbose=False, log_level="INFO", log_file="uat_tool.log"):
    """
    Configura el logging para toda la aplicación.

    Args:
        verbose: Si es True, muestra DEBUG en consola
        log_level: Nivel para archivo (DEBUG, INFO, WARNING, ERROR)
        log_file: Nombre del archivo de log
    """
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Niveles
    console_level = logging.DEBUG if verbose else logging.INFO
    file_level = getattr(logging, log_level.upper(), logging.INFO)

    # Handlers
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(console_level)
    console_handler.setFormatter(logging.Formatter("%(message)s"))

    file_handler = RotatingFileHandler(
        log_dir / log_file,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
        encoding="utf-8",
        mode='w' # Si no pones mode es append por defecto
    )
    file_handler.setLevel(file_level)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    # Configurar root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Limpiar handlers existentes y añadir nuevos
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Evitar propagación a logger root externo
    root_logger.propagate = False


def get_logger(name: str) -> logging.Logger:
    """Obtiene un logger configurado."""
    return logging.getLogger(name)
