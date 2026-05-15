from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# CREAR BASE DE DATOS
def crear_bd():
    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni TEXT UNIQUE,
        nombre TEXT,
        telefono TEXT,
        direccion TEXT
    )
    """)

    conexion.commit()
    conexion.close()

# Ejecutar al iniciar
crear_bd()


# PÁGINA PRINCIPAL
@app.route("/") # indicación ruta http://127.0.0.1:5000/
@app.route("/panelcliente") # indicación ruta http://127.0.0.1:5000/panelcliente
def inicio():
    return render_template("index.html")



# AGREGAR CLIENTE
@app.route("/agregar", methods=["GET", "POST"])
def agregar():

    if request.method == "POST":

        dni = request.form["dni"]
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        direccion = request.form["direccion"]

        conexion = sqlite3.connect("database.db")
        cursor = conexion.cursor()

        try:
            cursor.execute("""
            INSERT INTO clientes (dni, nombre, telefono, direccion)
            VALUES (?, ?, ?, ?)
            """, (dni, nombre, telefono, direccion))

            conexion.commit()

        except:
            return "Ese DNI ya existe"

        finally:
            conexion.close()

        return redirect("/lista")

    return render_template("agregar.html")



# VER TODOS LOS CLIENTES
@app.route("/lista")
def lista():

    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM clientes")

    clientes = cursor.fetchall()

    conexion.close()

    return render_template("lista.html", clientes=clientes)



# BUSCAR CLIENTE
@app.route("/buscar", methods=["GET", "POST"])
def buscar():

    cliente = None

    if request.method == "POST":

        dni = request.form["dni"]

        conexion = sqlite3.connect("database.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM clientes WHERE dni = ?", (dni,))

        cliente = cursor.fetchone()

        conexion.close()

    return render_template("buscar.html", cliente=cliente)



# BORRAR CLIENTE
@app.route("/borrar/<int:id>")
def borrar(id):

    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))

    conexion.commit()
    conexion.close()

    return redirect("/lista")



# INICIAR SERVIDOR
if __name__ == "__main__":
    app.run(debug=True)