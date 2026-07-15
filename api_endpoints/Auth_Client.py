class UserAuthClient:
    def __init__(self, api_context):
        self.api_context = api_context


    def get_all_users(self):
        response = self.api_context.get("/api/v1/users")
        return response

    def create_user(self, user_payload):
        response = self.api_context.post("/api/v1/users" data= user_payload)
        return response

    def get_user_by_id(self, user_id):
        response = self.api_context.post(f"/api/v1/users/{user_id}")
        return response

    def update_user(self, user_id, update_payload):
        response = self.api_context.put(f"/api/v1/users/{user_id}", data=update_payload)
        return response

    def delete_user(self, user_id):
        response = self.api_context.delete(f"/api/v1/users/{user_id}")
        return response

    def check_email_avialabilty(self, email_Payload):
        response = self.api_context.post("/api/v1/users/is_available", data=email_Payload)


        