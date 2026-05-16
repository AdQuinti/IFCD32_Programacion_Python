# IMPORTAMOS FLASK
from flask import Flask, render_template
import json
from pathlib import Path

# CREAMOS LA APLICACIÓN
app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent # Obtiene la carpeta donde está guardado 

# RUTA PRINCIPAL
@app.route("/videoclub") # http://127.0.0.1:5000/videoclub

def inicio():
    ruta_json = BASE_DIR / "peliculas.json" # construye la ruta completa al JSON dentro de esa carpeta
    # ABRIMOS EL ARCHIVO JSON
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        # CARGAMOS LOS DATOS JSON
        peliculas = json.load(archivo)

    # ENVIAMOS LOS DATOS A index.html
    return render_template(
        "index.html",
        titulo="Videoclub",
        peliculas=peliculas
    )

# EJECUTAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)