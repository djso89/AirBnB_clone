#!/usr/bin/python3
"""
Unittest for class State
"""
import unittest
from models.state import State
from models.base_model import BaseModel
import os
import pep8


class StateTest(unittest.TestCase):
    """Defines tests for class State"""

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = State()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "name"))
