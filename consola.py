# Herramientas de consola

def inputRestr(texto, opciones, retry):
    ''' Params texto a mostrar en la solicitud de entrada
               opciones de respuesta válida
               retry: texto a mostrar ante una respuesta inválida
        Toma entrada por consola dentro de un conjunto de opciones válidas.
        Sigue insistiendo hasta que se da una respuesta válida
        Return: respuesta'''
    resp = input(texto)
    while not resp in opciones:
        resp = input(retry)
    return resp

def typed_input(mensaje, tipo=str):
    ''' Toma entrada por consola de un tipo determinado, o vuelve a preguntar
        si el tipo no es válido
        Params: mensaje a mostrar en solicitud de entrada
                tipo: tipo de entrada válido'''
    print(mensaje, end = ' ')
    while True:
        try:
            return tipo(input(mensaje))
        except:
            pass


