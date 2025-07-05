import io
import pandas as pd
import requests
from fastapi import HTTPException

from app.config import MAP_KEY, FIRMS_API_URL_BASE

def get_fire_data(country: str, day_range: int):
    """
    Fetches and parses fire data from the NASA FIRMS API for a specific country and day range.
    """
    if not MAP_KEY:
        raise HTTPException(
            status_code=500,
            detail="NASA FIRMS MAP_KEY is not configured. Please update the .env file.",
        )

    map_key = MAP_KEY.strip('"')
    # Dynamically construct the API URL
    api_url = f"{FIRMS_API_URL_BASE}{map_key}/VIIRS_SNPP_NRT/{country}/{day_range}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        csv_data = response.text
        # Check for common error messages from the API before parsing
        if "Invalid country" in csv_data or "Invalid day range" in csv_data:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid parameter provided to FIRMS API. Response: {csv_data}",
            )
        
        if not csv_data or 'latitude' not in csv_data.splitlines()[0]:
            raise HTTPException(
                status_code=500,
                detail=f"FIRMS API did not return valid CSV data. Response text: {csv_data}",
            )

        csv_file = io.StringIO(csv_data)
        df = pd.read_csv(csv_file, dtype={'acq_time': str})
        return df.to_dict(orient="records")

    except requests.exceptions.HTTPError as http_err:
        # If the API returns a 4xx/5xx error, this will catch it
        detail = f"HTTP error occurred: {http_err}. Response: {response.text}"
        raise HTTPException(status_code=response.status_code, detail=detail)
    except requests.exceptions.RequestException as req_err:
        raise HTTPException(
            status_code=500, detail=f"Error connecting to FIRMS API: {req_err}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred during data processing: {e}"
        )
