import unittest
from datetime import datetime, timedelta
from src.utils import Utils
from src.task import Task

class TestUtils(unittest.TestCase):

    def test_parse_date(self):
        date_str = '2024-08-20 15:00'
        date_obj = Utils.parse_date(date_str)
        self.assertEqual(date_obj, datetime(2024, 8, 20, 15, 0))

    def test_format_date(self):
        date_obj = datetime(2024, 8, 20, 15, 0)
        date_str = Utils.format_date(date_obj)
        self.assertEqual(date_str, '2024-08-20 15:00')

    def test_get_upcoming_tasks(self):
        now = datetime.now()
        task1 = Task(name="Task 1", due_date=Utils.format_date(now + timedelta(hours=12)), priority="high", category="Work")
        task2 = Task(name="Task 2", due_date=Utils.format_date(now + timedelta(hours=26)), priority="medium", category="Personal")
        task3 = Task(name="Task 3", due_date=Utils.format_date(now - timedelta(hours=1)), priority="low", category="Home")
        tasks = [task1, task2, task3]
        upcoming_tasks = Utils.get_upcoming_tasks(tasks)
        self.assertEqual(len(upcoming_tasks), 1)
        self.assertEqual(upcoming_tasks[0].name, "Task 1")

if __name__ == '__main__':
    unittest.main()
