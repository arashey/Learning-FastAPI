# FastAPI Learning Project

This repository contains multiple mini-projects built with **FastAPI** to practice different features, starting from basic endpoints to a full CRUD application with a database.

## Features

- Basic FastAPI setup with `GET` endpoints.
- Handling **path parameters** and **query parameters**.
- Creating resources using **POST** requests with Pydantic models.
- Full CRUD operations (Create, Read, Update, Delete) with an in-memory list.
- Database integration using **Peewee ORM** and SQLite.
- Automatic docs available at:
  - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd fastapi-learning
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

---

## Project Structure

The repository contains **5 different stages** of FastAPI learning:

1. **Basic GET routes** – Returning a simple message and using path/query parameters.
2. **POST request with Pydantic model** – Creating items with validation.
3. **Optional query parameters** – Adding conditions to responses.
4. **CRUD with in-memory DB** – Full Create, Read, Update, Delete without persistence.
5. **CRUD with SQLite + Peewee ORM** – Persistent database integration with models.

---

## API Endpoints

### Stage 1 – Basic

- `GET /` → Returns a welcome message.
- `GET /items/{item_id}` → Returns item details with optional query string.

### Stage 2 – POST

- `POST /items/` → Create an item with `name`, `description`, and `price`.

### Stage 3 – Query Parameters

- `GET /items/{item_id}?q=something&short=true` → Returns item with filters.

### Stage 4 – CRUD (in-memory)

- `POST /items/` → Create an item.
- `GET /items/` → List all items.
- `GET /items/{id}` → Retrieve a single item.
- `PUT /items/{id}` → Update item.
- `DELETE /items/{id}` → Delete item.

### Stage 5 – CRUD (SQLite + Peewee ORM)

- `POST /items/` → Create and store item in database.
- `GET /items/` → Retrieve all items from database.
- `GET /items/{id}` → Retrieve single item from database.
- `DELETE /items/{id}` → Delete item by id.

---

## API Testing

You can test the API using **curl** or **HTTPie**.

### Example Requests

#### Create Item (POST)
```bash
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{
  "name": "Book",
  "price": 12.99,
  "description": "A nice book"
}'
```

#### Get All Items (GET)
```bash
curl http://127.0.0.1:8000/items/
```

#### Get Single Item (GET)
```bash
curl http://127.0.0.1:8000/items/1
```

#### Update Item (PUT)
```bash
curl -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{
  "name": "Updated Book",
  "price": 14.99,
  "description": "Updated description"
}'
```

#### Delete Item (DELETE)
```bash
curl -X DELETE http://127.0.0.1:8000/items/1
```

---

## Requirements

See `requirements.txt` for dependencies.

- fastapi
- uvicorn
- pydantic
- peewee

---

## License

This project is for **educational purposes** and demonstrates step-by-step learning of FastAPI.