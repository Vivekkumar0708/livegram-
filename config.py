from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID", None)
API_HASH = getenv("API_HASH")
TOKEN = getenv("TOKEN", None)
DB_URI = getenv("MONGO_URL")
LOGGER_ID = int(getenv("LOGGER_ID", None))
SUDO_USER = list(map(int, getenv("SUDO_USER", "").split()))
USER_MODE=getenv("USER_MODE",False)
#if you want use string session then turn on this and put you session down
SESSION = getenv("SESSION","")