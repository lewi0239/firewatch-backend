from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import item_routes

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include the API router
app.include_router(item_routes.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Firewatch API. Use the /api/fires endpoint to fetch data."}
