from decouple import config

MAP_KEY = config("MAP_KEY", default=None)

# FIRMS API URL for VIIRS S-NPP NRT data for the last 24 hours in the USA
FIRMS_API_URL_TEMPLATE = (
    "https://firms.modaps.eosdis.nasa.gov/api/country/csv/"
    "{map_key}/VIIRS_SNPP_NRT/USA/1"
)
