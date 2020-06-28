#!/usr/bin/python3
"""
Unittest for class - BaseModel
"""

import unittest
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    """ class BaseModel unittest """
    def test_print_id(self):
        b1 = BaseModel()
        print(b1.id)
