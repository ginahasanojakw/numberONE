# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: StudyTimer
def bulk_delete(confirm=False):
    if not sessions:
        print("Список сессий пуст.")
        return
    print("Текущие сессии:")
    for i, s in enumerate(sessions, 1):
        print(f"  {i}. {s['topic']} ({s['status']})")
    print("0 — отмена")
    choice = input("Выберите номер(а) через запятую или 'all' для всех: ").strip().lower()
    if choice == "all":
        if not confirm:
            print("Подтвердите удаление всех сессий (введите yes):")
            if input("> ") != "yes":
                print("Отмена.")
                return
        for s in sessions:
            sessions.remove(s)
        print("Все сессии удалены.")
        return
    ids = []
    for part in choice.split(","):
        part = part.strip()
        if not part.isdigit():
            print(f"Неверный выбор: {part}")
            return
        ids.append(int(part))
    if not ids:
        print("Ничего не выбрано.")
        return
    if not confirm:
        print("Подтвердите удаление выбранных сессий (введите их номера через запятую):")
        if input("> ") != choice:
            print("Отмена.")
            return
    for idx in ids:
        if 1 <= idx <= len(sessions):
            sessions.remove(sessions[idx - 1])
        else:
            print(f"Нет сессии с номером {idx}")
    print("Удаление завершено.")
