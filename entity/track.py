from sqlalchemy import Column, Integer, String, Boolean, types, ForeignKey, DateTime, DATETIME, UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from .base import Base, BaseEntity


# Entity Category
class Track(Base, BaseEntity):
    __tablename__ = 'Tracks'

    # id
    id = Column(Integer, primary_key=True)
    # Category name
    label = Column(String(200))
    # description
    description = Column(String(length=200))
    # access flags
    flags = Column(Integer, default=0)
    # Creater id
    creater_id = Column(Integer, ForeignKey('Users.id', ondelete='CASCADE'), nullable=False)
    # time created
    created_at = Column(Integer, default=int(datetime.now().timestamp()))
    # time updated
    updated_at = Column(Integer, default=int(datetime.now().timestamp()), onupdate=int(datetime.now().timestamp()))

    __table_args__ = (
        UniqueConstraint('label'),
    )


# Entity TrackPoints
class TrackPoints(Base, BaseEntity):
    __tablename__ = 'TrackPoints'

    # id
    id = Column(Integer, primary_key=True)
    # Tag id
    track_id = Column(Integer, ForeignKey('Tracks.id'), nullable=False)
    # Unit id
    point_id = Column(Integer, ForeignKey('Points.id'), nullable=False)

    __table_args__ = (
        # unique tag-unit
        UniqueConstraint('track_id', 'point_id'),
    )


# Entity TrackCategories
class TrackCategories(Base, BaseEntity):
    __tablename__ = 'TrackCategories'

    # id
    id = Column(Integer, primary_key=True)
    # Tag id
    track_id = Column(Integer, ForeignKey('Tracks.id'), nullable=False)
    # Unit id
    category_id = Column(Integer, ForeignKey('Categories.id'), nullable=False)

    __table_args__ = (
        # unique tag-unit
        UniqueConstraint('track_id', 'category_id'),
    )