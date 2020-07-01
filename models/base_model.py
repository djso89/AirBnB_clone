#!/usr/bin/python3
"""
This module define class BaseModel
"""

import uuid
from datetime import datetime
import models


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
        try:
            self.id
        except Exception:
            self.id = str(uuid.uuid4())
        try:
            self.created_at
        except Exception:
            self.updated_at = datetime.now()
            self.created_at = datetime.now()

    def __str__(self):
        """
        return the string version of BaseModel
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """save the instances """
        self.updated_at = datetime.now()

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
