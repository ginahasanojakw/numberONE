# === Stage 45: Добавь восстановление из резервной копии ===
# Project: StudyTimer
import json
import os

def load_backup(backup_file, current_data):
    """Restore data from a backup JSON file."""
    if not os.path.exists(backup_file):
        return current_data
    try:
        with open(backup_file, 'r', encoding='utf-8') as f:
            backup = json.load(f)
        if isinstance(backup, dict):
            return backup
        else:
            return current_data
    except (json.JSONDecodeError, IOError):
        return current_data
