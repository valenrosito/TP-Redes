from fastapi import FastAPI, HTTPException, Body
import json
import os

app = FastAPI()

# Leer el archivo JSON al inicio
if os.path.exists('books.json'):
    with open('books.json', 'r') as file:
        books = json.load(file)
else:
    books = []

# Función para obtener todos los libros
@app.get("/books")
def get_all_books():
    return books

# Función para buscar libros por país
@app.get("/books/country/{country}")
def get_books_by_country(country: str):
    result = [book for book in books if book['country'].lower() == country.lower()]
    if not result:
        raise HTTPException(status_code=404, detail="Libros no encontrado")
    return result

# Función para buscar libros por autor
@app.get("/books/author/{author}")
def get_books_by_author(author: str):
    result = [book for book in books if book['author'].lower() == author.lower()]
    if not result:
        raise HTTPException(status_code=404, detail="Libros no encontrado")
    return result


# Función para obtener información de un libro por título
@app.get("/books/info/{title}")
def get_book_info(title: str):
    for book in books:
        if book["title"].lower() == title.lower():
            return {
                "Informacion": f"{book['title']} fue escrito en el año {book['year']} por {book['author']}, nacido en {book['country']}. Cuenta con un total de {book['pages']} páginas y este es su link a Wikipedia {book['link']}"
            }
    raise HTTPException(status_code=404, detail="Book not found")

# Función para obtener un libro por año
@app.get("/books/year/{year}")
def get_book_by_year(year: int):
    for book in books:
        if book['year'] == year:
            return {"Titulo": book['title']}
    raise HTTPException(status_code=404, detail="Book not found")

# Función para obtener la cantidad de páginas de un libro por título
@app.get("/books/pages/{title}")
def get_book_pages(title: str):
    for book in books:
        if book['title'].lower() == title.lower():
            return {"pages": book['pages']}
    raise HTTPException(status_code=404, detail="Book not found")

# Función para agregar un libro (POST request)
@app.post("/books")
async def add_book(title: str = Body(...), author: str = Body(...), country: str = Body(...),
                   imageLink: str = Body(...), language: str = Body(...), link: str = Body(...),
                   pages: int = Body(...), year: int = Body(...)):
    new_book = {
        "Titulo": title,
        "Autor": author,
        "Pais": country,
        "Link de imagen": imageLink,
        "Lenguaje": language,
        "Link": link,
        "Paginas": pages,
        "Año": year
    }
    books.append(new_book)
    with open('books.json', 'w') as file:
        json.dump(books, file)
    return new_book

# Función para eliminar un libro (DELETE request)
@app.delete("/books/{book_title}")
def delete_book(book_title: str):
    global books
    books = [book for book in books if book['title'] != book_title]
    with open('books.json', 'w') as file:
        json.dump(books, file)
    return {"Libro eliminado"}

# Ejecutar la aplicación con Uvicorn en el puerto 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
