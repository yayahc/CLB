# Generated by Django 3.2.4 on 2021-06-24 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0018_auto_20210624_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='status',
            new_name='in_stock',
        ),
        migrations.RemoveField(
            model_name='album',
            name='image6',
        ),
    ]
