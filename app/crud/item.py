import io
import pandas as pd
import requests
from fastapi import HTTPException

from app.config import MAP_KEY, FIRMS_API_URL_TEMPLATE

def get_fire_data():
    """
    Fetches and parses fire data from the NASA FIRMS API.
    """
    if not MAP_KEY:
        raise HTTPException(
            status_code=500,
            detail="NASA FIRMS MAP_KEY is not configured. Please update the .env file.",
        )

    map_key = MAP_KEY.strip('"')
    api_url = FIRMS_API_URL_TEMPLATE.format(map_key=map_key)

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        csv_data = response.text
        if not csv_data or 'latitude' not in csv_data.splitlines()[0]:
            raise HTTPException(
                status_code=500,
                detail=f"FIRMS API did not return valid CSV data. Response text: {csv_data}",
            )

        csv_file = io.StringIO(csv_data)
        df = pd.read_csv(csv_file, dtype={'acq_time': str})
        return df.to_dict(orient="records")

    except requests.exceptions.HTTPError as http_err:
        detail = f"HTTP error occurred: {http_err}. Response: {response.text}"
        raise HTTPException(status_code=response.status_code, detail=detail)
    except requests.exceptions.RequestException as req_err:
        raise HTTPException(
            status_code=500, detail=f"Error fetching data from FIRMS API: {req_err}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred: {e}"
        )
