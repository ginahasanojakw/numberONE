# === Stage 17: Добавь группировку записей по категориям ===
# Project: StudyTimer
from collections import defaultdict
def group_by_category(records: list[dict], key_field: str) -> dict[str, list]:
    grouped = defaultdict(list)
    for rec in records:
        cat = rec.get(key_field, 'Uncategorized')
        grouped[cat].append(rec)
    return {k: sorted(v, key=lambda x: x.get('timestamp', 0)) for k, v in grouped.items()}
