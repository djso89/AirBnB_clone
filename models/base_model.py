#!/usr/bin/python3
"""
Base model module
"""

import json
import uuid
import os


class BaseModel:
    """Base class """

    def __init__(self):
        # generate unique id and convert to string
        #convert uid to string
        self.id = str(uuid.uuid4())
