#uvicorn app.main:app --reload
#Uvicorn is a lightweight, high-performance web server for Python, designed to run ASGI applications.
from fastapi import FastAPI
from app.outlook_api import get_calendar_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Adds Permissions for Vite Server to work
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/calendar")
def read_calendar():
    return get_calendar_data()

@app.get("/")
def read_root():
    return {"message": "Hello from backend"}
