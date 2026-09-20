# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: StudyTimer
def export_report(session_data, export_path):
    with open(export_path, 'w', encoding='utf-8') as f:
        f.write(f"StudyTimer Report\n")
        f.write(f"Date: {session_data.get('date', 'N/A')}\n")
        f.write(f"Total sessions: {session_data.get('total_sessions', 0)}\n")
        f.write(f"Total study time: {session_data.get('total_study_time', 0)}\n")
        f.write(f"Average focus score: {session_data.get('avg_focus', 0)}\n")
        f.write(f"Completed themes: {session_data.get('completed_themes', 0)}\n")
        f.write(f"Completed goals: {session_data.get('completed_goals', 0)}\n")
