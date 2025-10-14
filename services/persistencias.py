import json
import os

class Persistencia:
    """
    Permite guardar y cargar datos desde archivos JSON.
    """
    @staticmethod
    def cargar_datos(ruta):
        if not os.path.exists(ruta):
            return []
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def guardar_datos(ruta, datos):
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

