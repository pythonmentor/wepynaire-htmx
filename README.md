# Petit exemple de Django + HTMX utilisant hx-swap-oob

Cet exemple minimal d'application Django + HTMX a été construit avec l'objectif d'expliquer
le comportement de l'attribut hx-swap-oob de HTMX. 

Cet attribut htmx est ici utiliser pour gérer l'affichage des messages de succès ou 
d'erreur lors de la création d'une tâche.

## Installation des dépendances back-end

Ce projet utilise l'outil pipenv pour gérer ses dépendances back-end. S'il n'est pas
déjà installé sur votre ordinateur, vous pouvez l'installer à l'aide de la commande
`pip install pipenv`.

Une fois pipenv installé, il vous suffit de suivre les instructions suivantes:
- Installer les dépendances avec `pipenv install --dev`
- Exécuter les migrations avec `pipenv run python manage.py migrate`
- Créer un super-utilisateur avec `pipenv run python manage.py createsuperuser`

Pour tester l'exemple dans votre navigateur favori, lancez le serveur de développement
à l'aide de la commande `pipenv run python manage.py runserver`, puis visitez la
[page d'accueil du site](http://locahost:8000).