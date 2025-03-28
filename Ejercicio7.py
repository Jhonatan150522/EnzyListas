# De las listas trabajadas en el ejercicio #2, ingresar nuevos elementos a estas listas en
# diferentes posiciones y mostrar al final la nueva lista modificada
lista=[2,6,7,4,8,2,8,]
listaO=[2,6,7,4,8,2,8,]
# Se ingresa los nuermos de la lista
n = int (input("Cuantos numeros desea ingresar? "))#Se toma una variable para saber la cantidad de numeros
print ("-"*40)
for i in range(n): # se agrega un for para almacenar y agregar 
    Num = int(input(f"Digite el numero {i+1}: ")) #Se hace una variable para saber que cantidad ingresa el usuario
    posicion= int(input("DIgite la posicion deseada: "))# Esta variable se utiliza para saber donde querremos agregar elemento

lista.insert(posicion, Num)#Esta es la lista modifica donde se agrega el numero a la diferente posicion 
#Se muestran los resultado
print("-"*40)
print("Esta es la lista original",listaO)
print("La lista modificada es esta: ", lista)
