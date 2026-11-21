from abc import ABC, abstractmethod
from datetime import datetime


class Entidad(ABC):
    """Clase abstracta común para las entidades del sistema."""

    def __init__(self, identificador):
        if identificador is None or str(identificador).strip() == "":
            raise ValueError("El identificador es obligatorio.")
        self._identificador = str(identificador).strip()
        self.fecha_registro = datetime.now()

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def describir(self):
        """Cada entidad debe implementar su descripción."""
        pass
