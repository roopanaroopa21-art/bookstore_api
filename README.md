📚 Bookstore API

Project Description

The Bookstore API is a simple REST API built using Python and FastAPI.
It allows users to perform CRUD operations (Create, Read, Update, Delete) on books.

This project demonstrates how to build and test APIs using FastAPI and the Swagger UI documentation.

---

🚀 Technologies Used

- Python
- FastAPI
- Uvicorn
- VS Code

---

📂 Project Structure

bookstore_api/
│
├── main.py        # Main FastAPI application
└── README.md      # Project documentation

---

⚙️ Installation

1. Clone the repository

git clone https://github.com/your-username/bookstore-api.git

2. Navigate to the project folder

cd bookstore-api

3. Install required packages

pip install fastapi uvicorn

---

▶️ Run the Application

Start the server using Uvicorn:

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

---

📖 API Documentation

FastAPI provides automatic API documentation.

Open in browser:

http://127.0.0.1:8000/docs

Here you can test all API endpoints.

---

🔧 API Endpoints

Method| Endpoint| Description
GET| /books| Get all books
GET| /books/{book_id}| Get a book by ID
POST| /books| Add a new book
PUT| /books/{book_id}| Update a book
DELETE| /books/{book_id}| Delete a book

---

📌 Example Book Data

{
 "id": 1,
 "title": "Harry Potter",
 "author": "JK Rowling",
 "price": 500
}

---

🎯 Features

- Add new books
- View all books
- Search book by ID
- Update book information
- Delete books

---

👨‍💻 Author

Roopa N A
