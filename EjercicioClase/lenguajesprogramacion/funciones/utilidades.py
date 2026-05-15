# Función que busca un lenguaje dentro de la lista
# Recibe:
# - lenguajes: lista completa del JSON
# - slug: texto identificador del lenguaje, por ejemplo "python"
def buscar_lenguaje_por_slug(lenguajes, slug):

    # Recorremos uno por uno todos los lenguajes
    for lenguaje in lenguajes:

        # Si el slug coincide, devolvemos ese lenguaje
        if lenguaje["slug"] == slug:
            return lenguaje

    # Si no encuentra ninguno, devuelve None
    return None