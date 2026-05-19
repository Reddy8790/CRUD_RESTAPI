# 🚀 CRUD REST API – Django Project (Books Management)

##📌 Project Description

CRUD_RESTAPI is a backend web application built using Django and Django REST Framework. It is designed to manage book records through REST APIs and demonstrates how CRUD (Create, Read, Update, Delete) operations work in real-world backend systems.
The project uses Django models to store data in the database and serializers to convert data into JSON format. API views handle HTTP requests and return structured responses to the client.
This project helps in understanding backend development concepts such as API creation, database interaction, request handling, and response formatting using Django REST Framework.


## 🎯 What This Project Does
This API allows users to:

- ➕ Add new books to the database  
- 📄 View all books  
- 🔍 View a single book by ID  
- ✏️ Update existing book details  
- ❌ Delete books from database  

---

## 🛠️ Technologies Used
- Python 🐍  
- Django 🟢  
- Django REST Framework ⚡  
- SQLite Database 🗄️  

---

## ⚙️ How It Works
This project follows a simple backend flow:

1. **Model (Database Layer)**  
   Stores book information like name, author, and reader.

2. **Serializer (Data Conversion Layer)**  
   Converts Django models into JSON format and validates input data.

3. **Views (Logic Layer)**  
   Handles API requests like GET, POST, PUT, DELETE.

4. **URLs (Routing Layer)**  
   Maps API endpoints to specific functions.

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | /api/books/ | Get all books |
| POST   | /api/books/create/ | Create new book |
| GET    | /api/books/{id}/ | Get book by ID |
| PUT    | /api/books/update/{id}/ | Update book |
| DELETE | /api/books/delete/{id}/ | Delete book |

---

## 🧪 Example Request (POST)
```json
{
  "name": "Clean Code",
  "author": "Robert C. Martin",
  "read_by": "Shashikala"
}
