from sqlalchemy import Column, Integer, String, types, Boolean, ForeignKey, DateTime, DATETIME, UniqueConstraint
from datetime import datetime
from .base import Base, BaseEntity


# Entity Category
class User(Base, BaseEntity):
    __tablename__ = 'Users'

    # id
    id = Column(Integer, primary_key=True)
    # name User
    name = Column(String(length=100), unique=True)
    # description
    description = Column(String(length=200))
    # password
    password = Column(String(30), nullable=False)
    # email
    email = Column(String(30))
    # access flags
    flags = Column(Integer, default=0)
    # data
    data = Column(types.JSON)
    # time created
    created_at = Column(Integer, default=int(datetime.now().timestamp()))
    # time updated
    updated_at = Column(Integer, default=int(datetime.now().timestamp()), onupdate=int(datetime.now().timestamp()))

    __table_args__ = (
        UniqueConstraint('name'),
    )