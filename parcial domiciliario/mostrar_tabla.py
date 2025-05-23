
def mostrar_tabla (producto:list, venta:list):

    """ 
        Parametros:
                    producto (list): Lista de nombres/códigos de productos.
                    venta (list): Matriz con las ventas que corresponde a cada producto.

        Funcion: Muestra la lista de productos y la matriz de ventas,
                 ordenados segun trimestre.
    """

    print ("Producto # | T1 | T2 | T3 |")
    print ("--------------------------")

    for i in range (len(producto)):

        print (f"Producto {producto [i]} |", end = "")

        for j in range (len(venta)):
             print (f" {venta [i][j]} |", end = "")
        
        print ("\n")