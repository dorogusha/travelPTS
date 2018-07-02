from sqlalchemy.sql import any_
from settings import logger
from entity.validators import TrackCreateSchema, TrackSchema
from .BaseModel import BaseModel
from entity.track import Track


# business-model by entity User
class TrackModel(BaseModel):
    def __init__(self, select_fields: set=set()):
        """
        :param select_fields: set, list fields for result
        """
        super().__init__(
            entity_cls=Track,
            all_fields=(
                'id',
                'label',
                'description',
                'flags',
                # 'points',
                'creater_id',
                'created_at',
                'updated_at',
            ),
            select_fields=select_fields
        )

    # Schema for create
    def _get_create_schema(self):
        return TrackCreateSchema()

    # Schema for update
    def _get_update_schema(self):
        return TrackSchema()