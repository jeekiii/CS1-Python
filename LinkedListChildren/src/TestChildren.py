#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import random
import timeout_decorator

import CorrChildren as corr
import main


class TestChildren(unittest.TestCase):

    @timeout_decorator.timeout(1, exception_message=_("Be sure you stop once you are back to the first children."
                                                            " you don't want to have more than you already have..."))
    def test_basic_loop(self):
        node1 = corr.Child()
        node2 = corr.Child()
        node3 = corr.Child()
        node1.next = node2 # 12->99
        node2.next = node3 # 99->37
        node3.next = node1
        self.assertEqual(True, main.is_every_child_here(node1),  msg="Well... You got it wrong, so try again.");




    @timeout_decorator.timeout(1, exception_message=_("Be sure you stop once you are back to the first children."
                                                            " you don't want to have more than you already have..."))
    def test_broken_loop(self):
        node1 = corr.Child()
        node2 = corr.Child()
        node3 = corr.Child()
        node1.next = node2 # 12->99
        node2.next = node3 # 99->37
        self.assertEqual(False, main.is_every_child_here(node1),  msg="Well... You got it wrong, so try again.");

        
if __name__ == '__main__':
    unittest.main()
