from django.db import models
from .vehicle_type import Vehicle_type


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField('name', max_length=45)
    short_description = models.CharField('short_description', max_length=45)
    long_description = models.CharField('long_description', max_length=300)
    color = models.CharField("color", max_length=25)
    img_url = models.CharField("img_url", max_length=300)
    type = models.ForeignKey(
        Vehicle_type, related_name="vehicle", on_delete=models.SET_NULL, null = True)
    in_use = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
