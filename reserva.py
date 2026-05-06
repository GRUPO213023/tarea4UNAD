class Reserva:

    def __init__(self, cliente, servicio):
        # Se guarda el cliente asociado
        self.cliente = cliente

        # Se guarda el servicio asociado
        self.servicio = servicio

        # Estado inicial de la reserva
        self.estado = "pendiente"

    # Confirmar la reserva
    def confirmar(self):
        self.estado = "confirmada"

    # Cancelar la reserva
    def cancelar(self):
        self.estado = "cancelada"

    # Mostrar información de la reserva
    def mostrar_reserva(self):
        print("Cliente:", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre)
        print("Estado:", self.estado)
        print("Costo:", self.servicio.calcular_costo())
        
        #VERIFICACION DE COMMIT
        #prueba Paola 2