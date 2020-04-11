import sys

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func

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

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable = False )
    password = Column(String(250), nullable = False )
    email = Column(String(250), nullable = False)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

    @property 
    def serialize(self):
        return {
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'date_created': self.date_created,
            'updated': self.updated,
            'id':self.id
        }

def _get_date():
    return datetime.datetime.now()



class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(String(250), nullable=False)
    author_id = Column(Integer, nullable = False)
    contact_id = Column(Integer, nullable=False)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())

    @property
    def serialize(self):
        return {
            'title':self.title,
            'content':self.content,
            'author_id':self.author_id,
            'contact_id':self.contact_id,
            'date_created':self.date_created,
            'updated':self.updated,
            'id':self.id
        }

engine = create_engine("sqlite:///contact-collection.db")
Base.metadata.create_all(engine)