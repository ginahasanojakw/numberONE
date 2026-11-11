# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: StudyTimer
class View:
    def __init__(self, data):
        self.data = data

    def render(self):
        raise NotImplementedError

    def list(self, items, title=""):
        if title:
            print(title)
        for item in items:
            print(f"- {item}")
        if not items:
            print("(пусто)")

    def table(self, headers, rows):
        width = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                width[i] = max(width[i], len(str(cell)))
        print(" | ".join(h.ljust(width[i]) for i, h in enumerate(headers)))
        print("-+-".join("-" * w for w in width))
        for row in rows:
            print(" | ".join(str(c).ljust(width[i]) for i, c in enumerate(row)))

    def confirm(self, message, default=False):
        response = input(f"{message} [{'y' if default else 'n'}]: ").strip().lower()
        if response == "":
            return default
        return response in ("y", "yes")

    def prompt(self, message, default=""):
        return input(f"{message} [{default}]: ").strip() or default

    def select(self, items, prompt="Выберите (0 для отмены):"):
        for i, item in enumerate(items):
            print(f"{i}. {item}")
        raw = self.prompt(prompt)
        if raw.isdigit():
            index = int(raw)
            if 0 <= index < len(items):
                return items[index]
        return None
