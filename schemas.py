from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str(dump=True)
    name = fields.Str(required=True)
    price = fields.Str(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump=True)
    name = fields.Str(required=True)