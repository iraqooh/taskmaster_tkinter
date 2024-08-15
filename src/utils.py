from datetime import datetime

class Utils:
    @staticmethod
    def parse_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M')

    @staticmethod
    def format_date(date_obj):
        return date_obj.strftime('%Y-%m-%d %H:%M')

    @staticmethod
    def get_upcoming_tasks(tasks, within_hours=24):
        upcoming_tasks = []
        now = datetime.now()
        for task in tasks:
            task_due_date = Utils.parse_date(task.due_date)
            time_difference = (task_due_date - now).total_seconds() / 3600
            if 0 < time_difference <= within_hours:
                upcoming_tasks.append(task)
        return upcoming_tasks
