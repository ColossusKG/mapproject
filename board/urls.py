from django.urls import path
from . import views

app_name = 'board'

urlpatterns=[
    path('', views.index,name='index'),
    path('comment/<id>/',views.shop_comment,name='shop_comment'),
    path('comment/create/<id>/',views.shop_comment_create,name='comment_create'),
    path('comment/modify/<id>/', views.shop_comment_modify ,name='comment_modify'),
    path('comment/delete/<id>/', views.shop_comment_delete ,name='comment_delete'),

]