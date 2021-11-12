from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class gg01(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    mark = models.ManyToManyField(User)

    def __str__(self):
        return self.name, type


class gg02(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg03(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg04(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg05(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg06(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg07(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg08(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg09(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg10(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg11(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg12(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg13(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg14(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg15(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg16(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg17(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg18(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg19(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg20(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg21(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg22(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg23(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg24(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg25(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg26(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg27(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type


class gg28(models.Model):
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    def __str__(self):
        return self.name, type



