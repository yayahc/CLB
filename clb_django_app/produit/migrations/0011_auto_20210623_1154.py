# Generated by Django 3.2.4 on 2021-06-23 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0010_auto_20210623_1144'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Moto',
            new_name='Produit_par_categorie',
        ),
        migrations.AlterModelOptions(
            name='produit_par_categorie',
            options={'verbose_name': 'Produit_par_categorie', 'verbose_name_plural': 'Produit_par_categorie'},
        ),
        migrations.RenameField(
            model_name='produit_par_categorie',
            old_name='produit',
            new_name='produit_par_categorie',
        ),
    ]
