# 📂 api_endpoints/Auth_Client.py

class UserAuthClient:
    def __init__(self, api_context):
        self.api_context = api_context

    def get_all_users(self):
        return self.api_context.get("/api/v1/users/")

    def create_user(self, user_payload):
      
        return self.api_context.post("/api/v1/users/", data=user_payload)

    def get_user_by_id(self, user_id):
        return self.api_context.get(f"/api/v1/users/{user_id}")

    def update_user(self, user_id, update_payload):
      
        return self.api_context.put(f"/api/v1/users/{user_id}", data=update_payload)

    def delete_user(self, user_id):
        return self.api_context.delete(f"/api/v1/users/{user_id}")

    def check_email_avialabilty(self, email_Payload):
       
        return self.api_context.post("/api/v1/users/is-available", data=email_Payload)