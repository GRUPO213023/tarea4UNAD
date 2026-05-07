from EXCEPTIONS.EXCEPTIONS import ErrorCliente
from logger import registrar_log

class Cliente:

    def __init__(self, nombre, identificacion):
        try:
            self._validar_nombre(nombre)
            self._validar_identificacion(identificacion)

            self.__nombre = nombre
            self.__identificacion = identificacion

        except ErrorCliente:
            registrar_log(f"Error al crear cliente con nombre='{nombre}', id='{identificacion}'")
            raise

        else:
            print(f"Cliente '{nombre}' creado exitosamente.")

        finally:
            print(f"Proceso de creación de cliente finalizado.")

    def _validar_nombre(self, nombre):
        try:
            if not isinstance(nombre, str):
                raise TypeError("El nombre debe ser texto")
            if not nombre.strip():
                raise ValueError("El nombre no puede estar vacío o ser solo espacios")
        except (TypeError, ValueError) as error_base:
            raise ErrorCliente(
                f"Nombre inválido: {error_base}"
            ) from error_base

    def _validar_identificacion(self, identificacion):
        try:
            if not isinstance(identificacion, str):
                raise TypeError("La identificación debe ser texto")
            if not identificacion.strip():
                raise ValueError("La identificación no puede estar vacía")
            if not identificacion.strip().isalnum():
                raise ValueError("La identificación solo puede contener letras y números")
        except (TypeError, ValueError) as error_base:
            raise ErrorCliente(
                f"Identificación inválida: {error_base}"
            ) from error_base

    @property
    def nombre(self):
        return self.__nombre

    @property
    def identificacion(self):
        return self.__identificacion

    def mostrar_datos(self):
        print(f"Cliente: {self.__nombre} - ID: {self.__identificacion}")