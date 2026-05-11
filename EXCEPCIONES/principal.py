from abc import ABC, abstractmethod

print("Sistema de gestión iniciado")


# Función para guardar errores en un archivo txt
def registrar_log(error):

    archivo = open("errores.txt", "a")

    archivo.write(error + "\n")

    archivo.close()


# Excepciones personalizadas
class ServicioError(Exception):
    pass


class DatoInvalidoError(ServicioError):
    pass


# Clase Cliente
class Cliente:

    def __init__(self, nombre, identificacion):

        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        if not identificacion:
            raise ValueError("La identificación no puede estar vacía")

        self.nombre = nombre
        self.identificacion = identificacion

    # Mostrar datos del cliente
    def mostrar_datos(self):
        print("Cliente:", self.nombre, "- ID:", self.identificacion)


# Clase abstracta Servicio
class Servicio(ABC):

    def __init__(self, nombre, costo_base):

        if not nombre:
            raise DatoInvalidoError(
                "El nombre del servicio no puede estar vacío"
            )

        if costo_base <= 0:
            raise DatoInvalidoError(
                "El costo base debe ser mayor a 0"
            )

        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Servicio Sala
class ServicioSala(Servicio):

    def __init__(self, nombre, costo_base, horas):

        super().__init__(nombre, costo_base)

        if horas <= 0:
            raise DatoInvalidoError(
                "Las horas deben ser mayores a 0"
            )

        self.horas = horas

    # Calcular costo
    def calcular_costo(self, descuento=0):

        try:
            costo = self.costo_base * self.horas
            costo -= costo * descuento
            return costo

        except Exception as e:
            raise ServicioError(
                f"Error en ServicioSala: {e}"
            )

    # Descripción del servicio
    def descripcion(self):
        return f"Sala reservada por {self.horas} horas"


# Clase Reserva
class Reserva:

    def __init__(self, cliente, servicio):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "pendiente"

    # Confirmar reserva
    def confirmar(self):
        self.estado = "confirmada"

    # Mostrar reserva
    def mostrar_reserva(self):

        print("\n===== RESERVA =====")
        print("Cliente:", self.cliente.nombre)
        print("Servicio:", self.servicio.nombre)
        print("Estado:", self.estado)
        print("Costo:", self.servicio.calcular_costo())


# =========================
# PROGRAMA PRINCIPAL
# =========================

while True:

    try:

        # Nombre cliente
        while True:

            nombre = input(
                "Ingrese el nombre del cliente: "
            )

            if not nombre:
                print("Error: el nombre no puede estar vacío")
                registrar_log(
                    "Error: nombre vacío"
                )
            else:
                break

        # Identificación
        while True:

            identificacion = input(
                "Ingrese la identificación: "
            )

            if not identificacion:
                print(
                    "Error: la identificación no puede estar vacía"
                )

                registrar_log(
                    "Error: identificación vacía"
                )

            else:
                break

        cliente = Cliente(
            nombre,
            identificacion
        )

        # Nombre servicio
        while True:

            nombre_servicio = input(
                "Nombre del servicio: "
            )

            if not nombre_servicio:

                print(
                    "Error: el nombre del servicio está vacío"
                )

                registrar_log(
                    "Error: servicio vacío"
                )

            else:
                break

        # Costo
        while True:

            costo_input = input("Costo base: ")

            if not costo_input:

                print(
                    "Error: el costo no puede estar vacío"
                )

                registrar_log(
                    "Error: costo vacío"
                )

            else:

                costo = float(costo_input)

                if costo <= 0:

                    print(
                        "Error: el costo debe ser mayor a 0"
                    )

                    registrar_log(
                        "Error: costo inválido"
                    )

                else:
                    break

        # Horas
        while True:

            horas_input = input("Horas: ")

            if not horas_input:

                print(
                    "Error: las horas no pueden estar vacías"
                )

                registrar_log(
                    "Error: horas vacías"
                )

            else:

                horas = int(horas_input)

                if horas <= 0:

                    print(
                        "Error: las horas deben ser mayores a 0"
                    )

                    registrar_log(
                        "Error: horas inválidas"
                    )

                else:
                    break

        # Crear servicio
        servicio = ServicioSala(
            nombre_servicio,
            costo,
            horas
        )

        # Crear reserva
        reserva = Reserva(
            cliente,
            servicio
        )

        # Confirmar reserva
        reserva.confirmar()

        # Mostrar datos
        reserva.mostrar_reserva()

        # Finaliza el programa si todo salió bien
        break

    except Exception as e:

        print("\nOcurrió un error:", e)

        registrar_log(str(e))