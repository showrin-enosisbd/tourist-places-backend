from django.utils import timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, TEXT, ForeignKey
from sqlalchemy.orm import relationship

from backend.session import Base
from account.models import User


class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime,
                        default=timezone.now(), nullable=True)
    updated_at = Column(DateTime, onupdate=timezone.now())
    name = Column(String(100))
    address = Column(String(255))
    rating = Column(Integer)
    type = Column(String(50))
    picture = Column(TEXT)
    creator_id = Column(Integer, ForeignKey(
        User.id, ondelete="CASCADE"), nullable=False)

    creator = relationship('User')
