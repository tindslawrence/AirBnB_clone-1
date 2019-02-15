#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Defines methods for storing files.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        odict = FileStorage.__objects
        ocname = obj.__class__.__name__
        odict["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict = {}
        for i, o in FileStorage.__objects.items():
            objdict[i] = o.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = {}
                objdict = json.load(f)
                for i, o in objdict.items():
                    self.new(BaseModel(**o))
        except FileNotFoundError:
            return
