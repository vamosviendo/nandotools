# Herramientas de conversión

def dicttotwolists(dict):
    """ Toma un diccionario y devuelve una lista con las claves y otra 
        con los valores."""
    keylist = []
    valuelist = []
    for key, value in dict:
        keylist.add(key)
        valuelist.add(value)
    return keylist, valuelist
