task-manager/
│
├── .venv/                 # Entorno virtual de Python (ignorado por Git)
├── .gitignore             # Archivos que Git debe ignorar (.venv, __pycache__, etc.)
├── pyproject.toml         # Dependencias y configuración del proyecto
└── src/                   # Carpeta raíz del código fuente
    ├── __init__.py
    ├── main.py            # Punto de entrada (crea la instancia de FastAPI)
    ├── config.py          # Variables de entorno y configuración general (Pydantic BaseSettings)
    ├── database.py        # Conexión a la base de datos (SQLAlchemy / Motor, etc.)
    │
    ├── models/            # Modelos de base de datos (ej. SQLAlchemy ORM)
    │   ├── __init__.py
    │   └── task.py
    │
    ├── schemas/           # Modelos de Pydantic para validar Request y Response
    │   ├── __init__.py
    │   └── task.py
    │
    ├── routers/           # Los endpoints separados por módulos/recursos
    │   ├── __init__.py
    │   ├── auth.py
    │   └── tasks.py
    │
    └── services/          # Lógica de negocio pesada (separada de los endpoints)
        ├── __init__.py
        └── task_service.py