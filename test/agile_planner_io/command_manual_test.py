import unittest

from src.agile_planner_io.command_manual import CommandManual


class CommandManualTest(unittest.TestCase):

    def test_dir(self):
        cm = CommandManual()
        self.assertEqual("NAME\n\tlist - lists all possible commands\n\nSYNOPSIS\n\t" +
                         "list\n\nDESCRIPTION\n\tLists all possible commands available" +
                         "within AGILE Planner command line interface", cm.manual.get("list"))
        self.assertEqual("NAME\n\tschedule - displays entire schedule\n\nSYNOPSIS\n\t" +
                         "schedule\n\nDESCRIPTION\n\tDisplays all days and their respective" +
                         "tasks from the schedule. Items in each day are sorted by priority.",
                         cm.manual.get("schedule"))
        self.assertEqual("NAME\n\tadd - adds a task to schedule\n\nSYNOPSIS\n\tadd [name] [hours] " +
                         "[due_date]\n\nDESCRIPTION\n\tAdds any particular task to the schedule assuming" +
                         "no time conflict has occurred", cm.manual.get("add"))
        self.assertEqual("NAME\n\tremove - removes task from schedule\n\nSYNOPSIS\n\tremove [day_index] " +
                         "[task_index]\n\nDESCRIPTION\n\tRemoves any particular task from schedule assuming " +
                         "it exists and is not archived", cm.manual.get("remove"))
        self.assertEqual("NAME\n\tedit - edits a task within the schedule\n\nSYNOPSIS\n\tedit [day_index] " +
                         "[task_index] [hours]\n\nDESCRIPTION\n\tEdits a given task within the schedule to " +
                         "possess a valid modification such as name, hours, or due date", cm.manual.get("edit"))
        self.assertEqual("NAME\n\tday - views current day schedule\n\nSYNOPSIS\n\tday\n\nDESCRIPTION\n\tViews " +
                         "the entire day's schedule with all tasks in sorted order based on priority",
                         cm.manual.get("day"))
        self.assertEqual("NAME\n\tlog - prints a log of all recent commands\n\nSYNOPSIS\n\tlog\n\nDESCRIPTION\n\tViews"
                         + " the entire day's logging commands history", cm.manual.get("log"))
        self.assertEqual(
            "NAME\n\tprint - prints the entire schedule\n\nSYNOPSIS\n\tprint [file_name]\n\nDESCRIPTION\n\t" +
            "Prints the entire schedule to the default schedule folder with the title format: " +
            "schedule-yyyy-mm-dd.txt", cm.manual.get("print"))
        self.assertEqual(
            "NAME\n\tread - reads in the schedule\n\nSYNOPSIS\n\tread [file_name]\n\nDESCRIPTION\n\tReads " +
            "in the schedule from the default folder and overwrites the current schedule", cm.manual.get("read"))
        self.assertEqual("NAME\n\ttime - gets current time\n\nSYNOPSIS\n\ttime\n\nDESCRIPTION\n\t" +
                         "Gets the actual time within the system clock in the format of yyyy-mm-dd HH-MM-SS",
                         cm.manual.get("time"))
