# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: StudyTimer
class DataLog:
    def __init__(self):
        self._log = []

    def log(self, action, details=None):
        self._log.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details or ""
        })

    def get_log(self):
        return self._log

    def clear_log(self):
        self._log.clear()
