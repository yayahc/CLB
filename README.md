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

Bravo 🎉