from entidades import Entidad

class ErrorServicio(Exception):
    pass

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

class ReservaSala(Servicio):
    def validar(self):
        super().validar()
        if self.costo_base < 50:
            raise ErrorServicio("Costo de sala demasiado bajo")

class AlquilerEquipo(Servicio):
    def validar(self):
        super().validar()
        if self.costo_base < 20:
            raise ErrorServicio("Costo de equipo inválido")

class AsesoriaEspecializada(Servicio):
    def validar(self):
        super().validar()
        if self.costo_base < 100:
            raise ErrorServicio("Costo de asesoría inválido")
