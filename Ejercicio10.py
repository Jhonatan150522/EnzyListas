# Crear una lista de palabras ingresadas por teclado, e identificar si alguna de ellas es
# palíndroma o no, al final arrojar cuantas, y cuales palabras son palíndromas, y mostrar la lista
# original.
# Pedir al usuario que ingrese varias palabras separadas por espacio
entrada = input("Ingresa varias palabras separadas por espacio: ")

# Convertir la entrada en una lista de palabras
palabras = entrada.split()

# Inicializar las listas y variables
palindromas = []
contador_palindromas = 0

# Verificar si las palabras son palíndromas
for palabra in palabras:
    # Normalizamos la palabra a minúsculas y verificamos si es igual a su reverso
    if palabra.lower() == palabra[::-1].lower():
        palindromas.append(palabra)
        contador_palindromas += 1

# Mostrar los resultados
print("\nLista original de palabras:", palabras)
print("Palabras palíndromas:", palindromas)
print(f"Cantidad de palabras palíndromas: {contador_palindromas}")