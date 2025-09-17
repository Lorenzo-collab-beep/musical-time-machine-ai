import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID_SPOTIFY = os.getenv("CLIENT_ID_SPOTIFY")
CLIENT_SECRET_SPOTIFY = os.getenv("CLIENT_SECRET_SPOTIFY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")