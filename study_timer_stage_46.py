# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: StudyTimer
import copy

def migrate_study_sessions_to_v3(sessions):
    """
    Миграция: добавляет поле 'focus_score' (0-100) к каждой сессии.
    Если поле уже существует, ничего не меняем.
    """
    if not sessions:
        return sessions

    for session in sessions:
        if 'focus_score' not in session:
            session['focus_score'] = int(
                (session.get('completed', False) and 85) or (not session.get('completed', False) and 45)
            )
    return sessions
