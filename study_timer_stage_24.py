# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: StudyTimer
import json, os, time as _time

def print_record(record):
    if not record:
        return
    r = record.get('record', {})
    topic = r.get('topic', '') or ''
    goal = r.get('goal', '') or ''
    start = r.get('start_time')
    end = r.get('end_time')
    break_count = r.get('break_count', 0)
    focus_score = r.get('focus_score', 0)
    duration_min = (r.get('total_seconds', 0) or 0) // 60
    if start:
        t1 = _time.strptime(start, '%Y-%m-%d %H:%M')
        s_str = f"{t1.tm_mon}/{t1.tm_mday} {t1.tm_hour}:{t1.tm_min}"
    else:
        s_str = '---'
    if end:
        t2 = _time.strptime(end, '%Y-%m-%d %H:%M')
        e_str = f"{t2.tm_mon}/{t2.tm_mday} {t2.tm_hour}:{t2.tm_min}"
    else:
        e_str = '---'
    print(f"[{topic[:30]:30s}] Goal: {goal[:40]:40s}")
    print(f"  {s_str} → {e_str} | {duration_min} min | breaks={break_count} | focus={focus_score}/10")

def show_all(records_path='study_timer.json'):
    if not os.path.exists(records_path):
        print("Нет записей.")
        return
    with open(records_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    records = data.get('records', [])
    for rec in records:
        print_record(rec)

if __name__ == '__main__':
    show_all()
