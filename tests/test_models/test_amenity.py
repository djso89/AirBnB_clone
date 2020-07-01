#!/usr/bin/python3
"""
Unittest for class Amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os
import pep8


class AmenityTest(unittest.TestCase):
    """Defines tests for class Amenity"""

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = Amenity()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "name"))
