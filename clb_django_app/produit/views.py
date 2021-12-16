from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Produit, Categorie, Vendeur


def categories(request):
    return {
        'categories': Categorie.objects.all()
    }

def home(request):
    produit = Produit.objects.filter(in_home=True)
    return render(request, 'pages/home.html', {'produit':produit})

def detail(request, slug):
    produit = get_object_or_404(Produit, slug=slug, in_stock=True)
    return render(request, 'pages/detail.html', {'produit':produit})

def categorie_list(request, categorie_slug):
    categorie = get_object_or_404(Categorie, slug=categorie_slug)
    produit = Produit.objects.filter(categorie=categorie)
    return render(request, 'pages/categorie.html', {'produit':produit, 'categorie':categorie})

def achat(request):
    return render(request, 'produit/achat.html')