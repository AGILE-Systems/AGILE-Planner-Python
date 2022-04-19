from datetime import datetime


class Task:

    _name = None
    _total_hr = None
    _due_date = None

    def __init__(self, name, total_hr, incrementation):
        self._avg_hr = 0
        self._used_hr = 0
        self.set_name(name)
        self.set_total_hr(total_hr)
        self.set_due_date(incrementation)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_total_hr(self, total_hr):
        self._total_hr = total_hr

    def get_total_hr(self):
        return self._total_hr

    def set_due_date(self, due_date):
        self._due_date = due_date

    def get_due_date(self):
        return self._due_date

    def add_sub_task(self, hours, overflow):
        subtask = None
        if hours > 0 and self._used_hr + hours <= self._total_hr:
            subtask = Task.SubTask(self, hours, overflow)
            self._used_hr += hours
        return subtask

    def reset(self):
        self._used_hr = 0
        self._avg_hr = 0

    def get_subtotal_remaining(self):
        return self._total_hr - self._used_hr

    def __cmp__(self, other):
        time_diff = self._due_date - other.get_due_date
        if time_diff < 0 or time_diff == 0 and self.get_subtotal_remaining() > other.get_subtotal_remaining():
            return -1
        elif time_diff > 0 or time_diff == 0 and self.get_subtotal_remaining() < other.get_subtotal_remaining():
            return 1
        else:
            return 0

    def set_avg_hr(self, date):
        # TODO Need to add Time utility class
        days = Time.determine_range(date, self.get_due_date) + 1
        avg = self._total_hr / days
        if self._total_hr % days != 0:
            avg += 1
        self._avg_hr = avg

    def __str__(self):
        return "Task [name=" + self._name + ", total=" + self._total_hr + "]"

    class SubTask:
        def __init__(self, task, hours, overflow):
            self._task = task
            self._hours = hours
            self._overflow = overflow

        def get_task(self):
            return self._task

        def get_hours(self):
            return self._hours

        def get_overflow(self):
            return self._overflow

        def __str__(self):
            return "SubTask [name=" + self._task.get_name + ", hours=" + self._hours + "]"

        def __cmp__(self, other):
            return self.get_task.__cmp__(other.get_task)
