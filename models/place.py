#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy import *

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref='place', cascade='delete')
    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        viewonly=False, backref='place_amenities')

    @property
    def reviews(self):
        """reviews in FileStorage"""
        review_list = []
        dict_review = models.storage.all(models.Review)
        for key, value in dict_review:
            if value.place_id == self.id:
                review_list.append(value)
        return(review_list)

    @property
    def amenities(self):
        """amenitiesfor FileStorage"""
        amenity_list = []
        amenity_dict = models.storage.all(models.Amenity)
        for key, value in amenity_dict.items():
            for amenid in self.amenity_ids:
                if amenid == value.id:
                    amenity_list.append(value)
        return(amenity_list)

    @amenities.setter
    def amenities(self, obj):
        """set aminities in place"""
        if obj.__name__ == Amenity:
            self.amenity_ids.append(obj.id)
