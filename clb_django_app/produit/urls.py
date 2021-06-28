from django.urls import path

from . import views

app_name = 'produit'

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<slug:slug>/', views.detail, name='detail'),
    path('search/<slug:categorie_slug>/', views.categorie_list, name='categorie_list'),
    path('achat/', views.achat, name='achat'),
]