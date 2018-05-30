from aiohttp import web
from core.web_view import DefaultMethodsImpl
from entity.models.CategoryModel import CategoryModel


# Class View
class Category(DefaultMethodsImpl):
    # get business-model
    def get_model(self):
        return CategoryModel(select_fields=self.request_def_params['fields'])
