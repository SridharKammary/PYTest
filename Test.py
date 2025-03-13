from dotenv import load_dotenv
import os

load_dotenv()
print(f"API Key = {os.environ.get('API_KEY')}")
