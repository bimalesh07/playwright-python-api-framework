from utilities.Custom_logger import LogGen

class Auth_login_users:
    logger = LogGen.loggen()

    def __init__(self, api_context):
        self.api_context = api_context
        
    def login_user(self, login_data):
        self.logger.info("********* Start login ***************")
        return self.api_context.post("/api/v1/auth/login", data=login_data)

    def get_profile(self, headers=None):
        self.logger.info("********* Getting Profile ***********")
        return self.api_context.get("/api/v1/auth/profile", headers=headers)

    def refresh_token(self, refresh_token_payload):
        self.logger.info("********** Refresh Token to get a new token ************")
        return self.api_context.post("/api/v1/auth/refresh-token", data=refresh_token_payload)