#!/usr/bin/python3
"""Module contains test case for Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test case for Place"""

    def test_place_instance(self):
        """Test if instance is Place and BaseModel"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_place_attributes(self):
        """Test all attributes are available"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_place_attribute_defaults(self):
        """Test default values of attributes"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attribute_assignment(self):
        """Test attributes assignment"""
        place = Place()
        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "Cozy Cottage"
        place.number_rooms = 3
        place.price_by_night = 100
        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.price_by_night, 100)
