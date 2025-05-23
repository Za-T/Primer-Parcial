from biblioteca import *

def buscar_venta (producto:list, venta:list):

    """ 
        Parametros: ingresa la lista de productos y ventas.

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
