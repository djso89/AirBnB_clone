#!/usr/bin/python3
"""
file_storage module
"""
import json
import models
from models.base_model import BaseModel

class FileStorage:
    """ FileStorage Class """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Public method for getting dictionary object """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id
        """
        class_name = obj.__class__.__name__
        key = class_name + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        if file_path exist
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode="w") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, mode="r") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**(value))
                    self.__objects[key] = value
        except Exception:
            pass
