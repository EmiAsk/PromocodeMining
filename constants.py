from dotenv import load_dotenv
import os

load_dotenv('.env')

API_HASH = os.getenv('API_HASH')
API_ID = int(os.getenv('API_ID'))

CHANNELS = ['@emilsrochno', -1001494940862, -1001522434370, -1001155793151]


# SESSIONS_PATH = os.path.join(os.path.dirname(__file__), 'Sessions')
SESSIONS_PATH = './Sessions'
