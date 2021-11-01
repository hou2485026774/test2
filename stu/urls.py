#子路由

from django.urls import path #引入包
from . import  views
urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('register/',views.register),
    path('to_register/',views.to_register),
    path('show_user/',views.show_user),
    path('show_user2/',views.show_user2),
    path('delete/',views.delete),
    path('JoinShow/',views.JoinShow),
    path('xs/',views.XueSheng)

    # path('home/',views.home)

]