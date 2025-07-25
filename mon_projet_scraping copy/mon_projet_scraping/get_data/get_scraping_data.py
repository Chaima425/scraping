#contient la fonction utile qui va faire le scraping. 
# Les fonctions utiles sont : 
#get_books_html(url):Récupère les blocs HTML des livres
#extract_*: Extrait chaque champ (titre, prix, rating, disponibilité)
#extract_book_info(book): Crée un dictionnaire avec toutes les infos d’un livre
#scrape_books(pages): Récupère les livres de plusieurs pages (liste de dictionnaires)
#scrape_books_df(pages):Transforme tout en un pandas.DataFrame propre et prêt à traiter
#decode('utf-8'): pour regler le problème d'encodage des caractères

import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_books_html(url: str) -> list:
    """Récupère les balises HTML des livres sur une page donnée."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    return soup.find_all('article', class_='product_pod')


def extract_title(book) -> str:
    """Extrait le titre du livre."""
    return book.h3.a['title'] if book.h3 and book.h3.a else 'no title'


def extract_price(book) -> str:
    """Extrait le prix du livre."""
    return book.find('p', class_='price_color').text


def extract_rating(book) -> str:
    """Extrait la note du livre (Exp: 'Three', 'Five')."""
    return book.find('p', class_='star-rating')['class'][1]


def extract_availability(book) -> str:
    """Extrait la disponibilité du livre."""
    return book.find('p', class_='instock availability').text.strip()


def extract_book_info(book) -> dict:
    """Extrait toutes les informations d'un livre sous forme de dictionnaire."""
    return {
        'title': extract_title(book),
        'price': extract_price(book),
        'rating': extract_rating(book),
        'availability': extract_availability(book),
    }


def scrape_books(pages: int) -> list:
    """Scrape les livres sur plusieurs pages du site."""
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    all_books = []

    for page_num in range(1, pages + 1):
        url = base_url.format(page_num)
        books_html = get_books_html(url)
        page_books = [extract_book_info(book) for book in books_html]
        all_books.extend(page_books)

    return all_books


def scrape_books_df(pages: int) -> pd.DataFrame:
    """Scrape les livres et retourne un DataFrame pandas."""
    books_data = scrape_books(pages)
    return pd.DataFrame(books_data)


if __name__ == "__main__":
    df = scrape_books_df(2)
    print(df.head())
