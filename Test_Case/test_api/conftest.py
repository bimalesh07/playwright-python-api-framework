import pytest
from playwright.sync_api import Playwright
from utilities.read_env import ReadEnv
from utilities.Custom_logger import LogGen
from api_endpoints.Auth_Client import UserAuthClient

logger = LogGen.loggen()

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
  
    logger.info("Backend API Request Client...")

    base_api_url = ReadEnv.get_base_api()
    
    browser_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }

    request_context = playwright.request.new_context(
        base_url=base_api_url,
        extra_http_headers=browser_headers
    )
    
    yield request_context
    
    logger.info("Backend API Network Context Connection safely...")
    request_context.dispose()


@pytest.fixture(scope="function")
def user_auth_client(api_context):
  
    logger.info("Instantiating isolated User Authorization endpoint model client...")

    client = UserAuthClient(api_context)

    yield client
    
    logger.info("Tearing down function instance container successfully.")