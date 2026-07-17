import pytest
import random
from utilities.Custom_logger import LogGen

class TestAuthModule:
    logger = LogGen.loggen()

    @pytest.fixture(scope="function")
    def register_temp_user(self, user_login_client):
        self.logger.info("Creating temporary user...")
        unique_email = f"auth.test.{random.randint(1000, 9999)}@yadav.com"
        password = "LoginPassword123"
    
        payload = {
            "name": "Auth Tester",
            "email": unique_email,
            "password": password,
            "avatar": "https://picsum.photos/640/480"
        }
        
     
        response = user_login_client.api_context.post("/api/v1/users/", data=payload)
        assert response.status == 201
        user_id = response.json()["id"]
        
        yield {"email": unique_email, "password": password}
        
        self.logger.info(f"Deleting user ID: {user_id}")
        user_login_client.api_context.delete(f"/api/v1/users/{user_id}")

    def test_auth_end_to_end_workflow(self, user_login_client, register_temp_user):
        obj = user_login_client
        credentials = register_temp_user
        
        self.logger.info(f"Attempting auth login for: {credentials['email']}")
        login_payload = {
            "email": credentials["email"],
            "password": credentials["password"]
        }
        
        login_res = obj.login_user(login_payload)
        assert login_res.status in [200, 201]
        
        token = login_res.json()["access_token"]
        self.logger.info("Login Success! Token generated.")

        # ---------------- PROFILE CHECK ----------------
        self.logger.info("Verifying Profile with the generated token...")
        headers = {"Authorization": f"Bearer {token}"}
        
        profile_res = obj.get_profile(headers=headers)
        
        # Strict status check
        assert profile_res.status == 200
        
        profile_data = profile_res.json()
        assert profile_data["email"] == credentials["email"]
        self.logger.info(f"Profile Verified! Confirmed user: {profile_data['name']}")