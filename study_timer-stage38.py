# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: StudyTimer
import unittest

class TestStudyTimerEdgeCases(unittest.TestCase):
    def test_zero_duration(self):
        timer = StudyTimer()
        timer.add_session("Math", 0, 0)
        self.assertEqual(timer.get_total_study_time(), 0)
        self.assertEqual(timer.get_total_break_time(), 0)
        self.assertEqual(timer.get_current_session(), None)

    def test_negative_duration_rejected(self):
        timer = StudyTimer()
        with self.assertRaises(ValueError):
            timer.add_session("Math", -5, 0)

    def test_invalid_theme(self):
        timer = StudyTimer()
        with self.assertRaises(ValueError):
            timer.add_session(None, 20, 0)

    def test_invalid_goal(self):
        timer = StudyTimer()
        with self.assertRaises(ValueError):
            timer.add_session("Math", 20, None)

    def test_invalid_goal_value(self):
        timer = StudyTimer()
        with self.assertRaises(ValueError):
            timer.add_session("Math", 20, "not a number")

    def test_invalid_break_duration(self):
        timer = StudyTimer()
        with self.assertRaises(ValueError):
            timer.add_session("Math", 20, 0, -10)

    def test_invalid_break_value(self):
        timer = StudyTimer()
        with self.assertRaises(ValueError):
            timer.add_session("Math", 20, 0, "not a number")

    def test_empty_session_list(self):
        timer = StudyTimer()
        self.assertEqual(timer.get_session_list(), [])
        self.assertEqual(timer.get_session_count(), 0)

    def test_single_session(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        sessions = timer.get_session_list()
        self.assertEqual(len(sessions), 1)
        self.assertEqual(sessions[0].theme, "Math")
        self.assertEqual(sessions[0].duration, 20)

    def test_session_count(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        timer.add_session("Physics", 15, 0, 3)
        self.assertEqual(timer.get_session_count(), 2)

    def test_get_nonexistent_session(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        with self.assertRaises(ValueError):
            timer.get_session("NonExistent")

    def test_get_current_session_none(self):
        timer = StudyTimer()
        self.assertEqual(timer.get_current_session(), None)

    def test_get_current_session_returns_last(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        timer.add_session("Physics", 15, 0, 3)
        current = timer.get_current_session()
        self.assertEqual(current.theme, "Physics")
        self.assertEqual(current.duration, 15)

    def test_invalid_session_index(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        with self.assertRaises(IndexError):
            timer.get_session_at(5)

    def test_invalid_session_index_negative(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        with self.assertRaises(IndexError):
            timer.get_session_at(-1)

    def test_invalid_session_index_zero(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        with self.assertRaises(IndexError):
            timer.get_session_at(0)

    def test_invalid_session_index_out_of_range(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        with self.assertRaises(IndexError):
            timer.get_session_at(100000)

    def test_invalid_session_index_negative_large(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        with self.assertRaises(IndexError):
            timer.get_session_at(-100000)

    def test_invalid_session_index_out_of_range_negative(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        with self.assertRaises(IndexError):
            timer.get_session_at(-999999)

    def test_invalid_session_index_out_of_range_positive(self):
        timer = StudyTimer()
        timer.add_session("Math", 20, 0, 2)
        with self.assertRaises(IndexError):
            timer.get_session_at(999999)
