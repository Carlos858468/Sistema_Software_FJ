from abc import ABC, abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidosError, ServicioNoDisponibleError

class Servicio(Entidad, ABC):
    def __init__(self, identificador, nombre, tarifa, disponible=True):
        super().__init__(identificador)
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")
        if not isinstance(tarifa, (int, float)) or tarifa <= 0:
            raise DatosInvalidosError("La tarifa debe ser un número mayor que cero.")
        self.nombre = nombre.strip()
        self.tarifa = float(tarifa)
        self.disponible = bool(disponible)

    def validar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre}' no está disponible.")

    @abstractmethod
    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def validar_parametros(self, cantidad):
        pass

    @abstractmethod
    def describir(self):
        pass

class ReservaSalas(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0 or cantidad > 12:
            raise DatosInvalidosError("La reserva de sala debe ser de 1 a 12 horas.")

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(cantidad)
        return max(0, self.tarifa * cantidad * (1 + impuesto) - descuento)

    def describir(self):
            return f"Sala: {self.nombre} - ${self.tarifa:,.0f}".replace(",", ".") + " por hora"

class AlquilerEquipos(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, int) or cantidad < 1 or cantidad > 20:
            raise DatosInvalidosError("La cantidad de equipos debe estar entre 1 y 20.")

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(cantidad)
        return max(0, self.tarifa * cantidad * (1 + impuesto) - descuento)

    def describir(self):
        return f"Equipos: {self.nombre} - ${self.tarifa:,.0f}".replace(",", ".") + " por unidad"

class AsesoriaEspecializada(Servicio):
    def validar_parametros(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad <= 0 or cantidad > 40:
            raise DatosInvalidosError("La asesoría debe durar entre 1 y 40 horas.")

    def calcular_costo(self, cantidad, impuesto=0, descuento=0):
        self.validar_disponibilidad()
        self.validar_parametros(cantidad)
        return max(0, self.tarifa * cantidad * (1 + impuesto) - descuento)

    def describir(self):
        return f"Asesoría: {self.nombre} - ${self.tarifa:,.0f}".replace(",", ".") + " por hora"
