from biblioteca_funciones import *

# Lista de estudiantes 
estudiantes = ["Ana", "Bruno", "Carla", "Diego"]

# Matriz de calificaciones por estudiante 
#[matemática, historia, biología]
calificaciones = [
    [9, 8, 10],    # Ana
    [6, 7, 8],     # Bruno
    [10, 10, 9],   # Carla
    [7, 6, 5]      # Diego
]

lista_opciones = ["Mostrar la lista de estudiantes y la matriz de calificaciones.", 
  "Ordenar a los estudiantes de mayor a menor según su promedio general.", 
  "Buscar un estudiante por nombre y mostrar sus calificaciones. ",
  "Buscar una calificación en la matriz y mostrar a qué estudiante y materia pertenece." ]

lista_fun = [mostrar_estudiantes, ordenar_lista_segun_promedio, buscar_estudiante, buscar_nota]


