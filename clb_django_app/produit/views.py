from django.shortcuts import render, get_object_or_404
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

def detail(request, slug):
    produit = get_object_or_404(Produit, slug=slug, in_stock=True)
    return render(request, 'produit/detail.html', {'produit':produit})