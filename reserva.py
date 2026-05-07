from EXCEPTIONS.EXCEPTIONS import ErrorReserva
from logger import registrar_log

# CLASE RESERVA
# Esta clase une a un Cliente con un Servicio y gestiona el estado de la reserva.

class Reserva:

    def __init__(self, cliente, servicio):
        try:
            if cliente is None:
                raise ErrorReserva("No se puede crear una reserva sin cliente")
            if servicio is None:
                raise ErrorReserva("No se puede crear una reserva sin servicio")

            self.cliente = cliente
            self.servicio = servicio
            self.estado = "pendiente"

        except ErrorReserva as error:
            registrar_log(f"Error al crear reserva: {error}")
            raise

        else:
            print(f"Reserva creada para cliente '{cliente.nombre}' con servicio '{servicio.nombre}'")

        finally:
            print("Proceso de creación de reserva finalizado.")

    # MÉTODO: confirmar()
    # Cambia el estado de la reserva a "confirmada".

    def confirmar(self):
        try:
            if self.estado != "pendiente":
                raise ErrorReserva(
                    f"No se puede confirmar una reserva en estado '{self.estado}'"
                )

            costo = self.servicio.calcular_costo()

            if costo <= 0:
                raise ErrorReserva("El costo calculado es inválido (debe ser mayor a 0)")

            self.estado = "confirmada"

        except ErrorReserva as error:
            registrar_log(f"Error al confirmar: {error}")
            raise  

        except Exception as error:
            registrar_log(f"Error inesperado al confirmar: {error}")
            raise

        else:
            print(f"Reserva confirmada. Costo total: ${costo:.2f}")

        finally:
            print(f"Intento de confirmación finalizado. Estado actual: {self.estado}")

    # MÉTODO: cancelar()
    # Cancela la reserva
    
    def cancelar(self):
        try:
            # Una reserva ya cancelada no puede cancelarse de nuevo
            if self.estado == "cancelada":
                raise ErrorReserva("La reserva ya está cancelada")

            self.estado = "cancelada"

        except ErrorReserva as error:
            registrar_log(f"Error al cancelar: {error}")
            raise

        else:
            print("Reserva cancelada exitosamente.")

        finally:
            print(f"Proceso de cancelación finalizado. Estado actual: {self.estado}")

    # MÉTODO: mostrar_reserva()
    # Muestra los datos de la reserva en pantalla.

    def mostrar_reserva(self):
        try:
            costo = self.servicio.calcular_costo()
            print("=" * 40)
            print(f"  Cliente  : {self.cliente.nombre}")
            print(f"  ID       : {self.cliente.identificacion}")
            print(f"  Servicio : {self.servicio.nombre}")
            print(f"  Estado   : {self.estado}")
            print(f"  Costo    : ${costo:.2f}")
            print("=" * 40)

        except Exception as error:
            registrar_log(f"Error al mostrar reserva: {error}")
            print(f"No se pudo mostrar la reserva: {error}")