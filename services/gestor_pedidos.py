from models import Pedido
from .persistencia import Persistencia

RUTA_PEDIDOS = "data/pedidos.json"


class GestorPedidos:
    def __init__(self):
        self.pedidos = [Pedido.from_dict(
            p) for p in Persistencia.cargar_datos(RUTA_PEDIDOS)]

    def crear_pedido(self, cliente_nombre, tipo_trabajo, cantidad, costo_unitario, tiempo):
        pedido = Pedido(cliente_nombre, tipo_trabajo,
                        cantidad, costo_unitario, tiempo)
        self.pedidos.append(pedido)
        self.guardar()
        return pedido

    def listar_pedidos(self):
        if not self.pedidos:
            print("No hay pedidos registrados.")
        for p in self.pedidos:
            print(f"- {p.cliente_nombre}: {p}")

    def guardar(self):
        Persistencia.guardar_datos(
            RUTA_PEDIDOS, [p.to_dict() for p in self.pedidos])
