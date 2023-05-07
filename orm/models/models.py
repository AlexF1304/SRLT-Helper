from tortoise.models import Model
from tortoise import fields


class RMANumberTable(Model):
    id = fields.BigIntField(pk=True)
    rma_number = fields.CharField(max_length=20)

    def __str__(self):
        return self.rma_number
