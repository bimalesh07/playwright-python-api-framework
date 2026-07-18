import pytest
from playwright.sync_api import Playwright
from utilities.read_env import ReadEnv
from utilities.Custom_logger import LogGen
from api_endpoints.Auth_Client import UserAuthClient
from api_endpoints.Auth_Login import Auth_login_users
from api_endpoints.Categroy_Client import CategoryClient
import random

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
  
    logger.info("User Authorization endpoint model client...")

    client = UserAuthClient(api_context)

    yield client
    logger.info("Tearing down function instance container successfully.")


@pytest.fixture(scope="function")
def user_login_client(api_context):
    logger.info("*********User Login endpoint*****************")

    login_clinet = Auth_login_users(api_context)
    yield login_clinet

    logger.info("Tearing down functions")

@pytest.fixture(scope="function")
def categories_client(api_context):
    logger.info("**********Categories Validations *********")
    categories_product = CategoryClient(api_context)
    yield categories_product
    logger.info("Tearing down")


@pytest.fixture(scope="session")
def user_access_token(api_context):
    auth_client = Auth_login_users(api_context)
    unique_email = f"session.auth.{random.randint(1000, 9999)}@yadav.com"
    password = "GlobalSecurePassword123"
    user_payload = {
        "name": "Session Secure User",
        "email": unique_email,
        "password": password,
        "avatar": "https://picsum.photos/640/480"
    }
    
    
    create_res = api_context.post("/api/v1/users/", data=user_payload)
    assert create_res.status == 201
    user_id = create_res.json()["id"]
    
    login_payload = {"email": unique_email, "password": password}
    login_res = auth_client.login_user(login_payload)
    assert login_res.status in [200, 201]
    
    token = login_res.json()["access_token"]
    
    yield token

    api_context.delete(f"/api/v1/users/{user_id}")