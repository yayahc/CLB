from django.contrib import admin

# Register your models here.

from .models import Produit, Album, Categorie

admin.site.register(Produit)
admin.site.register(Album)
admin.site.register(Categorie)