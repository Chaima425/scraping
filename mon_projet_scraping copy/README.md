# Projet Scraping : Collecte de données multi sources

## Description

Ce projet a pour objectif de collecter automatiquement des données provenant de plusieurs sources web via des techniques de scraping.  
Les données collectées sont ensuite nettoyées, transformées, puis stockées dans une base de données pour une exploitation facilitée.

Ce travail a été organisé de façon modulaire, pour reproduire les bonnes pratiques d’un projet professionnel, et faciliter la maintenance et l’évolution du code.

## Vocabulaire utile

- **Script** : fichier `.py` contenant du code Python exécuté séquentiellement (ligne à ligne).  
- **Module** : fichier `.py` contenant des fonctions, classes, etc. pouvant être importé dans d’autres scripts.  
- **Package** : dossier contenant un fichier `__init__.py` (même vide), permettant d’importer facilement tous les modules qu’il contient.  
- Depuis Python 3.3, `__init__.py` n’est plus strictement obligatoire mais recommandé pour une bonne organisation.

**Exemple d’import** :  from mon_module import ma_fonction

### Points clés du projet :

- Collecte des données depuis site web et API, grâce à des fonctions de scraping dédiées.
- Nettoyage des données : gestion des valeurs manquantes, conversion des types, suppression des doublons, uniformisation des formats.
- Stockage des données nettoyées dans une base de données locale et sauvegarde des données brutes dans des fichiers CSV pour traçabilité.
- Structure claire du projet, avec un découpage en modules Python et dossiers spécifiques pour chaque étape du traitement.

---

## Organisation du projet

mon_projet_scraping/
│
├── data/                        # **Contient les fichiers CSV des données brutes**
│
├── get_data/                   # **Package de récupération des données**
│   ├── __init__.py
│   └── get_scraping_data.py    # **Fonctions de scraping (implémentées depuis le notebook 1)**
│
├── database/                   # **Package pour gérer la base de données**
│   ├── __init__.py
│   └── insert_data.py          # **Fonctions pour créer, insérer et vérifier les données en base (notebook 2)**
│
├── process_data/               # **Package de traitement des données**
│   ├── __init__.py
│   └── process_scrapping_data.py  # **Fonctions de nettoyage, conversion de types, etc. (notebook 2)**
│
├── pipelines/                  # **Package orchestration du pipeline complet**
│   ├── __init__.py
│   └── pipeline_scraping.py   # **Fonction `run_scraping_pipeline` qui regroupe toutes les étapes**
│
├── main.py                    # **Script principal pour lancer le pipeline**
│
├── README.md                  # **Documentation du projet (ce fichier)**
│
└── requirements.txt           # **Liste des dépendances Python à installer**


### Pipeline principal (pipeline_scraping.py)

La fonction principale **run_scraping_pipeline** réalise :

**1** Le scraping des données sous forme d’un DataFrame via **get_scraping_data.py**

**2** La sauvegarde des données brutes dans **un fichier CSV** (data/data_scraping.csv)

**3** Le nettoyage et la préparation des données (conversion des types, traitement) via **process_scrapping_data.py**

**4** L’insertion des données nettoyées dans la base via **insert_data.py**

**5** L’affichage des étapes pour informer l’utilisateur


---

## Usage

### Lancer le pipeline complet

Pour exécuter le pipeline complet de récupération, traitement et insertion des données, on doit placer  à la racine du projet et lancez la commande suivante dans un terminal :
**python3 main.py**

Ce script appelle **la fonction run_scraping_pipeline()** située dans **pipelines/pipeline_scraping.py**. Cette fonction réalise les étapes suivantes :

Collecte des données via **get_data/get_scraping_data.py**

Sauvegarde des données brutes dans **data/raw/data_scraping.csv**

Nettoyage et préparation des données avec **process_data/process_scrapping_data.py**

Insertion des données nettoyées dans la base via **database/insert_data.py**

Affichage dans le terminal des étapes en cours pour suivre l’exécution


## Exemple d’utilisation dans un script Python

Pour également importer et utiliser directement le pipeline dans n’importe quel script Python comme ceci :

python:

from pipelines.pipeline_scraping import run_scraping_pipeline

run_scraping_pipeline()
Cela permet d’intégrer facilement ce pipeline dans des scripts plus larges ou des automatisations.

## Exécution dans un environnement de développement

Le projet est compatible avec les environnements comme Visual Studio Code.
Vous pouvez lancer les scripts en cliquant droit sur le fichier puis Run Python File in Terminal,
ou démarrer un débogage (F5) pour suivre pas à pas l’exécution et analyser les variables en temps réel.

## Installation
 on doit installer les dépendances nécessaires **via pip** en utilisant **le fichier requirements.txt** :

bash:dans le terminale : 
pip install -r requirements.txt

Cela garantit que toutes les bibliothèques utilisées **(requests, pandas, sqlite3, etc.)** sont installées.

## Remarques
Cette organisation modulaire, avec séparation claire des responsabilités, permet :

**1°** De maintenir et faire évoluer le projet plus facilement

**2°** D’ajouter rapidement de nouvelles sources de données ou étapes de traitement

**3°** De faciliter la collaboration avec d’autres développeurs

**4°** D’assurer une traçabilité des données brutes et traitées

## Licence
Ce projet est sous licence MIT.