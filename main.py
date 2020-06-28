#!/usr/bin/python3
""" 0-main """
from models.base_model import BaseModel

if __name__ == "__main__":

    my_model = BaseModel()
    my_model.name = "Holberton"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
