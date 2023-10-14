#!/usr/bin/python3
"""This is the Base Model script"""

import uuid
from datetime import datetime
# from models import storage


class BaseModel:
    """Defines a parent class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes Public instance Attributes

        Args:
             *args - list of arguments
             **kwargs - dictionary representation of arguments
        """
        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)

    def __str__(self):
        """Returns the official string representation of object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves and update the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        # storage.save()

    def to_dict(self):
        """Returns a dictionary of all keys and values of __dict__ instance"""
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = type(self).__name__
        base_dict["created_at"] = base_dict["created_at"].isoformat()
        base_dict["updated_at"] = base_dict["updated_at"].isoformat()
        return base_dict
