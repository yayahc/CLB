from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from clb_service import views

urlpatterns = [
    path('', views.clb_service),
]
