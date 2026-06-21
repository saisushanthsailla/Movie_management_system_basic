# 🎬 Movie Explorer & Review Management System

## 📌 Project Overview

Movie Explorer & Review Management System is a full-stack web application built using **FastAPI** and **Streamlit**. The application allows users to manage movie records through a simple and interactive interface.

Users can:

* View all movies
* Search and filter movies
* Add new movies
* Update existing movie details
* Delete movies

The project demonstrates CRUD operations, REST API development, and frontend-backend integration using Python.

---

## 🚀 Features

### 🎥 View All Movies

Display the complete list of available movies.

### 🔍 Search / Filter Movies

Filter movies based on:

* Genre
* Language
* Rating

### ➕ Add New Movie

Add a new movie record with details such as:

* Movie ID
* Movie Name
* Genre
* Language
* Rating

### ✏️ Update Movie

Modify existing movie details using the Movie ID.

### 🗑️ Delete Movie

Remove a movie record using the Movie ID.

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### Communication

* Requests Library
* REST API

---

## 📂 Project Structure

```text
Movie_Explorer_python_fastapi/
│
├── app.py               # Streamlit Frontend
├── main.py              # FastAPI Backend
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/saisushanthsailla/Movie_management_system_basic.git
cd Movie_management_system_basic
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Start FastAPI Server

```bash
uvicorn main:app --reload
```

FastAPI will run at:

```text
http://127.0.0.1:8000
```

### Start Streamlit Application

Open a new terminal and run:

```bash
streamlit run app.py
```

---

## 📡 API Endpoints

| Method | Endpoint            | Description              |
| ------ | ------------------- | ------------------------ |
| GET    | `/movies`           | View all movies          |
| GET    | `/filter`           | Search and filter movies |
| POST   | `/addmovie`         | Add a new movie          |
| PUT    | `/updatemovie/{id}` | Update movie details     |
| DELETE | `/deletemovie/{id}` | Delete movie             |

---


## 👨‍💻 Author

**Sai Sushanth Sailla**


GitHub: https://github.com/saisushanthsailla
