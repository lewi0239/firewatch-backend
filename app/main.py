from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import fire_report, my_bag, my_family, item_routes

app = FastAPI(
    title="Firewatch API",
    description="API for fire reports, personal bags, family members, and other items.",
    version="0.1.0",
)

# Add CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the Firewatch API. Use /docs to see the documentation."}

# Include routers for different features
app.include_router(fire_report.router, prefix="/api", tags=["Fire Reports"])
app.include_router(my_bag.router, prefix="/api", tags=["My Bags"])
app.include_router(my_family.router, prefix="/api", tags=["My Family"])
app.include_router(item_routes.router, prefix="/api", tags=["Items"])
