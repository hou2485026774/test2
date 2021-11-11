from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('to_add/',views.to_add),
    path('add/',views.add),
    path('delete/',views.delete),
    path('update1/',views.update1),
    path('update2/',views.update2),
]