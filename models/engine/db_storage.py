#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from console import all_classes
from sqlalchemy import Column, Integer, String, create_engin
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __engine: None
        __Session: None
    """
    __engine = None
    __Session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                        .format(HBNB_MYSQL_DB, HBNB_MYSQL_USER,
                        HBNB_MYSQL_HOST, HBNB_MYSQL_PWD, pool_pre_ping=True)
        ***Base.metadata.create_all(engine))
        if HBNB_ENV == test:
            drop_all(tables)

    def all(self, cls=None):
        s1 = session()
        store_dict = {}
        if cls is not None:
            objects = s1.query(cls).all()
            for obj in objects:
                key = type(obj).__name__ + "." + obj.id
                store_dict.update({key: obj})
            return store_dict
        else:
            for a_class in all_classes:
                objects = s1.query(a_class).all()
                for obj in objects:
                    key = type(a_class).__name__ + "." + obj.id
                    store_dict.update({key: obj})
            return store_dict

    def new(self, obj):
        '''add object'''
        session().add(obj)

    def save(self):
        '''save the session'''
        session().commit()

    def delete(self, obj=None):
        '''delete the obj'''
        if obj is not None:
            sel = session.query(obj).all()
            for ob in sel:
                session.delete(ob)
            self.save()

    def reload(self):
        '''reload database'''
        Base.metadata.create_all(engine)
        self.__session = sessionmaker(bind=engine, expire_on_commit=False)
        session = scoped_session(self.__session)
