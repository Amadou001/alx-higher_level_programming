#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_non_empty_list(self):
        self.assertEqual(max_integer([1, -4, 7]), 7)
    

