#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import random
import unicodedata

import CorrSort as corr
import sortingHat


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


class TestChecker(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(sortingHat, 'house_designation'), _("You did not name the method as expected."))

    def test_2_houses(self):
        a = ['smart', 'wise', 'bold', 'brave']
        ans = _("Should you really belong to this house? \n Another one wasn't suited too for the qualities {}?")
        stu_ans = sortingHat.house_designation(a)
        corr_ans = corr.house_designation(a)
        self.assertEqual(equal_string(corr_ans), equal_string(stu_ans), ans.format(a))

    def test_designation(self):
        qualities = ['bold', 'wise', 'curious', 'smart', 'cunning', 'loyal', 'patient', 'brave', 'pretty', 'wily']
        a = [[random.choice(qualities) for _ in range(3)] for _ in range(5)]
        ans = _("Should you really belong to this house? \n"
                "Your returned {}, another one wasn't suited too for the qualities {}?")
        for i in range(len(a)):
            stu_ans = sortingHat.house_designation(a[i])
            corr_ans = corr.house_designation(a[i])
            self.assertEqual(equal_string(corr_ans), equal_string(stu_ans), ans.format(stu_ans, a[i]))


if __name__ == '__main__':
    unittest.main()
