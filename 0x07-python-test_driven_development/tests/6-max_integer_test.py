#!/usr/bin/python3
"""Unittests for max_integer module"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer"""

    def test_emptyness(self):
        """Tests an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_floats(self):
        """Tests a list of floats"""
        floats = [1.5, 6.9, 4.6, 12.5, 3.1]
        self.assertEqual(max_integer(floats), 12.5)

    def test_mixed_list(self):
        """ Tests a mixed list"""
        mixed_list = [2, 12.5, 5, 7, 6.3, 15, 8.2]
        self.assertEqual(max_integer(mixed_list), 15)
    
    def test_one_element(self):
        """Tests a list with just one element"""
        one_element = [12]
        self.assertEqual(max_integer(one_element), 12)

    def test_strings_list(self):
        """Tests a list of strings"""
        list_of_strings = ["Musa", "Kabo", "Tino", "Syanda"]
        self.assertEqual(max_integer(list_of_strings), "Tino")

    def test_string(self):
        """Tests if a string is passed instead"""
        string = 'Kaboentle'
        self.assertEqual(max_integer(string), 't')

    def test_ordered_list(self):
        """Tests an ordered list"""
        ordered = [1, 2, 3, 5, 6, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Tests and unordered list"""
        no_order = [2, 1, 6, 3, 8, 5]
        self.assertEqual(max_integer(no_order), 8)
