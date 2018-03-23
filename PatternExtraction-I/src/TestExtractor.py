#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random
import string

import CorrExtractor as corr
import extractor


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


def generate_code():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))


def strip_trailing_space(s):
    if s[-1] == ' ': return s[:-1]
    return s


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(extractor, 'extract'), _("You did not name the method as expected."))

    def test_extract(self):
        a = [generate_code() for _ in range(5)]
        ans = _("The natures of {} is {} and you returned {}.")
        for e in a:
            stu_ans = extractor.extract(e)
            corr_ans = corr.extract(e)
            self.assertEqual(equal_string(corr_ans), equal_string(strip_trailing_space(stu_ans)), ans.format(e, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
