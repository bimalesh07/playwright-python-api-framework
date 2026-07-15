


class UserAuthClient:
    def __init__(self, api_context):
        self.api_context = api_context


    def check_email_availability(self, email_payload):

        return self.api_context.post()
        