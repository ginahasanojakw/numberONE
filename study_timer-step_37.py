# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: StudyTimer
import unittest

class TestStudyTimer(unittest.TestCase):
    def setUp(self):
        from study_timer import StudyTimer
        self.timer = StudyTimer()

    def test_start_session(self):
        self.timer.start_session("Полуперки", 30 * 60)
        self.assertEqual(self.timer.current_topic, "Полуперки")
        self.assertEqual(self.timer.remaining_seconds, 1800)

    def test_end_session(self):
        self.timer.start_session("Полуперки", 30 * 60)
        self.timer.end_session()
        self.assertEqual(self.timer.current_topic, "")

    def test_add_goal(self):
        self.timer.add_goal("Выучить главу 1")
        self.assertEqual(len(self.timer.goals), 1)

    def test_add_break(self):
        self.timer.add_break(5 * 60)
        self.assertEqual(self.timer.break_duration, 300)

    def test_add_break_to_session(self):
        self.timer.start_session("Полуперки", 30 * 60)
        self.timer.add_break_to_session(5 * 60)
        self.assertEqual(self.timer.break_duration, 300)

    def test_focus_stats(self):
        self.timer.add_focus_stat("Полуперки", 30)
        self.assertEqual(self.timer.focus_stats["Полуперки"], 30)

    def test_focus_stats_multiple(self):
        self.timer.add_focus_stat("Полуперки", 30)
        self.timer.add_focus_stat("Полуперки", 45)
        self.assertEqual(self.timer.focus_stats["Полуперки"], 75)

    def test_focus_stats_different_topics(self):
        self.timer.add_focus_stat("Полуперки", 30)
        self.timer.add_focus_stat("Математика", 45)
        self.assertEqual(self.timer.focus_stats["Полуперки"], 30)
        self.assertEqual(self.timer.focus_stats["Математика"], 45)

    def test_focus_stats_multiple_sessions(self):
        self.timer.start_session("Полуперки", 30 * 60)
        self.timer.add_focus_stat("Полуперки", 30)
        self.timer.end_session()
        self.timer.start_session("Полуперки", 30 * 60)
        self.timer.add_focus_stat("Полуперки", 45)
        self.assertEqual(self.timer.focus_stats["Полуперки"], 75)

    def test_focus_stats_multiple_days(self):
        self.timer.start_session("Полуперки", 30 * 60)
        self.timer.add_focus_stat("Полуперки", 30)
        self.timer.end_session()
        self.timer.start_session("Полуперки", 30 * 60)
        self.timer.add_focus_stat("Полуперки", 45)
        self.assertEqual(self.timer.focus_stats["Полуперки"], 75)
