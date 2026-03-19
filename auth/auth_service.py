# auth/auth_service.py

import hashlib
from db.connection import get_connection
from models.user_context import UserContext

"""
Servicio de autenticación: login de usuarios
- Verifica credenciales contra la base de datos
- Devuelve un UserContext con la información del usuario si el login es exitoso
- Si el login falla, devuelve None

Hash_password: función para hashear la contraseña usando SHA-256 (no es la mejor opción para producción, pero sirve para este ejemplo)
    ESTA FUNCIÓN ES LA MISMA DE generar_base_de_datos.py, podríamos moverla a un módulo utils.py para evitar duplicación
"""

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def login(username: str, password: str):
    conn = get_connection()
    cursor = conn.cursor()

    password_hash = hash_password(password)

    query = """
        SELECT id_usuario, username, id_organizacion, rol
        FROM usuarios
        WHERE username = ? AND password_hash = ? AND activo = 1
    """

    cursor.execute(query, (username, password_hash))
    result = cursor.fetchone()

    conn.close()

    if result:
        return UserContext(*result)
    else:
        return None