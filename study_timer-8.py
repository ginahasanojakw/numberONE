# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: StudyTimer
def show_menu():
    print("\n=== StudyTimer Menu ===")
    print("1. Start new session")
    print("2. View statistics")
    print("3. Add break reminder")
    print("4. Exit program")
    choice = input("Select option (1-4): ").strip()
    if choice == "1":
        start_session()
    elif choice == "2":
        view_stats()
    elif choice == "3":
        add_break_reminder()
    elif choice == "4":
        print("Goodbye!")
        return False
    else:
        print("Invalid option.")
    return True

def start_session():
    topic = input("Enter study topic: ").strip() or "General"
    duration = int(input("Duration in minutes: ") or 25)
    goals = input("Goals (comma-separated): ").strip().split(",") if input("Set goals? (y/n)").lower() == 'y' else []
    print(f"\nSession started for '{topic}' ({duration} min). Goals: {goals}")

def view_stats():
    total_minutes = sum(s['duration'] for s in sessions) - sum(b['duration'] for b in breaks)
    avg_focus = len([s for s in sessions if not any(b['session_id'] == s.get('id') and b['type']=='focus' for b in breaks)]) / max(len(sessions), 1) * 100
    print(f"\nTotal study time: {total_minutes} min")
    print(f"Average focus rate: {avg_focus:.1f}%")

def add_break_reminder():
    break_duration = int(input("Break duration in minutes: ") or 5)
    breaks.append({'duration': break_duration, 'session_id': None})
    print(f"\nBreak reminder added for {break_duration} min.")
