#!/usr/bin/python3
"""A module that holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import hashlib


class User(BaseModel, Base):
    """The Representation of a user """
    def __init__(self, *args, **kwargs):
        """this initializes user"""
        if kwargs.get('password'):
            pwd = hashlib.md5(kwargs['password'].encode()).hexdigest()
            kwargs['password'] = pwd
        super().__init__(*args, **kwargs)

    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """this initializes user"""
        super().__init__(*args, **kwargs)
