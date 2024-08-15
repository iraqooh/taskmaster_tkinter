import unittest
from src.task import Task

class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task(name="Test Task", due_date="2024-08-20 15:00", priority="high", category="Work")
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.due_date, "2024-08-20 15:00")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.category, "Work")
        self.assertFalse(task.completed)

    def test_task_mark_completed(self):
        task = Task(name="Test Task", due_date="2024-08-20 15:00", priority="high", category="Work")
        task.mark_completed()
        self.assertTrue(task.completed)

    def test_task_to_dict(self):
        task = Task(name="Test Task", due_date="2024-08-20 15:00", priority="high", category="Work")
        task_dict = task.to_dict()
        expected_dict = {
            'name': "Test Task",
            'due_date': "2024-08-20 15:00",
            'priority': "high",
            'category': "Work",
            'completed': False
        }
        self.assertEqual(task_dict, expected_dict)

    def test_task_from_dict(self):
        task_dict = {
            'name': "Test Task",
            'due_date': "2024-08-20 15:00",
            'priority': "high",
            'category': "Work",
            'completed': False
        }
        task = Task.from_dict(task_dict)
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.due_date, "2024-08-20 15:00")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.category, "Work")
        self.assertFalse(task.completed)

if __name__ == '__main__':
    unittest.main()
