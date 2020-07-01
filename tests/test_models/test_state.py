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
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "not pep8 compliant")

    def test_docstring(self):
        """Test compliance with doctring requirements"""
        self.assertTrue(len(State.__init__) > 1)
        self.assertTrue(len(State.__doc__) > 1)
        self.assertTrue(len(State.__str__) > 1)
        self.assertTrue(len(State.to_dict.__doc__) > 1)
        self.assertTrue(len(State.save.__doc__) > 1)

    def test_attributes(self):
        """Test if instance of BaseModel successfully made"""
        kuppa = State()
        self.assertTrue(hasattr(kuppa, "id"))
        self.assertTrue(hasattr(kuppa, "created_at"))
        self.assertTrue(hasattr(kuppa, "updated_at"))
        self.assertTrue(hasattr(kuppa, "name"))
