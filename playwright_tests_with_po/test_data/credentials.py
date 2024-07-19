import os
from dotenv import load_dotenv

load_dotenv()

standard_user = {
    'username': os.getenv('USERNAME_SAUCEDEMO'),
    'password': os.getenv('PASSWORD_SAUCEDEMO'),
}
