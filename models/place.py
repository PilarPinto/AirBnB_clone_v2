#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import models
import os


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"), primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"), primary_key=True,
                             nullable=False))


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
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship("Review", cascade="delete", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")

    else:
        @property
        def reviews(self):
            """ Getter for reviews
            Return:
            the list of Review instances with place_id equals
            to the current Place.id
            """
            objs = models.storage.all(Review)
            return [v for k, v in objs.items() if v.place_id == self.id]

        @property
        def amenities(self):
            """ Getter for amenities
            Return:
            list of Amenity instances based on the attribute amenity_ids that
            contains all Amenity.id linked to the Place
            """
            objs = models.storage.all(Amenity)
            return [v for k, v in objs.items() if v.place_id == self.id]

        @amenities.setter
        def amenities(self, value):
            """ Setter for amenities
            Return:
            Handles append method for adding an Amenity.id to
            the attribute amenity_ids
            """
            if 'Amenity' in value:
                self.amenity_ids.append(value)
