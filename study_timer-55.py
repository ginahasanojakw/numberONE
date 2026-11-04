# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: StudyTimer
DUPLICATE_KEYS = ("topic", "goal")


def find_duplicate(session):
    for field in DUPLICATE_KEYS:
        value = session.get(field)
        if value is None:
            continue
        for existing in sessions:
            if existing is session:
                continue
            if existing.get(field) == value:
                return existing
    return None


def add_session_with_check(**kwargs):
    session = dict(kwargs)
    duplicate = find_duplicate(session)
    if duplicate:
        print(f"Запись '{session.get('topic', 'без темы')}' уже существует")
        return None
    sessions.append(session)
    return session
