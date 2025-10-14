class Pedido:
    """
    Representa un pedido de impresión.
    """
    def __init__(self, cliente_nombre, tipo_trabajo, cantidad, costo_unitario, tiempo_estimado):
        self.cliente_nombre = cliente_nombre
        self.tipo_trabajo = tipo_trabajo
        self.cantidad = cantidad
        self.costo_unitario = costo_unitario
        self.tiempo_estimado = tiempo_estimado  # en horas

    def calcular_costo_base(self):
        # Proporcionalidad directa: costo = cantidad × costo_unitario
        return self.cantidad * self.costo_unitario

    def to_dict(self):
        return {
            "cliente_nombre": self.cliente_nombre,
            "tipo_trabajo": self.tipo_trabajo,
            "cantidad": self.cantidad,
            "costo_unitario": self.costo_unitario,
            "tiempo_estimado": self.tiempo_estimado
        }

    @staticmethod
    def from_dict(data):
        return Pedido(**data)

    def __str__(self):
        return f"{self.tipo_trabajo} x{self.cantidad} (${self.costo_unitario}/u)"
