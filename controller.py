from aiohttp import web
from core.web_view import DefaultMethodsImpl
from entity.models.CategoryModel import CategoryModel

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
