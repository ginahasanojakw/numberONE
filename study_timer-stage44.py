# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: StudyTimer
import shutil, os

def backup_data_file(data_path, backup_dir="backups"):
    if not os.path.exists(data_path):
        return
    os.makedirs(backup_dir, exist_ok=True)
    ts = f"_backup_{os.path.getmtime(data_path):.0f}"
    shutil.copy2(data_path, os.path.join(backup_dir, os.path.basename(data_path) + ts))

def restore_data_file(data_path, backup_dir="backups"):
    if not os.path.exists(backup_dir):
        return
    for f in os.listdir(backup_dir):
        if f.startswith(os.path.basename(data_path)):
            shutil.copy2(os.path.join(backup_dir, f), data_path)
            return
