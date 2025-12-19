🛒 E-commerce Product API (Capstone Project)
📌 Project Overview

This project is a backend E-commerce Product Management API built using Django and Django REST Framework (DRF).
It provides secure and scalable RESTful APIs for managing users, product categories, and products, designed to be easily integrated with any frontend or mobile application.

The system focuses on authentication, authorization, CRUD operations, search, filtering, pagination, and API documentation.

🎯 Features
🔐 Authentication

JWT-based authentication using SimpleJWT

Secure login endpoint

Protected routes for admin operations

👤 User Management (Admin Only)

Create users

View all users

Update users

Deactivate users

🗂️ Category Management

Create, read, update, and delete categories

Unique category names and slugs

📦 Product Management

Full CRUD operations

Products linked to categories and sellers

Fields include name, description, price, stock, and status

Automatic timestamps (created / updated)

🔍 Search & Filtering

Search products by:

Name

Category

Partial text matching supported

Pagination enabled for large datasets

📘 API Documentation

Swagger UI for interactive API documentation

Postman collection for API testing

🛠️ Technologies Used

Python

Django

Django REST Framework

PostgreSQL / SQLite

JWT (SimpleJWT)

Postman

Swagger (drf-yasg)

🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/Tsegaw-tech/Ecommerce.git
cd ecommerce-api

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create .env file:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/ecommerce

5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create Superuser
python manage.py createsuperuser

7️⃣ Run Server
python manage.py runserver

📘 API Documentation

Swagger UI:

http://localhost:8000/swagger/


Postman Collection:
Included in the repository as:

ecommerce-api.postman_collection.json

🧪 Testing

All endpoints tested using Postman

JWT token required for protected routes

Admin-only access enforced for user and product management

🌍 Deployment

The project can be deployed on:

Heroku

PythonAnywhere

Railway

🔮 Future Enhancements

Product reviews & ratings

Wishlist functionality

Multiple product images

Discount & promotion system

Stock auto-reduction on purchase

👨‍💻 Author

Tsegaw Wayessa
Backend Developer
Capstone Project – E-commerce Product API

📜 License

This project is for educational purposes only.