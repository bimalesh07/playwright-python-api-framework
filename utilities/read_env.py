
import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, '.env')

load_dotenv(dotenv_path=ENV_PATH)

class ReadEnv:
    @staticmethod
    def get_base_api():
        return os.getenv("BASE_API_URL", "https://api.escuelajs.co")