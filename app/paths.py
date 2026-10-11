import os
from pathlib import Path


def _normalize_separators(value: str) -> str:
    return value.replace("/", os.sep).replace("\\", os.sep)


def ensure_folder(path: str | Path) -> Path:
    folder = Path(_normalize_separators(str(path)))
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def normalize_paths(config):
    root_dir = Path(__file__).resolve().parent.parent
    result = dict(config)
    for key in (
        "database_file_path",
        "usage_subtraction_file_path",
        "usage_addition_file_path",
        "done_folder_path",
    ):
        value = result.get(key)
        if value:
            normalized = _normalize_separators(str(value))
            resolved = Path(normalized)
            if not resolved.is_absolute():
                result[key] = str((root_dir / resolved).resolve())
            else:
                result[key] = str(resolved)
    return result
