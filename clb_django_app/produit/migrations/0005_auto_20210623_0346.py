# Generated by Django 3.2.4 on 2021-06-23 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0004_auto_20210623_0023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Album', 'verbose_name_plural': 'Album'},
        ),
        migrations.AlterModelOptions(
            name='produit',
            options={'verbose_name': 'Produit', 'verbose_name_plural': 'Produit'},
        ),
    ]
