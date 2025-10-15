from models import Presupuesto


class GestorPresupuestos:
    def generar_presupuesto(self, pedido, tipo_cliente):
        return Presupuesto(pedido, tipo_cliente)
