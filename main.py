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


if __name__ == "__main__":
    main()
