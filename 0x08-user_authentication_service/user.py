#!/usr/bin/env python3
""" 
n this task you will create a SQLAlchemy model named
User for a database table named users (by using the 
mapping declaration of SQLAlchemy).

The model will have the following attributes:

    id, the integer primary key
    email, a non-nullable string
    hashed_password, a non-nullable string
    session_id, a nullable string
    reset_token, a nullable string
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ User class """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, *args, **kwargs):
        """ init method """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """ str method """
        return "{}: {}".format(self.id, self.email)

    def to_json(self):
        """ to_json method """
        return {
            "id": self.id,
            "email": self.email,
            "hashed_password": self.hashed_password,
            "session_id": self.session_id,
            "reset_token": self.reset_token
        }
