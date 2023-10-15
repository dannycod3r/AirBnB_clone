#!/usr/bin/python3
"""Module contains test case for State class
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test case for State"""

    def test_state_instance(self):
        """Test instance is State and BaseModel"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_state_attributes(self):
        """Test instance has all attribute"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_state_attribute_default(self):
        """Test default attribute is empty string"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attribute_assignment(self):
        """Test attribute assignment"""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")
