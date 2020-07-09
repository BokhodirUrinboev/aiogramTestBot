import os
from dotenv import load_dotenv

load_dotenv()
LANG_STORAGE = {}
NUMBER_STORAGE = {}
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
]
admin_id = int(os.getenv("ADMIN_ID"))
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
ip = os.getenv("ip")
host = "localhost"

# I18N_DOMAIN = 'testbot'
path = os.getcwd()
# parent directory
BASE_DIR = os.path.abspath(os.path.join(path, os.pardir))
# LOCALES_DIR = BASE_DIR + '\\locales'

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
