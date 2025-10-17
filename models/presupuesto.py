class Presupuesto:
    """
    Calcula el presupuesto total de un pedido aplicando funciones matemáticas
    y condiciones lógicas (descuentos, márgenes, etc.).
    """

    def __init__(self, pedido, tipo_cliente="ocasional"):
        self.pedido = pedido
        self.tipo_cliente = tipo_cliente

    def calcular_total(self):
        # Costo fijo mínimo (gastos generales)
        costo_fijo = 1000

        # Costo variable proporcional
        costo_variable = self.pedido.calcular_costo_base()

        # Margen de ganancia del 20%
        margen = 0.2

        # Función principal: total = (costo_fijo + costo_variable) × (1 + margen)
        subtotal = costo_fijo + costo_variable
        total = subtotal * (1 + margen)

        # Aplicación de lógica condicional (descuento)
        if self.tipo_cliente == "frecuente" and total > 10000:
            total *= 0.9  # descuento del 10%

        return round(total, 2)

    def __str__(self):
        return (f"Presupuesto para {self.pedido.cliente_nombre}\n"
                f"  Trabajo: {self.pedido.tipo_trabajo}\n"
                f"  Cantidad: {self.pedido.cantidad}\n"
                f"  Total a cobrar: ${self.calcular_total()}")
