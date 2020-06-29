#!/use/bin/python3
"""
This module define class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class defines User information"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
