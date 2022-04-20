class Day:

    def __int__(self, capacity, incrementation):
        self.capacity = capacity
        self.date = incrementation
        self.subtask_manager = []
        self.size = 0

    def add_subtask(self, task):
        if self.date == task.due_date:
            hours = task.get_subtotal_remaining()
            overflow = hours > self.get_spare_hours()
            subtask = task.add_sub_task(hours, overflow)
            self.subtask_manager.append(subtask)
            self.size += hours
            return not overflow
        if task.avg_hr == 0:
            task.set_avg_hr(self.date)
        hours = task.avg_hr
        if hours > task.get_subtotal_remaining():
            hours = task.get_subtotal_remaining()
        if hours + self.size > self.capacity:
            hours = self.capacity - self.size
        subtask = task.add_sub_task(hours, False)
        self.subtask_manager.append(subtask)
        self.size += hours
        return True

    def get_parent_task(self, subtask_index):
        subtask = self.subtask_manager.index(subtask_index)
        return subtask.task

    """
    def add_subtask_manually(self, task, hours):
        #TODO
    """

    def get_spare_hours(self):
        return self.capacity - self.size

    def num_subtask(self):
        return len(self.subtask_manager)

    def has_spare_hours(self):
        return self.get_spare_hours() > 0

    def __str__(self):
        count = 1
        sb = "MM-dd-yyyy\n"
        for st in self.subtask_manager:
            sb += str(count) + ". "
            count += 1
            sb += st.task.name + ", "
            sb += str(st.hours) + "hr, Due "
            sb += st.task.due_date
            if st.overflow:
                sb += " OVERFLOW"
            sb += "\n"
        return sb
