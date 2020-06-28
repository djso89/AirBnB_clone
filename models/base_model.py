#!/usr/bin/python3
"""
This module define class BaseModel
"""

import json
import uuid
import os
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> be54d524cf81f1c08f627f7cde5a3fef7eb5bce8
from datetime import datetime, date, time
=======
from datetime import datetime
>>>>>>> 19afae46fb63fe70b160282ddad688b415715ec4



class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initialize a BaseModel class"""
        self.id = str(uuid.uuid4())
<<<<<<< HEAD
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
<<<<<<< HEAD
=======
        #assign created_at
        self.created_at = datetime.now()
=======

>>>>>>> be54d524cf81f1c08f627f7cde5a3fef7eb5bce8

    def __str__(self):
        #return the string version of BaseModel
        return ("[{}] ({}) {}".
                format(self.__class__.__name__,self.id, self.__dict__))
<<<<<<< HEAD
>>>>>>> 19afae46fb63fe70b160282ddad688b415715ec4
=======

>>>>>>> be54d524cf81f1c08f627f7cde5a3fef7eb5bce8
