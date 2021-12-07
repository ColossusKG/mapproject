from django.contrib import admin
from .models import data

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    search_fields = ['name','author']

admin.site.register(data,DataAdmin)

