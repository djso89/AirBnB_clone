#!/usr/bin/python3
"""
This module define class BaseModel
"""

import json
import uuid
from datetime import datetime, date, time
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel class """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        return the string version of BaseModel
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """save the instances """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all the keys of __dict__
        of the instances
        """
        base_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                value = value.isoformat()
            base_dict[key] = value
        return base_dict
