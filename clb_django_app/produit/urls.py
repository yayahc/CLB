from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('<str:produit_name>/', views.detail, name='detail'),
]