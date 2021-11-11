#子路由

from django.urls import path #引入包
from . import  views
urlpatterns = [
    path('',views.index),
    path('login/',views.login),
    path('register/',views.register),#用户注册
    path('to_register/',views.to_register),#注册跳转
    path('show_user/',views.show_user),
    path('show_user2/',views.show_user2),#展示用户信息
    path('delete/',views.delete),
    path('JoinShow/',views.JoinShow),
    path('xs/',views.XueSheng),
    path('techer_register/',views.techer_register),#原生上传
    path('techer_register2/',views.techer_register2),#教师信息注册 含图片上传
    path('download/',views.download),#教师图片下载

    # path('home/',views.home)

]