#!/usr/bin/python3
"""Defines new class FileStorage"""
import json
import datetime
import os


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """Stores a new object in the __objects dictionary using a key"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON FILE to __file_path(file.json)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as op_file:
            Ndict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(Ndict, op_file)

    def reload(self):
        """Deserializes JSON FILE to __objects(dict) if path exists"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(File.__file_path, "r", encoding="utf-8") as op_file:
            convt_dict = json.load(op_file)
        FileStorage.__objects = convt_dict

    def classes(self):
        """Returns all Implemented classes"""
        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}
        return classes
