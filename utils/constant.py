import os
from dotenv import load_dotenv

load_dotenv()

# Open AI Compatibility API
OPENAI_COMPATIBILITY_API = os.getenv("OPENAI_COMPATIBILITY_API", "https://api.openai.com/v1")
OPENAI_COMPATIBILITY_API_KEY = os.getenv("OPENAI_COMPATIBILITY_API_KEY", "your-openai-compatibility-api-key")

# GEMINI API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your-gemini-api-key")

# Deepl api key
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY", "your-deepl-api-key")
