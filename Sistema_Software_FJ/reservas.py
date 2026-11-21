from datetime import datetime
from entidades import Entidad
from excepciones import ReservaError

class Reserva(Entidad):
    ESTADOS = ("Pendiente", "Confirmada", "Cancelada", "Procesada")

    def __init__(self, identificador, cliente, servicio, cantidad):
        super().__init__(identificador)
        if cliente is None or servicio is None:
            raise ReservaError("La reserva necesita un cliente y un servicio.")
        servicio.validar_disponibilidad()
        servicio.validar_parametros(cantidad)
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "Pendiente"
        self.fecha = datetime.now()
        self.costo = None

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ReservaError("Solo se pueden confirmar reservas pendientes.")
        self.estado = "Confirmada"
        return "Reserva confirmada."

    def cancelar(self):
        if self.estado not in ("Pendiente", "Confirmada"):
            raise ReservaError("No se puede cancelar esta reserva.")
        self.estado = "Cancelada"
        return "Reserva cancelada."

    def procesar(self, impuesto=0.19, descuento=0):
        if self.estado != "Confirmada":
            raise ReservaError("La reserva debe estar confirmada antes de procesarse.")
        if not 0 <= impuesto <= 1 or descuento < 0:
            raise ReservaError("Impuesto o descuento no válido.")
        self.costo = self.servicio.calcular_costo(self.cantidad, impuesto, descuento)
        self.estado = "Procesada"
        return self.costo

    def describir(self):
        return (f"Reserva {self.identificador} | Cliente: {self.cliente.nombre} | "
                f"Servicio: {self.servicio.nombre} | Estado: {self.estado}")

    def __str__(self):
        return self.describir()
