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

INIT_URLS = [
             "https://summitps.instructure.com/courses/5460/quizzes/51858",
             "https://summitps.instructure.com/courses/5460/quizzes/51904",
             "https://summitps.instructure.com/courses/5460/quizzes/51897",
             "https://summitps.instructure.com/courses/5460/quizzes/51897",
]

INIT_URLS_PROD = [
    "https://summitps.instructure.com/courses/5460/quizzes/51864/take?user_id=3822",
    "https://summitps.instructure.com/courses/5460/quizzes/51992/take?user_id=3822",
    "https://summitps.instructure.com/courses/5460/quizzes/51986/take?user_id=3822",
    "https://summitps.instructure.com/courses/5460/quizzes/51856/take?user_id=3822",
    "https://summitps.instructure.com/courses/5460/quizzes/51951/take?user_id=3822",
    "https://summitps.instructure.com/courses/5460/quizzes/51961/take?user_id=3822",
    "https://summitps.instructure.com/courses/5460/quizzes/51862/take?user_id=3822",
    "https://summitps.instructure.com/courses/5460/quizzes/51999/take?user_id=3822",
    "https://summitps.instructure.com/courses/5460/quizzes/51872/take?user_id=3822",
]