# Almacenar una lista de números, identificar la longitud de la lista si es par: Los elementos
# invertir los elementos de la lista. Imprimir la lista original y lista invertida.
# Se realiza por primero una lista
lista=[]
# Se ingresa los nuermos de la lista
n = int (input("Cuantos numeros desea ingresar? "))
for i in range(n):
    Num = int(input(f"Digite el numero {i+1}: "))
    lista.append(Num)
#Se verifica si la longitud de la lista es par
longitud = len(lista)
# Se coloca otra condicional if
if longitud % 2 == 0:
    print("La longitud de la lista es par. ")
else: 
    print("La longitud de la lista es Impar")
#Ahora se inviete la lista
Listainver= lista[::-1]
# Se imprimen los resultados
print("La lista original: ",lista)
print("La lista iinvertida:",Listainver)