import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from src.ui import TaskmasterUI
from src.task import Task

class TestTaskmasterUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = TaskmasterUI(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('src.storage.Storage.load_tasks')
    def test_load_tasks(self, mock_load_tasks):
        mock_load_tasks.return_value = [Task("Task 1", "2024-08-20 15:00", "high", "Work")]
        self.app.load_tasks()
        self.assertEqual(self.app.task_list.size(), 1)

    @patch('src.storage.Storage.save_tasks')
    def test_new_task(self, mock_save_tasks):
        task = Task(name="New Task", due_date="2024-08-20 15:00", priority="high", category="Work")
        self.app.add_task_to_listbox(task)
        self.assertEqual(self.app.task_list.size(), 1)

if __name__ == '__main__':
    unittest.main()
