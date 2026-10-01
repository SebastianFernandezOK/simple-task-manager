```text
task-manager/
│
├── .venv/                 # Python virtual environment (ignored by Git)
├── .gitignore             # Files to be ignored by Git (.venv, __pycache__, etc.)
├── pyproject.toml         # Project dependencies and configuration
└── src/                   # Source code root directory
    ├── __init__.py
    ├── main.py            # Entry point (creates the FastAPI instance)
    ├── config.py          # Environment variables and general settings (Pydantic BaseSettings)
    ├── database.py        # Database connection (SQLAlchemy / Motor, etc.)
    │
    ├── models/            # Database models (e.g., SQLAlchemy ORM)
    │   ├── __init__.py
    │   └── task.py
    │
    ├── schemas/           # Pydantic models for Request and Response validation
    │   ├── __init__.py
    │   └── task.py
    │
    ├── routers/           # Endpoints separated by modules/resources
    │   ├── __init__.py
    │   ├── auth.py
    │   └── tasks.py
    │
    └── services/          # Heavy business logic (separated from endpoints)
        ├── __init__.py
        └── task_service.py