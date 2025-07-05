from decouple import config

MAP_KEY = config("MAP_KEY", default=None)

# Base URL for the FIRMS API
FIRMS_API_URL_BASE = "https://firms.modaps.eosdis.nasa.gov/api/country/csv/"
