# models/user_context.py

class UserContext:
    def __init__(self, id_usuario, username, id_organizacion, rol):
        self.id_usuario = id_usuario
        self.username = username
        self.id_organizacion = id_organizacion
        self.rol = rol

    def __repr__(self):
        return f"<UserContext {self.username} | Org: {self.id_organizacion} | Rol: {self.rol}>"