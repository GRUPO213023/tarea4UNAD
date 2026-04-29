# Este print sirve para verificar que el programa está corriendo correctamente
print("Sistema de gestión iniciado")

# Se define la clase Cliente para representar a los clientes del sistema

class Cliente:

    def __init__(self, nombre, identificacion):

        # Validación de nombre
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        # Validación de identificación
        if not identificacion:
            raise ValueError("La identificación no puede estar vacía")

        # Se guarda el nombre del cliente
        self.nombre = nombre

        # Se guarda la identificación del cliente
        self.identificacion = identificacion

    def mostrar_datos(self):
        print("Cliente:", self.nombre, "- ID:", self.identificacion)

try:
    nombre = input("Ingrese el nombre: ")
    identificacion = input("Ingrese la identificación: ")

    cliente = Cliente(nombre, identificacion)
    cliente.mostrar_datos()

except Exception as e:
    print("Error:", e)
    
from abc import ABC, abstractmethod


# Clase base para los servicios
class Servicio(ABC):

    def __init__(self, nombre, costo_base):
        # Se guarda el nombre del servicio
        self.nombre = nombre

        # Se guarda el costo base del servicio
        self.costo_base = costo_base

    # Método obligatorio para las clases hijas
    @abstractmethod
    def calcular_costo(self):
        pass


# Servicio de tipo sala
class ServicioSala(Servicio):

    def __init__(self, nombre, costo_base, horas):
        # Se inicializa la clase padre
        super().__init__(nombre, costo_base)

        # Se guardan las horas de uso
        self.horas = horas

    # Se calcula el costo según las horas
    def calcular_costo(self):
        return self.costo_base * self.horas
    
# Servicio de alquiler de equipos
class ServicioEquipo(Servicio):

    def __init__(self, nombre, costo_base, cantidad):
        super().__init__(nombre, costo_base)

        # Se guarda la cantidad de equipos
        self.cantidad = cantidad

    def calcular_costo(self):
        return self.costo_base * self.cantidad


# Servicio de asesoría
class ServicioAsesoria(Servicio):

    def __init__(self, nombre, costo_base, horas):
        super().__init__(nombre, costo_base)

        # Se guardan las horas de asesoría
        self.horas = horas

    def calcular_costo(self):
        return self.costo_base * self.horas * 1.2
    
# Clase para gestionar reservas
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