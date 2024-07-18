import requests

SERVER_IP = '192.168.0.44'  # Reemplaza con la IP del servidor

# Obtener todos los libros
response = requests.get(f"http://{SERVER_IP}:8000/books")
print("Todos los libros:", response.json())

# Agregar un nuevo libro
new_book = {
    "title": "Dune",
    "author": "Frank Herbert",
    "country": "USA",
    "imageLink": "link_to_image",
    "language": "English",
    "link": "link_to_wikipedia",
    "pages": 100,
    "year": 2024
}
response = requests.post(f"http://{SERVER_IP}:8000/books", json=new_book)
print("Libro agregado:", response.json())

# Eliminar un libro
book_title = "Dune"
response = requests.delete(f"http://{SERVER_IP}:8000/books/{book_title}")
print("Libro eliminado:", response.json())
