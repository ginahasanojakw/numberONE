# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: StudyTimer
def edit_session(session_id: int, updates: dict) -> None:
    with open("sessions.json", "r") as f:
        sessions = json.load(f)
    if session_id not in sessions:
        print(f"Сессия {session_id} не найдена.")
        return
    old_data = sessions[session_id].copy()
    for key, value in updates.items():
        if key in ["id", "createdAt"]:
            continue
        old_data[key] = value
    sessions[session_id] = old_data
    with open("sessions.json", "w") as f:
        json.dump(sessions, f, indent=2)
    print(f"Сессия {session_id} обновлена.")
