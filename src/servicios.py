from entidades import Entidad

# Excepción personalizada para manejar errores relacionados con los servicios.

class ErrorServicio(Exception):
    pass

# Clase base Servicio que hereda de Entidad.
# Representa cualquier tipo de servicio con un nombre y un costo base.

class Servicio(Entidad):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    def validar(self):
        if self.costo_base <= 0:
            raise ErrorServicio("Costo inválido")

    def descripcion(self):
        return f"Servicio: {self.nombre}, Costo base: {self.costo_base}"

    def calcular_costo(self, duracion=1, impuesto=0.19, descuento=0):
        return (self.costo_base * duracion) * (1 + impuesto) - descuento


# Clase específica para reservas de salas.
# Aplica una validación adicional sobre el costo mínimo.

class ReservaSala(Servicio):
    def validar(self):
        super().validar()
        if self.costo_base < 50:
            raise ErrorServicio("Costo de sala demasiado bajo")


# Clase específica para alquiler de equipos.
# Valida que el costo sea razonable para este tipo de servicio.

class AlquilerEquipo(Servicio):
    def validar(self):
        super().validar()
        if self.costo_base < 20:
            raise ErrorServicio("Costo de equipo inválido")


# Clase específica para asesorías especializadas.
# Exige un costo mínimo más alto por la naturaleza del servicio.

class AsesoriaEspecializada(Servicio):
    def validar(self):
        super().validar()
        if self.costo_base < 100:
            raise ErrorServicio("Costo de asesoría inválido")