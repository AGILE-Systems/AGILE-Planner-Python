import unittest

from src.agile_planner_task.task import Task


class TaskTest(unittest.TestCase):

    def test_constructor(self):
        t1 = Task("CSC316", 4, 2)
        self.assertEqual("CSC316", t1.get_name)
        self.assertEqual(4, t1.get_total_hr)
        self.assertEqual(2, t1.get_due_date)

    def test_add_sub_task(self):
        t1 = Task("CSC116", 4, 2)
        self.assertIsNone(t1.add_sub_task(0, False))
        st1 = t1.add_sub_task(2, False)
        self.assertEqual(2, st1.get_hours)
        self.assertIsNone(t1.add_sub_task(3, False))
        t1.add_sub_task(2, False)
        self.assertEqual(0, t1.get_subtotal_remaining())

    def test_get_subtotal_remaining(self):
        t1 = Task("CSC116", 5, 2)
        st1 = t1.add_sub_task(2, False)
        self.assertEqual(2, st1.get_hours)
        self.assertEqual(3, t1.get_subtotal_remaining())
        self.assertIsNone(t1.add_sub_task(4, False))
        t1.add_sub_task(3, False)
        self.assertEqual(0, t1.get_subtotal_remaining())

    def test_sort(self):
        t1 = Task("CSC116", 5, 2)
        t2 = Task("CSC216", 1, 1)
        t3 = Task("CSC316", 6, 2)
        t4 = Task("Test", 1, 1)
        self.assertEqual(-1, t3.__cmp__(t1))
        self.assertEqual(0, t1.__cmp__(t1))
        self.assertEqual(1, t1.__cmp__(t3))
        self.assertEqual(-1, t2.__cmp__(t3))
        self.assertEqual(0, t2.__cmp__(t4))
        self.assertEqual(1, t1.__cmp__(t2))

    def test__str__(self):
        t1 = Task("A", 2, 0)
        self.assertEqual("Task [name=A, total=2]", t1.__str__())

    def test_subtask(self):
        t1 = Task("CSC316", 5, 2)
        st1 = t1.add_sub_task(2, False)
        self.assertEqual(t1, st1.get_task)
        self.assertEqual(2, st1.get_hours)
        # self.assertEqual("SubTask [name=CSC116, hours=2]", st1.__str__())
        self.assertEqual(0, t1.avg_hr)

        t2 = Task("CSC216", 4, 1)
        st2 = t2.add_sub_task(3, False)
        self.assertEqual(-1, st2.__cmp__(st1))
        self.assertEqual(0, st1.__cmp__(st1))
        self.assertEqual(0, st2.__cmp__(st2))
        self.assertEqual(1, st1.__cmp__(st2))

        t2.reset()
        self.assertEqual(4, t2.get_subtotal_remaining())
        self.assertEqual(0, t2.avg_hr)

        self.assertFalse(st2.get_overflow)

        #TypeError: can only concatenate str (not "int") to str
        #self.assertEqual("SubTask [name=CSC116, hours=2]", st1.__str__())

        #self.assertEqual(1, t2.get_subtotal_remaining())
        #self.assertTrue(t2.add_sub_task(1, True).overflow)

        t3 = Task("Z", 17, 1)
        #Calendar operation (store in 'current' variable)
        #t3.set_avg_hr(current)
        #self.assertEqual(9, t3.avg_hr)