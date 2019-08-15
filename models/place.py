#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
import models


class Place(BaseModel):
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
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    reviews = relationship("Review", cascade=delete, backref='place')

    @property
    def reviews(self):
        """reviews in FileStorage"""
        review_list = []
        dict_review = models.storage.all(models.Review)
        for key, value in dict_review:
            if value.place_id == self.id:
                review_list.append(value)
        return(review_list)
