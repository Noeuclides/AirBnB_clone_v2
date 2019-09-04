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
from os import environ, getenv


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine: None
        __Session: None
    """
    __engine = None
    __session = None

    all_classes = {State, City, Place, User, Review, Amenity}

    def __init__(self):
        """initialize DBStorage class"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB'),
                pool_pre_ping=True))
        if "HBNB_ENV" in environ:
            if environ['HBNB_ENV'] == 'test':
                Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """show all instance of a class"""
        s1 = self.__session
        store_dict = {}
        if cls is not None:
            objects = s1.query(eval(cls)).all()
            for obj in objects:
                key = type(obj).__name__ + "." + obj.id
                store_dict.update({key: obj})
            return store_dict
        else:
            for a_class in self.all_classes:
                objects = s1.query(a_class).all()
                for obj in objects:
                    key = a_class.__name__ + "." + obj.id
                    store_dict.update({key: obj})
            return store_dict

    def new(self, obj):
        """add object"""
        self.__session.add(obj)

    def save(self):
        """save the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete the obj"""
        if obj is not None:
            sel = self.__session.query(obj).all()
            for ob in sel:
                self.__session.delete(ob)
            self.save()

    def reload(self):
        """reload database"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """close method
        """
        self.__session.close()
