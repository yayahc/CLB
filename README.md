# Django Starter 

<br>

## Créer un nouveau projet
```
mkdir mon_projet
```

## Ouvrir son projet
```
cd mon_projet
```

## Créer un environement virtuel

- Pour windows
```
virtualenv venv
```

- Pour Mac
```
python3 -m venv venv
```

- Pour Linux
```
virtualenv venv
```
## Activer votre environement virtuel

- Pour windows
```
venv\Scripts\activate
```

- Pour Mac
```
.source venv/bin/activate
```

- Pour Linux
```
source venv/bin/activate
```
## Desactiver votre environement virtuel

- Pour windows
```
deactivate
```

- Pour Mac
```
deactivate
```

- Pour Linux
```
deactivate
```

## Installer Django
```
pip install django
```

## Verifier que Django est bien installer
```
python -m django --version
```

## Créer un projet Django
```
django-admin startproject mon_project
```

## Lancez le serveur de Django
```
mon_project/manage.py runserver
```

Bravo 🎉 <br><br>

## Ajout d'un modèle dans models.py
```
class Produit(models.Model):
    name = models.CharField(max_length=200, unique=True)
    number = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="clb_service")
    status = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
```
## Création du fichier de migration
```
python manage.py makemigrations
```

## Exécution des migrations
```
python manage.py migrate
```