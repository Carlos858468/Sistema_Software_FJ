import re
from entidades import Entidad
from excepciones import DatosInvalidosError

class Cliente(Entidad):
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = valor.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", valor):
            raise DatosInvalidosError("El correo electrónico no es válido.")
        self.__correo = valor.strip().lower()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        numero = re.sub(r"\D", "", str(valor))
        if len(numero) < 7 or len(numero) > 15:
            raise DatosInvalidosError("El teléfono debe contener entre 7 y 15 dígitos.")
        self.__telefono = numero

    def describir(self):
        return f"Cliente {self.identificador}: {self.nombre} ({self.correo})"

    def __str__(self):
        return self.describir()