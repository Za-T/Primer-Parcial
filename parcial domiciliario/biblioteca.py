def validar_int (valor: str, desde: int, hasta: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    entero = int (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while entero < desde or entero > hasta:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))
    
    return entero

def validar_str (valor: str, op1: str, op2: str) -> str:

    '''Validar que la cadena de caracteres ingresada sea correcta'''

    cadena = str((input (f"Ingrese {valor} ({op1}/{op2}): ")))

    while cadena != op1 and cadena != op2:
        cadena = (input (f"Error, respuesta ingresada no valida. Ingrese una nueva respuesta ({op1},{op2}): "))

    return cadena

def auxiliar_listas (lista:list,i:int,j:int):

    """
        Parametro: 
                    lista: cualquier list
                    i: valor de iteracion
                    j:segundo valor de iteracion
        
        Funcion: Es una funcion auxiliar para realizar la secuencia 
        interior en un ordenamiento de lista. Intercambia los elementos
        en las posiciones i y j.
    """

    aux = lista [i]
    lista [i] = lista [j]
    lista [j] = aux        