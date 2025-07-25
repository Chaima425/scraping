# 📚 Projet Scraping Livres (Site + API)

## Description
Ce projet vise à collecter des données de livres depuis deux sources :
- 🌐 Le site [Books to Scrape](http://books.toscrape.com)
- 📡 L'API Google Books

Les données sont ensuite nettoyées, enregistrées dans des fichiers `.csv` et stockées dans une base SQLite (`books.db`).

## Structure
- `get_data/` : récupération des données (web + API)
- `process_data/` : nettoyage et préparation
- `database/` : insertion dans la base SQLite
- `pipelines/` : exécution des différentes étapes
- `main.py` : point d'entrée du projet

## Utilisation

```bash
# Cloner le projet et aller dans le dossier
git clone <url_du_repo>
cd mon_projet_scraping

# Créer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer le traitement complet
python3 main.py
