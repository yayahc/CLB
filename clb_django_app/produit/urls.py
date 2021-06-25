from django.urls import path

from . import views

app_name = 'produit'

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<slug:slug>/', views.detail, name='detail'),
]