# Student API (FastAPI + SQLite)

Quick demo backend to store student data and expose CRUD REST endpoints for integration with a Flutter app.

Setup

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn main:app --reload
```

API Endpoints

- `POST /students` : create student
- `GET /students` : list students
- `GET /students/{id}` : get student
- `PUT /students/{id}` : update student
- `DELETE /students/{id}` : delete student

Open interactive docs at `http://127.0.0.1:8000/docs` after starting the server.
