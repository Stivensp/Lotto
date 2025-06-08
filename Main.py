#Imports
import json
import os
import random
import webview

#---------------Globables--------------#
userIndex = None  #inidice del usuario en la base de datos
ruta="data.json"
baseDatos = []
menu = 0

#---------------Menu------------------·


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
    
    er = f"[Error] {error}  {msg}"
    return er


def Comprar():
    global userIndex
    try:
        with open(ruta, "r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print("Error al decodificar JSON:", e)
    except FileNotFoundError:
        print("Archivo no encontrado:", ruta)
    except Exception as e:
        print("Error inesperado:", e)   
    
    lista_boletas=[]  
    for i in range(0,50):
        lista_boletas.append(i)

    boletas=[]

    #cant=int(input("Cuantas boletas quieres comprar?"))

    for i in range(cant):
        buy=0#int(input("Que boletas quieres comprar")) 
        if buy in range(len(lista_boletas)):
            lista_boletas.pop(buy)
            boletas.append(buy)

    print(lista_boletas)
    print(boletas)   
    
    index_user_ticket=data[userIndex]
    index_user_ticket["tickets"].extend([int(b) for b in boletas])
    #Guardar en json
    with open(ruta,"w",encoding="utf-8")as file:
        json.dump(data,file,indent=4) 
        
def EliminaTicket():
    global userIndex
    try:
        with open(ruta,"r",encoding="utf-8")as file:
            data=json.load(file)
    except json.JSONDecodeError as e:
        print(e)    
    
    #ticket_to_remove=int(input("Que boleta quieres eliminar?"))
    tickets_user=data[userIndex]
    tickets=tickets_user["tickets"]
    print(tickets) 
    try:
        if ticket_to_remove in tickets:
         tickets.remove(ticket_to_remove)
         print("Boleta Eliminada Exitosamente")
    except ValueError:
        print(ValueError)
        
    with open(ruta,"w",encoding="utf-8")as file:
     json.dump(data,file,indent=4) 
            
            
def list_boleta():
    global userIndex
    try:
        with open(ruta,"r",encoding="utf-8")as file:
         data=json.load(file)
    except json.JSONDecodeError as e:
        print(e)
        
    user_with_keys=data[userIndex]
    boletas=user_with_keys["tickets"]
    for i in boletas:
        print(i)
            
                   
class API:

    def registrarse(self, value, passs):
        password = passs
        userName = value 
        printTitle("Registrarse")
        try:
            with open(ruta, "r", encoding="utf-8") as file:
                data = json.load(file)
                global baseDatos
                baseDatos = data
                userData  = data
        except json.JSONDecodeError as e:
                    return printError("Error al cargar los datos", e)
        if len(userName) > 0:
            if any(usuario["user"] == userName for usuario in data):# ------------------------------------------------------ verifica si el usuario ya existe
                return printError("El nombre de usuario ya existe", "Nombre de usuario invalido")
            else:
                if userName.count(" ") < 1:# ----------------------------------------------- verifica si el nombre de usuario no contiene espacios
                    if password.isdigit():# ------------------------------------------------ verifica si la contraseña es numerica
                        if len(str(password)) <= 8 and len(str(password)) >= 4:#------------ verifica si la contraseña tiene entre 4 y 8 digitos
                            id = asignarId(1)
                            baseDatos.append({"id": id,"user": userName, "password": int(password), "tikects": []})
                            with open(ruta, "w", encoding="utf-8") as file:
                                json.dump(baseDatos, file, indent=2)
                            return "Usuario registrado."
                        else:
                            return printError("La contraseña debe tener entre 4 y 8 digitos", "Contraseña invalida")
                    else:
                        return printError("La contraseña debe ser solo numerica", "Contraseña invalida")
                else:
                    return printError("El nombre de usuario no puede contener espacios", "Nombre de usuario invalido")
                
        else:
            return printError("Usuario invalido", "Ingresar el nombre de usuario es obligatorio")
    
    def iniciarSesion(self, user, passs):

        userName = user
        password = passs
        try:
            with open(ruta, "r", encoding="utf-8") as file:
                data = json.load(file)
                baseDatos = data
        except json.JSONDecodeError as e:
            printError("Error al cargar los datos", e)
        
        for i in data:
            userData = i
            
        if userName == userData["user"]:
            if password == userData["password"]:
                print(f"Inicio de sesion exitoso ID({userData["id"]})")
                global userIndex
                userIndex = userData["id"] - 1
                print(userIndex)
                return "Sesion iniciada!!"
            else:
                return printError("La contraseña no coincide.", "Contraseña invalida")
        else:
            return printError("El usuario no existe", "Nombre de usuario invalido")
        
#Cargador de Archivos Simples        
    def get_nombre(self):
     global userIndex
     with open(ruta, "r", encoding="utf-8") as file:
        data = json.load(file)
     return {"nombre": data[userIndex]["user"]}
 #Cargador de Archivos Simples  
    def change_user_index():
     global userIndex
     with open(ruta, "r", encoding="utf-8") as file:
      data = json.load(file)
      
      

if __name__ == '__main__':
    api = API()
    webview.create_window('Lotto', 'sLoad.html', js_api=api, width=1210, height=720)
    webview.start(debug=True)
