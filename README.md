# Django_work

Installer python, py charm via les sites web (ajouter les application aux variable d'environnement)

>python -m venv project_django

>cd project_django

>cd Scripts

>activate

>cd ../

>pip install Django

>django-admin startproject django_project

>cd django_project

>python manage.py runserver

>python manage.py makemigrations django_project

>python manage.py migrate

Remplacer le dossier "django_project" par celui de ce répertoire GitHub puis refaire une migration->

>python manage.py makemigrations django_project

>python manage.py migrate

Site visible en locale avec runserver -> 

>python manage.py runserver

(copier adresse de l'url puis l'ouvrir dans le naviguateur)
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
