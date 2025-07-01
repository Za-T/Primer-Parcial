import copy
#----------------VALIDACIONES----------------

def validar_int (texto: str, minimo: int, maximo: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango
    
        Parametros:
        texto: texto que se muestra para indicarle al usuario que debe ingresar un valor.
        minimo: indica el valor minimo que se puede introducir.
        maximo: indica el valor maximo que se puede introducir.

        Retorno:
        Retorna el entero ingresado por el usuario.
        '''

    entero = int (input (f"{texto} en este rango ({minimo} - {maximo}): "))

    while entero < minimo or entero > maximo:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({minimo} - {maximo}): "))

    return entero

def solicitar_int (nombre_valor: str) -> int:

    ''' Solicita al usuario el ingreso de un número entero y lo retorna

        Parametro:
            nombre_valor: el nombre del valor a ingresar
        Retorno:
            Retorna el entero ingresado por el usuario'''
    
    entero = int(input (f"{nombre_valor}: "))
    return entero

def validar_str (texto: str, op1: str, op2: str, op3: str = None) -> str:

    '''Validar que la cadena de caracteres ingresada este disponible entre 2 o 3 opciones.

    Parametros:
        texto: Texto que se muestra para indicarle al usuario que debe ingresar un valor. 
        op1: Opcion 1 a elegir
        op2: Opcion 2 a elegir,
        op3: Opcion 3 a elegir. Se asume que esta opcion esta vacia, 
        si en los parametros reales se ingresa un valor, entonces ahi se muestra esta opcion.

    Retorno:
        Retorna la respuesta elegida dentro de las opciones validas.'''

    if op3 != None:
        cadena = input (f"{texto} ({op1},{op2},{op3}): ")
        while cadena != op1 and cadena != op2 and cadena != op3:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2},{op3}): "))

    else:
        cadena = input (f"{texto} ({op1},{op2}): ")
        while cadena != op1 and cadena != op2:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

def solicitar_str (nombre_valor: str) -> str:
    
    '''Solicita al usuario el ingreso de una cadena y la retorna.
        Parametro:
            nombre_valor: el nombre del valor a ingresar
        Retorno:
            Retorna la cadena ingresada por el usuario'''
    
    cadena = str (input (f"Ingresar {nombre_valor}: "))
    return cadena
    
#---------------- Mostrar elementos ----------------

def mostrar_estudiantes (nombres:list, calificaciones:list):
    
    '''La funcion printea el nombre de los estudiantes, y a su lado sus notas correspondientes.
        
        Parametros:
            nombres: lista de nombres que se van a imprimir.
            calificaciones: calificaciones que se van a imprimir.'''

    print ("Estudiantes y calificaciones:")

    for i in range (len(nombres)):
       
        print (f"{nombres [i]}: ", end= "")
       
        for j in range (len (calificaciones[i])):
            
            if j == (len(calificaciones[i])-1):
                print (f"{calificaciones [i][j]}", end= "")
            else:
                print (f"{calificaciones [i][j]}", end= ", ")
        
        print ("")

#---------------- Ordenar promedio ----------------

def promediar_matriz (matriz:list) -> list:

    '''La funcion recibe una matriz, y promedia los elementos de cada lista anidada.
        
        Parametros:
            matriz: recibe la matriz que va a ser promediada.
        Retorno: 
            Retorna una lista que contiene el promedio de cada fila de la matriz'''

    lista_promedio = []

    for i in range (len(matriz)):
        
        sumar_item = 0

        for j in range (len(matriz [i])):

            sumar_item += matriz [i][j]
            divisor = len(matriz [i])

        promedio = sumar_item / divisor

        lista_promedio.append(promedio)
    
    return lista_promedio

def auxiliar_listas (lista:list,i,j):

    '''Intercambia dos elementos de una lista en las posiciones indicadas.
        
        Parametros:
            lista: lista en la cual se van a intercambiar los elementos.
            i: indice del primer elemento a intercambiar.
            j: indice del segundo elemento a intercambiar.'''

    aux = lista [i]
    lista [i] = lista [j]
    lista [j] = aux

def ordenar_lista_segun_promedio (nombres:list, calificaciones:list):

    '''Ordena las listas de nombres y calificaciones segun el promedio de las calificaciones,
    de mayor a menor, y muestra el resultado.
        
        Parametros:
            nombres: lista de nombres de estudiantes.
            calificaciones: matriz de calificaciones de cada estudiante.'''

    print ("Ordenando por promedio general...")

    nombres_c = copy.deepcopy(nombres)
    calificaciones_c = copy.deepcopy(calificaciones)

    lista_promedio = promediar_matriz(calificaciones_c)

    for i in range (len(lista_promedio)-1):

        for j in range (i+1, len(lista_promedio)):

            if lista_promedio [i] <  lista_promedio [j]:
                auxiliar_listas (lista_promedio,i,j)
                auxiliar_listas (nombres_c,i,j)
                auxiliar_listas (calificaciones_c,i,j)
    
    print ("Estudiantes ordenados por promedio:")
    for i in range (len(nombres_c)):
        print (f"{nombres_c[i]}: {lista_promedio[i]}")

#---------------- Buscar cadena ----------------

def buscar_cadena (texto:str, lista:list)->list:

    '''Busca una cadena especifica en una lista y retorna las posiciones donde se encuentra.
        
        Parametros:
            valor: descripcion del valor que se solicita al usuario.
            lista: lista en la cual se va a buscar la cadena.
        Retorno:
            Retorna una lista con los indices donde se encontro la cadena.'''

    cadena = solicitar_str (texto)

    lista_posicion = []
    encontrado = False

    for i in range (len(lista)):
            if lista [i] == cadena:
                lista_posicion.append (i)
                encontrado = True

    if encontrado == False:    
        respuesta = validar_str ("No hay valor que coincida con el ingresado. Ingrese si quiere buscar otro valor", "s","n")
        if respuesta == "s":
            lista_posicion = buscar_cadena (texto, lista)
        else:
            print ("No se buscara un nuevo valor. La lista devuelta esta vacia.")
        encontrado = True

    return lista_posicion

def buscar_estudiante (nombres: list, calificaciones: list):

    '''Busca un estudiante por nombre y muestra sus calificaciones correspondientes.
        
        Parametros:
            nombres: lista de nombres de estudiantes.
            calificaciones: matriz de calificaciones de cada estudiante.'''

    list_posicion = buscar_cadena ("el nombre a buscar", nombres)

    for i in range (len(list_posicion)):

        nombre_encontrado = nombres[list_posicion[i]]
        notas_correspondientes =  calificaciones[list_posicion[i]]

        print (f"Notas de {nombre_encontrado}: {notas_correspondientes}")

#---------------- Buscar entero ----------------

def buscar_int (texto:str, lista:list)->list:

    '''Busca un entero especifico en una matriz y retorna las posiciones donde se encuentra.
        
        Parametros:
            valor: descripcion del valor que se solicita al usuario.
            lista: matriz en la cual se va a buscar el entero.
        Retorno:
            Retorna una lista con las coordenadas [fila, columna] donde se encontro el entero.'''

    entero = solicitar_int (texto)

    lista_entero = []
    encontrado = False

    for i in range (len(lista)):
            for j in range (len(lista[i])):
                if lista [i][j] == entero:
                    lista_entero.append ([i,j])
                    encontrado = True

    if encontrado == False:    
            respuesta = validar_str ("No hay valor que coincida con el ingresado. Ingrese si quiere buscar otro valor", "s","n")
            if respuesta == "s":
                lista_entero = buscar_int (texto, lista)
            else:
                print ("No se buscara un nuevo valor. La lista devuelta esta vacia.")
            encontrado = True

    return lista_entero

def buscar_nota (nombres: list, calificaciones: list):

    '''Busca una nota especifica en la matriz de calificaciones y muestra 
    el estudiante y materia correspondiente.
        
        Parametros:
            nombres: lista de nombres de estudiantes.
            calificaciones: matriz de calificaciones de cada estudiante.'''

    materias = ["Matematica", "Historia", "Biologia"]

    list_posicion = buscar_int ("Ingrese la nota a buscar", calificaciones)

    for i in range (len(list_posicion)):
        
        fila = list_posicion[i][0] 
        columna = list_posicion[i][1] 
        nota_encontrada = calificaciones[fila][columna] 
        
        print (f"Nota encontrada: {nota_encontrada} -> Estudiante: {nombres[fila]}, Materia = {materias[columna]}")