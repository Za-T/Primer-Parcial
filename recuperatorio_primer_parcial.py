def temperatura_media_alta (temperaturas: list, umbral:int)-> bool:#parametros formales

    '''La funcion se encarga de promediar la lista de temperaturas dada, y verifica si es mayor o no al umbral.
        
        Parametros formales:
            temperaturas: lista que contiene cada entero con el grado de temperatura.
            umbral: entero que indica cual es el valor de comparacion.
            '''

    suma_temp = 0
    divisor = len(temperaturas)

    for i in range (len(temperaturas)):
        suma_temp += temperaturas[i]

    promedio_temp = suma_temp / divisor

    if promedio_temp > umbral:
        retorno = True
    else:
        retorno = False
    
    return retorno

temperaturas = [18,22,25,20,21]
umbral = 20

resultado = temperatura_media_alta (temperaturas, umbral) #invocacion y parametros actuales

print (resultado)

