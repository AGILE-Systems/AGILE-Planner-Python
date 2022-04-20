from queue import PriorityQueue

from src.agile_planner_io.io_processing import IOProcessing


class ScheduleManager:

    def __init__(self):
        self.task_manager = PriorityQueue()
        self.schedule = []
        self.process_schedule()
        self.error_count = 0

    def process_tasks(self, filename):
        try:
            self.task_manager = IOProcessing.read_schedule(filename)
            self.schedule = []
            self.error_count = 0
            self.generate_schedule()
        except (FileNotFoundError, IOError):
            print("File could not be found")

    def process_schedule(self):
        #TODO

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
        task = day.get_parent(task_index)
        self.task_manager.get()
        self.reset_schedule()
        self.generate_schedule()
        return task

    def edit_task(self, day_index, task_index):
        #TODO

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
        #TODO

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

    def schedule_file(self, filename):
        #TODO

    def schedule_is_empty(self):
        return len(self.schedule) == 0