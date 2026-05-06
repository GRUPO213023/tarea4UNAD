from abc import ABC, abstractmethod
from EXCEPTIONS.EXCEPTIONS import ErrorServicio

# Clase base abstracta
class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        if costo_base <= 0:
            raise ErrorServicio("El costo base debe ser mayor a 0")

        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass


# Servicio de Sala
class ServicioSala(Servicio):

    def __init__(self, nombre, costo_base, horas):
        super().__init__(nombre, costo_base)

        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a 0")

        self.horas = horas

    def calcular_costo(self):
        return self.costo_base * self.horas


# Servicio de Equipos
class ServicioEquipo(Servicio):

    def __init__(self, nombre, costo_base, cantidad):
        super().__init__(nombre, costo_base)

        if cantidad <= 0:
            raise ErrorServicio("La cantidad debe ser mayor a 0")

        self.cantidad = cantidad

    def calcular_costo(self):
        return self.costo_base * self.cantidad


# Servicio de Asesoría
class ServicioAsesoria(Servicio):

    def __init__(self, nombre, costo_base, horas):
        super().__init__(nombre, costo_base)

        if horas <= 0:
            raise ErrorServicio("Las horas deben ser mayores a 0")

        self.horas = horas

    def calcular_costo(self):
        return self.costo_base * self.horas * 1.2