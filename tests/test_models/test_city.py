#!/usr/bin/python3
"""
Unittest for class City
"""
import unittest
from models.city import City
from models.base_model import BaseModel
import os
import pep8


class CityTest(unittest.TestCase):
    """Defines tests for class City"""

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = City()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "state_id"))
        self.assertTrue(hasattr(kuppa, "name"))
