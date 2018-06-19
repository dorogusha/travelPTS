from sqlalchemy import Column, Integer, String, Boolean, types, ForeignKey, DateTime, DATETIME, UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from .base import Base, BaseEntity


# Entity Category
class Point(Base, BaseEntity):
    __tablename__ = 'Points'

    # id
    id = Column(Integer, primary_key=True)
    # Category name
    label = Column(String(200))
    # description
    description = Column(String(length=200))
    # access flags
    flags = Column(Integer, default=0)
    # categories
    categories = Column(ARRAY(types.JSON), nullable=True)
    # Creater id
    creater_id = Column(Integer, ForeignKey('Users.id', ondelete='CASCADE'), nullable=False)
    # time created
    created_at = Column(Integer, default=int(datetime.now().timestamp()))
    # time updated
    updated_at = Column(Integer, default=int(datetime.now().timestamp()), onupdate=int(datetime.now().timestamp()))

    __table_args__ = (
        UniqueConstraint('label'),
    )