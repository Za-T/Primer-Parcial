from listas import *
from biblioteca_funcioness import *

def manejar_menu (lista_opciones:list, lista_fun:list, lista1:list, lista2:list):

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

        lista_fun [opcion](lista1, lista2)

        repetir = validar_str ("\nIngrese si quiere solicitar otra opcion", "s", "n")
    
    print ("\nFin del programa.")

manejar_menu (lista_opciones, lista_fun, estudiantes, calificaciones)