
from biblioteca import validar_str

def buscar_prd_nombre (producto:list, venta:list):

    """ 
        Parametros:
                    producto (list): Lista de nombres/códigos de productos.
                    venta (list): Matriz con las ventas que corresponde a cada producto.

        Funcion: Buscar un producto por nombre y mostrar sus ventas. 
        
    """

    flag = "s"

    nombre = input ("Ingrese nombre de producto: ")
    
    for i in range (len(producto)):
            
        if flag == "s":

            if producto [i] == nombre:

                print ("Producto # | T1 | T2 | T3 |")            
                print ("--------------------------")

                print (f"Producto {producto [i]} |", end = "")

                for j in range (len(venta)):
                    print (f" {venta [i][j]} |", end = "")

                reintento = "n"
                flag = "n"
             
            elif i == (len(producto)-1):

                print ("Ese producto no existe.")

                reintento = validar_str ("si quiere probar otro nombre","s","n")
                
                if reintento == "s":
                    buscar_prd_nombre (producto, venta)
        
    print ("\n")