#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary
        Return:
            returns a dictionary of a given cls
            or
            returns a dictionary of __object
        """
        val_dict = {}
        dup_dict = {}
        for key in self.__objects:
            val_dict = self.__objects[key].__dict__
            if "_sa_instance_state" in val_dict:
                del val_dict["_sa_instance_state"]
            dup_dict[key] = val_dict
        if cls in dup_dict:
            return (dup_dict[cls])
        else:
            return (dup_dict)

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes the obj from __objects
        """
        if obj is not None:
            del_obj = type(obj).__name__ + "." + obj.id
            if del_obj in self.__objects:
                self.__objects.pop(del_obj)
