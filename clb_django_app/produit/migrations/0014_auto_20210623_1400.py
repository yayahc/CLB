# Generated by Django 3.2.4 on 2021-06-23 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0013_auto_20210623_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='produit',
        ),
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produit.categorie'),
        ),
    ]
