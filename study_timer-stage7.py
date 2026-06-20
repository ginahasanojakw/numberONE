# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: StudyTimer
def sort_sessions(sessions, key='date'):
    if not sessions: return []
    reverse = False
    if key == 'priority':
        def _sort(x): return -x['priority']
        reverse = True
    elif key == 'name':
        def _sort(x): return x['name'].lower()
    else: # date
        def _sort(x): return x.get('date', datetime.min)
    return sorted(sessions, key=_sort, reverse=reverse)
