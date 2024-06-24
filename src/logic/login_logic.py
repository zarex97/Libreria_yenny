from src.models.user import get_user
from src.auth.auth import verify_password


def login(email, password):
    user = get_user(email)

    if user:
        if verify_password(password, user.password):
            return user
    else:
        return None





