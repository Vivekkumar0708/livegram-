from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID", 25488022)
API_HASH = getenv("API_HASH", "0c999a454fddd79251213be7944811e8")
TOKEN = getenv("TOKEN", "7146371782:AAEVQ9SUWYxnpWgME3CecKJEetiPIufKFyY")
DB_URI = getenv("MONGO_URL","mongodb+srv://Lucifer121:vivek@jaishreeram.z0o2fuy.mongodb.net/?retryWrites=true&w=majority")
LOGGER_ID = int(getenv("LOGGER_ID", -1002042572827))
SUDO_USER = list(map(int, getenv("SUDO_USER", "").split()))
