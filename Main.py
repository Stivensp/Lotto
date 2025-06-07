#Imports
import json
import os
#---------------Globables--------------#
userIndex = None  #inidice del usuario en la base de datos
ruta="data.json"
baseDatos = []
menu = 0

#---------------Menu------------------·
menuLogin = """

    █░░ █▀█ ▀█▀ █▀▀ █▀█ █ ▄▀█
    █▄▄ █▄█ ░█░ ██▄ █▀▄ █ █▀█

    1. Registrarse
    2. Iniciar sesion.
    
"""



#----------------Funciones-------------#
def asignarId(idd):
    with open(ruta, "r") as file:
        data = json.load(file)
    
    if len(data) > 0:
        for i in data:
            if i["id"] == idd:
                idd += 1
            else:
                idd = idd
                break
    else:
        idd = 1
    return idd

def printTitle(title):
    print(f"======= {title} =======")

def limpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def printError(msg, error):
    print(f"\n [Error] {error} \n {msg}")

def registrarse(): 
    printTitle("Registrarse")
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            data = json.load(file)
            baseDatos = data
    except json.JSONDecodeError as e:
        printError("Error al cargar los datos", e)
    
    userName = input("Ingrese el nombre de usuario: ") 
    for i in data:
        userData = i["user"]
        
    if userName != userData:# ------------------------------------------------------ verifica si el usuario ya existe
        if userName.count(" ") < 1:# ----------------------------------------------- verifica si el nombre de usuario no contiene espacios
            password = input("Ingrese la contraseña: ")
            if password.isdigit():# ------------------------------------------------ verifica si la contraseña es numerica
                if len(str(password)) <= 8 and len(str(password)) >= 4:#------------ verifica si la contraseña tiene entre 4 y 8 digitos
                    id = asignarId(1)
                    baseDatos.append({"id": id,"user": userName, "password": password, "tikects": []})
                    with open(ruta, "w", encoding="utf-8") as file:
                        json.dump(baseDatos, file, indent=2)
                    print("Usuario registrado exitosamente")
                    input("Presione Enter para continuar...")
                else:
                    printError("La contraseña debe tener entre 4 y 8 digitos", "Contraseña invalida")
                    input("Presione Enter para continuar...")
            else:
                printError("La contraseña debe ser solo numerica", "Contraseña invalida")
                input("Presione Enter para continuar...")
        else:
            printError("El nombre de usuario no puede contener espacios", "Nombre de usuario invalido")
            input("Presione Enter para continuar...")
    else:
        printError("El nombre de usuario ya existe", "Nombre de usuario invalido")
        input("Presione Enter para continuar...")

def iniciarSesion():
    printTitle("Iniciar Sesion")
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            data = json.load(file)
            baseDatos = data
    except json.JSONDecodeError as e:
        printError("Error al cargar los datos", e)
    
    for i in data:
        userData = i

    userName = input("Ingrese el nombre de usuario: ")
    if userName == userData["user"]:
        password = input("Ingrese la contraseña: ")
        if password == userData["password"]:
            print(f"Inicio de sesion exitoso ID({userData["id"]})")
            global userIndex
            userIndex = userData["id"] - 1
            print(userIndex)
            global menu
            menu = 1
            input("Presione Enter para continuar...")
        else:
            printError("La contraseña no coincide.", "Contraseña invalida")
            input("Presione Enter para continuar...")
    else:
        printError("El usuario no existe", "Nombre de usuario invalido")
        input("Presione Enter para continuar...")



#----------------Main-----------------·#
def main():

    while True:
        global menu
        with open(ruta, "r", encoding="utf-8") as file:
            data = json.load(file)
            baseDatos = data

        if menu == 0:
            limpiarConsola()
            print(menuLogin)
            try:
                o = int(input("Escoge Opcion: "))
                if o==1:
                    limpiarConsola()
                    registrarse()
                elif o==2:
                    limpiarConsola()
                    iniciarSesion()
            except ValueError as e:
                printError("Opcion no valida",e)
                input("Presione Enter para continuar...")
        elif menu == 1:
            menuUser = f"""

        █░░ █▀█ ▀█▀ █▀▀ █▀█ █ ▄▀█
        █▄▄ █▄█ ░█░ ██▄ █▀▄ █ █▀█
        
        Usuario {baseDatos[userIndex]["user"]} ID({baseDatos[userIndex]["id"]})

        1. Comprar boletas.
        2. Ver boletas.
        3. Generar numero ganador.
        4. Ver premios.
        5. Cerrar sesion.
        
    """

            limpiarConsola()
            print(menuUser)
            try:
                o = int(input("Escoge Opcion: "))
                if o==1:
                    pass
                elif o==2:
                    pass
                elif o==3:
                    pass
                elif o==4:
                    pass
                elif o==5:
                    pass
            except ValueError as e:
                printError("Opcion no valida",e)
                input("Presione Enter para continuar...")
        
main()    



