from django.utils import timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ARRAY
from sqlalchemy.orm import relationship
from backend.session import Base


class User(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(150))
    email = Column('email', String(255), unique=True)
    created_at = Column('created_at', DateTime, default=timezone.now())
    updated_at = Column('updated_at', DateTime, onupdate=timezone.now())

    places = relationship('Place')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
