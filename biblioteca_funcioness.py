import copy
#----------------VALIDACIONES----------------

def validar_int (valor: str, desde: int, hasta: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    entero = int (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while entero < desde or entero > hasta:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return entero

def solicitar_int (nombre_valor: str) -> int:

    ''' Solicita al usuario el ingreso de un número entero y lo retorna'''
    entero = int(input (f"{nombre_valor}: "))
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

#---------------- MENU ----------------

def manejar_menu (lista_opciones:list, lista_fun:list, nombre:list, notas:list):

    primero = 0
    ultimo = len(lista_opciones)-1
    
    repetir = "s"

    while repetir == "s":

        print ("\nMenu de opciones\n")
        
        for i in range(len(lista_opciones)):
            print (f"{i}. {lista_opciones[i]}")
        
        print (" ")
        opcion = validar_int("opcion",primero,ultimo)
        print (" ")

        lista_fun [opcion](nombre, notas)

        repetir = validar_str ("\nIngrese si quiere solicitar otra opcion", "s", "n")
    
    print ("\nFin del programa.")
    
#---------------- Mostrar elemntos ----------------

def mostrar_listas (nombres:list, calificaciones:list):

    print ("Estudiantes y calificaciones:")

    for i in range (len(nombres)):
       print (f"{nombres [i]}: {calificaciones [i]}")

#---------------- Ordenar promedio ----------------

def promediar_notas (nombres, calificaciones) -> list:

    lista_promedio = []

    for i in range (len(nombres)):
        
        suma_notas = 0

        for j in range (len(calificaciones [i])):

            suma_notas += calificaciones [i][j]
            divisor = len(calificaciones [i])

        promedio = suma_notas / divisor

        lista_promedio.append(promedio)
    
    return lista_promedio

def auxiliar_listas (lista:list,i,j):
    aux = lista [i]
    lista [i] = lista [j]
    lista [j] = aux

def ordenar_lista_segun_promedio (nombres:list, calificaciones:list):

    print ("Ordenando por promedio general...")

    nombres_c = copy.deepcopy(nombres)
    calificaciones_c = copy.deepcopy(calificaciones)

    lista_promedio = promediar_notas(nombres_c, calificaciones_c)

    for i in range (len(lista_promedio)-1):

        for j in range (i+1, len(lista_promedio)):

            if lista_promedio [i] <  lista_promedio [j]:
                auxiliar_listas (lista_promedio,i,j)
                auxiliar_listas (nombres_c,i,j)
                auxiliar_listas (calificaciones_c,i,j)
    
    print ("Estudiantes ordenados por promedio:")
    for i in range (len(nombres)):
        print (f"{nombres_c[i]}: {lista_promedio[i]}")

#---------------- Buscar cadena ----------------

def buscar_cadena (valor:str, lista:list)->list:

    cadena = solicitar_str (valor)

    lista_cadena = []
    encontrado = "n"

    for i in range (len(lista)):
            if lista [i] == cadena:
                lista_cadena.append (i)
                encontrado = "s"

    while encontrado == "n":    
        if len(lista_cadena) == 0:
            respuesta = validar_str ("No hay valor que coincida con el ingresado. Ingrese si quiere buscar otro valor", "s","n")
            if respuesta == "s":
                lista_cadena = buscar_cadena (valor, lista)
            else:
                print ("No se buscara un nuevo valor. La lista devuelta esta vacia.")
            encontrado = "s"

    return lista_cadena

def buscar_estudiante (nombres: list, calificaciones: list):

    list_posicion = buscar_cadena ("el nombre a buscar", nombres)

    for i in range (len(list_posicion)):
            print (f"Notas de {nombres[list_posicion[i]]}: {calificaciones[list_posicion[i]]}")

#---------------- Buscar monto ----------------

def buscar_int (valor:str, lista:list)->list:

    entero = solicitar_int (valor)

    lista_entero = []
    encontrado = "n"

    for i in range (len(lista)):
            for j in range (len(lista[i])):
                if lista [i][j] == entero:
                    lista_entero.append ([i,j])
                    encontrado = "s"

    while encontrado == "n":    
        if len(lista_entero) == 0:
            respuesta = validar_str ("No hay valor que coincida con el ingresado. Ingrese si quiere buscar otro valor", "s","n")
            if respuesta == "s":
                lista_entero = buscar_int (valor, lista)
            else:
                print ("No se buscara un nuevo valor. La lista devuelta esta vacia.")
            encontrado = "s"

    return lista_entero

def buscar_nota (nombres: list, calificaciones: list):

    materias = ["Matematica", "Historia", "Biologia"]

    list_posicion = buscar_int ("Ingrese la nota a buscar", calificaciones)

    for i in range (len(list_posicion)):
        
        fila = list_posicion[i][0]  # Índice del estudiante
        columna = list_posicion[i][1]  # Índice de la materia
        nota_encontrada = calificaciones[fila][columna]  # Obtener la nota específica
        
        print (f"Nota encontrada: {nota_encontrada} -> Estudiante: {nombres[fila]}, Materia = {materias[columna]}")