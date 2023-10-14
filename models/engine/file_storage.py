#!/usr/bin/python3
"""Defines new class FileStorage"""
import json
import datetime
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary object"""
        return self.__objects

    def new(self, obj):
        """Stores a new object in the __objects dictionary using a key"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON FILE to __file_path(file.json)"""
        Ndict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as op_file:
            json.dump(Ndict, op_file)

    def reload(self):
        """Deserializes JSON FILE to __objects(dict) if path exists"""
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, 'r') as file:
            data = json.load(file)
            for key, value in data.items():
                class_name = key.split('.')[0]
                cls = eval(class_name)
                self.__objects[key] = cls(**value)

    def classes(self):
        """return a list of class names"""
        return {
            'BaseModel': BaseModel, 
            'User': User,
            'Amenity': Amenity,
            'City': City,
            'State': State,
            'Place': Place,
            'Review': Review
            }
