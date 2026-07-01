# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: StudyTimer
def generate_summary(stats, active_sessions):
    """Генерирует текстовую сводку текущей активности."""
    lines = ["=== СВОДКА StudyTimer ==="]
    
    if not stats and not active_sessions:
        lines.append("Нет активных данных для отображения.")
        return "\n".join(lines)
    
    total_focus_time = sum(s.get('duration', 0) for s in stats.values())
    active_count = len(active_sessions)
    
    lines.append(f"Активные сессии: {active_count}")
    if active_count > 0:
        avg_duration = total_focus_time / active_count if active_count else 0
        lines.append(f"Средняя длительность активной сессии: {avg_duration:.1f} мин")
    
    topics_covered = set()
    for topic, data in stats.items():
        if data.get('completed', False):
            topics_covered.add(topic)
    
    if topics_covered:
        lines.append(f"Завершенные темы ({len(topics_covered)}): {', '.join(sorted(topics_covered))}")
    
    return "\n".join(lines)
