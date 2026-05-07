from abc import abstractmethod

from entidades import EntidadSistema
from exceptions import DatosInvalidosError, ServicioNoDisponibleError, CalculoCostosError


class Servicio(EntidadSistema):
    def __init__(self, nombre, tarifa_base, disponible=True):
        super().__init__(nombre)
        self.tarifa_base = tarifa_base
        self._disponible = disponible

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise DatosInvalidosError("La tarifa base debe ser positiva.")
        self._tarifa_base = float(valor)

    @property
    def disponible(self):
        return self._disponible

    def activar(self):
        self._disponible = True

    def desactivar(self):
        self._disponible = False

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre}' no esta disponible.")

    def calcular_costo_total(self, duracion, impuesto=0.0, descuento=0.0, **opciones):
        try:
            self.validar_parametros(duracion, **opciones)
            subtotal = self.calcular_costo(duracion, **opciones)

            if not 0 <= impuesto <= 1:
                raise ValueError("El impuesto debe estar entre 0 y 1.")

            if not 0 <= descuento <= 1:
                raise ValueError("El descuento debe estar entre 0 y 1.")

            total = subtotal * (1 + impuesto) * (1 - descuento)
            return round(total, 2)

        except (DatosInvalidosError, ServicioNoDisponibleError):
            raise
        except Exception as error:
            raise CalculoCostosError("No fue posible calcular el costo.") from error

    @abstractmethod
    def validar_parametros(self, duracion, **opciones):
        pass

    @abstractmethod
    def calcular_costo(self, duracion, **opciones):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    def resumen(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} | Tarifa: ${self.tarifa_base} | {estado}"


class ReservaSala(Servicio):
    def __init__(self, nombre, tarifa_base, capacidad, incluye_video_beam):
        super().__init__(nombre, tarifa_base)

        if capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser positiva.")

        self.capacidad = capacidad
        self.incluye_video_beam = incluye_video_beam

    def validar_parametros(self, duracion, **opciones):
        self.validar_disponibilidad()

        asistentes = opciones.get("asistentes", 1)

        if duracion <= 0 or duracion > 12:
            raise DatosInvalidosError("La duracion de sala debe estar entre 1 y 12 horas.")

        if asistentes > self.capacidad:
            raise DatosInvalidosError("Los asistentes superan la capacidad de la sala.")

    def calcular_costo(self, duracion, **opciones):
        recargo = 25000 if self.incluye_video_beam else 0
        return self.tarifa_base * duracion + recargo

    def describir_servicio(self):
        return f"Sala para {self.capacidad} personas."


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, tarifa_base, tipo_equipo, garantia):
        super().__init__(nombre, tarifa_base)

        if garantia < 0:
            raise DatosInvalidosError("La garantia no puede ser negativa.")

        self.tipo_equipo = tipo_equipo
        self.garantia = garantia

    def validar_parametros(self, duracion, **opciones):
        self.validar_disponibilidad()

        unidades = opciones.get("unidades", 1)

        if duracion <= 0 or duracion > 30:
            raise DatosInvalidosError("El alquiler debe durar entre 1 y 30 dias.")

        if unidades <= 0:
            raise DatosInvalidosError("Las unidades deben ser positivas.")

    def calcular_costo(self, duracion, **opciones):
        unidades = opciones.get("unidades", 1)
        return self.tarifa_base * duracion * unidades + self.garantia

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.tipo_equipo}"


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, tarifa_base, area, consultor):
        super().__init__(nombre, tarifa_base)
        self.area = area
        self.consultor = consultor

    def validar_parametros(self, duracion, **opciones):
        self.validar_disponibilidad()

        modalidad = opciones.get("modalidad", "virtual")

        if duracion <= 0 or duracion > 8:
            raise DatosInvalidosError("La asesoria debe durar entre 1 y 8 horas.")

        if modalidad not in ["virtual", "presencial"]:
            raise DatosInvalidosError("La modalidad debe ser virtual o presencial.")

    def calcular_costo(self, duracion, **opciones):
        modalidad = opciones.get("modalidad", "virtual")
        recargo = 60000 if modalidad == "presencial" else 0
        return self.tarifa_base * duracion + recargo

    def describir_servicio(self):
        return f"Asesoria en {self.area} con {self.consultor}"
