from django.db import models

# Create your models here.

class Produit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="clb_service")
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)