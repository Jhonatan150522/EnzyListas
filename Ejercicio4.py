# generar dos listas de longitudes n y m, la primera lista ordenarla de manera ascendente y la
# segunda de manera descendente. 

# Se realizan las dos listas correspondientes que son n y m 
n =[]
m = []
#Se le pide al usuario los elemntos de la lista n
longitud_n = int(input("Ingrese la cantidad de elementos para la lista n (Maximo 5): "))
# Se agrega la condicional for
for i in range(longitud_n):
    numN= int(input(f"Ingrese el elemento {i + 1} de la lista n: "))
    n.append(numN)

# Se le pide al usuario los elemtos de la lista m
longitud_m = int(input("Ingrese la cantidad de elementos para la lista m (Maximo 5)"))
# Se agrega la condicional for
for i in range (longitud_m):
    numM = int(input(f"Ingrese el elemento {i + 1} de la lista m: "))
    m.append(numM)
# Ahora se organiza la lista de ascedente y descendente 
n.sort()
m.sort(reverse=True)
#Se muestran los resultados 
print("Lista n ordenada de manera ascendente:", n)
print("Lista m ordenada de manera descendente: ",m) 