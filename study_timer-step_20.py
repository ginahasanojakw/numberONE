# === Stage 20: Добавь восстановление записей из архива ===
# Project: StudyTimer
def restore_from_archive():
    """Восстанавливает записи из CSV-архива в структуру данных."""
    import csv, os, datetime
    
    archive_path = "study_timer_data.csv"
    
    if not os.path.exists(archive_path):
        return
        
    records = []
    with open(archive_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = {
                "id": int(row["id"]),
                "session_start": datetime.datetime.fromisoformat(row["session_start"]),
                "session_end": datetime.datetime.fromisoformat(row["session_end"]),
                "topic_name": row["topic_name"],
                "goal_description": row["goal_description"],
                "break_duration_min": int(row["break_duration_min"]),
                "concentration_score": float(row["concentration_score"]),
                "completed": True if row["completed"] == "True" else False,
            }
            records.append(record)
    
    return records
