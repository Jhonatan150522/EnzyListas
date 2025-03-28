# Convertir cada elemento guardado en la lista del ejercicio #6, en mayúsculas y minúsculas,
# Al final mostrar en pantalla el listado original y luego los dos nuevos listados respectivamente.
# Se trae la lista del punto 6 
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
librosMayu=[libros.upper()for libros in libros]
librosMinus=[libros.lower()for libros in libros]
# Mostrar los tres listados
print("-"*100)
print("Listado original:")
print(libros)
print("-"*100)

print("-"*100)
print("\nListado en mayúsculas:")
print(librosMayu)
print("-"*100)

print("-"*100)
print("\nListado en minúsculas:")
print(librosMinus)
print("-"*100)
