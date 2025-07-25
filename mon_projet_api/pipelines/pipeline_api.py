#Exécution de la pipeline API
from get_data.get_api_data import get_books_from_api
from process_data.process_api_data import clean_api_data
from database.insert_api_data import insert_api_books

def run_api_pipeline():
    print("Démarrage de la pipeline API Google Books...")
    df_api = get_books_from_api()
    df_api_clean = clean_api_data(df_api)
    insert_api_books(df_api_clean)
    print(" Pipeline API terminée avec succès.")
