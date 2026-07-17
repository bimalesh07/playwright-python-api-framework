
import pytest
import random
from utilities.Custom_logger import LogGen

class TestAuthModule:
    logger = LogGen.loggen()
    
    token = None
    refresh_token = None

    global_email = f"auth.workflow.{random.randint(1000, 9999)}@yadav.com"
    global_password = "WorkflowSecurePassword123"
    global_user_id = None

    @pytest.fixture(scope="function")
    def register_temp_user(self, user_login_client):
        if TestAuthModule.global_user_id is None:
            self.logger.info(f"Creating workflow user with email: {TestAuthModule.global_email}")
            
            payload = {
                "name": "Auth Workflow User",
                "email": TestAuthModule.global_email,
                "password": TestAuthModule.global_password,
                "avatar": "https://picsum.photos/640/480"
            }
            
            # User register kiya
            response = user_login_client.api_context.post("/api/v1/users/", data=payload)
            assert response.status == 201
            TestAuthModule.global_user_id = response.json()["id"]
            self.logger.info(f" User registered with ID: {TestAuthModule.global_user_id}")

    # LOGIN CHECK
    def test_successful_login_and_token_generation(self, user_login_client, register_temp_user):
        obj = user_login_client
        
        login_payload = {
            "email": TestAuthModule.global_email,
            "password": TestAuthModule.global_password
        }
        
        response = obj.login_user(login_payload)
        assert response.status in [200, 201]
        
        res_data = response.json()
        # Tokens save kar liye
        TestAuthModule.token = res_data["access_token"]
        TestAuthModule.refresh_token = res_data["refresh_token"]
        self.logger.info("Access and Refresh tokens successfully captured.")

    # TEST : GET PROFILE 
    def test_get_profile(self, user_login_client):
        obj = user_login_client
        token = TestAuthModule.token
        
        headers = {"Authorization": f"Bearer {token}"}
        res = obj.get_profile(headers=headers)
        
        assert res.status == 200
        assert res.json()["email"] == TestAuthModule.global_email
        self.logger.info(f"👤 Profile Verified for: {res.json()['name']}")

    # TEST 3: REFRESH TOKEN 
    def test_refresh_token_generation(self, user_login_client):
        obj = user_login_client
        old_refresh_token = TestAuthModule.refresh_token
        
        refresh_payload = {
            "refreshToken": old_refresh_token
        }
        
        res = obj.refresh_token(refresh_payload)
        assert res.status in [200, 201]
        assert "access_token" in res.json()
        self.logger.info(" Refresh Token successful! Brand new Access Token received.")

        self.logger.info(f"Deleting workflow user ID: {TestAuthModule.global_user_id}")
        obj.api_context.delete(f"/api/v1/users/{TestAuthModule.global_user_id}")
        self.logger.info("Database clean! All auth tests passed.")