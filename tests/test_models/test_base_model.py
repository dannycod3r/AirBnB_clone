#!/usr/bin/python3
"""Module contains test case for BaseModel
"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def test_initialization(self):
        """Test initialization"""
        # initialize test object
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

        # check if object has attributes
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

        # check the types of attributes
        self.assertEqual(type(obj.id), str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_with_kwargs(self):
        """Test object creation with keyword arguments"""
        model_data = {
            'id': '12345',
            'created_at': '2023-10-14T12:34:56.789',
            'updated_at': '2023-10-14T12:34:56.789'
        }
        obj = BaseModel(**model_data)
        self.assertEqual(obj.id, model_data['id'])
        self.assertEqual(
            obj.created_at, datetime.fromisoformat(model_data['created_at']))
        self.assertEqual(
            obj.updated_at, datetime.fromisoformat(model_data['updated_at']))

    def test_save(self):
        """Test the save method"""
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertGreater(obj.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test the to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_string_representation_of_instance(self):
        """ """
        obj = BaseModel()
        # Get the string representation of the instance
        string_output = str(obj)
        # Expected string representation format
        expected_string_output = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        # Check if the actual and expected representations match
        self.assertEqual(string_output, expected_string_output)
