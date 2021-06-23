from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image1 = models.ImageField(upload_to="produit", height_field=None, width_field=None)
    image2 = models.ImageField(upload_to="produit", height_field=None, width_field=None)
    image3 = models.ImageField(upload_to="produit", height_field=None, width_field=None)
    image4 = models.ImageField(upload_to="produit", height_field=None, width_field=None)
    image5 = models.ImageField(upload_to="produit", height_field=None, width_field=None)
    image6 = models.ImageField(upload_to="produit", height_field=None, width_field=None)

    class Meta:
        """Meta definition for Album."""

        verbose_name = "Album"
        verbose_name_plural = "Album"

    def __str__(self):
        return self.name

class Produit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    date_upd = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    number = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    description = models.TextField()

    class Meta:
        """Meta definition Produit."""

        verbose_name = "Produit"
        verbose_name_plural = "Produit"

    def __str__(self):
        return self.name