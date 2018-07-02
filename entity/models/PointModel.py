from sqlalchemy.sql import any_
from settings import logger
from entity.validators import PointCreateSchema, PointSchema
from .BaseModel import BaseModel
from entity.point import Point


# business-model by entity User
class PointModel(BaseModel):
    def __init__(self, select_fields: set=set()):
        """
        :param select_fields: set, list fields for result
        """
        super().__init__(
            entity_cls=Point,
            all_fields=(
                'id',
                'label',
                'description',
                'position',
                'location',
                'flags',
                'creater_id',
                'created_at',
                'updated_at',
            ),
            select_fields=select_fields
        )

    # Schema for create
    def _get_create_schema(self):
        return PointCreateSchema()

    # Schema for update
    def _get_update_schema(self):
        return PointSchema()