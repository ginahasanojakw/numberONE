# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: StudyTimer
import json, os, time
DATA_FILE = "study_timer_data.json"
def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[Ошибка сохранения] {e}")

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"sessions": [], "breaks": 0, "focus_minutes": 0}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстанавливаем таймеры из сохраненных данных (упрощено для примера)
        return data
    except Exception as e:
        print(f"[Ошибка загрузки] {e}")
        return {"sessions": [], "breaks": 0, "focus_minutes": 0}

# Пример использования в цикле программы:
# current_data = load_state()
# ... логика работы с данными ...
# save_state(current_data)
