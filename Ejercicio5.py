# calcular la nota máxima y nota mínima de cada estudiante del curso de programación.
# Recordar que por cada estudiante al almacena 5 notas, las dos primeras son evaluaciones
# que equivalen al 30% de la nota final, la tercera y cuarta nota es de trabajos y equivale el 10%
# y la última nota es examen final que equivale al 60%. Al final por cada estudiante se debe
# mostrar su nombre, sus notas y su nota máxima y mínima. el curso está conformado por un
# total de 20 aprendices en total y con rango de notas que van de 1 al 10 en su escala.
# Se define un diciionario para almacenar las notas de los estudiantes
# Definir un diccionario para almacenar las notas de los estudiantes
estudiantes = {}

# Ingresar las notas de 20 estudiantes
for i in range(5):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    
    # Almacenar las notas de cada estudiante (5 notas)
    notas = []
    for j in range(5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {j+1} para {nombre} (entre 1 y 10): "))
                if 1 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1 y 10. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Por favor ingrese un número.")
    
    # Calcular la nota máxima, mínima y la nota final ponderada
    nota_maxima = max(notas)
    nota_minima = min(notas)
    
    # Cálculo de la nota final ponderada
    nota_final = (notas[0] + notas[1]) * 0.30 + (notas[2] + notas[3]) * 0.10 + notas[4] * 0.60
    
    # Almacenar los datos en el diccionario
    estudiantes[nombre] = {
        "notas": notas,
        "nota_maxima": nota_maxima,
        "nota_minima": nota_minima,
        "nota_final": round(nota_final, 2)
    }

# Mostrar los resultados
for nombre, datos in estudiantes.items():
    print(f"\nEstudiante: {nombre}")
    print(f"Notas: {datos['notas']}")
    print(f"Nota máxima: {datos['nota_maxima']}")
    print(f"Nota mínima: {datos['nota_minima']}")
    print(f"Nota final ponderada: {datos['nota_final']}")
