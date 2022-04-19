from datetime import datetime


class Task:

    _name = None
    _total_hr = None
    _due_date = None

    def __init__(self, name, total_hr, incrementation):
        self._avg_hr = 0
        self._used_hr = 0
        self.name(name)
        self.total_hr(total_hr)
        self.due_date(incrementation)

    @_name.setter
    def name(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @_total_hr.setter
    def total_hr(self, total_hr):
        self._total_hr = total_hr

    @property
    def total_hr(self):
        return self._total_hr

    @_due_date.setter
    def due_date(self, due_date):
        self._due_date = due_date

    @property
    def due_date(self):
        return self._due_date

    def add_sub_task(self, hours, overflow):
        subtask = None
        if hours > 0 and self.used_hr + hours <= self.total_hr:
            subtask = Task.SubTask(self, hours, overflow)
            self.used_hr += hours
        return subtask

    def reset(self):
        self._used_hr = 0
        self._avg_hr = 0

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
        # TODO Need to add Time utility class
        days = Time.determine_range(date, self.due_date) + 1
        avg = self.total_hr / days
        if self.total_hr % days != 0:
            avg += 1
        self._avg_hr = avg

    def __str__(self):
        return "Task [name=" + self.name + ", total=" + self.total_hr + "]"

    class SubTask:
        def __init__(self, task, hours, overflow):
            self._task = task
            self._hours = hours
            self._overflow = overflow

        @property
        def task(self):
            return self._task

        @property
        def hours(self):
            return self._hours

        @property
        def overflow(self):
            return self._overflow

        def __str__(self):
            return "SubTask [name=" + self._task.name + ", hours=" + self._hours + "]"

        def __cmp__(self, other):
            return self.task.__cmp__(other.task)
