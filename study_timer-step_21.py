# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: StudyTimer
class Reminder:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
    
    def is_due(self, today):
        if isinstance(today, datetime.date):
            return self.due_date <= today
        elif isinstance(today, str):
            return datetime.date.fromisoformat(today) >= self.due_date
        return False

    def format_summary(self):
        status = "overdue" if self.is_due(datetime.date.today()) else "upcoming"
        return f"[{status}] {self.title} (due: {self.due_date})"
