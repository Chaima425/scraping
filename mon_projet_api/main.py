#Mise à jour pour appeler les 2 pipelines
from pipelines.pipeline_scraping import run_scraping_pipeline
from pipelines.pipeline_api import run_api_pipeline

if __name__ == "__main__":
    print("Lancement du projet multi-source...")
    run_scraping_pipeline()
    run_api_pipeline()
    print("Traitement complet terminé.")
