import os
import secrets

# Dev only
# from dotenv import load_dotenv
# load_dotenv()

# Reddit Credentials
reddit_username = os.environ.get("REDDIT_USERNAME")
reddit_password = os.environ.get("REDDIT_PASSWORD")
client_id = os.environ.get("REDDIT_CID")
client_secret = os.environ.get("REDDIT_CSECRET")


# App Settings
PORT = 3000
SECRET_KEY = secrets.token_hex(16)
WTF_CSRF_ENABLED = False
