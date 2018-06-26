from aiohttp import web
from core.web_view import DefaultMethodsImpl
from entity.models.CategoryModel import CategoryModel
from entity.models.UserModel import UserModel
from entity.models.TrackModel import TrackModel
from entity.models.PointModel import PointModel

from marshmallow import Schema, fields, UnmarshalResult


# Class View
class Category(DefaultMethodsImpl):
    # get business-model
    def get_model(self):
        return CategoryModel(select_fields=self.request_def_params['fields'])

    # HTTP: GET
    async def get(self):
        # get users by get-params
        data = await (self.get_model()).get_entities(
            ids=self.request_def_params['ids'],
            filter_name=self.request.rel_url.query.get('label', None)
        )

        return web.json_response(data=dict(result=data[0], errors=data[1]))


# Class View
class User(DefaultMethodsImpl):
    # get business-model
    def get_model(self):
        return UserModel(select_fields=self.request_def_params['fields'])


# Class View
class Track(DefaultMethodsImpl):
    # get business-model
    def get_model(self):
        return TrackModel(select_fields=self.request_def_params['fields'])


# Class View
class Point(DefaultMethodsImpl):
    # get business-model
    def get_model(self):
        return PointModel(select_fields=self.request_def_params['fields'])