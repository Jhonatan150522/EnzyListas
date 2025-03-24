# Almacenar dos listos de números enteros, lista1 y lista2, y generar la tercera lista con los
# siguientes criterios: Sumar el primer elemento de la lista1 con el último elemento de la lista2 y
# guardar el resultado en la lista3, luego el segundo elemento de la lista1 sumarlo con el noveno
# elemento de la lista2. Al final imprimir las tres listas.

#Se realizan las listas y dentro de ellas le pido al usuario que ingrese los numeros de la lista y 
# el rango de 5
lista1= [int(input(f"Ingrese el elemento {i + 1} de la lista 1: ")) for i in range(10)]
lista2= [int(input(f"Ingrese el elemento {i + 1} de la lista 2: "))for i in range(10)]
#Se agrega la 3 lista para almacenar los resultados
lista3 = []
# Se realiza las sumas correspondinetes
lista3.append(lista1[0] + lista2[-1]) #Primer elemento con el ultimo
lista3.append(lista1[1] + lista2[8]) #Segundo elemento con el noveno
#Se muestran las 3 listas 
print("Lista 1 ",lista1)
print("Lista 2 ",lista2)
print("Lista 3 ",lista3)
