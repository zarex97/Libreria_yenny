from src.models.user import get_user
from src.auth.auth import verify_password


def login(username, password):
    user_data = get_user(username)

    if user_data:
        user_id, name, hashed_password, email, role_id = user_data
        if verify_password(password, hashed_password):
            print(f"Se inicio sesion correctamente {name}")
        else:
            print("Usuario o contraseña incorrecta")
    else:
        print(f"Usuario {username} no encontrado")




