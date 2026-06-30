# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: StudyTimer
def search_sessions(query, fields=None):
    if fields is None:
        fields = ['topic', 'goal']
    query_lower = query.lower()
    results = []
    for session in sessions:
        match = False
        for field_name in fields:
            value = getattr(session, field_name, '')
            if isinstance(value, str) and query_lower in value.lower():
                match = True
                break
        if match:
            results.append(session)
    return results
