# fichier  lance le pipeline
from pipelines.pipeline_scraping import run_scraping_pipeline

if __name__ == "__main__":
    print("Début du script main.py")
    run_scraping_pipeline()
    print("Fin du script main.py")
