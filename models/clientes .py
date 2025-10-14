class Cliente:
    """
    Representa un cliente de la imprenta.
    """
    def __init__(self, nombre, tipo="ocasional"):
        self.nombre = nombre
        self.tipo = tipo  # puede ser 'frecuente' u 'ocasional'

    def to_dict(self):
        return {"nombre": self.nombre, "tipo": self.tipo}

    @staticmethod
    def from_dict(data):
        return Cliente(data["nombre"], data["tipo"])

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
