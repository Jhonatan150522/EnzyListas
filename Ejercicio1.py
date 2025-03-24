#Almacenar en una lista 15 números e imprimir cuantos son ceros, negativos, positivos, además
# imprimir la suma de números positivos y suma de números negativos.
# Se inician las variables cuando sea (Ceros, negativos, positivos)
cero = 0
posiitivos = 0
negativos  = 0
#se hacen los contadores y acumuladores para dar el resultado de los positivos y negativo
SumaPos= 0
SumaNega= 0
# Se agrega la lista para almacenar los datos
lista= []
# Se utiliza la condicional for que se va a utilizar paran almacenar los datos
for i in range(0,5,1):
    Num=int(input("Digite los valores: "))
    lista.append(Num)
# Se agrega otro for para poder realizar las operaciones Segun sean lo datos
for x in lista:
    if x < 0:
        negativos += 1
        SumaNega= SumaNega - x
    elif x > 0:
        posiitivos += 1
        SumaPos= SumaPos + x
    else:
        cero += 1
# Se muestran los resultados
print(f"La cantida de Ceros: {cero}")
print(f"Cantidad de numeros negativos: {negativos}")
print(f"Cantidad de numeros Positivos: {posiitivos}")
print(f"Suma de los numeros Positivos: {SumaPos}")
print(f"Suma de los numeros negativos: {SumaNega}")