import os
import json
from task import Task

class Storage:
    FILE_PATH = 'data/tasks.json'

    @staticmethod
    def load_tasks():
        if os.path.exists(Storage.FILE_PATH):
            with open(Storage.FILE_PATH, 'r') as file:
                tasks_data = json.load(file)
                return [Task.from_dict(data) for data in tasks_data]
        return []

    @staticmethod
    def save_tasks(tasks):
        with open(Storage.FILE_PATH, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file)

    @staticmethod
    def add_task(task):
        tasks = Storage.load_tasks()
        tasks.append(task)
        Storage.save_tasks(tasks)

    @staticmethod
    def remove_task(task_name):
        tasks = Storage.load_tasks()
        tasks = [task for task in tasks if task.name != task_name]
        Storage.save_tasks(tasks)
