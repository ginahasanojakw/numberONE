# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: StudyTimer
def export_state_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "sessions": list(timer.sessions.values()),
        "stats": timer.stats.copy() if hasattr(timer, 'stats') else {},
        "config": {"default_break_minutes": 5}
    }
    return json.dumps(state, indent=2)
