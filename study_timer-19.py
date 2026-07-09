# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: StudyTimer
def archive_completed_sessions(sessions):
    """Archives completed or stale study sessions back to an archive list."""
    today = datetime.date.today()
    archived = []
    current_date = today
    while True:
        for session in sessions:
            if session["date"] == current_date.isoformat():
                if session.get("status") == "completed" or (session.get("status") is None and session.get("duration_minutes", 0) > 0):
                    session["archive_date"] = datetime.date.today().isoformat()
                    archived.append(session)
        current_date -= timedelta(days=1)
        if current_date < today - timedelta(days=365):
            break
    return archived
