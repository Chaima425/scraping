#contient les fonctions pour créer la base SQLite, insérer les données et vérifier l’insertion. 
import sqlite3
import pandas as pd

def create_database(df_books: pd.DataFrame, db_name: str = "books.db") -> None:
    """
    Crée une base de données SQLite et insère les données du DataFrame dans une table "books".

    Args:
        df_books (pd.DataFrame): Le DataFrame contenant les informations sur les livres.
        db_name (str): Le nom du fichier de base de données. Par défaut : 'books.db'.
    """

    # Connexion à la base de données (création si elle n'existe pas)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Création de la table "books" si elle n'existe pas déjà
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            price REAL,
            availability BOOLEAN,
            rating INTEGER
        );
    """)

    # Insertion des données (remplacement de la table si elle existe déjà)
    df_books.to_sql('books', conn, if_exists='replace', index=False)

    # Enregistrement et fermeture de la connexion
    conn.commit()
    conn.close()
 



