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
    - macOs/unix : source env/bin/activate
    - Windows : .\env\Scripts\activate

2. **Installer les dépendances :**

    ```bash
    pip install -r requirements.txt

3. **Installer le projet :**

    ```bash
    pip install -e .

Apres installatation lancer les [Tests](#tests) est recommandé

## Utilisation

Pour utiliser ce projet lancer le main.py à l'aide de python en version compatible après avoir suivi l'[Installation](#installation) à la racine du projet comme suit: python3 -m src.main
En lui fournissant les arguments suivant:
- protocol: str, pouvant être (http ou https)
- hostname: str (exemple: google.fr)
- uri: str (exemple: /api)
- threshold: int , nombre de secondes avant de stopper la requête.

exemple de requete:

    ```bash
    python3 -m src.main --protocol "https" --hostname "dummyjson.com" --uri "/products" --threshold 5
    ```

## Test

Pour lancer les tests du projet utliser la commande:

    ```bash
    python -m unittest discover -s tests
    ```

Ceci va tester uniquement le bon formatage de la fonction format_url() et ne vérifie pas le protocole, nom d'hôte ou autre !
