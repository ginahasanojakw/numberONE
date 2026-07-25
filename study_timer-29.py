# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: StudyTimer
DEFAULT_CONFIG = {
    "session_duration": 25,        # минуты активной работы по умолчанию
    "break_duration": 5,           # минуты перерыва по умолчанию
    "pomodoro_count": 4,           # количество сессий до длинного отдыха
    "long_break_duration": 15,     # минуты длинного перерыва
    "focus_streak_multiplier": 1.2,# коэффициент бонуса за серии фокуса
    "streak_threshold": 3,         # минимальная серия для начисления бонуса
    "max_topics": 50,              # лимит сохранённых тем
    "history_limit": 100,          # количество записей истории
    "ui_theme": "default",         # 'dark', 'light', 'default'
    "font_size": 14,               # размер шрифта в интерфейсе
}
