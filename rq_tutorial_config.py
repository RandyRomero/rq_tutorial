from dotenv import load_dotenv
import os

load_dotenv('.env')
redispass = os.environ.get('REDISPASS')