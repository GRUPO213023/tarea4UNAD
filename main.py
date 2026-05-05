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


# MEJORA MÓDULO SERVICIOS

from abc import ABC, abstractmethod

#  Se crean excepciones personalizadas para manejar errores específicos
class ServicioError(Exception):
    pass

class DatoInvalidoError(ServicioError):
    pass


#  Clase abstracta base (ABSTRACCIÓN)
class Servicio(ABC):

    def __init__(self, nombre, costo_base):
        #  Validaciones para garantizar datos correctos (ENCAPSULACIÓN)
        if not nombre:
            raise DatoInvalidoError("El nombre del servicio no puede estar vacío")

        if costo_base <= 0:
            raise DatoInvalidoError("El costo base debe ser mayor a 0")

        self.nombre = nombre
        self.costo_base = costo_base

    #  Método abstracto obligatorio (POLIMORFISMO)
    @abstractmethod
    def calcular_costo(self, **kwargs):
        pass

    #  Método abstracto para descripción del servicio
    @abstractmethod
    def descripcion(self):
        pass


# SERVICIO SALA

# Herencia desde Servicio
class ServicioSala(Servicio):

    def __init__(self, nombre, costo_base, horas):
        super().__init__(nombre, costo_base)

        # Validación de horas
        if horas <= 0:
            raise DatoInvalidoError("Las horas deben ser mayores a 0")

        self.horas = horas

    # Parámetro opcional → simula sobrecarga (descuento)
    def calcular_costo(self, descuento=0):
        try:
            costo = self.costo_base * self.horas
            costo -= costo * descuento
            return costo
        except Exception as e:
            #  Manejo controlado de errores
            raise ServicioError(f"Error en ServicioSala: {e}")

    def descripcion(self):
        # Implementación polimórfica
        return f"Sala reservada por {self.horas} horas"


# SERVICIO EQUIPO

class ServicioEquipo(Servicio):

    def __init__(self, nombre, costo_base, cantidad):
        super().__init__(nombre, costo_base)

        #  Validación de cantidad
        if cantidad <= 0:
            raise DatoInvalidoError("La cantidad debe ser mayor a 0")

        self.cantidad = cantidad

    # Parámetro opcional (seguro adicional)
    def calcular_costo(self, seguro=False):
        try:
            costo = self.costo_base * self.cantidad

            if seguro:
                costo += 20  # costo adicional

            return costo
        except Exception as e:
            raise ServicioError(f"Error en ServicioEquipo: {e}")

    def descripcion(self):
        return f"Alquiler de {self.cantidad} equipos"


# SERVICIO ASESORÍA

class ServicioAsesoria(Servicio):

    def __init__(self, nombre, costo_base, horas):
        super().__init__(nombre, costo_base)

        #  Validación de horas
        if horas <= 0:
            raise DatoInvalidoError("Las horas deben ser mayores a 0")

        self.horas = horas

    #  Niveles de servicio (lógica extendida)
    def calcular_costo(self, nivel="normal"):
        try:
            multiplicador = 1

            if nivel == "alta":
                multiplicador = 1.5
            elif nivel == "premium":
                multiplicador = 2

            return self.costo_base * self.horas * multiplicador

        except Exception as e:
            raise ServicioError(f"Error en ServicioAsesoria: {e}")

    def descripcion(self):
        return f"Asesoría por {self.horas} horas"
    
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