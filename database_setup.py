import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable= False)
    last_name = Column(String(250), nullable = False)
    phone = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    street = Column(String(250))
    city = Column(String(250))
    state = Column(String(250))
    zip = Column(String(250))

    @property
    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'id': self.id
        }

engine = create_engine("sqlite:///contact-collection.db")
Base.metadata.create_all(engine)