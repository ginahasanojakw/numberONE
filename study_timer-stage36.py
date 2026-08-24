# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: StudyTimer
def validate_and_repair(data):
    if not isinstance(data, dict):
        return data
    if 'sessions' not in data:
        data['sessions'] = []
    if 'stats' not in data:
        data['stats'] = {'total_study': 0, 'total_breaks': 0, 'sessions_count': 0}
    for s in data.get('sessions', []):
        if not isinstance(s, dict):
            data['sessions'] = [dict(s) if isinstance(s, dict) else {} for s in data.get('sessions', [])]
            continue
        if 'session_id' not in s:
            s['session_id'] = 0
        if 'theme' not in s:
            s['theme'] = 'unknown'
        if 'goal' not in s:
            s['goal'] = 0
        if 'duration' not in s:
            s['duration'] = 0
        if 'breaks' not in s:
            s['breaks'] = []
        if 'start_time' not in s:
            s['start_time'] = 0
        if 'end_time' not in s:
            s['end_time'] = 0
        for b in s.get('breaks', []):
            if not isinstance(b, dict):
                b = {'break_id': 0, 'duration': 0, 'type': 'short'}
    return data
