#!/usr/bin/python3
"""Unittests for base module"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Defines the unittests for base class"""
    def test_id_value_assignment(self):
       """Test when id value is not None"""
       id_value = 5
       obj = Base(id_value)
       self.assertEqual(obj.id, id_value)

    def test_id_without_value(self):
        """Test when id value is None"""
        obj_1 = Base()
        obj_2 = Base()
        self.assertEqual(obj_1.id, 3)
        self.assertEqual(obj_2.id, 4)
    
    def test_to_json_string_empty_list(self):
        """Test to_json_string_empty_list method with an empty list"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, '[]')

    def test_to_json_string(self):
        """Test to_json_string with a list of dictionaries"""
        list_dictionaries = [{'id': 1, 'name': 'Musa'}, {'id': 2, 'name': 'Kabo'}]
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, '[{"id": 1, "name": "Musa"}, {"id": 2, "name": "Kabo"}]')

    def test_to_json_string_none(self):
        """Test to_json_string_empty_list method with None"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_save_to_file_empty_list(self):
        """Test save_to_file method with an empty list"""
        Base.save_to_file([])
        with open('Base.json', 'r') as f:
            json_data = f.read()
            self.assertEqual(json_data, '[]')
    
    def test_save_to_file_none(self):
        """Test save_to_file method with None"""
        Base.save_to_file(None)
        with open('Base.json', 'r') as f:
            json_data = f.read()
            self.assertEqual(json_data, '[]')

    def test_save_to_file(self):
        """Test save_to_file method with a list of instances"""
        list_objs = [Base(1), Base(2)]
        Base.save_to_file(list_objs)
        with open('Base.json', 'r') as f:
            json_data = f.read()
            self.assertEqual(json_data, [{'id': 1}, {'id': 2}])

    def test_from_json_string_empty_string(self):
        """Test from_json_string method with an empty string"""
        dictioneries = Base.from_json_string('')
        self.assertEqual(dictioneries, [])

    def test_from_json_string_none(self):
        """Test from_json_string method with None"""
        dictioneries = Base.from_json_string(None)
        self.assertEqual(dictioneries, [])

    def test_from_json_string(self):
        """Test from_json_string method with JSON string"""
        json_string = '[{"id": 1, "name": "Musa"}, {"id": 2, "name": "Kabo"}]'
        dictioneries = Base.from_json_string(json_string)
        self.assertEqual(dictioneries, [{'id': 1, 'name': 'Musa'}, {'id': 2, 'name': 'Kabo'}])

    def test_create_rectangle(self):
        """Test create method with attributes for Rectangle class"""
        rectangle_dict = {'id': 1, 'width': 15, 'height': 25}
        rectangle = Base.create(**rectangle_dict)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 25)

    def test_create_square(self):
        """Test create method with attributes for Square class"""
        square_dict = {'id': 1, 'size': 7}
        square = Base.create(**square_dict)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)

    def test_update_with_args_rectangle(self):
        """Test update method with positional arguments for Rectangle class"""
        rectangle = Base(1)
        rectangle.update(2, 15, 25)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 25)

    def test_update_with_args_square(self):
        """Test update method with positional arguments for Square class"""
        square = Base(1)
        square.update(2, 7)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 7)

    def test_update_with_kwargs_rectangle(self):
        """Test update method with keyword arguments for Rectangle class"""
        rectangle = Base(1)
        rectangle.update(width=10, height=20)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)

    def test_update_with_kwargs_square(self):
        """Test update method with keyword arguments for Square class"""
        square = Base(1)
        square.update(size=7)
        self.assertEqual(square.size, 7)

    def test_load_from_file_no_file(self):
        """Test load_from_file method when the file does not exist"""
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file_empty_file(self):
        """Test load_from_file method when the file is empty"""
        with open('Base.json', 'w') as f:
            f.write('')
        instances = Base.load_from_file()
        self.assertEqual(instances, [])

    def test_load_from_file(self):
        """Test load_from_file method with a valid JSON data"""
        json_data = '[{"id": 1}, {"id": 2}]'
        with open('Base.json', 'w') as f:
            f.write(json_data)
        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)




if __name__ == '__main__':
    unittest.main()
