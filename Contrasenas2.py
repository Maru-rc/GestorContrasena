intentos = 0
especial = None
numero = None
mayus = None 
while intentos != 4:
    if intentos == 3:
        print("Numero maximo de intentos alcanzado")
        break
    Contrasena = input("Ingresa una contraseña: ")

    for i in Contrasena:
        if i.isupper():
            mayus = True

        elif i.isdigit():
            numero = True
        
        elif i.isalnum() == False:
            especial = True
        
    if len(Contrasena) < 8 and (mayus == None and numero == None and especial == None):
        intentos += 1
        print(f"Por favor, ingresa una mayuscula, un numero o un caracter especial \n" if intentos !=3 else ("Numero maximo de intentos alcanzado"))
        if intentos == 3:
            break

    if len(Contrasena) >=8 and (mayus == True and numero == True or mayus == True and especial == True or numero == True and especial == True):
        print("Contraseña guardada, nivel de seguridad alto!")
        break

    if len(Contrasena) >= 8 and (mayus == True and numero == True and especial == True):
        print("Contraseña guardada, nivel de extremadamente alto")
        break

    if len(Contrasena) >= 8 and (mayus == True or numero == True or especial == True):
        print("Contraseña guardada correctamente! nivel de seguridad bajo")
        break