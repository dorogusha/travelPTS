from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, DATETIME, UniqueConstraint
from datetime import datetime
from .base import Base, BaseEntity


# Entity Category
class Category(Base, BaseEntity):
    __tablename__ = 'Category'

    # id
    id = Column(Integer, primary_key=True)
    # Category name
    label = Column(String(100), unique=True)
    # description
    description = Column(String(length=200))
    # access flags
    flags = Column(Integer, default=0)
    # Creater id
    creater_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    # time created
    created_at = Column(Integer, default=int(datetime.now().timestamp()))
    # time updated
    updated_at = Column(Integer, default=int(datetime.now().timestamp()), onupdate=int(datetime.now().timestamp()))

    __table_args__ = (
        UniqueConstraint('name'),
    )
