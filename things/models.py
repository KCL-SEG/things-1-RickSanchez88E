from django.core.exceptions import ValidationError
from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(blank=True, max_length=120)
    quantity = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super(Thing, self).__init__(*args, **kwargs)

    def clean(self):
        if self.quantity < 0:
            raise ValidationError({
                'quantity': 'Quantity must be greater than or equal to 0'
            })
        if self.quantity>100:
            raise ValidationError({
                'quantity': 'Quantity is over 100'
            })
