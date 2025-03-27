# Generar una lista de nombres de libros del autor Gabriel García Márquez mínimo 10 obras
# del autor, al final mostrar el nombre del libro, la cantidad de caracteres del título y remplazar
# cada letra A con la letra X mayúscula. y mostrar el resultado de las modificaciones de la lista
# original.

# Lista de libros de Gabriel García Márquez con una cantidad de 10 obras 
libros = [
    "Cien años de soledad",
    "El otoño del patriarca",
    "Crónica de una muerte anunciada",
    "El amor en los tiempos del cólera",
    "La hojarasca",
    "El general en su laberinto",
    "Memoria de mis putas tristes",
    "Los funerales de la Mamá Grande",
    "Doce cuentos peregrinos",
    "El coronel no tiene quien le escriba"
]

# Iterar sobre la lista y mostrar los resultados
for libro in libros:
    # Reemplazar "A" por "X"
    libro_modificado = libro.replace('A', 'X').replace('a', 'X')
    # Mostrar el libro original, la cantidad de caracteres y el libro modificado
    print(f"Original: {libro}")
    print(f"Cantidad de caracteres: {len(libro)}")
    print(f"Modificado: {libro_modificado}")
    print("-" * 40)
