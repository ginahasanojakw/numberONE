# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: StudyTimer
from collections import defaultdict


class Profile:
    def __init__(self, name="Default", focus_minutes=25, break_minutes=5):
        self.name = name
        self.focus_minutes = focus_minutes
        self.break_minutes = break_minutes
        self.streak = 0

    def reset_streak(self):
        self.streak = 0


def add_profiles_to_app(app):
    app.profiles = {
        "Default": Profile(),
        "Intensive": Profile("Intensive", focus_minutes=50, break_minutes=10),
        "Relaxed": Profile("Relaxed", focus_minutes=15, break_minutes=3),
    }
    current_profile = None

    def switch_profile(profile_name):
        nonlocal current_profile
        if profile_name not in app.profiles:
            print(f"Профиль '{profile_name}' не найден.")
            return False
        current_profile = app.profiles[profile_name]
        print(f"Переключен на профиль: {current_profile.name}")
        return True

    def get_current_profile():
        if current_profile is None:
            return app.profiles["Default"]
        return current_profile

    def reset_all_streaks():
        for p in app.profiles.values():
            p.reset_streak()
        print("Все streak'и сброшены.")

    app.switch_profile = switch_profile
    app.get_current_profile = get_current_profile
    app.reset_all_streaks = reset_all_streaks
