#!/usr/bin/python3
"""This is the Base Model script"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines a parent class BaseModel"""

    def __init__(self):
        """Initializes Public instance Attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the official string representation of object"""
        return f"[{type(self).__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Saves and update the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary of all keys and values of __dict__ instance"""
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = type(self).__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()
        return base_dict
