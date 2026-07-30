# === Stage 32: Добавь журнал действий пользователя ===
# Project: StudyTimer
import json, os

class ActionLog:
    def __init__(self):
        self.actions = []
        log_path = "study_timer_actions.json"
        if os.path.exists(log_path):
            with open(log_path) as f:
                self.actions = json.load(f)

    def record(self, action_type, details=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "type": action_type,
            "details": details
        }
        self.actions.append(entry)
        print(f"[LOG] {action_type}: {details}")

    def save(self):
        log_path = "study_timer_actions.json"
        with open(log_path, 'w') as f:
            json.dump(self.actions, f, indent=2)

    def get_log(self):
        return self.actions[-10:]  # last 10 entries
