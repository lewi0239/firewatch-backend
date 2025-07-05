import io
import pandas as pd
import requests
from decouple import config
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

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

# Load credentials from .env file
MAP_KEY = config("MAP_KEY", default=None)

# FIRMS API URL for VIIRS S-NPP NRT data for the last 24 hours in the USA
FIRMS_API_URL_TEMPLATE = (
    "https://firms.modaps.eosdis.nasa.gov/api/country/csv/"
    "{map_key}/VIIRS_SNPP_NRT/USA/1"
)

# Pydantic model for the fire data points
# Based on the expected CSV/JSON output from FIRMS
class FireData(BaseModel):
    latitude: float
    longitude: float
    bright_ti4: float
    scan: float
    track: float
    acq_date: str
    acq_time: str
    satellite: str
    confidence: str
    version: str
    bright_ti5: float
    frp: float
    daynight: str

@app.get("/api/fires", response_model=List[FireData])
def get_fires():
    """
    Fetches fire data from the NASA FIRMS API.
    Requires MAP_KEY to be set in a .env file.
    The data is returned as JSON.
    """
    if not MAP_KEY:
        raise HTTPException(
            status_code=500,
            detail="NASA FIRMS MAP_KEY is not configured. Please update the .env file.",
        )

    map_key = MAP_KEY.strip('"')
    
    # Format the URL with the actual map key
    api_url = FIRMS_API_URL_TEMPLATE.format(map_key=map_key)

    try:
        # The API for CSV data does not require the Bearer token, only the MAP_KEY in the URL.
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        # The response is CSV, so we need to parse it.
        csv_data = response.text
        
        # Check if the response is actually CSV data and not an error message
        if not csv_data or not 'latitude' in csv_data.splitlines()[0]:
             raise HTTPException(
                status_code=500,
                detail=f"FIRMS API did not return valid CSV data. Response text: {csv_data}",
            )

        # Use an in-memory text buffer (StringIO) to read the CSV data with pandas
        csv_file = io.StringIO(csv_data)
        df = pd.read_csv(csv_file, dtype={'acq_time': str})
        
        # Convert the DataFrame to a JSON format (list of records)
        data = df.to_dict(orient="records")
        return data

    except requests.exceptions.HTTPError as http_err:
        # Provide more specific error details from FIRMS if possible
        detail = f"HTTP error occurred: {http_err}. Response: {response.text}"
        raise HTTPException(status_code=response.status_code, detail=detail)
    except requests.exceptions.RequestException as req_err:
        raise HTTPException(
            status_code=500, detail=f"Error fetching data from FIRMS API: {req_err}"
        )
    except Exception as e:
        # Catch other potential errors, like pandas parsing errors
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {e}"
        )

@app.get("/")
def read_root():
    return {"message": "Welcome to the Firewatch API. Use the /api/fires endpoint to fetch data."}
