from EXCEPTIONS.EXCEPTIONS import ErrorReserva

# Clase que gestiona una reserva entre un cliente y un servicio
class Reserva:

    # Inicializa la reserva con validaciones básicas
    def __init__(self, cliente, servicio):
        if cliente is None:
            raise ErrorReserva("Cliente inválido")
        if servicio is None:
            raise ErrorReserva("Servicio inválido")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"

    # Cambia el estado de la reserva a confirmada
    def confirmar(self):
        self.estado = "confirmada"

    # Muestra la información principal de la reserva
    def mostrar_reserva(self):
        print("Cliente:", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre)
        print("Estado:", self.estado)
        print("Costo:", self.servicio.calcular_costo())