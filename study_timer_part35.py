# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: StudyTimer
def get_next_action(state):
    """Return a short recommendation based on current state."""
    if not state:
        return "Начни с выбора темы — открой файл config.py и задай список тем."
    
    topic = state.get("current_topic", "")
    goal = state.get("goal", "")
    timer_running = state.get("timer_running", False)
    break_count = state.get("break_count", 0)
    total_study_min = state.get("total_study_minutes", 0)
    
    if not topic:
        return "Сначала определи тему для изучения — введи её через input()."
    if not goal:
        return f"У тебя тема '{topic}', но нет цели. Установи цель (например: 'Выучить 10 терминов')."
    if timer_running and break_count < 2:
        time_left = state.get("time_left_seconds", 3600)
        return f"Продолжай сессию — осталось {int(time_left/60)} минут."
    if timer_running and break_count >= 2:
        return "Достигнут лимит перерывов. Закончи текущую тему и начни отдыхать."
    if total_study_min > 0 and state.get("session_complete", False):
        return f"Сессия завершена! Ты изучил {total_study_min} мин.{topic}. Отметь достижение в config.py."
    if break_count == 2:
        return "Перерывы закончились. Оцени свой прогресс и решай, стоит ли продолжить или отдохнуть."
    
    return f"Ты на теме '{topic}' с целью {goal}. Фокусируйся и не отвлекайся."
