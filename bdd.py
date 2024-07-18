import requests

url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"

response = requests.get(url)
books = response.json()

print(f"Cantidad total de objetos: {len(books)}")

for book in books:
    if book["title"] == "The Divine Comedy":
        print(f"\n{book['title']} fue escrito en el año {book['year']} por {book['author']}, nacido en {book['country']}.")
        print(f"Cuenta con un total de {book['pages']} páginas y este es su link a wikipedia {book['link']}")
