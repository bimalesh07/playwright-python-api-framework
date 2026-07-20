import pytest
import os
from utilities.Custom_logger import LogGen

class TestFilesModule:
    logger = LogGen.loggen()
    uploaded_filename = None

    @pytest.fixture(scope="class", autouse=True)
    def create_dummy_local_file(self):
        dummy_path = "dummy_test_image.png"
        with open(dummy_path, "wb") as f:
            f.write(b"Fake PNG image binary data for API framework testing.")
        
        yield dummy_path
        
        # Cleanup local file after tests finish
        if os.path.exists(dummy_path):
            os.remove(dummy_path)

    def test_upload_file_validation(self, files_client, create_dummy_local_file):
        file_path = create_dummy_local_file
        res = files_client.Upload_File(file_path=file_path, file_name="test_image.png")
        
        assert res.status == 201
        res_data = res.json()
        assert "filename" in res_data
        assert "location" in res_data
        
        # Storing for downstream get request validation
        TestFilesModule.uploaded_filename = res_data["filename"]
        self.logger.info(f"File uploaded successfully. Server Name: {TestFilesModule.uploaded_filename}")

    def test_get_uploaded_file_by_name(self, files_client):
        assert TestFilesModule.uploaded_filename is not None, "Skipping because upload failed."
        
        res = files_client.Get_File_By_Name(TestFilesModule.uploaded_filename)
        assert res.status == 200
        # Files return data as binary, not JSON
        assert len(res.body()) > 0
        self.logger.info("File contents successfully retrieved from server.")