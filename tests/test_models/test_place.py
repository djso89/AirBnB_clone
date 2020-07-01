#!/usr/bin/python3
"""
Unittest for class Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel
import os
import pep8


class PlaceTest(unittest.TestCase):
    """Defines tests for class Place"""

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
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertTrue(len(Place.__init__) > 1)
        self.assertTrue(len(Place.__doc__) > 1)
        self.assertTrue(len(Place.__str__) > 1)
        self.assertTrue(len(Place.to_dict.__doc__) > 1)
        self.assertTrue(len(Place.save.__doc__) > 1)

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
