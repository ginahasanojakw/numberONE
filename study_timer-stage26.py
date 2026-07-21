# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: StudyTimer
def demo_commands():
    """Run a sequence of demo commands for quick manual testing."""
    try:
        from study_timer import StudyTimer
    except ImportError as e:
        print(f"Import failed: {e}")
        return
    
    timer = StudyTimer()
    
    # Create some sample topics
    timer.add_topic("Python Basics", goals=20, interval_minutes=5)
    timer.add_topic("Data Structures", goals=30, interval_minutes=10)
    timer.add_topic("Algorithms", goals=15, interval_minutes=5)
    
    # Create some sample sessions
    session = timer.create_session()
    session.add_topic("Python Basics")
    session.add_goal("Understand variables and types")
    session.add_goal("Practice basic syntax")
    session.start_timer(30 * 60)  # 30 minutes
    
    # Simulate progress (for testing only - modify as needed)
    print(f"Session started: {session}")
    print(f"Topics added to session: {len(session.topics)}")
    
    # Print demo info
    print("\n=== Demo Commands Complete ===")
    print("You can now test the StudyTimer with these sample topics and sessions.")

if __name__ == "__main__":
    demo_commands()
