from entidades import Entidad

class ErrorCliente(Exception):
    pass

class Cliente(Entidad):
    def __init__(self, nombre, email, telefono):
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    def validar(self):
        if "@" not in self._email:
            raise ErrorCliente("Email inválido")
        if not self._telefono.isdigit():
            raise ErrorCliente("Teléfono inválido")

    def descripcion(self):
        return f"Cliente: {self._nombre}, Email: {self._email}, Tel: {self._telefono}"
