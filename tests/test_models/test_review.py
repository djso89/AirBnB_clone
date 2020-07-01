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

    def setUp(self):
        """Set up testing environment"""
        pass

    def tearDown(self):
        """Reset testing environment"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8(self):
        """Test pep8 compliance"""
        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertTrue(len(Review.__init__) > 1)
        self.assertTrue(len(Review.__doc__) > 1)
        self.assertTrue(len(Review.__str__) > 1)
        self.assertTrue(len(Review.to_dict.__doc__) > 1)
        self.assertTrue(len(Review.save.__doc__) > 1)

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = Review()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "place_id"))
        self.assertTrue(hasattr(kuppa, "user_id"))
        self.assertTrue(hasattr(kuppa, "text"))
