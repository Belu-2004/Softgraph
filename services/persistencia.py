import json
import os

class Persistencia:
    @staticmethod
    def cargar_datos(ruta):
        # Si el archivo no existe, devolvemos lista vacía
        if not os.path.exists(ruta):
            return []
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
                # Si el archivo está vacío, devolvemos lista vacía
                if not contenido:
                    return []
                # Intentamos convertir el texto a estructura Python (lista o dict)
                return json.loads(contenido)
        except (json.JSONDecodeError, FileNotFoundError):
            # Si el archivo está dañado o no se puede leer, devolvemos lista vacía
            return []

    @staticmethod
    def guardar_datos(ruta, datos):
        # Guardamos los datos en formato JSON con formato legible
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
