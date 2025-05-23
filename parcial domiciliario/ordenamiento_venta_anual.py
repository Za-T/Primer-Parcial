from biblioteca import *

def ordenar_vnt_anual (producto:list, venta:list):

    """ 
        Parametros:
                producto (list): Lista de nombres/códigos de productos.
                venta (list): Matriz con las ventas que corresponde a cada producto.

        Funcion: Suma las ventas de cada prducto, y una vez conseguido el total,
        ordena los productos de mayor a menor segun sus ventas totales.
    """

    suma_ventas_A = 0
    suma_ventas_B = 0
    suma_ventas_C = 0

    ventas_ord = [0] * (len(producto))

    for i in range (len(venta)):

        suma_ventas_A += venta [0] [i]
        
        suma_ventas_B += venta [1] [i]

        suma_ventas_C += venta [2] [i]
    
    ventas_ord [0] = suma_ventas_A
    ventas_ord [1] = suma_ventas_B
    ventas_ord [2] = suma_ventas_C

    for i in range(len(ventas_ord)-1):

        for j in range (i+1,len(ventas_ord)):

            if (ventas_ord [i] < ventas_ord[j]):

                auxiliar_listas (ventas_ord, i, j)
                auxiliar_listas (producto, i, j)
    
    print (ventas_ord, producto)

    print ("Producto # | Total |")
    print ("--------------------------")

    for i in range (len(ventas_ord)):

        print (f"Producto {producto [i]} |", end = "")

        print (f" {ventas_ord [i]} |", end = "")
        
        print ("\n")