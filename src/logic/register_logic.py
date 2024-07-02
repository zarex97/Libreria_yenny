from src.models.user import set_user, verify_email, get_user
from src.auth.auth import hash_password


def register(username, password, email):
    if not verify_email(email):
        hashed_password = hash_password(password)
        set_user(username, hashed_password, email)
        user = get_user(email)
        return user
    else:
        return None
