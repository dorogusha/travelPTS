from sqlalchemy import Column, Integer, String, Boolean, types, ForeignKey, DateTime, DATETIME, UniqueConstraint
from sqlalchemy.sql import select, update, and_, any_, join, outerjoin, delete
from datetime import datetime
from .base import Base, BaseEntity
from common.managers.dbManager import DBManager


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

    @classmethod
    # select tags for units
    async def select_by_tracks(cls, track_ids: list = None, point_ids: list or set = None, fields: list=None) -> list:
        # join
        j = join(TrackPoints, Track, TrackPoints.track_id == Track.id, isouter=True)

        # set selected fields
        if not fields:
            fields = [TrackPoints, Track]

        # query to db
        query = select(fields)

        # conditions
        # by track_ids
        if track_ids:
            query = query.where(TrackPoints.track_id == any_(track_ids))
        # by point_ids
        if point_ids:
            query = query.where(TrackPoints.point_id == any_(point_ids))

        # add join
        query = query.select_from(j)

        # return all records
        return await DBManager().query_fetch(query)


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