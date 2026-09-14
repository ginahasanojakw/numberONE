# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: StudyTimer
def _format_duration(seconds):
    """Convert seconds to 'HH:MM:SS' string."""
    h, rem = divmod(int(seconds), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def _format_stats(stats):
    """Pretty-print study stats as a compact summary string."""
    if not stats:
        return "  Нет данных"
    lines = [
        f"  Сессий: {stats.get('sessions', 0) or 0}",
        f"  Тем: {stats.get('topics', 0) or 0}",
        f"  Перерывов: {stats.get('breaks', 0) or 0}",
        f"  Всего минут: {stats.get('total_minutes', 0) or 0}",
    ]
    return "\n".join(lines)
