#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ

print(type(environ['HBNB_TYPE_STORAGE']))
if environ['HBNB_TYPE_STORAGE'] == 'db':
    print("enviro DB: ")
    from .engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    print("filestorage if:")
    from .engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
