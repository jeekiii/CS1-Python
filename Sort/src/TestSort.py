#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random

import CorrSort as corr
import sort


class MyList(list):
    def sort(self):
        raise AttributeError(_("Nice try! But using the predefined 'sort' function is a bit of cheating.\n"
                             "\t\tTry to implement an actual algorithm for sorting the list."))


class TestSort(unittest.TestCase):
    def test_sort(self):
        lists = [[random.randint(1, 100) for _ in range(random.randint(1, 20))] for _ in range(random.randint(1, 20))]
        ans = _("The sorted version of {} is {} and you returned {}.")
        for i in range(len(lists)):
            stu_ans = sort.sorter(MyList(lists[i]))
            corr_ans = corr.sorter(lists[i])
            self.assertEqual(corr_ans, stu_ans, ans.format(lists[i], corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
