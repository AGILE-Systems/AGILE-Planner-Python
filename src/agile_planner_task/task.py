class Task:
    used_hr = 0
    avg_num_hr = 0

    def __init__(self, name, total_hr, incrementation):
        self.name = name
        self.total_hr = total_hr
        self.due_date = incrementation

    def reset(self):
        self.used_hr = 0
        self.avg_num_hr = 0

    def get_subtotal_hr_remaining(self):
        return self.total_hr - self.used_hr

    def __str__(self):
        return "Task [name=" + self.name + ", total=" + self.total_hr + "]"

    def __cmp__(self, other):
        time_diff = self.due_date - other.due_date
        if time_diff < 0 or time_diff == 0 and self.get_subtotal_hr_remaining() > other.get_subtotal_hr_remaining():
            return -1
        elif time_diff > 0 or time_diff == 0 and self.get_subtotal_hr_remaining() < other.get_subtotal_hr_remaining():
            return 1
        else:
            return 0


class SubTask:
    def __init__(self, task, sub_hr, overflow_status):
        self.task = task
        self.sub_hr = sub_hr
        self.overflow_status = overflow_status

    def __str__(self):
        return "SubTask [name=" + self.task.name + ", hours=" + self.sub_hr + "]"

"""
NOTE: Will need to call this in invoking class
    def add_subtask(self, hours, overflow_status):
        subtask = None
        if hours > 0 and self.subtotal_hr + hours <= self.total_hr:
            subtask = SubTask(self, hours, overflow_status)
            self.subtotal_hr += hours
        return subtask
"""