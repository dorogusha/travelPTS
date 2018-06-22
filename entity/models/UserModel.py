from sqlalchemy.sql import any_
from settings import logger
from .BaseModel import BaseModel
from entity.user import User


# business-model by entity User
class UserModel(BaseModel):
    def __init__(self, select_fields: set=set()):
        """
        :param select_fields: set, list fields for result
        """
        super().__init__(
            entity_cls=User,
            all_fields=(
                'id',
                'name',
                'description',
                'password',
                'email',
                'flags',
                'data',
                'created_at',
                'updated_at',
            ),
            select_fields=select_fields
        )