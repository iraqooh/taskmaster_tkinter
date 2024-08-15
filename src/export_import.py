from tkinter import filedialog
import csv
import json
from storage import Storage
from task import Task

class ExportImport:

    @staticmethod
    def export_tasks():
        filetypes = [('CSV Files', '*.csv'), ('JSON Files', '*.json')]
        file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=filetypes)
        tasks = Storage.load_tasks()

        if file_path.endswith('.csv'):
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Due Date', 'Priority', 'Category', 'Completed'])
                for task in tasks:
                    writer.writerow([task.name, task.due_date, task.priority, task.category, task.completed])

        elif file_path.endswith('.json'):
            with open(file_path, 'w') as file:
                json.dump([task.to_dict() for task in tasks], file)

    @staticmethod
    def import_tasks():
        filetypes = [('CSV Files', '*.csv'), ('JSON Files', '*.json')]
        file_path = filedialog.askopenfilename(filetypes=filetypes)

        if file_path.endswith('.csv'):
            with open(file_path, newline='') as file:
                reader = csv.DictReader(file)
                tasks = [Task(row['Name'], row['Due Date'], row['Priority'], row['Category'], row['Completed'] == 'True') for row in reader]

        elif file_path.endswith('.json'):
            with open(file_path) as file:
                tasks_data = json.load(file)
                tasks = [Task.from_dict(data) for data in tasks_data]

        Storage.save_tasks(tasks)
