from entidades import Entidad

# Defino una excepción personalizada para manejar errores específicos de clientes
class ErrorCliente(Exception):
    pass

# La clase Cliente hereda de Entidad y representa a cada cliente del sistema
class Cliente(Entidad):
    def __init__(self, nombre, email, telefono):
	# Uso atributos privados para encapsular la información del cliente
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    # Método para validar los datos del cliente antes de guardarlos o usarlos
    def validar(self):
	# Verifico que el email tenga un formato básico válido
        if "@" not in self._email:
            raise ErrorCliente("Email inválido")
	# Verifico que el teléfono contenga solo dígitos
        if not self._telefono.isdigit():
            raise ErrorCliente("Teléfono inválido")
    # Método que devuelve una descripción legible del cliente
    def descripcion(self):
        return f"Cliente: {self._nombre}, Email: {self._email}, Tel: {self._telefono}"