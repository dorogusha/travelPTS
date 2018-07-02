from marshmallow import Schema, fields, UnmarshalResult

# TODO: add required fields

# -- Base Schemas --
# schema for create new base entity
class EntityCreateSchema(Schema):
    description = fields.String(length=200)
    flags = fields.Integer()
    created_at = fields.Integer(dump_only=True)
    updated_at = fields.Integer(dump_only=True)


# schema for update base entity
class EntitySchema(EntityCreateSchema):
    id = fields.Integer()
# -- END Base Schemas --


class UserCreateSchema(EntityCreateSchema):
    name = fields.String(length=100)
    password = fields.String(load_only=True)
    email = fields.Email()
    data = fields.Dict()

class UserSchema(UserCreateSchema):
    id = fields.Integer()


class CategoryCreateSchema(EntityCreateSchema):
    label = fields.String(length=100)
    creater_id = fields.Integer()


class CategorySchema(CategoryCreateSchema):
    id = fields.Integer()


class TrackCreateSchema(EntityCreateSchema):
    label = fields.String(length=100)
    creater_id = fields.Integer()


class TrackSchema(TrackCreateSchema):
    id = fields.Integer()


class PointCreateSchema(EntityCreateSchema):
    label = fields.String(length=100)
    position = fields.Dict()
    location = fields.String(length=200)
    creater_id = fields.Integer()


class PointSchema(TrackCreateSchema):
    id = fields.Integer()