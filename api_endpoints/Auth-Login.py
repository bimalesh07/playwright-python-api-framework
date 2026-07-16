from utilities.Custom_logger import LogGen


class Auth_login:
    logger = LogGen.loggen()

    def __init__(self,api_context ):
        self.api_context = api_context
        

    def Login_user(self, login_data):
        self.logger.info("*********Start login ***************")
        return self.api_context.post("/api/v1/auth", data=login_data)

    def Profile(self):
        self.logger.info("*********Geting Profile***********")
        return self.api_context.get("api/v1/profile")

    def Refresh_token(self, refresh_token):
        self.logger.info("**********Refresh Token to hget a new token ************")
        return self.api_context.post("/api/v1/auth/refresh-token", data= refresh_token)


    

