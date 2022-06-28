from datetime import datetime
from multiprocessing import current_process


def log(message: str, level: str = 'info') -> None:
    now = datetime.utcnow()
    print(f"[{now}][{level.upper()}][{current_process().name}]: {message}")