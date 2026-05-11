from EXCEPTIONS.EXCEPTIONS import ErrorCliente

# Clase que representa un cliente del sistema
class Cliente:

    # Inicializa el cliente con validaciones básicas
    def __init__(self, nombre, identificacion):
        if not nombre:
            raise ErrorCliente("El nombre no puede estar vacío")
        if not identificacion:
            raise ErrorCliente("La identificación no puede estar vacía")

        self.nombre = nombre
        self.identificacion = identificacion

    # Muestra la información del cliente
    def mostrar_datos(self):
        print("Cliente:", self.nombre, "- ID:", self.identificacion)