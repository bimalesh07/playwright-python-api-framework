import pytest
from utilities.Custom_logger import LogGen

class TestLocationsModule:
    logger = LogGen.loggen()

    def test_get_locations_success(self, locations_client):
        radius = 10.5
        size = 5
        origin = "40.7128,-74.0060"  
        
        res = locations_client.Get_Locations(radius=radius, size=size, origin=origin)
        
        assert res.status == 200, f"Expected 200 OK, got {res.status}. Response: {res.text()}"
        
        res_data = res.json()
        assert isinstance(res_data, (list, dict)), "Response should be a JSON array or object"
        self.logger.info("Locations retrieved successfully.")