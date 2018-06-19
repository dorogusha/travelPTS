from marshmallow import Schema, fields, UnmarshalResult

# TODO: add required fields

# -- Base Schemas --
# schema for create new base entity
class EntityCreateSchema(Schema):
    label = fields.String(length=100)
    description = fields.String(length=200)
    flags = fields.Integer()
    created_at = fields.Integer(dump_only=True)
    updated_at = fields.Integer(dump_only=True)


# schema for update base entity
class EntitySchema(EntityCreateSchema):
    id = fields.Integer()
# -- END Base Schemas --