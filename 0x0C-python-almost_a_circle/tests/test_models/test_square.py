#!/usr/bin/python3
"""Unittests for square module"""

import unittest
from models.rectangle import Rectangle
from models.square import Square
class TestSquare(unittest.TestCase):
    """Defines the unittests for Square class"""
    
    def test_constructor(self):
        """Test constructor with different values"""

        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        square = Square(10, 2, 3)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_str(self):
        square = Square(5, 2, 3, 4)
        expected_output = "[Square] (4) 2/3 - 5"
        self.assertEqual(str(square), expected_output)

    def test_getter_setter(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update(self):
        square = Square(5)
        square.update(10)
        self.assertEqual(square.id, 10)

        square.update(1, 2)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)

        square.update(1, 2, 3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)

        square.update(1, 2, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

        square.update(x=5)
        self.assertEqual(square.x, 5)

        square.update(size=6, y=1)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.y, 1)

        square.update(size=6, id=89,y=1)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.y, 1)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_dict, expected_dict)

        square1 = Square(8, 0, 0, 2)
        square1_dict = square1.to_dictionary()
        expected_dict1 = {'id': 2, 'size': 8, 'x': 0, 'y': 0}
        self.assertEqual(square1_dict, expected_dict1)


if __name__ == '__main__':
    unittest.main()
