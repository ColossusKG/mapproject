from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


class Gmap01(models.Model):
    num = models.IntegerField(max_length=10)
    city = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    cate = models.CharField(max_length=50)
    doroaddr = models.CharField(max_length=100)
    dongaddr = models.CharField(max_length=100)
    zipcode = models.IntegerField(max_length=10)
    lat = models.FloatField(max_length=20)
    lng = models.FloatField(max_length=20)
