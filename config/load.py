import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

USER_AGENT = os.getenv('USER_AGENT')
ACCOUNT_USERNAME = os.getenv('ACCOUNT_USERNAME')
ACCOUNT_PASSWORD = os.getenv('ACCOUNT_PASSWORD')
