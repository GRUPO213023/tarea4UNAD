# Definición de excepciones personalizadas del sistema

# Error relacionado con validaciones de clientes
class ErrorCliente(Exception):
    pass

# Error relacionado con servicios
class ErrorServicio(Exception):
    pass

# Error relacionado con reservas
class ErrorReserva(Exception):
    pass