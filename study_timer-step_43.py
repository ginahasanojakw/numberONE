# === Stage 43: Добавь пагинацию длинных списков ===
# Project: StudyTimer
class Pagination:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size
        self.total_pages = max(1, (len(items) + page_size - 1) // page_size)
        self.current_page = 1

    def get_page(self):
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def get_info(self):
        return {
            "current_page": self.current_page,
            "total_pages": self.total_pages,
            "total_items": len(self.items),
            "page_size": self.page_size,
        }

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        else:
            self.current_page = 1

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        else:
            self.current_page = self.total_pages
