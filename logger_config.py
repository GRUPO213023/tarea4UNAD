import logging
from pathlib import Path

LOG_DIR = Path('logs')
LOG_FILE = LOG_DIR / 'software_fj.log'

def configurar_logger():
    LOG_DIR.mkdir(exist_ok=True)

    logger = logging.getLogger('software_fj')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        formato = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        manejador = logging.FileHandler(LOG_FILE, encoding='utf-8')
        manejador.setFormatter(formato)
        logger.addHandler(manejador)

    return logger