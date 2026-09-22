# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: StudyTimer
import json


def load_records_from_file(filepath):
    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(',')
            if len(parts) == 6:
                records.append({
                    'session_id': parts[0],
                    'topic': parts[1],
                    'goal': parts[2],
                    'duration_min': int(parts[3]),
                    'focus_score': int(parts[4]),
                    'break_taken': bool(parts[5])
                })
    return records


def save_records_to_file(records, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        for r in records:
            f.write(f"{r['session_id']},{r['topic']},{r['goal']},{r['duration_min']},{r['focus_score']},{r['break_taken']}\n")
