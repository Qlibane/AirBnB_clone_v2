#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime
import models
import sys
import os
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
    A base class for all hbnb models
    """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), nullable=False, unique=True, primary_key=True)
        created_at = Column(DateTime,
                            nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime,
                            nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if kwargs.get('__clas__', None):
                del kwargs['__class__']
            if kwargs.get('id', None) is None:
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update(
            {'__class__': (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """
        delete this objects instance from the storage engine
        """
        models.storage.delete(self)
