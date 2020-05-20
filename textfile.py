def contar_caracteres(archivo):
    """
    Devuelve la cantidad de caracteres de un archivo de texto
    :param archivo:
    :return int:
    """
    cadena = ''
    with open(archivo, 'r') as arch:
        for line in arch:
            cadena += line
    return len(cadena)