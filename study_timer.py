# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: StudyTimer
import time
from datetime import datetime, timedelta

# --- StudyTimer: Базовая структура и демо-данные ---

class StudySession:
    def __init__(self, topic, goal, duration_minutes):
        self.topic = topic
        self.goal = goal
        self.duration = timedelta(minutes=duration_minutes)
        self.start_time = None
        self.end_time = None
        self.is_active = False

    def start(self):
        if self.is_active:
            return "Сессия уже запущена!"
        self.start_time = datetime.now()
        self.is_active = True
        return f"Старт сессии: {self.topic} ({self.duration_minutes} мин)"

    def stop(self):
        if not self.is_active:
            return "Сессия не активна."
        self.end_time = datetime.now()
        self.is_active = False
        actual_duration = self.end_time - self.start_time
        return f"Сессия завершена. Тема: {self.topic}. Факт: {actual_duration}"

    @property
    def duration_minutes(self):
        return int(self.duration.total_seconds() / 60)

# --- Демо-данные и точка входа ---

def main():
    # Инициализация демо-сессий
    sessions = [
        StudySession("Python Основы", "Изучить функции", 25),
        StudySession("Математика", "Решить 10 задач", 45),
        StudySession("Английский", "Чтение статей", 30),
    ]

    print(f"Доступные темы: {[s.topic for s in sessions]}")

    # Демонстрация работы (запуск первой сессии)
    if sessions:
        result = sessions[0].start()
        print(result)
        
        # Имитация завершения через 5 секунд для демонстрации
        time.sleep(5) 
        result_stop = sessions[0].stop()
        print(result_stop)

if __name__ == "__main__":
    main()
