# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: StudyTimer
TEMPLATES = [
    {"id": "pomodoro", "name": "Помодоро (25/5)", "focus_min": 25, "break_min": 5},
    {"id": "deep_work", "name": "Глубокая работа (90/15)", "focus_min": 90, "break_min": 15},
    {"id": "exam_prep", "name": "Подготовка к экзамену (60/10)", "focus_min": 60, "break_min": 10},
]

class Template:
    def __init__(self, template_id, name, focus_min, break_min):
        self.id = template_id
        self.name = name
        self.focus_min = focus_min
        self.break_min = break_min
    
    @classmethod
    def from_template(cls, template_id):
        for t in TEMPLATES:
            if t["id"] == template_id:
                return cls(t["name"], t["focus_min"], t["break_min"])
        raise ValueError(f"Unknown template: {template_id}")

def use_template(template_id):
    t = Template.from_template(template_id)
    print(f"\n📋 Используем шаблон: {t.name} ({t.focus_min} мин фокус / {t.break_min} мин перерыв)")
    session = Session()
    session.set_focus_duration(t.focus_min)
    session.set_break_duration(t.break_min)
    return session

if __name__ == "__main__":
    s = use_template("pomodoro")
