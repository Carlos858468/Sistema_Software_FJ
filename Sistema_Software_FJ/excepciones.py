class ErrorSistema(Exception):
    "Error base del sistema."


class DatosInvalidosError(ErrorSistema):
    "Se genera cuando un dato no cumple las validaciones."


class ServicioNoDisponibleError(ErrorSistema):
    "Se genera cuando un servicio no está disponible."


class ReservaError(ErrorSistema):
    "Se genera cuando una operación de reserva no es válida."
