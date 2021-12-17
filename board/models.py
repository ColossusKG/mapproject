from django.db import models
from django.contrib.auth.models import User
# from maps.models import *

# Create your models here.


class ShopComment(models.Model):
    shop = models.ForeignKey('maps.data', on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="") # views함수로 경로 지정
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content

