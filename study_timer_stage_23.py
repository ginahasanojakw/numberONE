# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: StudyTimer
def print_study_stats(stats):
    """Compact table output for study statistics."""
    w = lambda s: f"{s:>12}"
    print("╔" + "═"*60 + "╗")
    print(f"║ {w('Session')}{w('Topic')}  {w('Minutes')}{w('Focus %')}{w('Target')} ║")
    print("╠" + "═"*60 + "╣")
    for s in stats:
        print(f"║ {w(s['session']):>12} {w(s.get('topic','')):>12}  {w(str(int(s['minutes']))):>12} {w(str(round(s.get('focus_pct',0)))):>12}%{w(s.get('target','')):>8} ║")
    print("╚" + "═"*60 + "╝")
