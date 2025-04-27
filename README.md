# URL Shortener API

This is a simple URL Shortener API built using **FastAPI** and **PostgreSQL**.

## Features
- Shorten a long URL into a short code
- Redirect from the short URL to the original long URL
- Simple and fast API built with FastAPI

## Technologies Used
- Python 3.10
- FastAPI
- PostgreSQL
- SQLAlchemy
- Uvicorn

## Setup Instructions

1. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. Install dependencies:
    ```bash
    pip install fastapi uvicorn psycopg2-binary sqlalchemy
    ```

3. Start PostgreSQL and set up the database:
    ```sql
    CREATE DATABASE url_db;
    \c url_db
    CREATE TABLE urls (
        id SERIAL PRIMARY KEY,
        long_url TEXT NOT NULL,
        short_code VARCHAR(10) UNIQUE NOT NULL
    );
    ```

4. Run the server:
    ```bash
    uvicorn main:app --reload
    ```

The API will be available at `http://127.0.0.1:8000`.

Swagger UI (API Docs) will be available at `http://127.0.0.1:8000/docs`.

## API Endpoints

### POST `/shorten`
- Accepts a long URL and returns a short URL.

### GET `/{short_code}`
- Redirects to the original URL.

---

