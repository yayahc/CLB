from django.db import models

# Create your models here.
class Produit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    date_upd = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    number = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    description = models.TextField()