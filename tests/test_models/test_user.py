#!/usr/bin/python3
"""
Unittest for class User
"""
import unittest
from models.user import User
from models.base_model import BaseModel
import os
import pep8


class UserTest(unittest.TestCase):
    """Defines tests for class User"""

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
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertTrue(len(User.__init__) > 1)
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__str__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = User()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "email"))
        self.assertTrue(hasattr(kuppa, "password"))
        self.assertTrue(hasattr(kuppa, "first_name"))
        self.assertTrue(hasattr(kuppa, "last_name"))
