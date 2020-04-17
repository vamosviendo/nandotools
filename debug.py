# Herramientas para facilitar la depuración

MARCADOR = "###############################################################################"

def mostrar(*args, marcador=MARCADOR):
    """ Muestra por consola los argumentos que se le pasan, rodeados por un
        marcador que los resalta, para que se vean claramente en medio de 
        todo el otro texto que salga por consola
    """
    print(MARCADOR)
    for arg in args:
        print(arg)
    print(MARCADOR)

