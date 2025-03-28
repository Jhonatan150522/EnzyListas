# Crear un programa que añada números a una lista hasta que introducimos u número negativo.
# A continuación, debe crear una nueva lista igual que la anterior, pero eliminando los números
# duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.
# Inicializamos la lista
numeros = []

# Pedir números al usuario hasta que ingrese uno negativo
while True:
    numero = int(input("Ingresa un número (número negativo para terminar): "))
    if numero < 0:
        break
    numeros.append(numero)

# Crear una nueva lista sin duplicados
numeros_unicos = list(set(numeros))

# Mostrar la lista original y la lista sin duplicados
print("Lista original de números:", numeros)
print("Lista sin números duplicados:", numeros_unicos)
