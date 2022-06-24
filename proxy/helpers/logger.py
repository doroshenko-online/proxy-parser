from datetime import datetime


def log(message: str, level: str = 'info') -> None:
    now = datetime.utcnow()
    print(f"[{now}] [{level.upper()}]: {message}")