from openpyxl import *
from datetime import date

def crearUsuario():
    
    book = load_workbook("bd_login.xlsx")
    
    max_row = book.active.max_row
    
    #print(max_row)
    
    #datos del usuario
    
    userName = input("Ingrese nombre del usuario: ")
    password = input("Ingrese el password del usuario (mayor a 5 digitos, y que tenga letras y numeros): ")
    confirpassword = input("Confirme el password del usuario: ")
    
    if password == confirpassword and len(password) > 5:
        #agregar el ID
        sheet = book.active
        sheet[f"A{max_row + 1}"] = max_row
        #agregar el user name
        sheet = book.active
        sheet[f"B{max_row + 1}"] = userName
        #agregar el password
        sheet = book.active
        sheet[f"C{max_row + 1}"] = password
        #agregar fecha de creacion
        sheet = book.active
        sheet[f"D{max_row + 1}"] = date.today()
        
        print ("Usuario Registrado Con Exito...........")
        book.save("bd_login.xlsx")
    else:
        print ("El password del usuario no cumple con los requerimientos.")
        
crearUsuario()