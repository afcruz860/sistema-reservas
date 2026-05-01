import logging
from clientes import ErrorCliente
from servicios import ErrorServicio

logging.basicConfig(
    filename="logs.txt",
    filemode="a",   
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ErrorReserva(Exception):
    pass

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            self.cliente.validar()
            self.servicio.validar()
            self.estado = "Confirmada"
            logging.info("Reserva confirmada correctamente.")
            return "Reserva confirmada"
        except (ErrorCliente, ErrorServicio) as e:
            logging.error(f"Error al confirmar la reserva: {e}")
            raise ErrorReserva("Error en la confirmación de la reserva") from e

    def cancelar(self):
        try:
            if self.estado != "Confirmada":
                raise ErrorReserva("No se puede cancelar una reserva no confirmada")
            self.estado = "Cancelada"
            logging.info("Reserva cancelada correctamente.")
            return "Reserva cancelada"
        except ErrorReserva as e:
            logging.error(f"Error al cancelar la reserva: {e}")
            raise

    def procesar(self, impuesto=0.0, descuento=0.0):
        try:
            costo_total = self.servicio.calcular_costo(self.duracion, impuesto, descuento)
            logging.info(f"Reserva procesada: costo total = {costo_total}")
            return f"Costo total de la reserva: {costo_total}"
        except Exception as e:
            logging.error(f"Error al procesar la reserva: {e}")
            raise ErrorReserva("Error en el procesamiento de la reserva") from e
