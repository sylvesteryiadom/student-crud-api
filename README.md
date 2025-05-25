# Student CRUD REST API

A simple, production-ready REST API for managing students, built with Python and Flask.  
This project demonstrates best practices for API design, configuration management, database migrations, and SRE-friendly architecture.

---

## Features

- **CRUD operations** for student records
- **RESTful API** with proper HTTP verbs and status codes
- **API versioning** (e.g., `/api/v1/students`)
- **Database migrations** using Flask-Migrate
- **Configuration via environment variables** (Twelve-Factor App principle)
- **Structured logging** for observability
- **/healthcheck** endpoint for readiness/liveness checks
- **Unit tests** for endpoints
- **Postman collection** for easy API testing

---

## Tech Stack

- **Python 3.x**
- **Flask**
- **Flask-SQLAlchemy**
- **PostgreSQL**
- **Flask-Migrate**
- **pytest**

---

## Getting Started

### Prerequisites

- Python 3.x installed
- PostgreSQL installed and running
- [pip](https://pip.pypa.io/en/stable/) installed

### Clone the repository

```bash
git clone https://github.com/<your-username>/student-crud-api.git
cd student-crud-api


### Set up environment variables

Create a `.env` file in the project root:

```env
FLASK_APP=app
FLASK_ENV=development
DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<database>
```

### Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run database migrations

```bash
flask db upgrade
```

### Run the API server

```bash
flask run
```

Or use the Makefile:

```bash
make run
```

---

## API Endpoints

| Method | Endpoint                   | Description                  |
|--------|----------------------------|------------------------------|
| GET    | /api/v1/students           | Get all students             |
| GET    | /api/v1/students/<id>      | Get student by ID            |
| POST   | /api/v1/students           | Add a new student            |
| PUT    | /api/v1/students/<id>      | Update student information   |
| DELETE | /api/v1/students/<id>      | Delete a student             |
| GET    | /healthcheck               | Health check endpoint        |

---

## Testing

To run unit tests:

```bash
make test
```

---

## Postman Collection

A Postman collection is provided in the `postman/` directory for easy API testing.

---

## License

MIT

---

## Author

- [Sylvester Yiadom](https://github.com/sylvesteryiadom)
```