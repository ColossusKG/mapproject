from django.urls import path
from . import views


app_name="mypage"

urlpatterns=[
    path('',views.index, name='index'),
    #path('',views.save_list, name='save_list'),
    path('mypage/<int:data_id>', views.save_delete, name='save_delete')

]