# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: StudyTimer
def _format_elapsed(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def _format_duration(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h:d}ч {m:d}м"
    return f"{m:d}м {s:d}с"

def _format_progress(fraction: float, total: int) -> str:
    done = int(round(fraction * total))
    return f"{done}/{total}"

def _format_target(target: dict) -> str:
    return f"🎯 {target.get('topic', '')}: {target.get('goal', '')}"

def _format_session_result(result: dict) -> str:
    r = result.get('result', {})
    elapsed = r.get('elapsed_seconds', 0)
    score = r.get('score', 0)
    break_count = r.get('break_count', 0)
    return f"⏱ {_format_elapsed(elapsed)} | 📊 {score}% | 🔄 {break_count} перерывов"

def _format_daily_stats(stats: dict) -> str:
    d = stats.get('daily', {})
    total_minutes = d.get('total_minutes', 0)
    focus_sessions = d.get('focus_sessions', 0)
    return f"📅 Сегодня: {_format_duration(total_minutes)} | 🧠 {focus_sessions} фокус-сессий"

def _format_achievements(achievements: dict) -> str:
    lines = []
    for name, count in achievements.items():
        if count:
            lines.append(f"  • {name}: {count}")
    return "\n".join(lines)
