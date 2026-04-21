from pathlib import Path
from dotenv import load_dotenv

import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env.api")
load_dotenv(BASE_DIR / ".env.auth")

GROQ_API_KEY_1 = os.getenv("GROQ_API_KEY_1")
GROQ_API_KEY_2 = os.getenv("GROQ_API_KEY_2")
GROQ_API_KEY_3 = os.getenv("GROQ_API_KEY_3")
GROQ_API_KEY_4 = os.getenv("GROQ_API_KEY_4")
GROQ_API_KEYS = [GROQ_API_KEY_1, GROQ_API_KEY_2, GROQ_API_KEY_3, GROQ_API_KEY_4]

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
AUTH = [EMAIL,PASSWORD]

INIT_URL_DICT = {"https://summitps.instructure.com/courses/5460/quizzes/51872/take?user_id=3822": "test"
                 }