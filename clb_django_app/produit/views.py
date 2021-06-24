from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Produit, Album, Categorie, Vendeur


def categories(request):
    return {
        'categories': Categorie.objects.all()
    }

def home(request):
    produit = Produit.objects.all()
    return render(request, 'produit/home.html', {'produit':produit})