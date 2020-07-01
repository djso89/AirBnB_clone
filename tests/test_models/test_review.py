#!/usr/bin/python3
"""
Unittest for class Review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
import os
import pep8


class ReviewTest(unittest.TestCase):
    """Defines tests for class Review"""

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = Review()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "place_id"))
        self.assertTrue(hasattr(kuppa, "user_id"))
        self.assertTrue(hasattr(kuppa, "text"))
