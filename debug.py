# Herramientas para facilitar la depuración

MARCADOR = "###############################################################################"


def marca(titulo=''):
    """ Devuelve una cadena de '#' con un título incrustado"""
    largo = len(titulo)

    # Si el título es de más de 66 caracteres, se la recorta
    if largo > 66:
        largo = 66
        titulo = titulo[0:60]

    respuesta = "## " + titulo + " "
    for x in range(0, 75-largo):
        respuesta += "#"

    return respuesta


def mostrar(*args, marcador=MARCADOR, titulo=''):
    """ Muestra por consola los argumentos que se le pasan, rodeados por un
        marcador que los resalta, para que se vean claramente en medio de 
        todo el otro texto que salga por consola
    """
    print(marca(titulo=titulo))
    for arg in args:
        print(arg)
    print(marcador)

