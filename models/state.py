#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='delete')

    @property
    def cities(self):
        """getter attribute to return list of city instance"""
        city_list = []
        for key, value in models.storage.all(models.City).items():
            if value.state_id == self.id:
                city_list.append(value)
        return(city_list)
