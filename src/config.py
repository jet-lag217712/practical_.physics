import os
from dotenv import load_dotenv

load_dotenv(".env.api")
load_dotenv(".env.auth")

GROQ_API_KEY_1 = os.getenv("GROQ_API_KEY_1")
GROQ_API_KEY_2 = os.getenv("GROQ_API_KEY_2")
GROQ_API_KEY_3 = os.getenv("GROQ_API_KEY_3")
GROQ_API_KEY_4 = os.getenv("GROQ_API_KEY_4")
GROQ_API_KEYS = [GROQ_API_KEY_1, GROQ_API_KEY_2, GROQ_API_KEY_3, GROQ_API_KEY_4]

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
AUTH = [EMAIL,PASSWORD]