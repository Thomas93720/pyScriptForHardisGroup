# TP: ScriptForHardisGroup

Ce script effectue un GET à l'endpoint désiré et retourne un JSON des données de celle-ci si la page le permet dans le temps imparti.

## Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Tests](#tests)

## Installation

Pour installer ce projet, suivez les étapes ci-dessous :

1. **Clonez le dépôt :**

   ```bash
   git clone https://github.com/Thomas93720/pyScriptForHardisGroup.git
   cd pyScriptForHardisGroup

3. **Créer un environement virtuel :**

    ```bash
    python -m venv env

2. **Lancer la commande :**

    ```bash
    pip install -e .

Celle-ci va se charger d'installer le projet correctement

## Utilisation

Pour utiliser ce projet lancer le main.py à l'aide de python en version compatible après avoir suivi l'[Installation](#installation)
En lui fournissant les arguments suivant:
- protocol: str, pouvant être (http ou https)
- hostname: str (exemple: google.fr)
- uri: str (exemple: /api)
- threshold: int , nombre de secondes avant de stopper la requête.

## Test

Pour lancer les tests du projet utliser la commande:

    ```bash
    python -m unittest discover -s tests
    ```

Ceci va tester uniquement le bon formatage de la fonction format_url() et ne vérifie pas le protocole, nom d'hôte ou autre !
