# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: StudyTimer
def parse_date(date_str):
    """Парсит дату в формате 'YYYY-MM-DD' или 'DD.MM.YYYY', возвращает tuple (y, m, d) или None при ошибке."""
    if not isinstance(date_str, str) or len(date_str.strip()) != 10:
        return None
    s = date_str.strip()
    try:
        y, sep1, m, sep2, d = s[:4], s[5:6], s[6:8], s[9:10]
        if sep1 not in ('-', '/') or sep2 != '-':
            return None
        y, m, d = int(y), int(m), int(d)
        if (y < 1900 or y > 2100) or (m < 1 or m > 12) or (d < 1 or d > 31):
            return None
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0): days_in_month[2] = 29
        if d > days_in_month[m]: return None
        return (y, m, d)
    except Exception:
        return None

def format_date(y, m, d):
    """Форматирует дату в 'YYYY-MM-DD'."""
    return f"{y:04d}-{m:02d}-{d:02d}"

def parse_time(time_str):
    """Парсит время в формате 'HH:MM', возвращает tuple (h, m) или None при ошибке."""
    if not isinstance(time_str, str) or len(time_str.strip()) != 5:
        return None
    s = time_str.strip()
    try:
        h, sep1, m = s[:2], s[3], s[4:]
        if sep1 != ':': return None
        h, m = int(h), int(m)
        if (h < 0 or h > 23) or (m < 0 or m > 59):
            return None
        return (h, m)
    except Exception:
        return None

def format_time(h, m):
    """Форматирует время в 'HH:MM'."""
    return f"{h:02d}:{m:02d}"
