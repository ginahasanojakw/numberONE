# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: StudyTimer
class StudyTimer:
    def __init__(self):
        self.sessions = []
        self.focus_stats = {}

    def add_session(self, topic: str, goal: str, duration_minutes: int) -> dict:
        session_id = len(self.sessions) + 1
        record = {
            "id": session_id,
            "topic": topic,
            "goal": goal,
            "duration_minutes": duration_minutes,
            "start_time": None,
            "end_time": None,
            "completed": False,
            "focus_score": 0.0
        }
        self.sessions.append(record)
        return record

    def start_session(self, session_id: int):
        if not self.sessions or session_id < 1 or session_id > len(self.sessions):
            raise ValueError("Invalid session ID")
        current = self.sessions[session_id - 1]
        import time
        current["start_time"] = time.strftime("%Y-%m-%d %H:%M:%S")
        return current

    def end_session(self, session_id: int) -> dict:
        if not self.sessions or session_id < 1 or session_id > len(self.sessions):
            raise ValueError("Invalid session ID")
        current = self.sessions[session_id - 1]
        import time
        current["end_time"] = time.strftime("%Y-%m-%d %H:%M:%S")
        current["completed"] = True
        if not current.get("focus_score"):
            current["focus_score"] = round(random.uniform(0.5, 1.0), 2)
        topic_key = current["topic"].lower()
        self.focus_stats[topic_key] = self.focus_stats.get(topic_key, 0) + current["focus_score"]
        return current

    def get_session(self, session_id: int):
        if not self.sessions or session_id < 1 or session_id > len(self.sessions):
            raise ValueError("Invalid session ID")
        return self.sessions[session_id - 1]
