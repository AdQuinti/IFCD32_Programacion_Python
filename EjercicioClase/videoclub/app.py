# IMPORTAMOS FLASK
from flask import Flask, render_template
import json

# CREAMOS LA APLICACIÓN
app = Flask(__name__)

# RUTA PRINCIPAL
@app.route("/videoclub")

def inicio():
    # ABRIMOS EL ARCHIVO JSON
    with open("peliculas.json", "r", encoding="utf-8") as archivo:

        # CARGAMOS LOS DATOS JSON
        peliculas = json.load(archivo)

    # ENVIAMOS LOS DATOS A index.html
    return render_template(
        "index.html",
        titulo="Videoclub",
        peliculas=peliculas
    )

# EJECUTAR SERVIDOR
# EJECUTAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)