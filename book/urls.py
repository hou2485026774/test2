from django.urls import path
from . import views

urlpatterns = [
    path('',views.index1),#登录页
    path('index/',views.index),#图书主页
    path('login/',views.login),
    path('register/',views.register),
    path('to_register/',views.to_register),
    path('to_add/',views.to_add),
    path('add/',views.add),
    path('delete/',views.delete),
    path('update1/',views.update1),
    path('update2/',views.update2),
    path('person/',views.person),#个人中心
    path('lend/',views.lend),#借阅图书
    path('lend_history/',views.lend_history)#借阅历史查询
]