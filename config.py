import os

# Reddit Credentials
reddit_username = os.environ.get('REDDIT_USERNAME')
reddit_password = os .environ.get('REDDIT_PASSWORD')
client_id = os.environ.get('REDDIT_CID')
client_secret = os.environ.get('REDDIT_CSECRET')


# App Settings
DEBUG = True
PORT = 3000
SECRET_KEY = '3453KJA9S8D7AS3453FASAD1651'
WTF_CSRF_ENABLED = False
