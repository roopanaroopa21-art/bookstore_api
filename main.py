from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float

books = []

@app.get("/")
def home():
    return {"message": "Welcome to Bookstore API"}

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully"}

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}



def update_book(book_id: int, updated_book: dict):
    for book in books:
        if book["id"] == book_id:
            book.update(updated_book)
            return {"message": "Book updated"}
    return {"message": "Book not found"}


def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}


    

