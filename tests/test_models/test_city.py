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
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertTrue(len(City.__init__) > 1)
        self.assertTrue(len(City.__doc__) > 1)
        self.assertTrue(len(City.__str__) > 1)
        self.assertTrue(len(City.to_dict.__doc__) > 1)
        self.assertTrue(len(City.save.__doc__) > 1)

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = City()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "state_id"))
        self.assertTrue(hasattr(kuppa, "name"))
