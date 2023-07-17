#!/usr/bin/python3
"""Unittests for rectangle module"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):
    """Defines the unittests for Rectangle class"""
    
    def test_constructor(self):
        """Test constructor with different values"""

        obj = Rectangle(15, 25, 5, 5,)
        self.assertEqual(obj.width, 15)
        self.assertEqual(obj.height, 25)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 5)

    def test_constructor_passing_invalid_width_type(self):
        """Test constructor when invalid width value type is passed""" 
        with self.assertRaises(TypeError) as e:
            Rectangle("Musa", 25, 5, 5)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_constructor_passing_invalid_width_value(self):
        """Test constructor when invalid width value is passed"""
        with self.assertRaises(ValueError) as e:
            Rectangle(-15, 25, 5, 5)
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_constructor_passing_invalid_height_type(self):
        """Test constructor when invalid height value type is passed"""
        with self.assertRaises(TypeError) as e:
            Rectangle(15, "Musa", 5, 5)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_constructor_passing_invalid_height_value(self):
        """Test constructor when invalid height value is passed"""
        with self.assertRaises(ValueError) as e:
            Rectangle(15, -25, 5, 5)
        self.assertEqual(str(e.exception), 'height must be > 0')

    def test_constructor_passing_invalid_x_type(self):
        """Test constructor when invalid x value type is passed"""
        with self.assertRaises(TypeError) as e:
            Rectangle(15, 25, "Musa", 5)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_constructor_passing_invalid_x_value(self):
        """Test constructor when invalid x value is passed"""
        with self.assertRaises(ValueError) as e:
            Rectangle(15, 25, -5, 5)
        self.assertEqual(str(e.exception), 'x must be >= 0')

    def test_constructor_passing_invalid_y_type(self):
        """Test constructor when invalid y value type is passed"""
        with self.assertRaises(TypeError) as e:
            Rectangle(15, 25, 5, "Musa")
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_constructor_passing_invalid_y_value(self):
        """Test constructor when invalid y value is passed"""
        with self.assertRaises(ValueError) as e:
            Rectangle(15, 25, 5, -5)
        self.assertEqual(str(e.exception), 'y must be >= 0')

    def test_inheritence(self):
        """Test if Rectangle class inherits from Base class"""
        obj = Rectangle(15, 25)
        self.assertIsInstance(obj, Base)

    def test_area(self):
        """Test the area method"""
        rectangle = Rectangle(10, 20)
        expected_area = 10 * 20
        self.assertEqual(rectangle.area(), expected_area)

    def test_display(self):
        """Test the display method"""
        rectangle = Rectangle(3, 4, 2, 3)
        expected_output = "\n\n\n  ###\n  ###\n  ###\n  ###\n"
        # redirect stdout to a StringIO object
        stdout = sys.stdout
        sys.stdout = StringIO()

        rectangle.display()     # call display method
        printed_output = sys.stdout.getvalue()    # get printed output
        sys.stdout =  stdout    # 
        # check for matches between printed and expected
        self.assertEqual(printed_output, expected_output)

    def test_str(self):
        """Test the __str__ method"""
        rectangle = Rectangle(15, 25, 5, 5, 100)
        expected_output = "[Rectangle] (100) 5/5 - 15/25"
        actual_output = str(rectangle)
        self.assertEqual(actual_output, expected_output)

    def test_update(self):
        """test the update method"""
        rectangle = Rectangle(10, 10, 10, 10, 1)

        # update with *agrs
        rectangle.update(1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/10")
        
        rectangle.update(1, 2)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 2/10")

        rectangle.update(1, 2, 3)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 3/10 - 2/3")

        rectangle.update(1, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 3/4 - 2/3")

        rectangle.update(1, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 3/5 - 2/3")

        # update with **kwargs
        rectangle.update(id=89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 1/3")

        rectangle.update(id=89, widht=2)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 2/3")

        rectangle.update(id=89, width=2, height=1)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 2/1")

        rectangle.update(id=89, width=2, height=1, x=3)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 2/1")

        rectangle.update(id=89, width=2, height=1, x=3, y=4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 2/1")

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        rectangle = Rectangle(10, 5, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'width': 10,
            'height': 5,
            'x': 2,
            'y': 3
        }
        actual_dict = rectangle.to_dictionary()
        self.assertEqual(actual_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
