# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: StudyTimer
def filter_sessions(status=None, category=None, tags=None):
    filtered = []
    for session in sessions:
        if status and session['status'] != status: continue
        if category and session.get('category') != category: continue
        if tags:
            session_tags = set(session.get('tags', []))
            if not any(tag in session_tags for tag in tags): continue
        filtered.append(session)
    return filtered

def get_stats_by_category():
    stats = {}
    for s in sessions:
        cat = s.get('category') or 'General'
        if cat not in stats: stats[cat] = {'count': 0, 'total_minutes': 0}
        stats[cat]['count'] += 1
        stats[cat]['total_minutes'] += int(s['duration'])
    return {k: v for k, v in sorted(stats.items(), key=lambda x: -x[1]['count'])}

def get_recent_sessions(limit=5):
    return sessions[-limit:] if len(sessions) >= limit else sessions[:]
