# Scraping API Google Books
import requests
import pandas as pd

def get_books_from_api(query="data science", max_results=40):
    """Récupère les livres depuis l'API Google Books selon une requête"""
    print("🔍 Récupération des données depuis l'API Google Books...")

    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    response = requests.get(url)
    data = response.json()

    books = []
    for item in data.get("items", []):
        info = item.get("volumeInfo", {})
        books.append({
            "title": info.get("title", ""),
            "authors": ", ".join(info.get("authors", [])) if "authors" in info else "",
            "published_date": info.get("publishedDate", ""),
            "categories": ", ".join(info.get("categories", [])) if "categories" in info else "",
            "rating": info.get("averageRating", 0)
        })

    return pd.DataFrame(books)
