from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "siem.db"
LOG_PATH = DATA_DIR / "events.jsonl"
DATA_DIR.mkdir(exist_ok=True)
