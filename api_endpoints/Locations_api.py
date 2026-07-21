# 📂 api_endpoints/Locations_api.py
from utilities.Custom_logger import LogGen

class LocationsClient:
    logger = LogGen.loggen()

    def __init__(self, api_context):
        self.api_context = api_context

    def Get_Locations(self, radius: float, size: int, origin: str):
        self.logger.info(f"******* Fetching locations (radius={radius}, size={size}, origin='{origin}') *********")
        
        query_params = {
            "radius": radius,
            "size": size,
            "origin": origin
        }
        
        return self.api_context.get(
            "/api/v1/locations",
            params=query_params
        )