# Project Management API

A **production-style REST API** built with **Django REST Framework** for managing projects and tasks.
This API includes **JWT authentication, filtering, pagination, permissions, and rate limiting**, ensuring secure and scalable backend functionality.

Users can register, authenticate using JWT tokens, create projects, manage tasks, and filter tasks by status or project.

---

## 🚀 Live Demo

Live API Base URL
[https://project-management-api-bzlb.onrender.com](https://project-management-api-bzlb.onrender.com)

Swagger Documentation
[https://project-management-api-bzlb.onrender.com/swagger/](https://project-management-api-bzlb.onrender.com/swagger/)

GitHub Repository
[https://github.com/selvakalusu003/project-management-api](https://github.com/selvakalusu003/project-management-api)

---

## ✨ Features

* User registration API
* JWT authentication (Login with access token)
* Refresh token support
* Create, update, delete projects
* Create, update, delete tasks
* User-specific data access (users manage only their own data)
* Task filtering by status
* Task filtering by project
* Pagination for API responses
* Secure API permissions
* Rate limiting to prevent abuse
* Interactive API documentation using Swagger
* Clean Django REST Framework architecture

---

## 🔑 Authentication

This API uses **JWT (JSON Web Token)** authentication.

### Obtain Token

POST

```
/api/token/
```

Example request

```json
{
  "username": "username",
  "password": "password"
}
```

Response

```json
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

---

### Refresh Token

POST

```
/api/token/refresh/
```

Example request

```json
{
  "refresh": "refresh_token"
}
```

---

# 📡 API Endpoints

## User Registration

POST

```
/register/
```

Create a new user account.

---

## Projects API

### Get all projects

GET

```
/api/projects/
```

### Create project

POST

```
/api/projects/
```

Example request

```json
{
  "name": "First Project",
  "description": "My project description"
}
```

### Get single project

GET

```
/api/projects/{id}/
```

### Update project

PUT / PATCH

```
/api/projects/{id}/
```

### Delete project

DELETE

```
/api/projects/{id}/
```

---

## 📋 Tasks API

### Get all tasks

GET

```
/api/tasks/
```

---

### Create task

POST

```
/api/tasks/
```

Example request

```json
{
  "title": "Build Backend",
  "description": "Create backend API using Django REST Framework",
  "project": 1,
  "status": "pending"
}
```

---

### Get single task

GET

```
/api/tasks/{id}/
```

---

### Update task

PUT / PATCH

```
/api/tasks/{id}/
```

---

### Delete task

DELETE

```
/api/tasks/{id}/
```

---

## 🔎 Filtering

Tasks can be filtered using query parameters.

Filter by status

```
/api/tasks/?status=pending
```

```
/api/tasks/?status=completed
```

Filter by project

```
/api/tasks/?project=1
```

---

## 📄 Pagination

All list endpoints support pagination.

Example response

```json
{
  "count": 10,
  "next": "next_page_url",
  "previous": "previous_page_url",
  "results": []
}
```

---

## 🔐 Permissions

* All project and task APIs require authentication.
* Users can only access **their own projects and tasks**.
* Unauthorized requests return **401 Unauthorized**.

---

## ⚡ Rate Limiting

Rate limiting is implemented to prevent excessive API requests.

Example configuration:

* Anonymous users → limited requests
* Authenticated users → higher request limit

This helps protect the API from abuse.

---

## 📑 Swagger API Documentation

Interactive API documentation is available at:

```
/swagger/
```

Swagger allows you to:

* Test APIs directly
* Authenticate with JWT
* Send requests and view responses
* Explore all endpoints easily

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* SimpleJWT
* Django Filter
* Swagger (drf-yasg)
* SQLite
* Git & GitHub
* Render (Deployment)

---

## 📂 Project Structure

```
project-management-api
│
├── project_management_api
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── projects
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
│
├── requirements.txt
├── build.sh
└── Procfile
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/selvakalusu003/project-management-api.git
```

Navigate into project

```
cd project-management-api
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run migrations

```
python manage.py migrate
```

Create superuser

```
python manage.py createsuperuser
```

Run server

```
python manage.py runserver
```

Open browser

```
http://127.0.0.1:8000/swagger/
```

---

## ☁️ Deployment

This API is deployed on **Render**.

### Build Command

```
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

### Start Command

```
gunicorn project_management_api.wsgi:application
```

---

## 🧠 Challenges Faced

* Implementing JWT authentication
* Handling token authorization in Swagger
* Implementing filtering using Django Filter
* Managing user-specific data permissions
* Configuring deployment on Render
* Setting up environment variables for production

---

## 📚 What I Learned

* Django REST Framework architecture
* JWT authentication with SimpleJWT
* Building secure REST APIs
* Filtering and pagination in DRF
* API documentation with Swagger
* Rate limiting in APIs
* Deploying production-ready APIs

---

## 🔮 Future Improvements

* Task priority levels
* Task deadlines
* Email notifications
* Role-based permissions
* PostgreSQL for production database
* Docker containerization

---

## 👨‍💻 Author

Selva Kalusalingam R

GitHub
[https://github.com/selvakalusu003](https://github.com/selvakalusu003)
