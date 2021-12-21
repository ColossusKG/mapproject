from django.urls import path, include
from . import views

app_name = 'maps'

urlpatterns = [
    path('', views.index, name='index'),  # main.html로 이어짐
    path('list/', views.shop_list, name='shop_list'),
    path('list/<id>', views.naver, name='naver'),
    path('test_marker', views.ajax_marker, name='marker'),
    path('test_recommend', views.ajax_recommend, name='recommend'),

]
