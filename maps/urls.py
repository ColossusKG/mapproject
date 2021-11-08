from django.urls import path, include
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.index, name= 'shop_list'),
]