import unittest
import os
from unittest.mock import patch, mock_open
from src.export_import import ExportImport
from src.storage import Storage
from src.task import Task

class TestExportImport(unittest.TestCase):

    def setUp(self):
        self.task = Task(name="Test Task", due_date="2024-08-20 15:00", priority="high", category="Work")
        self.tasks = [self.task]
        Storage.FILE_PATH = 'data/test_tasks.json'
        Storage.save_tasks(self.tasks)

    def tearDown(self):
        if os.path.exists(Storage.FILE_PATH):
            os.remove(Storage.FILE_PATH)

    @patch('builtins.open', new_callable=mock_open)
    @patch('tkinter.filedialog.asksaveasfilename')
    def test_export_tasks_csv(self, mock_saveas, mock_open):
        mock_saveas.return_value = 'test.csv'
        ExportImport.export_tasks()
        mock_open.assert_called_once_with('test.csv', 'w', newline='')

    @patch('builtins.open', new_callable=mock_open)
    @patch('tkinter.filedialog.askopenfilename')
    def test_import_tasks_json(self, mock_openfile, mock_open):
        mock_openfile.return_value = 'test.json'
        mock_open.return_value.read.return_value = '[{"name": "Test Task", "due_date": "2024-08-20 15:00", "priority": "high", "category": "Work", "completed": false}]'
        ExportImport.import_tasks()
        tasks = Storage.load_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].name, "Test Task")

if __name__ == '__main__':
    unittest.main()
