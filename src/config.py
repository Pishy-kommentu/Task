from dotenv import load_dotenv
import os

load_dotenv()

APP_HOST = os.environ.get('APP_HOST')
APP_PORT = int(os.environ.get('APP_PORT'))

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
