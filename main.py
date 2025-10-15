import sys
import os
# Arregla la ruta para que Python encuentre 'models' y 'services'
sys.path.append(os.path.dirname(os.path.abspath(__file__))) 

from models import Cliente
from services import GestorClientes, GestorPedidos, GestorPresupuestos 


def menu():
    print("\n=== SOFTGRAPH - Sistema de Imprenta ===")
    print("1. Registrar cliente")
    print("2. Registrar pedido")
    print("3. Listar clientes")
    print("4. Listar pedidos")
    print("5. Generar presupuesto")
    print("0. Salir")
    return input("Elija una opción: ")

def main():
    clientes = GestorClientes()
    pedidos = GestorPedidos()
    presupuestos = GestorPresupuestos()

    while True:
        opcion = menu()

        if opcion == "1":
            nombre = input("Nombre del cliente: ")
            tipo = input("Tipo (frecuente/ocasional): ").lower() or "ocasional"
            clientes.agregar_cliente(nombre, tipo)
            print("Cliente agregado correctamente.")

        elif opcion == "2":
            cliente_nombre = input("Nombre del cliente: ")
            if not clientes.buscar_por_nombre(cliente_nombre):
                print("❌ Cliente no encontrado.")
                continue
            tipo_trabajo = input("Tipo de trabajo: ")
            cantidad = int(input("Cantidad: "))
            costo_unitario = float(input("Costo unitario ($): "))
            tiempo = float(input("Tiempo estimado (hs): "))
            pedidos.crear_pedido(cliente_nombre, tipo_trabajo, cantidad, costo_unitario, tiempo)
            print("Pedido registrado correctamente.")

        elif opcion == "3":
            clientes.listar_clientes()

        elif opcion == "4":
            pedidos.listar_pedidos()

        elif opcion == "5":
            cliente_nombre = input("Cliente: ")
            pedido_encontrado = None
            for p in pedidos.pedidos:
                if p.cliente_nombre.lower() == cliente_nombre.lower():
                    pedido_encontrado = p
                    break
            if not pedido_encontrado:
                print("❌ Pedido no encontrado.")
                continue

            cliente = clientes.buscar_por_nombre(cliente_nombre)
            presupuesto = presupuestos.generar_presupuesto(pedido_encontrado, cliente.tipo)
            print("\n" + str(presupuesto))

        elif opcion == "0":
            print("💾 Guardando y saliendo... ¡Hasta luego!")
            break

        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()