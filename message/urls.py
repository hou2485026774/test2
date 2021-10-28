from django.urls import path

from django.urls import path #引入包
from . import  views

urlpatterns = [
    path('',views.show_message),
    path('make_message/',views.make_message),
    path('delete_message/',views.delete_message),
    path('update_message/',views.update_message),
    path('update/',views.update)
]