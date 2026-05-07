class SistemaGestionError(Exception):
    '''Clase base para todos los errores del sistema de gestión. '''
    pass

class DatosInvalidosError(SistemaGestionError):
    '''Error cuando los datos de un objeto no son válidos. '''
    pass

class ServicioNoDisponibleError(SistemaGestionError):
    '''Error cuando un servicio no está disponible. '''
    pass

class ReservaError(SistemaGestionError):
    '''Error cuando una reserva no es válida. '''
    pass

class OperacionNoPermitidaError(SistemaGestionError):
    '''Error cuando una operación no es permitida. '''
    pass

class CalculoCostosError(SistemaGestionError):
    '''Error cuando no se pueden calcular los costos. '''
    pass