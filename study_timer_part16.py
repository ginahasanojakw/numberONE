# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: StudyTimer
def calculate_monthly_stats(stats: dict, current_date: datetime) -> None:
    if not stats.get('sessions'): return
    year = current_date.year
    month = current_date.month
    monthly_data = {year: [0] * 31}
    for session in stats['sessions']:
        d = session.get('date')
        if isinstance(d, str): d = datetime.strptime(d, '%Y-%m-%d').date()
        y, m = d.year, d.month
        if (y == year and m == month) or (year is None and m == month):
            idx = d.day - 1
            monthly_data.setdefault(y, [0] * 31)[idx] += session.get('duration', 0)
    stats['monthly_stats'] = {str(k): {'days': v} for k, v in monthly_data.items()}
