import google.generativeai as genai
from config import Config
        
config = Config()
API_KEY = config.get_api_key()

print(API_KEY)