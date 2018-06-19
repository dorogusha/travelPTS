from sqlalchemy.sql import any_
from settings import logger
from .BaseModel import BaseModel
from entity.category import Category


# business-model by entity User
class CategoryModel(BaseModel):
    def __init__(self, select_fields: set=set()):
        """
        :param tsp_id: int, id Account
        :param select_fields: set, list fields for result
        """
        super().__init__(
            entity_cls=Category,
            all_fields=(
                'id',
                'label',
                'description',
                'flags',
                'creater_id',
                'created_at',
                'updated_at',
            ),
            select_fields=select_fields
        )