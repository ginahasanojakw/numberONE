# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: StudyTimer
def calculate_weekly_stats(stats):
    if not stats: return {}
    from datetime import date, timedelta
    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    week_end = (week_start + timedelta(days=6)).isoformat()
    weekly_data = {d: {"sessions": 0, "total_minutes": 0} for d in range(int(week_start), int(week_end)+1)}
    for entry in stats:
        if not isinstance(entry.get("date"), str): continue
        try: start_date = date.fromisoformat(entry["date"])
        except ValueError: continue
        if week_start <= start_date.isoformat() <= week_end:
            weekly_data[start_date.isoformat()]["sessions"] += entry.get("count", 1)
            weekly_data[start_date.isoformat()]["total_minutes"] += entry.get("duration", 0)
    return weekly_data
