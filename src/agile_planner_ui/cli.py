from src.agile_planner_io.command_manual import CommandManual
from src.agile_planner_manager.manager import ScheduleManager
from src.agile_planner_task.task import Task


class CLI:

    def __init__(self):
        self.schedule_manager = ScheduleManager()
        self.command_manual = CommandManual()


def output_header():
    print("Welcome to AGILE Planner 0.2.0\n"
          + "\nChangelog:\n"
          + "-Added overflow notification system for scheduling ease and efficiency\n"
          + "-Added updated command manual operations\n"
          + "-Added the ability to add a task during the current session\n"
          + "-Added the ability to remove a task during the current session\n"
          + "-Added the ability to view just the current day\n"
          + "-Added the ability to process whatever file in \"data\" directory\n"
          + "-Added the ability to output to a specified file\n"
          + "-Added temporary Client email address for terminal prompt"
          + "(will be incorporating a Client configuration)\n"
          + "-Refactored codebase for ease of use\n"
          + "-Fixed unbalanced task bug that would produce overflow despite ample space\n"
          + "-Fixed overflow bug that prevented overflow from being reported\n"
          + "\n\n"
          + "To output all commands, enter: list\nTo access the manual for a command, enter: man <command>\n")


def execute(cli):
    output_header()

    while True:
        str_input = input("> ")
        if str_input == "list":
            print("list\nschedule\ntime\nadd\nremove\nedit\nday\nlog\nprint\nread\nquit")
        elif str_input == "time":
            print("Current time")
        elif str_input == "schedule":
            cli.schedule_manager.schedule_stdio()
        elif str_input == "add":
            try:
                name = input("Name: ")
                hours = int(input("Hours: "))
                due_date = int(input("Due Date: "))
                cli.schedule_manager.add_task(Task(name, hours, due_date))
            except ValueError:
                print("Invalid input")
        elif str_input == "remove":
            try:
                day_index = int(input("Day Index: "))
                task_index = int(input("Task Index: "))
                if cli.schedule_manager.remove_task(day_index, task_index) is None:
                    print("Invalid command")
            except ValueError:
                print("Invalid input")
        elif str_input == "day":
            cli.schedule_manager.day_stdio()
        elif str_input == "print":
            filename = input("Filename: ")
            cli.schedule_manager.schedule_file("output/" + filename)
        elif str_input == "read":
            filename = input("Filename: ")
            cli.schedule_manager.process_tasks(filename)
        elif str_input == "quit":
            break
        elif str_input == "man":
            command = input("Command: ")
            if cli.command_manual.manual.get(command) is not None:
                print(cli.command_manual.manual.get(command))
            else:
                print("Invalid command")


if __name__ == "__main__":
    execute(CLI())
