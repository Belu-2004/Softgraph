<<<<<<< HEAD
from models.Clientes import Clientes
from services.Persistencias import Persistencias
=======
from models.clientes import Cliente
from services.persistencias import Persistencia
>>>>>>> santi

RUTA_CLIENTES = "data/clientes.json"


class GestorClientes:
    def __init__(self):
        self.clientes = [Cliente.from_dict(
            c) for c in Persistencia.cargar_datos(RUTA_CLIENTES)]

    def agregar_cliente(self, nombre, tipo="ocasional"):
        cliente = Cliente(nombre, tipo)
        self.clientes.append(cliente)
        self.guardar()
        return cliente

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        for c in self.clientes:
            print(f"- {c}")

    def buscar_por_nombre(self, nombre):
        for c in self.clientes:
            if c.nombre.lower() == nombre.lower():
                return c
        return None

    def guardar(self):
        Persistencia.guardar_datos(
            RUTA_CLIENTES, [c.to_dict() for c in self.clientes])
