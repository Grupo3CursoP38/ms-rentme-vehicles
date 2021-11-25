from django.db import models


class Vehicle_type(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=5)
    name = models.CharField('name', max_length=45, unique=True)

    def __str__(self):

        return self.name
