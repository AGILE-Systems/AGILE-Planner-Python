from collections import deque
import Task.SubTask

class Day:

    def __int__(self, capacity, incrementation):
        self.capacity = capacity
        self.date = incrementation
        subtask_manager = deque()
        self.size = 0

    def add_subtask(self, task):
        if self.date == task.due_date:
            overflow = task.get_subtotal_remaining() > self.get_spare_hours()
            hours = task.get_subtotal_remaining()
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
        subtask = self.subtask_manager.get(subtask_index)
        return subtask.task

    def add_subtask_manually(self, task, hours):
        #TODO

    def get_spare_hours(self):
        return self.capacity - self.size

    def num_subtask(self):
        return self.subtask_manager.size()

    def has_spare_hours(self):
        return self.get_spare_hours() > 0

    def __str__(self):
        #TODO need to format string like the following
        """
        SimpleDateFormat sdf = new SimpleDateFormat("MM-dd-yyyy");
		StringBuilder sb = new StringBuilder(sdf.format(this.date.getTime()) + "\n");
		int count = 1;
		for(SubTask st : subtaskManager) {
			sb.append(count + ". ");
			count++;
			sb.append(st.getParentTask().getName() + ", ");
			sb.append(st.getSubTaskHours() + "hr, Due ");
			sb.append(sdf.format(st.getParentTask().getDueDate().getTime()));
			if(st.getOverflowStatus()) {
				sb.append(" OVERFLOW");
			}
			sb.append("\n");
		}
		return sb.toString();
        :return:
        """