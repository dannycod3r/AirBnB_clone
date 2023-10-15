#!/usr/bin/python3
"""Module contains test case for City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test case for City"""

    def test_city_instance(self):
        """Test instance is City and BaseModel"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_city_attributes(self):
        """Test if attributes are available"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_city_attribute_defaults(self):
        """Test default attributes are empty strings"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attribute_assignment(self):
        """Test attributes assignment"""
        city = City()
        city.state_id = "state123"
        city.name = "New York"
        self.assertEqual(city.state_id, "state123")
        self.assertEqual(city.name, "New York")
