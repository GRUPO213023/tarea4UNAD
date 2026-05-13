from exceptions import DatosInvalidosError, SistemaGestionError
from reserva import Reserva


class SistemaGestion:
    def __init__(self, logger):
        self._clientes = []
        self._servicios = []
        self._reservas = []
        self._logger = logger

    def ejecutar_operacion(self, descripcion, operacion):
        print(f"\nOperacion: {descripcion}")

        try:
            self._logger.info(f"Inicia operacion: {descripcion}")
            resultado = operacion()

        except SistemaGestionError as error:
            self._logger.exception(f"Error controlado en '{descripcion}': {error}")
            print(f"  Error controlado: {error}")

            if error.__cause__:
                print(f"  Causa original: {error.__cause__}")

            return None

        except Exception as error:
            self._logger.exception(f"Error inesperado en '{descripcion}': {error}")
            print(f"  Error inesperado: {error}")
            return None

        else:
            self._logger.info(f"Operacion exitosa: {descripcion}")
            print(f"  Exito: {resultado}")
            return resultado

        finally:
            self._logger.info(f"Finaliza operacion: {descripcion}")

    def registrar_cliente(self, cliente):
        for existente in self._clientes:
            if existente.documento == cliente.documento:
                raise DatosInvalidosError("Ya existe un cliente con ese documento.")

        self._clientes.append(cliente)
        return cliente

    def registrar_servicio(self, servicio):
        for existente in self._servicios:
            if existente.nombre.lower() == servicio.nombre.lower():
                raise DatosInvalidosError("Ya existe un servicio con ese nombre.")

        self._servicios.append(servicio)
        return servicio

    def crear_reserva(self, cliente, servicio, duracion):
        if cliente not in self._clientes:
            raise DatosInvalidosError("El cliente debe estar registrado.")

        if servicio not in self._servicios:
            raise DatosInvalidosError("El servicio debe estar registrado.")

        reserva = Reserva(cliente, servicio, duracion)
        self._reservas.append(reserva)
        return reserva

    def listar_estado(self):
        return (
            f"Clientes: {len(self._clientes)} | "
            f"Servicios: {len(self._servicios)} | "
            f"Reservas: {len(self._reservas)}"
        )