import unittest

from src.agile_planner_task.task import Task, SubTask


class TaskTest(unittest.TestCase):

    def test_constructor(self):
        t1 = Task("CSC316", 4, 2)
        self.assertEqual("CSC316", t1.name)
        self.assertEqual(4, t1.total_hr)
        self.assertEqual(2, t1.due_date)

    def  test_subtotal(self):
        t1 = Task("CSC316", 4, 2)
        t1.used_hr = 1
        t1.avg_num_hr = 2
        self.assertEqual(3, t1.get_subtotal_hr_remaining())
        t1.reset()
        self.assertEqual(0, t1.used_hr)
        self.assertEqual(0, t1.avg_num_hr)

    def test__str__(self):
        t1 = Task("CSC316", 4, 2)
        self.assertEqual("Task [name=CSC316, total=4]", t1.__str__())

    def test_subtask(self):
        #TODO Need to finish
        t1 = Task("CSC316", 5, 2)
        st1 = SubTask(t1, 2, False)
        self.assertEqual(t1, st1.task)
        self.assertEqual(2, st1.sub_hr)
        #self.assertEqual("SubTask [name=CSC116, hours=2]", st1.__str__())
        self.assertEqual(0, t1.avg_num_hr)

        t2 = Task("CSC216", 4, 1)
        st2 = SubTask(t2, 3, False)
        self.assertEqual(-1, t2.__cmp__(t1))
        self.assertEqual(0, t1.__cmp__(t1))
        self.assertEqual(0, t2.__cmp__(t2))
        self.assertEqual(1, t1.__cmp__(t2))

        t2.reset()
        self.assertEqual(4, t2.get_subtotal_hr_remaining())
        self.assertEqual(0, t2.avg_num_hr)

        self.assertFalse(st2.overflow_status)


        """ REMAINING TESTS
		assertEquals("SubTask [name=CSC116, hours=2]", st1.toString());

		assertEquals(1, t2.getSubTotalHoursRemaining());

		assertTrue(t2.addSubTask(1, true).getOverflowStatus());

		Task t3 = new Task("Z", 17, 1);
		Calendar current = Time.getFormattedCalendarInstance(0);
		t3.setAverageNumHours(current);
		assertEquals(9, t3.getAverageNumHours());
        """