# FastAPI Boilerplate
This repository provides a comprehensive boilerplate for building web applications using FastAPI. It references the educational content provided by Sanjeev Thiyagarajan's FastAPI course on YouTube and GitHub, offering a structured starting point for developers to quickly set up and deploy FastAPI projects.

## Project Structure
```
/FastAPI_Project
├── /alembic
│   ├── /versions
│   └── env.py
├── /app
│   ├── /routers
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── sample.py
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── oauth2.py
│   ├── schemas.py
│   └── utils.py
├── .env
├── .gitignore
└── alembic.ini
```

## Getting Started
### Installation
1. **Clone this repository to your local machine using:**
    ```bash
    git clone https://github.com/kcrmin/FastAPI_Boilerplate.git
    ```
2. **Open directory:**
    ```bash
    cd FastAPI_Boilerplate
    ```
## Set up a virtual environment
### Setup Venv
1. **Create venv**
    ``` bash
    python3 -m venv venv
    ```
2. **Activate venv**
    ``` bash
    source venv/bin/activate  # On macOS
    myenv\Scripts\activate  # On Windows
    ```
3. **Deactivate venv**
    ``` bash
    deactivate
    ```
### Configure VSCode Interpreter
1. Open Command Palette:
  - Option 1:
    - ```Click:``` [Settings] View
    - ```Click:``` [Settings] Command Palette
  - Option 2:
    - ```Enter:``` [Shift + Command + P]
2. ```Click:``` Python: Select Interpreter
3. ```Click:``` Enter interpreter path…
4. ```Enter:``` [./FastAPI_Boilerplate/venv/bin/python]
### Install the required Python packages
```bash
pip install 'fastapi[all]'
pip install 'psycopg[binary, pool]'
pip install sqlalchemy
pip install 'passlib[bcrypt]'
pip install 'python-jose[cryptography]'
pip install alembic
```

## Configuration
1. **Edit `.env` file:** Store your environment variables in this file.
    ```
    DATABASE_HOSTNAME=localhost
    DATABASE_PORT=5432
    DATABASE_PASSWORD=password1234
    DATABASE_NAME=postgres
    DATABASE_USERNAME=postgres
    SECRET_KEY="Random_Secret_Key"
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```
2. **Edit `app/routers/__init__.py`:** Register routers to the application.
3. **Edit `app/schemas.py`:** Define Pydantic models.
4. **Edit `app/models.py`:** Define SQLAlchemy models.
5. **Add new router files:** Create new router files under `app/routers`.

## Running the Application
1. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload
   ```
2. **Access the API documentation:** Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

## Database Migrations
1. **Initialize Alembic migrations:**
   ```bash
   alembic revision --autogenerate -m "message"
   ```
2. **Check the current migration:**
   ```bash
   alembic current
   ```
3. **Apply the latest migration:**
   ```bash
   alembic upgrade head
   ```
4. **Revert the last migration:**
   ```bash
   alembic downgrade -1
   ```

## Resources

- **YouTube Course:** [FastAPI Course](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- **GitHub Source:** [FastAPI Course GitHub Repository](https://github.com/Sanjeev-Thiyagarajan/fastapi-course)
