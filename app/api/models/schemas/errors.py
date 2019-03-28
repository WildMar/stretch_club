from marshmallow import Schema
from marshmallow import fields


class ErrorSchema(Schema):
    status_code = fields.Integer()
    message = fields.String()
