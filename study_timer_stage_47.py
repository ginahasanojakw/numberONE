# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: StudyTimer
def demo():
    print("=" * 60)
    print("  StudyTimer — демо-сценарий")
    print("=" * 60)
    timer = StudyTimer()

    timer.add_topic("Python основы", goals=["переменные", "циклы"], duration=25)
    timer.add_topic("ООП", goals=["классы", "наследование"], duration=30)

    timer.set_break_duration(5)
    timer.set_focus_stats_threshold(0.9)

    timer.add_session_goal("Изучить базовый синтаксис")
    timer.start_timer()

    print("Сессия началась. Ожидание 5 минут...")
    time.sleep(5)
    print("Перерыв! Отдохни 5 минут.")
    time.sleep(5)
    print("Возвращаемся к учёбе. Ожидание 10 минут...")
    time.sleep(10)
    print("Сессия завершена. Статистика концентрации:")
    timer.print_stats()

    print("\nДобавляю тему на основе предыдущей...")
    timer.add_topic("Асинхронность", goals=["async/await", "футуры"], duration=35)
    print("Добавлена тема: Асинхронность")

    print("\nФинальная статистика:")
    timer.print_stats()
    print("\nСпасибо за использование StudyTimer! ✨")
