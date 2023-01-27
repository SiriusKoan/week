import firebase_admin
from firebase_admin import auth
from .config import app_name

app = firebase_admin.initialize_app()


def get_user(access_token):
    try:
        user = auth.verify_id_token(access_token)
        return user["email"] if user else False
    except Exception as e:
        return False
