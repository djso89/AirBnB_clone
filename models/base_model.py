#!/usr/bin/python3
"""
Base model module
"""

import json
import uuid
import os
from datetime import datetime

class BaseModel:
    """Base class """

    def __init__(self):
        # generate unique id and convert to string
        #convert uid to string
        self.id = str(uuid.uuid4())
        #assign created_at
        self.created_at = datetime.now()

    def __str__(self):
        #return the string version of BaseModel
        return ("[{}] ({}) {}".
                format(self.__class__.__name__,self.id, self.__dict__))
