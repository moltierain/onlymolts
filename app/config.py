import os
from dotenv import load_dotenv

load_dotenv()

PLATFORM_ADMIN_KEY = os.getenv("PLATFORM_ADMIN_KEY", "")
CSB_MOLTBOOK_API_KEY = os.getenv("CSB_MOLTBOOK_API_KEY", "")
