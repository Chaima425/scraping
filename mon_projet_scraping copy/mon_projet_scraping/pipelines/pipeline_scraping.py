#fichier orchestre toutes les étapes.
# Il importe les fonctions nécessaires pour le scraping, le traitement des données et l'insertion en base de données.   
import os
from get_data.get_scraping_data import scrape_books_df
from process_data.process_scraping_data import convert_types
from database.insert_scraping_data import create_database

def run_scraping_pipeline():
    print("run_scraping_pipeline démarrée")

    print("Étape 1 : Scraping des données...")
    df_books = scrape_books_df(2)
    print(f"{len(df_books)} livres récupérés.")

    print("Étape 2 : Sauvegarde des données brutes dans data/data_scraping.csv...")
    os.makedirs("data", exist_ok=True)
    df_books.to_csv("data/data_scraping.csv", index=False)

    print("Étape 3 : Nettoyage et traitement des données...")
    df_cleaned = convert_types(df_books)

    print("Étape 4 : Insertion en base de données SQLite...")
    create_database(df_cleaned)

    print("Pipeline terminée avec succès.")

