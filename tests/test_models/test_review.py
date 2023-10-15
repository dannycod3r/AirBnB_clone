#!/usr/bin/python3
"""Module contains case for Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test case for Review"""

    def test_review_instance(self):
        """Test review instance is Review and BaseModel"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_review_attributes(self):
        """Test instance has all attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_review_attribute_defaults(self):
        """Test default values are empty string"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attribute_assignment(self):
        """Test attribute assignment"""
        review = Review()
        review.place_id = "place123"
        review.user_id = "user123"
        review.text = "Great place to stay!"
        self.assertEqual(review.place_id, "place123")
        self.assertEqual(review.user_id, "user123")
        self.assertEqual(review.text, "Great place to stay!")
