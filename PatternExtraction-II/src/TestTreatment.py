#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
import unicodedata
import random
import string

import CorrTreatment as corr
import treatment


def equal_string(uni_string):
    return unicodedata.normalize('NFKD', uni_string)


def generate_intel():
    code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    natures = ""
    for c in code:
        if c.isdigit(): natures += "number "
        elif c in "aeiouy":
            if c.isupper(): natures += "vowel-up "
            else: natures += "vowel-low "
        else:
            if c.isupper(): natures += "consonant-up "
            else: natures += "consonant-low "
    return natures


class TestExtractor(unittest.TestCase):
    def test_exist(self):
        self.assertTrue(hasattr(treatment, 'treatment'), _("You did not name the method as expected."))

    def test_extract(self):
        a = [generate_intel() for _ in range(5)]
        ans = _("The pattern of {} is {} and you returned {}.")
        for e in a:
            stu_ans = treatment.treatment(e)
            corr_ans = corr.treatment(e)
            self.assertEqual(equal_string(corr_ans), equal_string(stu_ans), ans.format(e, corr_ans, stu_ans))


if __name__ == '__main__':
    unittest.main()
