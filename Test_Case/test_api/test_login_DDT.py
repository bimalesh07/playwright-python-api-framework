import pytest
import json
import os
import random
from utilities.Custom_logger import LogGen

def load_login_json():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    json_path = os.path.join(base_dir, "test_data", "login_data.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

class TestAuthLoginDDT:
    logger = LogGen.loggen()

    @pytest.fixture(scope="class")
    @classmethod
    def created_user(cls, api_context):
        rand_num = random.randint(10000, 99999)
        email = f"auto_ddt_{rand_num}@mail.com"
        password = "ValidPassword123"
        
        user_payload = {
            "name": f"DDT User {rand_num}",
            "email": email,
            "password": password,
            "avatar": "https://picsum.photos/800"
        }
        
        res = api_context.post("/api/v1/users/", data=user_payload)
        assert res.status == 201, f"User creation failed: {res.text()}"
        
        return {"email": email, "password": password}

    @pytest.mark.parametrize("data", load_login_json())
    def test_login_ddt(self, user_login_client, created_user, data):
        self.logger.info("****************login DDT are start ************")
        scenario = data["scenario"]
        expected_status = data["expected_status"]

        payload = {
            "email": data["email"],
            "password": data["password"]
        }

        if payload["email"] == "__DYNAMIC_USER__":
            payload["email"] = created_user["email"]

        if payload["password"] == "__DYNAMIC_PASSWORD__":
            payload["password"] = created_user["password"]

        self.logger.info(f"Running DDT Scenario: {scenario} (Testing Email: {payload['email']}) ---")

        res = user_login_client.login_user(payload)

        assert res.status == expected_status, (
            f"Scenario '{scenario}' failed. Expected {expected_status}, got {res.status}. "
            f"Response: {res.text()}"
        )

        if expected_status == 201:
            assert "access_token" in res.json()
            self.logger.info(f"Token generated for dynamic user {payload['email']}")