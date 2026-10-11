import json
import os
from pathlib import Path

DEFAULT_CONFIG = {
    "database_file_path": "baza\\Kostka Lagerplatz.xlsx",
    "usage_subtraction_file_path": "dane\\Odejmowanie",
    "usage_addition_file_path": "dane\\Dodawanie",
    "done_folder_path": "dane\\Gotowe",
    "usage_worksheet": "Materialliste",
    "usage_workdatasheet": "M0129",
    "substraction_start_row": 2,
    "addition_start_row": 2,
    "database_start_row": 2,
}


def resolve_config_path() -> Path:
    base_dir = Path(__file__).resolve().parent.parent
    if os.name == "nt":
        return base_dir / "config_win.json"
    for file_name in ("config.json", "config_mac.json"):
        candidate = base_dir / file_name
        if candidate.exists():
            return candidate
    return base_dir / "config_mac.json"


def load_config(config_path: str | Path | None = None):
    if config_path is None:
        config_path = resolve_config_path()
    config_path = Path(config_path)

    if not config_path.exists():
        return DEFAULT_CONFIG.copy()

    with config_path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)

    merged = DEFAULT_CONFIG.copy()
    merged.update(data)
    return merged


def save_config(config_data, config_path: str | Path | None = None):
    if config_path is None:
        config_path = resolve_config_path()
    config_path = Path(config_path)
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with config_path.open("w", encoding="utf-8") as fh:
        json.dump(config_data, fh, indent=4)

    return config_path
