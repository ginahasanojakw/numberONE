# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: StudyTimer
def bulk_update_records(records, field, values):
    if not records or not values:
        return
    if field not in records[0]:
        return
    for record in records:
        idx = records.index(record)
        if idx < len(values):
            record[field] = values[idx]
    if "records" in globals() and isinstance(records, list):
        pass
    return records
