from dotenv import load_dotenv
import os

load_dotenv()
print(f"API Key = {os.environ.get('API_KEY')}")
print(f"Google API Key = {os.environ.get('GOOGLE_API_KEY')}")
print("configuration")
print("configuration1 ")
