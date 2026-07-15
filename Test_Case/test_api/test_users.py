import pytest
import random
from utilities.Custom_logger import LogGen

class TestUsersModukeWorkFlow:
    logger = LogGen.loggen()
    unique_email = f"bimalesh.{random.randint(100, 999)}@yadav.com"
    created_user_id = None

    def test_1_veryfy_email_is_avaliable(self, user_auth_client):
        obj = user_auth_client
        self.logger.info(f"Checking availability for email: {self.unique_email}")

        paylod = {"email": self.unique_email}
        response = obj.check_email_avialabilty(paylod)
        assert response.status in [200, 201] 
        
        final_response = response.json()
        assert final_response["isAvailable"] is False
        self.logger.info("Email availability checked successfully. Email is completely free to register.")


    def test_create_user(self, user_auth_client):
        obj = user_auth_client
        self.logger.info(f"***************Creating a user************")
        user_payload = {
            "name": "Bimalesh YADAV",
            "email": self.unique_email,
            "password": "bimalesh12345",
            "avatar": "https://picsum.photos/640/480"
        }
        res = obj.create_user(user_payload)
        assert res.status in [200, 201]
        res_data = res.json()
        TestUsersModukeWorkFlow.created_user_id = res_data["id"]
        self.logger.info("Createing User are sucessfully completed")

    def test_get_user_by_id(self, user_auth_client):
        obj = user_auth_client
        self.logger.info("*********Created user Details via Get **********")
        user_id = TestUsersModukeWorkFlow.created_user_id
        self.logger.info(f"Fetching  data from ID: {user_id}")
        res = obj.get_user_by_id(user_id)
        assert res.status == 200
        res_data = res.json()
        assert res_data["email"] == self.unique_email

    def test_update_user_details(self, user_auth_client):
        obj = user_auth_client
        user_id = TestUsersModukeWorkFlow.created_user_id
        update_payload = {"name":"Bimalesh Kumar Yadav"}
        res = obj.update_user(user_id, update_payload)
        res_data = res.json()
        assert res.status ==200
        assert res_data["name"] == "Bimalesh Kumar Yadav"

    def test_get_all_users(self, user_auth_client):
        obj = user_auth_client
        res = obj.get_all_users()
        assert res.status ==200
        res_data = res.json()
        user_list = [user["email"] for user in res_data]
        assert self.unique_email in user_list
        self.logger.info(f"Verified {self.unique_email} exists in the Golobal users")











