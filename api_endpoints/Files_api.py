# 📂 api_endpoints/Files_api.py
from utilities.Custom_logger import LogGen

class FilesClient:
    logger = LogGen.loggen()

    def __init__(self, api_context):
        self.api_context = api_context

    def Upload_File(self, file_path, file_name, mime_type="image/png"):
        self.logger.info(f"******* Uploading file: {file_name} *********")
        
        with open(file_path, "rb") as file_bytes:
            return self.api_context.post(
                "/api/v1/files/upload",
                files=[
                    {
                        "name": "file",  
                        "filename": file_name,
                        "contentType": mime_type,
                        "file": file_bytes.read()
                    }
                ]
            )

    def Get_File_By_Name(self, filename):
        self.logger.info(f"******* Fetching file: {filename} *********")
        return self.api_context.get(f"/api/v1/files/{filename}")