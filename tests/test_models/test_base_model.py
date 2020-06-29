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
        print(b1)

    def test_to_dict(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
