from django.db import models

# Create your models here.


class Vendeur(models.Model):
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    lieu = models.CharField(max_length=200, unique=True)

    class Meta:
        """Meta definition for Vendeur."""

        verbose_name = "Vendeur"
        verbose_name_plural = "Vendeur"

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image1 = models.ImageField(upload_to="produit/media", height_field=None, width_field=None)
    image2 = models.ImageField(upload_to="produit/media", height_field=None, width_field=None)
    image3 = models.ImageField(upload_to="produit/media", height_field=None, width_field=None)
    image4 = models.ImageField(upload_to="produit/media", height_field=None, width_field=None)
    image5 = models.ImageField(upload_to="produit/media", height_field=None, width_field=None)

    class Meta:
        """Meta definition for Album."""

        verbose_name = "Album"
        verbose_name_plural = "Album"

    def __str__(self):
        return self.name

class Categorie(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = "Categorie"
        verbose_name_plural = "Categorie"

    def __str__(self):
        return self.name


class Produit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    categorie = models.ForeignKey(Categorie,related_name='produit', on_delete=models.CASCADE, null=True)
    sold_by = models.ForeignKey(Vendeur,related_name='vendeur_produit' ,on_delete=models.CASCADE, null=True)
    in_stock = models.BooleanField(default=True)
    pub_date = models.DateTimeField('date published')
    date_upd = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    number = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    class Meta:
        """Meta definition Produit."""

        verbose_name = "Produit"
        verbose_name_plural = "Produit"
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name