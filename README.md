# Django-Pro-AMDI
Site de commerce électronique pour l'expédition de cartes graphiques.
##Créer un nouveau dossier.
En utilisant votre interface de pc ou mac, ou sur l'invite de command:
```bash
mkdir myproject
cd myproject
```

##Préparation de l'environnement.
Creér un enivronnement virtuelle.
Sur windows.
```bash
python -m venv virtName
```
Activer l'environnement.

```bash
source virt/Scripts/activate
```
sur Mac.
```bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
```
##Télecharger le projet dans votre espace locale.
```bash
git clone https://github.com/abdelatiff/Django-Pro-AMDI.git
cd Django-Pro-AMDI
```

##Installer les packages requits

```bash
pip install -r requirements.txt
```
##Éxecuter l'application.
```bash
python manage.py runserver
```