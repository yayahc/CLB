# Backend with Django + Bonus

## Django (cheat code)

<br>

## Create project folder
```bash
mkdir my_projet
```

## Open project folder
```zsh
cd my_projet
```

## Create virtualenv

- windows
```bash
python -m virtualenv venv
```

- Mac
```zsh
python3 -m venv venv
```

- Linux
```bash
virtualenv venv
```
## Activate virtualenv

- windows
```bash
venv\Scripts\activate
```

- Mac
```zsh
.source venv/bin/activate
```

- Linux
```bash
source venv/bin/activate
```
## Deactivate virtualenv

- windows
```bash
deactivate
```

- Mac
```zsh
deactivate
```

- Linux
```bash
deactivate
```

## Install Django
```python
pip install django
```

## Verify if django is install
```python
python -m django --version
```

## Create django project
```python
django-admin startproject mon_project
```

## Run django server
```python
mon_project/manage.py runserver
```

Bravo 🎉 <br><br>

## Create django app
```python
django-admin startapp mon_app
```

## Add your models on your_app/models.py
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

## Install Pillow to use <ImageField>
```python
python -m pip install pillow
```

## Do the migrations
```python
python manage.py migrate
```

## Add your app in your django project into my_projet/settings.py file
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

## Create migration file
```python
python manage.py makemigrations mon_app

python manage.py sqlmigrate mon_app 0001

python manage.py migrate
```

Bingo 🎉 <br><br>

## Create user admin
```python
python manage.py createsuperuser

>>>
Username: admin
Email address: mon_email@gmail.com
Password: **********
Password (again): *********

python manage.py runserver
```
## Display a model into the admin page
```python
from django.contrib import admin

# Register your models here.

from .models import my_model

admin.site.register(my_model)
```

## Cceate view in views,py
```python
def my_app(request):
    latest_object_list = my_app.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.object_of_my_app_model for q in latest_object_list])
    return HttpResponse(output)
```

## Set the urls in my_app/urls.py
```python
urlpatterns = [
    path('', views.my_app, name='my_app'),
]
```

## Setting urls into my_project/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("my_app/", include("my_app.urls")),
]

```

Go 👌
Documentation : https://docs.djangoproject.com/en/3.2/intro/