from datetime import datetime
#logger
def registrar_log(mensaje):
    with open("logs.txt", "a") as archivo:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha}] {mensaje}\n")