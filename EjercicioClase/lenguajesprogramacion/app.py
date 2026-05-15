# Importamos Flask y las funciones que vamos a usar
from flask import Flask, render_template, request, redirect, url_for

# Importamos la función que carga los datos desde el JSON
from funciones.cargador import cargar_datos

# Importamos la función que busca un lenguaje por su slug
from funciones.utilidades import buscar_lenguaje_por_slug

# Creamos la aplicación Flask
app = Flask(__name__)

# Cargamos los datos una vez al iniciar la aplicación
datos_web = cargar_datos()


# Ruta inicial
# Cuando el usuario entra en "/", lo redirigimos a la página principal del proyecto
@app.route("/")
def inicio():
    return redirect(url_for("lenguajes_programacion"))


# Ruta principal de la web
# Aquí mostramos el select y, si se ha elegido un lenguaje, también su información
@app.route("/lenguajesprogramacion", methods=["GET"])
def lenguajes_programacion():

    # Recogemos el valor enviado desde el select
    # Si no viene nada, se guarda como cadena vacía
    slug = request.args.get("lenguaje", "")

    # Variable para guardar el lenguaje seleccionado
    # Al principio no hay ninguno
    lenguaje_seleccionado = None

    # Si el usuario ha elegido una opción distinta de vacío
    # buscamos ese lenguaje dentro de la lista del JSON
    if slug != "":
        lenguaje_seleccionado = buscar_lenguaje_por_slug(datos_web["lenguajes"], slug)

    # Enviamos a la plantilla:
    # - datos generales de la web
    # - listado de lenguajes para llenar el select
    # - lenguaje seleccionado para mostrar abajo su información
    # - slug actual para dejar marcada la opción elegida
    return render_template(
        "index.html",
        web=datos_web["web"],
        lenguajes=datos_web["lenguajes"],
        lenguaje_seleccionado=lenguaje_seleccionado,
        slug_actual=slug
    )


# Ruta adicional de ejemplo
# Sirve para probar rutas dinámicas con nombre y ciudad
@app.route("/saludar/<nombre>/<ciudad>")
def saludar(nombre, ciudad):
    return f"Hola {nombre}, saludos para {ciudad}. Visita la web en /lenguajesprogramacion"


# Manejador de error 404
# Si el usuario entra en una ruta que no existe, Flask mostrará esta página
@app.errorhandler(404)
def error_404(error):
    return render_template("404error.html", web=datos_web["web"]), 404


# Arranque de la aplicación en modo desarrollo
if __name__ == "__main__":
    app.run(debug=True)