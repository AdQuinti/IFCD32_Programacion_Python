import json
from pathlib import Path


def cargar_datos():
    ruta_base = Path(__file__).resolve().parent.parent
    ruta_json = ruta_base / "basedatos" / "datos.json"

    with open(ruta_json, "r", encoding="utf-8") as archivo:
        return json.load(archivo)