import sys
from queue import PriorityQueue


class IOProcessing:

    @staticmethod
    def write_day(day, error_count, output):
        if output is None:
            output = sys.stdout
        if error_count > 0:
            sys.stdout.write(error_count, "overflows have occurred within schedule...")
        output.write("Day 1: " + day.__str__())

    @staticmethod
    def write_schedule(day_list, error_count, output):
        if output is None:
            output = sys.stdout
        if error_count > 0:
            sys.stdout.write(error_count, "overflows have occurred within schedule...")
        i = 1
        for day in day_list:
            output.write("Day", i, ": ", day.__str__)
            i += 1

    @staticmethod
    def read_schedule(filename):
        #TODO
        pq = PriorityQueue()
        """Scanner
        fileScanner = new
        Scanner(new File(filename));
        fileScanner.useDelimiter(",|\\r\\n|\\n");
        while (fileScanner.hasNextLine()) {
            String name = fileScanner.next();
            int hours = fileScanner.nextInt();
            int date = fileScanner.nextInt();
            pq.add(new Task(name, hours, date));
        }
        fileScanner.close();"""
        return pq