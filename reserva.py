from datetime import datetime

from entidades import Cliente
from servicios import Servicio
from exceptions import DatosInvalidosError, OperacionNoPermitidaError, ReservaError


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("La reserva requiere un cliente valido.")

        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError("La reserva requiere un servicio valido.")

        if duracion <= 0:
            raise DatosInvalidosError("La duracion debe ser positiva.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "creada"
        self.costo_total = 0
        self.fecha = datetime.now()

    def confirmar(self):
        if self.estado != "creada":
            raise OperacionNoPermitidaError("Solo se pueden confirmar reservas creadas.")

        self.servicio.validar_disponibilidad()
        self.estado = "confirmada"

    def cancelar(self, motivo="Sin motivo"):
        if self.estado == "procesada":
            raise OperacionNoPermitidaError("No se puede cancelar una reserva procesada.")

        if self.estado == "cancelada":
            raise OperacionNoPermitidaError("La reserva ya fue cancelada.")

        self.estado = "cancelada"
        self.motivo_cancelacion = motivo

    def procesar(self, impuesto=0.19, descuento=0.0, **opciones):
        try:
            if self.estado != "confirmada":
                raise OperacionNoPermitidaError("La reserva debe estar confirmada antes de procesarse.")

            self.costo_total = self.servicio.calcular_costo_total(
                self.duracion,
                impuesto=impuesto,
                descuento=descuento,
                **opciones
            )

        except Exception as error:
            raise ReservaError("Fallo el procesamiento de la reserva.") from error

        else:
            self.estado = "procesada"
            return self.costo_total

        finally:
            self.ultimo_intento_proceso = datetime.now()

    def resumen(self):
        return (
            f"Reserva {self.estado} | Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | Costo: ${self.costo_total}"
        )

    def __str__(self):
        return self.resumen()