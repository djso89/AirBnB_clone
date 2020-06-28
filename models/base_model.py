#!/usr/bin/python3
"""
This module define class BaseModel
"""

import json
import uuid
import os

from datetime import datetime, date, time



class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize a BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        #return the string version of BaseModel
        return ("[{}] ({}) {}".
                format(self.__class__.__name__,self.id, self.__dict__))

