from cliente import Cliente
from servicio import ServicioSala
from reserva import Reserva
from logger import registrar_log

print("Sistema de gestión iniciado")

try:
    # Datos del cliente
    nombre = input("Ingrese el nombre del cliente: ")
    identificacion = input("Ingrese la identificación: ")

    cliente = Cliente(nombre, identificacion)

    # Datos del servicio
    nombre_servicio = input("Nombre del servicio: ")
    costo = float(input("Costo base: "))
    horas = int(input("Horas: "))

    servicio = ServicioSala(nombre_servicio, costo, horas)

    # Crear reserva
    reserva = Reserva(cliente, servicio)
    reserva.confirmar()

    reserva.mostrar_reserva()

except Exception as e:
    print("Error:", e)
    registrar_log(f"Error: {e}")

finally:
    print("El sistema sigue funcionando ")