#contient les fonctions pour nettoyer et préparer les données.
########
# les fonction utile : 
#convert_availability(value): Convertit la disponibilité en booléen (True si 'In stock').
#convert_rating(value): Convertit le rating textuel en note numérique.
#convert_types(df: pd.DataFrame) -> pd.DataFrame): Convertit les types de colonnes du DataFrame de livres.
#-> Fonction principale de traitement : applique les 3 fonctions ci-dessus sur le DataFrame
#clean_price(value: str) -> float: Nettoie le prix en retirant le symbole £ et en convertissant en float.

import pandas as pd

def convert_availability(value: str) -> bool:
    """Convertit la disponibilité en booléen (True si 'In stock')."""
    return 'In stock' in value

def convert_rating(value: str) -> int:
    """Convertit le rating textuel en note numérique."""
    ratings_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    
    return ratings_map.get(value, None)

def convert_types(df_books: pd.DataFrame) -> pd.DataFrame:
    """Convertit les types de colonnes du DataFrame de livres."""
    
    # Nettoyer le prix : retirer le symbole £ et convertir en float
    df_books["price"].dtype ==df_books["price"].astype(str).str.replace("£", "").astype(float)


    # Convertir la colonne 'availability' en booléen
    df_books["availability"] = df_books["availability"].apply(convert_availability)

    # Convertir la colonne 'rating' en entier
    df_books["rating"] = df_books["rating"].apply(convert_rating)

    # Convertir le titre en str (par sécurité)
    df_books["title"] = df_books["title"].astype(str)


    return df_books
