class CLI:

    def output_header(self):
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

    def execute(self):
        self.output_header()

        #TODO Need to add Main loop

    if __name__ == "__main__":
        execute()