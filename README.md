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
git clone https://github.com/sylvesteryiadom/student-crud-api.git
cd student-crud-api
