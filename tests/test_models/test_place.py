#!/usr/bin/python3
"""
Unittest for class Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import os
import pep8


class StateTest(unittest.TestCase):
    """Defines tests for class Place"""

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = Place()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "city_id"))
        self.assertTrue(hasattr(kuppa, "user_id"))
        self.assertTrue(hasattr(kuppa, "name"))
        self.assertTrue(hasattr(kuppa, "description"))
        self.assertTrue(hasattr(kuppa, "number_rooms"))
        self.assertTrue(hasattr(kuppa, "number_bathrooms"))
        self.assertTrue(hasattr(kuppa, "max_guest"))
        self.assertTrue(hasattr(kuppa, "price_by_night"))
        self.assertTrue(hasattr(kuppa, "latitude"))
        self.assertTrue(hasattr(kuppa, "longitude"))
        self.assertTrue(hasattr(kuppa, "amenity_ids"))
