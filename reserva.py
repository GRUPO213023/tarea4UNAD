<<<<<<< HEAD
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
=======
# ============================================
# SISTEMA DE GESTIÓN DE RESERVAS
# Software FJ
# ============================================


# --------------------------------------------
# EXCEPCIÓN PERSONALIZADA
# --------------------------------------------

class ReservaError(Exception):
    pass


# --------------------------------------------
# FUNCIÓN PARA REGISTRAR LOGS
# --------------------------------------------

def registrar_log(mensaje):

    with open("logs.txt", "a", encoding="utf-8") as archivo:

        archivo.write(mensaje + "\n")


# --------------------------------------------
# CLASE RESERVA
# --------------------------------------------

class Reserva:

    # Constructor
    def __init__(
        self,
        cliente,
        servicio,
        duracion,
        unidad_tiempo
    ):

        # Encapsulación
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__unidad_tiempo = unidad_tiempo
        self.__estado = "Pendiente"

    # Validar datos
    def validar_reserva(self):

        if self.__cliente.strip() == "":

            raise ReservaError(
                "El cliente no puede estar vacío"
            )

        if self.__servicio.strip() == "":

            raise ReservaError(
                "El servicio no puede estar vacío"
            )

        if self.__duracion <= 0:

            raise ReservaError(
                "La duración debe ser mayor a cero"
            )

    # Confirmar reserva
    def confirmar_reserva(self):

        try:

            self.validar_reserva()

        except ReservaError as error:

            registrar_log(
                f"ERROR EN RESERVA: {error}"
            )

            print("\n❌ ERROR:", error)

        else:

            self.__estado = "Confirmada"

            registrar_log(
                "Reserva confirmada correctamente"
            )

            print(
                "\n✅ Reserva confirmada correctamente"
            )

        finally:

            registrar_log(
                "Proceso de reserva finalizado"
            )

    # Cancelar reserva
    def cancelar_reserva(self):

        self.__estado = "Cancelada"

        registrar_log("Reserva cancelada")

        print("\n⚠️ Reserva cancelada")

    # Mostrar información
    def mostrar_reserva(self):

        print("\n================================")
        print("       INFORMACIÓN RESERVA")
        print("================================")

        print("Cliente :", self.__cliente)

        print("Servicio:", self.__servicio)

        print(
            "Duración:",
            self.__duracion,
            self.__unidad_tiempo
        )

        print("Estado  :", self.__estado)

        print("================================")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

if __name__ == "__main__":

    print("\n====================================")
    print("   SISTEMA DE GESTIÓN DE RESERVAS")
    print("            SOFTWARE FJ")
    print("====================================")

    # Solicitar cliente
    cliente = input(
        "\nIngrese el nombre del cliente: "
    )

    # Mostrar servicios
    print("\nServicios disponibles:")
    print("1. Reserva de salas")
    print("2. Alquiler de equipos")
    print("3. Asesorías especializadas")

    opcion_servicio = input(
        "\nSeleccione un servicio: "
    )

    # Validar servicio
    if opcion_servicio == "1":

        servicio = "Reserva de salas"

    elif opcion_servicio == "2":

        servicio = "Alquiler de equipos"

    elif opcion_servicio == "3":

        servicio = "Asesorías especializadas"

    else:

        print("\n❌ Servicio no válido")

        exit()

    # Mensaje según servicio
    if servicio == "Asesorías especializadas":

        mensaje_duracion = (
            "\nIngrese la duración de la asesoría: "
        )

    else:

        mensaje_duracion = (
            "\nIngrese la duración de la reserva: "
        )

    # Validar duración
    try:

        duracion = int(
            input(mensaje_duracion)
        )

    except ValueError:

        print(
            "\n❌ ERROR: Debe ingresar un número válido"
        )

        exit()

    # Unidad de tiempo
    print("\nUnidad de tiempo:")
    print("1. Horas")
    print("2. Minutos")

    opcion_unidad = input(
        "\nSeleccione una opción: "
    )

    # Validar unidad
    if opcion_unidad == "1":

        unidad_tiempo = "horas"

    elif opcion_unidad == "2":

        unidad_tiempo = "minutos"

    else:

        print("\n❌ Unidad no válida")

        exit()

    # Crear objeto reserva
    reserva1 = Reserva(
        cliente,
        servicio,
        duracion,
        unidad_tiempo
    )

    print(
        "\nLa solicitud fue registrada correctamente."
    )

    # Menú de acciones
    print("\n========== MENÚ ==========")
    print("1. Confirmar la solicitud")
    print("2. Cancelar la solicitud")
    print("==========================")

    opcion = input(
        "\nSeleccione una opción: "
    )

    # Procesar opción
    if opcion == "1":

        reserva1.confirmar_reserva()

    elif opcion == "2":

        reserva1.cancelar_reserva()

    else:

        print("\n❌ Opción inválida")

    # Mostrar resultado final
    reserva1.mostrar_reserva()

    print("\n✅ Programa finalizado")
>>>>>>> reserva
