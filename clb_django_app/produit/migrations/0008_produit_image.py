# Generated by Django 3.2.4 on 2021-06-23 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0007_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produit.album'),
        ),
    ]