# Generated by Django 3.2.9 on 2021-11-15 05:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0002_alter_data_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='mark',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]