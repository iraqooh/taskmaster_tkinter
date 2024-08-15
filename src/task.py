from datetime import datetime, timedelta

class Task:
    def __init__(self, name, due_date, priority, category, completed=False):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.completed = completed

    def mark_completed(self, completed=True):
        self.completed = completed

    def is_upcoming(self):
        now = datetime.now()
        task_due_date = datetime.strptime(self.due_date, '%Y-%m-%d %H:%M:%S')
        time_difference = task_due_date - now
        return time_difference <= timedelta(days=1) and time_difference > timedelta(0) and not self.completed

    def to_dict(self):
        return {
            'name': self.name,
            'due_date': self.due_date,
            'priority': self.priority,
            'category': self.category,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            name=data['name'],
            due_date=data['due_date'],
            priority=data['priority'],
            category=data['category'],
            completed=data['completed']
        )
