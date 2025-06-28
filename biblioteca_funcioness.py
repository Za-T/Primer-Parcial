

#----------------VALIDACIONES----------------

def validar_int (valor: str, desde: int, hasta: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    entero = int (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while entero < desde or entero > hasta:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return entero

def validar_str (valor: str, op1: str, op2: str, op3: str = None) -> str:

    '''Validar que la cadena de caracteres ingresada sea correcta'''

    if op3 != None:
        cadena = input (f"{valor} ({op1},{op2},{op3}): ")
        while cadena != op1 and cadena != op2 and cadena != op3:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2},{op3}): "))

    else:
        cadena = input (f"{valor} ({op1},{op2}): ")
        while cadena != op1 and cadena != op2:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

def solicitar_str (nombre_valor: str) -> str:
    '''Solicita al usuario el ingreso de una cadena y la retorna'''
    cadena = str (input (f"Ingresar {nombre_valor}: "))
    return cadena

#----------------VALIDACIONES----------------

def crear_menu (lista_opciones:list, lista_fun:list, datos: list):

    primero = 0
    ultimo = len(lista_opciones)
    
    repetir = "s"

    while repetir == "s":

        print ("\nMenu de opciones\n")
        
        for i in range(len(lista_opciones)):
            print (f"{i}. {lista_opciones[i]}")
        print ("\n")

        opcion = validar_int("opcion",primero,ultimo)

        lista_fun [opcion](datos)

        print ("\n")
        repetir = validar_str ("si quiere solicitar otra opcion", "s", "n")

#----------------VALIDACIONES----------------

def mostrar_tabla (nombre:list, nota:list):

    """ 
        Parametros:
                    producto (list): Lista de nombres/códigos de productos.
                    venta (list): Matriz con las ventas que corresponde a cada producto.

        Funcion: Muestra la lista de productos y la matriz de ventas,
                 ordenados segun trimestre.
    """

    print ("Producto # | T1 | T2 | T3 |")
    print ("--------------------------")

    for i in range (len(nombre)):

        print (f"Producto {nombre [i]} |", end = "")

        for j in range (len(nota)):
             print (f" {nota [i][j]} |", end = "")
        
        print ("\n")

#----------------VALIDACIONES----------------

def promediar_notas (datos:list):

    #por cada elemento de la lista
    for i in range (len(datos)):

        suma_notas = 0

        #por cada nota
        for j in range (len(datos [i]["notas"])):
            suma_notas += datos[i]["notas"][j]

        cant_notas = len(datos [i]["notas"])

        promedio = suma_notas // cant_notas

        datos [i]["promedio"] = promedio

def ordenar_asc_lista_dic (lista:list,key:str)->list:

    for i in range (len(lista)-1):

        for j in range (i+1, len(lista)):

            if lista [i][key] <  lista [j][key]:

                aux = lista [i]
                lista [i] = lista [j]
                lista [j] = aux                

    return lista

def auxiliar_listas (lista:list,i,j):
    aux = lista [i]
    lista [i] = lista [j]
    lista [j] = aux

#----------------VALIDACIONES----------------

def buscar_monto (producto:list, venta:list):

    """ 
        Parametros:
                    producto (list): Lista de nombres/códigos de productos.
                    venta (list): Matriz con las ventas que corresponde a cada producto.

        Funcion: Busca un valor de venta dentro de la matriz 
        y muestra en la tabla solo los valores que coinciden,
        los demas valores son representados con "--".
        
    """

    monto = validar_int ("monto", 0, 1000)

    print ("Producto # | T1 | T2 | T3 |")
    print ("--------------------------")

    for i in range (len(venta)):

        print (f"Producto {producto [i]} |", end = "")

        for j in range (len(venta[i])):

            if venta [i][j] == monto:
                print (f" {venta [i][j]} | ", end = "") 

            else:
                print (f" -- |", end = "") 

        print ("\n")

#----------------VALIDACIONES----------------