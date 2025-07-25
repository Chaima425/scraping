# Traitement des données API
def clean_api_data(df):
    """Nettoie le DataFrame issu de l'API Google Books"""
    print("🧹 Nettoyage des données API...")
    df = df.dropna(subset=["title"])  # on enlève les lignes sans titre
    df["rating"] = df["rating"].fillna(0).astype(float)
    return df
