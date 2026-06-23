# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: StudyTimer
import json, os, random, time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

INITIAL_DATA_JSON = '''
{
  "themes": [
    {"id": 1, "title": "Python Basics", "difficulty": "easy"},
    {"id": 2, "title": "Data Structures", "difficulty": "medium"},
    {"id": 3, "title": "Algorithms", "difficulty": "hard"}
  ],
  "goals": [
    {"id": 101, "theme_id": 1, "target_minutes": 45},
    {"id": 102, "theme_id": 2, "target_minutes": 60}
  ],
  "sessions_log": []
}'''

def load_initial_data() -> Dict[str, Any]:
    try:
        data_dict = json.loads(INITIAL_DATA_JSON)
        
        # Валидация структуры данных
        required_keys = {"themes", "goals", "sessions_log"}
        if not all(key in data_dict for key in required_keys):
            raise ValueError("Missing required keys in initial data")

        # Преобразование типов для удобства использования
        processed_data = {
            "themes": [dict(t) for t in data_dict["themes"]],
            "goals": [dict(g, status="pending", progress=0) for g in data_dict["goals"]],
            "sessions_log": []
        }

        # Генерация начального состояния для демо-сессий (опционально)
        if not processed_data["sessions_log"]:
            now = datetime.now()
            demo_session = {
                "id": 9001,
                "theme_id": 1,
                "start_time": str(now - timedelta(minutes=30)),
                "end_time": str(now),
                "duration_minutes": 25,
                "focus_score": random.randint(78, 95)
            }
            processed_data["sessions_log"].append(demo_session)

        return processed_data

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in initial data: {e}") from e
