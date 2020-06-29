#!/usr/bin/python3
"""
Unittest for class User
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class UserTest(unittest.TestCase):
    """Defines tests for class User"""

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
