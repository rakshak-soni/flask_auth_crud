# FLASK_AUTH_CRUD – Full Project Documentation

## Overview
This project is a complete **Flask-based REST API** with:
- User Authentication (JWT)
- Role-Based Authorization
- Category, Subcategory, and Product CRUD
- Fully separated **Frontend (HTML/CSS/JS)** and **Backend (Flask REST API)**
- Dockerized using:
  - Flask backend container
  - NGINX frontend container
  - MySQL database container

All services run together using **docker-compose**.

## Project Structure
```
FLASK_AUTH_CRUD/
│
├── backend_flask/
│   ├── base/
│   │   ├── com/
│   │   │   ├── controller
│   │   │   ├── dao
│   │   │   ├── middleware
│   │   │   ├── service
│   │   │   └── vo
│   │   └── utils
│   ├── static/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── frontend_flask/
│   ├── css/
│   ├── html/
│   ├── js/
│   ├── index.html
│   ├── nginx.conf
│   └── Dockerfile
│
└── docker-compose.yaml
```

## Technologies Used
### Backend
- Python 3.x  
- Flask  
- SQLAlchemy  
- MySQL  
- JWT Token Authentication  
- Role-Based Access Control  
- Exception handling

### Frontend
- HTML  
- CSS  
- JavaScript  
- Fetch API (REST API calls)

### Deployment
- Docker  
- Docker Compose  
- NGINX  

## Installation & Setup

### 1. Clone the Repository
```
git clone <repo-url>
cd FLASK_AUTH_CRUD
```

## 2. Create Environment Files

### Backend `.env`
```
DB_HOST=mysql_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=yourdb
JWT_SECRET=your_secret_key
```

## 3. Build & Run Using Docker Compose
```
docker-compose build
docker-compose up -d
```

### Docker Services Started
| Service | Description | URL |
|--------|-------------|-----|
| mysql_db | MySQL 8 Database | Internal only |
| backend | Flask REST API | http://localhost:5000 |
| frontend | NGINX + HTML/JS UI | http://localhost:3000 |

## Backend API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /register | Register new user |
| POST | /login | Login & get JWT |

### Category CRUD
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /insert_category | Add category (admin only) |
| GET | /view_category | View categories |
| PUT | /update_category/<id> | Update category |
| DELETE | /delete_category/<id> | Delete category |

### Subcategory CRUD
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /subcategories |
| GET | /subcategories |
| PUT | /subcategories/<id> |
| DELETE | /subcategories/<id> |

### Product CRUD
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /product |
| GET | /product |
| PUT | /product/<id> |
| DELETE | /product/<id> |

## Frontend
Built using:
- Plain HTML
- CSS
- JavaScript
- Fetch API for calling backend
- Protected routes using JWT stored in localStorage

### Example Fetch Call
```javascript
fetch("/view_category", {
    headers: { "Authorization": "Bearer " + localStorage.getItem("token") }
})
```

## Docker Compose Summary
Services included:
- backend_flask
- frontend_flask
- mysql_db
- All services run under same Docker network

## How to Stop Services
```
docker-compose down
```

## Future Improvements
- Pagination
- Search + filters
- User, Admin panel UI
