# Insertion en base SQLite
import sqlite3

def insert_api_books(df, db_name="books.db"):
    """Insère les données nettoyées issues de l’API dans une table SQLite"""
    print("Insertion des livres API dans la base...")
    conn = sqlite3.connect(db_name)
    df.to_sql("books_api", conn, if_exists="replace", index=False)
    count = conn.execute("SELECT COUNT(*) FROM books_api").fetchone()[0]
    conn.close()
    print(f" {count} livres API insérés dans la table 'books_api'.")
