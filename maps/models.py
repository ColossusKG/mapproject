from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class data(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    mark = models.ManyToManyField(User)


    class Meta:
       db_table = 'maps_data'
       managed = True

    def __str__(self):
        return self.name


class address(models.Model):
    city = models.CharField(max_length=10)
    area1_kind = models.CharField(max_length=20)
    area1 = models.CharField(max_length=20)
    area2 = models.CharField(max_length=20)

    class Meta:
        db_table = 'district'
        managed = False

    def __str__(self):
        return self.area2











