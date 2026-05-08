from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from sistema import SistemaGestion
from logger_config import configurar_logger, LOG_FILE


def main():
    logger = configurar_logger()
    sistema = SistemaGestion(logger)

    cliente_luis = Cliente("Luis Torres", "80123456", "luis@correo.com", "3117654321")

    sistema.ejecutar_operacion(
        "Registro valido de cliente Luis",
        lambda: sistema.registrar_cliente(cliente_luis).resumen()
    )

    sistema.ejecutar_operacion(
        "Registro invalido de cliente con correo incorrecto",
        lambda: sistema.registrar_cliente(
            Cliente("Ana Gomez", "12345678", "correo-invalido", "3001234567")
        )
    )

    sistema.ejecutar_operacion(
        "Registro duplicado de cliente",
        lambda: sistema.registrar_cliente(
            Cliente("Luis Duplicado", "80123456", "otro@correo.com", "3000000000")
        )
    )

    sala = ReservaSala("Sala Creativa", 80000, 12, True)
    equipo = AlquilerEquipo("Portatiles Empresariales", 55000, "Laptop", 150000)
    asesoria = AsesoriaEspecializada("Asesoria Cloud", 120000, "Cloud", "Sofia Marin")

    sistema.ejecutar_operacion(
        "Crear servicio de sala",
        lambda: sistema.registrar_servicio(sala).describir_servicio()
    )

    sistema.ejecutar_operacion(
        "Crear servicio de alquiler de equipos",
        lambda: sistema.registrar_servicio(equipo).describir_servicio()
    )

    sistema.ejecutar_operacion(
        "Crear servicio de asesoria",
        lambda: sistema.registrar_servicio(asesoria).describir_servicio()
    )

    sistema.ejecutar_operacion(
        "Crear servicio con tarifa negativa",
        lambda: sistema.registrar_servicio(
            ReservaSala("Sala Error", -50000, 10, False)
        )
    )

    reserva_sala = sistema.ejecutar_operacion(
        "Crear reserva de sala",
        lambda: sistema.crear_reserva(cliente_luis, sala, 3)
    )

    if reserva_sala:
        sistema.ejecutar_operacion(
            "Confirmar reserva de sala",
            lambda: reserva_sala.confirmar() or reserva_sala.resumen()
        )

        sistema.ejecutar_operacion(
            "Procesar reserva de sala",
            lambda: reserva_sala.procesar(impuesto=0.19, descuento=0.10, asistentes=10)
        )

        sistema.ejecutar_operacion(
            "Cancelar reserva ya procesada",
            lambda: reserva_sala.cancelar("Cambio de planes")
        )

    sala.desactivar()

    sistema.ejecutar_operacion(
        "Reserva fallida por servicio no disponible",
        lambda: sistema.crear_reserva(cliente_luis, sala, 2).confirmar()
    )

    reserva_equipo = sistema.ejecutar_operacion(
        "Crear reserva de equipos",
        lambda: sistema.crear_reserva(cliente_luis, equipo, 5)
    )

    if reserva_equipo:
        sistema.ejecutar_operacion(
            "Procesar reserva sin confirmar",
            lambda: reserva_equipo.procesar(unidades=2)
        )

        sistema.ejecutar_operacion(
            "Confirmar y procesar reserva de equipos",
            lambda: reserva_equipo.confirmar() or reserva_equipo.procesar(
                impuesto=0.19,
                descuento=0.05,
                unidades=2
            )
        )

    sistema.ejecutar_operacion(
        "Calculo fallido por impuesto invalido",
        lambda: asesoria.calcular_costo_total(2, impuesto=1.5, modalidad="virtual")
    )

    print("\nResumen final")
    print(sistema.listar_estado())
    print(f"Logs generados en: {LOG_FILE}")


<<<<<<< HEAD
if __name__ == "__main__":
    main()
=======
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
from cliente import Cliente
from servicio import Servicio
from reserva import Reserva


# Cliente
cliente1 = Cliente("Paola")

# Servicio
servicio1 = Servicio("Sala de reuniones", 50000)

# Reserva
reserva1 = Reserva(cliente1, servicio1, 3)

reserva1.confirmar_reserva()

reserva1.mostrar_reserva()
>>>>>>> reserva
