# Backend du projet gerer en Django + Bonnus Cours Django Starter

## Django Starter (cheat code)

<br>

## Créer un nouveau projet
```bash
mkdir mon_projet
```

## Ouvrir son projet
```zsh
cd mon_projet
```

## Créer un environement virtuel

- Pour windows
```bash
python -m virtualenv venv
```

- Pour Mac
```zsh
python3 -m venv venv
```

- Pour Linux
```bash
virtualenv venv
```
## Activer votre environement virtuel

- Pour windows
```bash
venv\Scripts\activate
```

- Pour Mac
```zsh
.source venv/bin/activate
```

- Pour Linux
```bash
source venv/bin/activate
```
## Desactiver votre environement virtuel

- Pour windows
```bash
deactivate
```

- Pour Mac
```zsh
deactivate
```

- Pour Linux
```bash
deactivate
```

## Installer Django
```python
pip install django
```

## Verifier que Django est bien installer
```python
python -m django --version
```

## Créer un projet Django
```python
django-admin startproject mon_project
```

## Lancez le serveur de Django
```python
mon_project/manage.py runserver
```

Bravo 🎉 <br><br>

## Créer une application Django
```python
django-admin startapp mon_app
```

## Ajout d'un modèle dans mon_app/models.py
```python
class my_model(models.Model):
    name = models.CharField(max_length=200, unique=True)
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    date_upd = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    number = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    description = models.TextField()
```

## Installer Pillow pour utiliser <ImageField>
```python
python -m pip install pillow
```


## Exécuter les migrations
```python
python manage.py migrate
```

## Ajouter votre app a votre projet Django dans mon_projet/settings.py
```python
INSTALLED_APPS = [
    'mon_app.apps.Mon_appConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Créer un fichier de migration
```python
python manage.py makemigrations mon_app

python manage.py sqlmigrate mon_app 0001

python manage.py migrate
```

Bingo 🎉 <br><br>

## Créer un utilisateur administrateur
```python
python manage.py createsuperuser

>>>
Username: admin
Email address: mon_email@gmail.com
Password: **********
Password (again): *********

python manage.py runserver
```
## Afficher un model sur la page d'administration Django
```python
from django.contrib import admin

# Register your models here.

from .models import my_model

admin.site.register(my_model)
```

## Creér une vue
```python
def my_app(request):
    latest_object_list = my_app.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.object_of_my_app_model for q in latest_object_list])
    return HttpResponse(output)
```

## Configurer les urls dans my_app/urls.py
```python
urlpatterns = [
    path('', views.my_app, name='my_app'),
]
```

## Configurer les urls dans mon_projet/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("my_app/", include("my_app.urls")),
]

```

Go 👌
Documentation Officielle : https://docs.djangoproject.com/en/3.2/intro/