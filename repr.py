# Herramientas de representación de tipos

def reprdict(diccionario):
    ''' Devuelve la representación de un diccionario''' 
    r = '{'
    c = 0
    for clave, valor in diccionario.items():
        c += 1
        r += f'{clave}: {valor}'
        if c < len(diccionario):
            r += ', '
    r += '}'
    return r


def reprdictvert(diccionario):
    ''' Devuelve la representación vertical de un diccionario, en forma
        vertical:
    
        {
         clave1: valor1,
         clave2: valor2,
         clave3: valor3,
         ...,
        }
    
    '''
    r = '{\n'
    for clave, valor in diccionario.items():
        r += f' {clave}: {valor},\n'
    r += '}'
    return r


def reprlist(lista):
    ''' Devuelve la representación de una lista'''
    r = '['
    for item in lista:
        r += f'{item}'
        if lista.index(item) < len(lista)-1:
            r += ', '
    r += ']'
    return r


def reprlistvert(lista):
    ''' Devuelve la representación vertical de una lista, en la forma 
        
        [
         item1,
         item2,
         item3,
         ...
        ]
    '''
    r = '[\n'
    for item in lista:
        r += f' {item}'
        if lista.index(item) < len(lista)-1:
            r += ','
        r += '\n'
    r += ']'
    return r

