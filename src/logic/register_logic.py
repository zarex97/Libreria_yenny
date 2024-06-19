from src.models.user import set_user, verify_email
from src.auth.auth import hash_password


def register(username, password, email):
    if not verify_email(email):
        hashed_password = hash_password(password)
        set_user(username, hashed_password, email)
        return True
    else:
        return False