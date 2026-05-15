from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Crear base de datos
def crear_bd():
    conexion = sqlite3.connect("sugerencias.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sugerencias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            mensaje TEXT
        )
    """)

    conexion.commit()
    conexion.close()

crear_bd()

# Página principal
@app.route("/") # http://127.0.0.1:5000/
def inicio():
    return render_template("index.html")

# Página contacto
@app.route("/contacto") # http://127.0.0.1:5000/contacto
def contacto():
    return render_template("contacto.html")

# Página sugerencias
@app.route("/sugerencias", methods=["GET", "POST"])  # http://127.0.0.1:5000/sugerencias
def sugerencias():

    if request.method == "POST":
        nombre = request.form["nombre"]
        mensaje = request.form["mensaje"]

        conexion = sqlite3.connect("sugerencias.db")
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO sugerencias (nombre, mensaje)
            VALUES (?, ?)
        """, (nombre, mensaje))

        conexion.commit()
        conexion.close()

        return "Sugerencia enviada correctamente"

    return render_template("sugerencias.html")

if __name__ == "__main__":
    app.run(debug=True)