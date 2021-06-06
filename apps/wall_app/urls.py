from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('message/create', views.msg_create),
    path('comment/create', views.cmnt_create),
]
