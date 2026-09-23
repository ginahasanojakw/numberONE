# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: StudyTimer
class FavoritesManager:
    def __init__(self, timer):
        self.timer = timer
        self.favorites = []
        self._load()

    def _save(self):
        import json
        path = os.path.join(self.timer.data_dir, "favorites.json")
        with open(path, "w") as f:
            json.dump(self.favorites, f, indent=2)

    def toggle_favorite(self, session):
        if session in self.favorites:
            self.favorites.remove(session)
        else:
            self.favorites.append(session)
        self._save()
        return self.favorites

    def get_favorites(self):
        return self.favorites

    def _load(self):
        import json
        path = os.path.join(self.timer.data_dir, "favorites.json")
        if os.path.exists(path):
            with open(path, "r") as f:
                self.favorites = json.load(f)
