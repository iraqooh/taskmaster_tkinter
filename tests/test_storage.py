import unittest
import os
import json
from src.task import Task
from src.storage import Storage

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_file = 'data/test_tasks.json'
        Storage.FILE_PATH = self.test_file

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_tasks_empty(self):
        tasks = Storage.load_tasks()
        self.assertEqual(tasks, [])

    def test_save_and_load_tasks(self):
        task = Task(name="Test Task", due_date="2024-08-20 15:00", priority="high", category="Work")
        Storage.add_task(task)
        tasks = Storage.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].name, "Test Task")

    def test_remove_task(self):
        task = Task(name="Test Task", due_date="2024-08-20 15:00", priority="high", category="Work")
        Storage.add_task(task)
        Storage.remove_task("Test Task")
        tasks = Storage.load_tasks()
        self.assertEqual(tasks, [])

if __name__ == '__main__':
    unittest.main()
