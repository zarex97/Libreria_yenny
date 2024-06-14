from src.models.user import set_user, verify_email
from src.auth.auth import hash_password


def register(username, password, email):
    if not verify_email(email):
        hashed_password = hash_password(password)
        set_user(username, hashed_password, email)
        print("El usuario se registro correctamente")
    else:
        print("Este correo esta vinculado a una cuenta existente") #mostrar mensaje de que el email ya existe en la vase de datos


