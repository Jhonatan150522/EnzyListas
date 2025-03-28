# Crear dos listas la primera contendrá el nombre del usuario y la segunda lista contendrá el
# password de cada usuario. Genere una rutina de código que permita validar que los usuarios
# y password, guardados coincidan con los datos ingresados por el usuario y si es correcto
# arrojar el mensaje de usuario registrado y de lo contrario arrojar el mensaje de usuario no
# valido.
# Se agrega dos listas con datos ya agregados
nombre=["Erika", "Juan", "Carlos", "Sebastian"]
contra=["Erila123", "Ju4S", "C4rlos", "Robertiño"]
# Se va a pedir al el usuario el nombre y la contra 
N= input("Digite su nombre: ").lower()
C=input("Digite a contraseña: ").lower() 
print("*"*50)
# Se coloca una condicional if 
for i in nombre:
    if i.lower() == N:
        print(f"Se encuentra registrado {i}")
    else:
        print("No se encuentra registrado")
        
for x in contra:
    if x.lower() == C:
        print(f"Si esta la contra {x}")
    else:
        print("No se encuentra registrado")
        

