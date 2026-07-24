# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: StudyTimer
def compute_study_metrics(all_sessions, all_breaks):
    """Вычисляет ключевые метрики таймера: среднее время фокуса, количество перерывов, продуктивность."""
    if not all_sessions:
        return {"avg_focus_minutes": 0.0, "total_focus_minutes": 0.0, "break_count": 0}

    total_focus = sum(s.get("focus_duration", 0) for s in all_sessions)
    break_count = len(all_breaks) if isinstance(all_breaks, list) else 0
    
    avg_focus = total_focus / len(all_sessions) if all_sessions else 0.0
    # Если breaks — это список словарей с "duration" и "type", считаем только реальные перерывы
    real_breaks = [b for b in (all_breaks or []) if isinstance(b, dict) and b.get("type") == "break"]
    
    return {
        "avg_focus_minutes": round(avg_focus, 1),
        "total_focus_minutes": total_focus,
        "break_count": len(real_breaks),
        "productivity_ratio": round(total_focus / (total_focus + sum(b.get("duration", 0) for b in real_breaks)), 2) if (total_focus + sum(b.get("duration", 0) for b in real_breaks)) > 0 else 0.0,
    }
