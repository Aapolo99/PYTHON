numero = int(input("Digite un numero entre 1 y 3."))
numeroTexto = ""

if(numero == 1):
    numeroTexto =  "Uno"
elif(numero == 2):
    numeroTexto = "Dos"
elif(numero == 3):
    numeroTexto = "Tres"
else:
    numeroTexto = "El numero ingresado esta fuera de rango."            
    
print(f"El Numero proporcionado: {numero} - {numeroTexto}")