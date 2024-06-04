# FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# psycopg3 Reaper
import asyncio
from contextlib import asynccontextmanager
from .database import get_pool

# Routers
from .routers import register_routers

# Check Connections (Psycopg3)
async def check_connections():
    while True:
        await asyncio.sleep(300)
        print("check connections")
        pool.check()

# Application lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(check_connections())
    yield

# Initialize database pool
pool = get_pool()

# Initialize FastAPI app with lifespan context manager
app = FastAPI(lifespan=lifespan)

# Configure CORS
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
register_routers(app)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Hellow World"}




