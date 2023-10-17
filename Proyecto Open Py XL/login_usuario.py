from openpyxl import *

def LoginUsuario():
    book = load_workbook("bd_login.xlsx")

    max_row = book.active.max_row
    
    #Datos de usuario
    userName = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese el password: ")
    
    #Activar la edicion
    sheet = book.active
    
    for i in range(max_row):
        variableApoyo = i + 2
        userConfi = sheet[f"B{variableApoyo}"]
        passwordConfi = sheet[f"C{variableApoyo}"]
        
        if userName == userConfi.value and password == passwordConfi.value:
            print(f"El usuario se ha logeado con exito.....")
            return True
    else:
        print(f"El usuario y/o el password no coinciden.")

LoginUsuario()