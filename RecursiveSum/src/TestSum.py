#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrSum as corr
import sum


class Counter(object):
    def __init__(self, fun):
        self._fun = fun
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self._fun(*args, **kwargs)


class TestFactorial(unittest.TestCase):
    def setUp(self):
        lst = [random.randint(1, 100) for _ in range(random.randint(4, 20))]
        ans = _("You did not use recursion in your algorithm ")
        sum.sum = Counter(sum.sum)
        stu_ans = sum.sum(lst)
        self.assertNotEqual(1, sum.sum.counter, ans)

    def test_sum(self):
        lists = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The sum of {} is {} and you returned {}.")
        for i in range(len(lists)):
            stu_ans = sum.sum(lists[i])
            corr_ans = corr.sum(lists[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(lists[i], corr_ans, stu_ans))

    def test_float(self):
        lists = [[random.random() for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The sum of {} is {} and you returned {}. Do you handle floats?")
        for i in range(len(lists)):
            stu_ans = sum.sum(lists[i])
            corr_ans = corr.sum(lists[i])
            self.assertAlmostEqual(corr_ans, stu_ans, 7, msg=ans.format(lists[i], corr_ans, stu_ans))

    def test_char(self):
        lists = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The sum list provided was {}. Did you take care of everything? ")
        for i in range(len(lists)):
            lists[i].append('e')
            try:
                stu_ans = sum.sum(lists[i])
                corr_ans = corr.sum(lists[i])
                self.assertEqual(corr_ans, stu_ans, ans.format(lists[i]))
            except TypeError:
                self.assertFalse(True, ans.format(lists[i]))

    def test_empty(self):
        lst = []
        ans = _("When the list is empty you should return 0.")
        self.assertEqual(0, sum.sum(lst), ans)


if __name__ == '__main__':
    unittest.main()
