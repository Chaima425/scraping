#fichier orchestre toutes les étapes.
def run_scraping_pipeline():
    print("run_scraping_pipeline démarrée")  # <-- ajoute ce print ici
    print(" Étape 1 : Scraping des données...")
    df_books = scrape_books_df(2)  # Par exemple scrape 2 pages
    print(f"{len(df_books)} livres récupérés.")

    print("Étape 2 : Sauvegarde des données brutes dans data/data_scraping.csv...")
    os.makedirs("data", exist_ok=True)
    df_books.to_csv("data/data_scraping.csv", index=False)

    print("Étape 3 : Nettoyage et traitement des données...")
    df_cleaned = convert_types(df_books)

    print("Étape 4 : Insertion en base de données SQLite...")
    create_database(df_cleaned)

    print("Pipeline terminée avec succès.")
