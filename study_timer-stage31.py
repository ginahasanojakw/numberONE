# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: StudyTimer
def switch_profile():
    """Переключение активного профиля: меню выбора, загрузка/сохранение."""
    profiles = [p for p in data["profiles"] if not p.get("locked", False)]
    if not profiles:
        print("Нет доступных профилей.")
        return None

    while True:
        print("\nДоступные профили:")
        for i, p in enumerate(profiles):
            name = p["name"] or "Безымянный"
            print(f"  [{i}] {name} (темы: {len(p.get('topics', []))}, цели: {len(p.get('goals', []))})")

        try:
            choice = int(input("Выберите профиль (0 для удаления, -1 для отмены): "))
        except ValueError:
            print("Некорректный ввод.")
            continue

        if choice == -1:
            return None
        elif choice == 0:
            if not profiles:
                print("Нельзя удалить последний профиль!")
                return None
            idx = len(profiles) - 1
            removed = data["profiles"].pop(idx)
            saved = save_data()
            print(f"Профиль удалён. Сохранено ({saved} байт).")
            return None
        elif 0 <= choice < len(profiles):
            new_profile = profiles[choice]
            if profile_id:
                data["currentProfileId"] = new_profile.get("id", "")
            else:
                data["profiles"].append(new_profile)
                data["currentProfileId"] = new_profile.get("id", "")

            saved = save_data()
            print(f"Профиль переключён на «{new_profile['name'] or 'Безымянный'}» ({saved} байт).")
            return new_profile
        else:
            print("Неверный выбор.")
