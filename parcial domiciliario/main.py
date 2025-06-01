
from biblioteca import *
from mostrar_tabla import *
from ordenamiento_venta_anual import *
from buscar_producto_nombre import *
from buscar_monto_venta import *
from datos import *   


repetir = "s"

while repetir == "s":

    print ("\n--- MENU DE OPCIONES---\n" \
            "1. Mostrar productos y ventas\n" \
            "2. Ordenar productos por ventas anuales (desc)\n" \
            "3. Buscar productos por nombre\n" \
            "4. Buscar monto de venta en la matriz\n" \
            "5. Salir\n")

    seleccionar = validar_int ("opcion",1,5)

    match seleccionar:

        case 1:
            mostrar_tabla (productos, ventas)

        case 2:
            ordenar_vnt_anual (productos_dup, venta_dup)

        case 3:
            buscar_prd_nombre (productos, ventas)

        case 4: 
            buscar_monto (productos, ventas)

        case 5:
            repetir = "n"
    
    if seleccionar != 5:
        repetir = validar_str ("si quiere elegir otra opcion","s","n")

