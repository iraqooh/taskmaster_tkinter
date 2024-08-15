class Settings:
    def __init__(self):
        self.notification_enabled = True
        self.notification_time = 15  # minutes before task is due

    def toggle_notifications(self):
        self.notification_enabled = not self.notification_enabled

    def set_notification_time(self, minutes):
        self.notification_time = minutes
