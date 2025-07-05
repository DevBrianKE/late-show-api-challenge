# 🎤 Late Show API — Flask Code Challenge

Welcome to the **Late Show API**, a RESTful backend application for managing a late-night TV show system. Built with Flask and PostgreSQL, it uses JWT authentication and follows the MVC architecture pattern.

---

## 📌 Overview

This API allows clients to manage:
- Guests
- Episodes
- Appearances (guests on episodes)
- User registration & login with JWT protection

---

## 🧠 Tech Stack

✅ Python + Flask  
✅ PostgreSQL (mandatory)  
✅ SQLAlchemy + Flask-Migrate  
✅ Flask-JWT-Extended (token-based auth)  
✅ Postman (API testing)  
✅ Git + GitHub for version control  
✅ Full documentation below ✅

---

## 🗂 Folder Structure

.
├── server/
│ ├── app.py # Entry point
│ ├── config.py # App configurations
│ ├── seed.py # Seed file for test data
│ ├── models/
│ │ ├── init.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ ├── appearance.py
│ │ └── user.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── guest_controller.py
│ │ ├── episode_controller.py
│ │ ├── appearance_controller.py
│ │ └── auth_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
└── README.md

### 🚀 Setup Instructions
## ✅ Install Dependencies
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
### ✅ PostgreSQL Setup
## In your PostgreSQL CLI or GUI:
CREATE DATABASE late_show_db;
## ✅ Configure Database URI
In server/config.py:
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
## ✅ Migrate & Seed the DB
export FLASK_APP=server/app.py

flask db init
flask db migrate -m "initial migration"
flask db upgrade

python server/seed.py
