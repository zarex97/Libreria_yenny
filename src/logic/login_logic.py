from src.models.user import get_user
from src.auth.auth import verify_password


def login(email, password):
    user = get_user(email)

    if user:
        print(f"Usuario encontrado: {user.email}, {user.password}")  # Diagnóstico
        if verify_password(password, user.password):
            print("Contraseña verificada correctamente")  # Diagnóstico
            return user
        else:
            print("Contraseña incorrecta")  # Diagnóstico
    else:
        print("Usuario no encontrado")  # Diagnóstico
    return None





