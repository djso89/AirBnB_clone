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
