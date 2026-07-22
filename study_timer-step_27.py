# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: StudyTimer
def reset_demo_data():
    """Сбросить демо-данные к начальным значениям."""
    global study_sessions, current_session, completed_topics, total_focus_minutes, timer_remaining
    
    study_sessions = [
        {
            "topic": "Python основы",
            "goal": "Изучить синтаксис и типы данных",
            "duration_seconds": 1800,
            "start_time": None,
            "completed": False
        },
        {
            "topic": "Структуры данных",
            "goal": "Понять списки, кортежи, словари",
            "duration_seconds": 2400,
            "start_time": None,
            "completed": False
        },
        {
            "topic": "Функции и лямбды",
            "goal": "Написать функции с аргументами и возвратами",
            "duration_seconds": 1500,
            "start_time": None,
            "completed": False
        },
        {
            "topic": "ООП в Python",
            "goal": "Создать классы и объекты",
            "duration_seconds": 3000,
            "start_time": None,
            "completed": False
        }
    ]
    
    current_session = {"current_topic_index": 0, "session_start": None}
    completed_topics = []
    total_focus_minutes = 0
    timer_remaining = 0
    
def clear_state():
    """Очистить все данные и вернуть в начальное состояние."""
    global study_sessions, current_session, completed_topics, total_focus_minutes, timer_remaining
    
    study_sessions = []
    current_session = {"current_topic_index": -1, "session_start": None}
    completed_topics = []
    total_focus_minutes = 0
    timer_remaining = 0
    
    print("Состояние полностью очищено. Готов к новым сессиям!")
