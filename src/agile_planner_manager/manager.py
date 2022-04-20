from queue import PriorityQueue

from src.agile_planner_io.io_processing import IOProcessing
from src.agile_planner_manager.day import Day


class ScheduleManager:

    def __init__(self):
        self.task_manager = PriorityQueue()
        self.schedule = []
        #self.process_schedule()
        self.error_count = 0

    def process_tasks(self, filename):
        try:
            self.task_manager = IOProcessing.read_schedule(filename)
            self.schedule = []
            self.error_count = 0
            self.generate_schedule()
        except (FileNotFoundError, IOError):
            print("File could not be found")

    """
    def process_schedule(self):
    """

    def add_task(self, task):
        self.reset_schedule()
        self.task_manager.put(task)
        self.generate_schedule()

    def remove_task(self, day_index, task_index):
        day_index -= 1
        task_index -= 1
        if day_index < 0 or day_index >= len(self.schedule):
            return None
        day = self.schedule.index(day_index)
        if task_index < 0 or task_index >= day.num_subtask():
            return None
        task = day.get_parent_task(task_index)
        self.task_manager.get()
        self.reset_schedule()
        self.generate_schedule()
        return task

    """
    def edit_task(self, day_index, task_index):
    """

    def reset_schedule(self):
        self.schedule = []
        copy = PriorityQueue()
        while self.task_manager.qsize() > 0:
            task = self.task_manager.get()
            task.reset()
            copy.put(task)
        self.task_manager = copy
        self.error_count = 0

    def generate_schedule(self):
        copy = PriorityQueue()
        processed = PriorityQueue()
        day_count = 0
        while self.task_manager.qsize() > 0:
            day_count += 1
            day = Day(8, day_count)
            while day.has_spare_hours() and self.task_manager.qsize() > 0:
                task = self.task_manager.get()
                valid_task_status = day.add_subtask(task)
                if task.get_subtotal_remaining() > 0:
                    processed.put(task)
                else:
                    copy.put(task)
                    self.error_count += 1
                    if valid_task_status:
                        self.error_count = 0
                    if not valid_task_status or not day.has_spare_hours():
                        while self.task_manager.qsize() > 0 and self.task_manager.queue[0].due_date == day.date:
                            copy.put(self.task_manager.queue[0])
                            day.add_subtask(self.task_manager.get())
                            self.error_count += 1

    def day_stdio(self):
        if len(self.schedule) == 0:
            print("Schedule is empty")
        else:
            IOProcessing.write_day(self.schedule.index(0), self.error_count, None)

    def schedule_stdio(self):
        if len(self.schedule) == 0:
            print("Schedule is empty")
        else:
            IOProcessing.write_schedule(self.schedule.index(0), self.error_count, None)

    """
    def schedule_file(self, filename):
        #TODO
    """

    def schedule_is_empty(self):
        return len(self.schedule) == 0