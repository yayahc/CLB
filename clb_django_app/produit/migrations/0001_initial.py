# Generated by Django 3.2.4 on 2021-06-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=None)),
                ('number', models.IntegerField(default=1)),
                ('description', models.TextField()),
            ],
        ),
    ]