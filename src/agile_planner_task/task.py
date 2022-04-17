from datetime import datetime

class Task:
    used_hr = 0
    avg_hr = 0

    def __init__(self, name, total_hr, incrementation):
        self.name = name
        self.total_hr = total_hr
        self.due_date = incrementation

    def add_sub_task(self, hours, overflow):
        subtask = None
        if hours > 0 and self.used_hr + hours <= self.total_hr:
            subtask = Task.SubTask(self, hours, overflow)
            self.used_hr += hours
        return subtask

    def reset(self):
        self.used_hr = 0
        self.avg_hr = 0

    def get_subtotal_remaining(self):
        return self.total_hr - self.used_hr

    def __cmp__(self, other):
        time_diff = self.due_date - other.due_date
        if time_diff < 0 or time_diff == 0 and self.get_subtotal_remaining() > other.get_subtotal_remaining():
            return -1
        elif time_diff > 0 or time_diff == 0 and self.get_subtotal_remaining() < other.get_subtotal_remaining():
            return 1
        else:
            return 0

    def set_avg_hr(self, date):
        #TODO Need to add Time utility class
        days = Time.determine_range(date, self.due_date) + 1
        avg = self.total_hr / days
        if self.total_hr % days != 0:
            avg += 1
        self.avg_hr = avg

    def __str__(self):
        return "Task [name=" + self.name + ", total=" + self.total_hr + "]"

    class SubTask:
        def __init__(self, task, hours, overflow):
            self.task = task
            self.hours = hours
            self.overflow = overflow

        def __str__(self):
            return "SubTask [name=" + self.task.name + ", hours=" + self.hours + "]"

        def __cmp__(self, other):
            return self.task.__cmp__(other.task)
