#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
import json
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import environ


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine: None
        __Session: None
    """
    __engine = None
    __Session = None

    all_classes = {"BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"}

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                environ['HBNB_MYSQL_USER'],
                environ['HBNB_MYSQL_PWD'],
                environ['HBNB_MYSQL_HOST'],
                environ['HBNB_MYSQL_DB'],
                pool_pre_ping=True))
        if "HBNB_ENV" in environ:
            if environ['HBNB_ENV'] == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        s1 = self.__session()
        store_dict = {}
        if cls is not None:
            objects = s1.query(cls).all()
            for obj in objects:
                key = type(obj).__name__ + "." + obj.id
                store_dict.update({key: obj})
            return store_dict
        else:
            for a_class in self.all_classes:
                objects = s1.query(eval(a_class)).all()
                print(objects)
                for obj in objects:
                    key = type(a_class).__name__ + "." + obj.id
                    store_dict.update({key: obj})
            return store_dict

    def new(self, obj):
        '''add object'''
        self.__session().add(obj)
        #Base.metadata.create_all(self.__engine)

    def save(self):
        '''save the session'''
        self.__session().commit()

    def delete(self, obj=None):
        '''delete the obj'''
        if obj is not None:
            sel = self.__session().query(obj).all()
            for ob in sel:
                self.__session().delete(ob)
            self.save()

    def reload(self):
        '''reload database'''
        print("reload before Base.metadata")
        print(self.__engine)
        #Base.metadata.create_all(self.__engine)
        print("reload after Base.metadata")
        self.__session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        scoped_session(self.__session)
