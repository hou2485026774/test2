from django.urls import path

from django.urls import path #引入包
from . import  views

urlpatterns = [
    path('',views.show_message),
    path('make_message/',views.make_message)
]