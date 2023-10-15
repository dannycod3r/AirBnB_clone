#!/usr/bin/python3
"""Module contains test case for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test case for amenity class"""

    def test_amenity_instance(self):
        """Test if instance is Amenity and BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_attributes(self):
        """Test if instance has correct attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_attribute_default(self):
        """Test the default value is empty string"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_attribute_assignment(self):
        """Test setting the name of amenity instance"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")
